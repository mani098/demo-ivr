from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import plivoxml

# This file will be played when a caller presses 2.
PLIVO_SONG = "https://s3.amazonaws.com/plivocloud/music.mp3"

# This is the message that callhub reads when the caller dials in
IVR_MESSAGE = "Welcome to call hub. Press 1 to hear a random \
				joke. Press 2 to listen to a song."

# This is the message that callhub reads when the caller does nothing at all
NO_INPUT_MESSAGE = "Sorry, I didn't catch that. Please hangup and try again \
					later."

# This is the message that callhub reads when the caller inputs a wrong number.
WRONG_INPUT_MESSAGE = "Sorry, it's wrong input."

def index(request):

	if request.method == 'POST':
		pass
	return render(request, 'index.html', {})

@csrf_exempt
def ivr(request):
	response = plivoxml.Response()
	if request.method == 'GET':
		getdigits_action_url = "http://117.254.121.119:5000" + reverse('ivr_call.views.ivr')	
		getDigits = plivoxml.GetDigits(action=getdigits_action_url,
									   method='POST', timeout=7, numDigits=1,
									   retries=1)

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