from models import IvrModel, PhoneModel


def update_ivr_data(post_data):
	
	for key, value in post_data.iteritems():
		if key.startswith('ivr') or key.startswith('option'):
			ivr_raw = key.split('-')
			ivr_id = int(ivr_raw[1])
			ivr_record_key = ivr_raw[0]
			record = IvrModel.objects.filter(id=ivr_id).update(**{ivr_record_key: value[0]})
		elif key.startswith('welcome_message'):
			ivr_raw = key.split('-')
			ivr_id = int(ivr_raw[1])
			ivr_record_key = ivr_raw[0]
			record = PhoneModel.objects.filter(id=ivr_id).update(**{ivr_record_key: value[0]})


def fetch_ivr_data(phone_number):
	
	ivrQueryset = IvrModel.objects.filter(phone__phone_number=phone_number).values('id', 'ivr_option', 'option_type', 'option_value')
	phoneQueryset = PhoneModel.objects.filter(phone_number=phone_number).values('id', 'welcome_message')[0]

	return ivrQueryset, phoneQueryset


def get_ivr_message(phone_number):

	phoneQueryset = PhoneModel.objects.filter(phone_number=phone_number).values('welcome_message')[0]

	ivr_message = phoneQueryset
	
	ivrQueryset = IvrModel.objects.filter(phone__phone_number=phone_number).values('ivr_option')

	for key, values in ivrQueryset.iteritems():
		pass

