from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import plivoxml

from controllers import update_ivr_data, fetch_ivr_data, get_ivr_data, get_ip_addr

# This file will be played when a caller presses 2.
PLIVO_SONG = "https://s3.amazonaws.com/plivocloud/music.mp3"

# IVR_MESSAGE
# This is the message that callhub reads when the caller dials in

# This is the message that callhub reads when the caller does nothing at all
NO_INPUT_MESSAGE = "Sorry, I didn't catch that. Please hangup and try again \
					later."

# This is the message that callhub reads when the caller inputs a wrong number.
WRONG_INPUT_MESSAGE = "Sorry, it's wrong input."

def index(request):
	ivrQueryset, phoneQueryset = fetch_ivr_data(phone_number='+1 888-314-8506')
	get_ivr_data(phone_number='+1 888-314-8506') # To be removed
	if request.method == 'POST':
		update_ivr_data(dict(request.POST.iterlists()))
		ivrQueryset, phoneQueryset = fetch_ivr_data(phone_number='+1 888-314-8506')
	return render(request, 'index.html', {'ivr_data': ivrQueryset, 'ivr_phone': phoneQueryset})

@csrf_exempt
def ivr(request):
	response = plivoxml.Response()
	IVR_MESSAGE, ivr_options = get_ivr_data(phone_number='+1 888-314-8506')
	if request.method == 'GET':
		getdigits_action_url = get_ip_addr() + reverse('ivr_call.views.ivr')	
		getDigits = plivoxml.GetDigits(action=getdigits_action_url,
									   method='POST', timeout=7, numDigits=1,
									   retries=1)
		
		getDigits.addSpeak(IVR_MESSAGE)
		response.add(getDigits)
		response.addSpeak(NO_INPUT_MESSAGE)

		return HttpResponse(str(response), content_type='text/xml')

	elif request.method == 'POST':
		digit = int(request.POST.get('Digits', None))

		if digit in ivr_options:
			if ivr_options[digit]['option_type'] == 'Redirect to':
				redirect_url = ivr_options[digit]['option_value']
				response.addRedirect(redirect_url)
				print redirect_url
			elif ivr_options[digit]['option_type'] == 'Add Speak':
				text = ivr_options[digit]['option_value']
				response.addSpeak(text)
		else:
			response.addSpeak(WRONG_INPUT_MESSAGE)

		return HttpResponse(str(response), content_type='text/xml')

@csrf_exempt
def ivr_redirect(request):
	response = plivoxml.Response()

	getdigits_action_url = get_ip_addr() + reverse('ivr_call.views.ivr_redirect')	
	getDigits = plivoxml.GetDigits(action=getdigits_action_url,
								   method='POST', timeout=7, numDigits=1,
								   retries=1)
	getDigits.addSpeak("This is a redirect call")
	response.add(getDigits)

	return HttpResponse(str(response), content_type='text/xml')