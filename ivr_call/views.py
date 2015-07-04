from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import plivoxml

from controllers import update_ivr_data, fetch_ivr_data, 

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
	if request.method == 'POST':
		print dict(request.POST.iterlists())
		update_ivr_data(dict(request.POST.iterlists()))
		ivrQueryset, phoneQueryset = fetch_ivr_data(phone_number='+1 888-314-8506')
	return render(request, 'index.html', {'ivr_data': ivrQueryset, 'ivr_phone': phoneQueryset})

@csrf_exempt
def ivr(request):
	response = plivoxml.Response()
	if request.method == 'GET':
		getdigits_action_url = "http://117.254.121.119:5000" + reverse('ivr_call.views.ivr')	
		getDigits = plivoxml.GetDigits(action=getdigits_action_url,
									   method='POST', timeout=7, numDigits=1,
									   retries=1)
		IVR_MESSAGE = get_ivr_message(phone_number='+1 888-314-8506')
		getDigits.addSpeak(IVR_MESSAGE)
		response.add(getDigits)
		response.addSpeak(NO_INPUT_MESSAGE)

		return HttpResponse(str(response), content_type='text/xml')

	elif request.method == 'POST':
		# print request.POST
		digit = str(request.POST.get('Digits', None))
		if digit == "1":
			joke = "dummy joke_from reddit"
			response.addSpeak(joke)
		elif digit == "2":
			# Listen to a song
			response.addPlay(PLIVO_SONG)
		else:
			response.addSpeak(WRONG_INPUT_MESSAGE)

		return HttpResponse(str(response), content_type='text/xml')

