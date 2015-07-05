from models import IvrModel, PhoneModel
import commands

def get_ip_addr():
	command_str = "ifconfig ppp0 | grep 'inet addr' |  cut -d: -f2 | awk '{print $1}'"
	return "http://"+ str(commands.getoutput(command_str)) + ":5000"

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


def get_ivr_data(phone_number):

	count = 1
	ivr_options = {}
	
	phoneQueryset = PhoneModel.objects.filter(phone_number=phone_number).values('welcome_message')[0]
	ivr_message = str(phoneQueryset['welcome_message'])
	ivrQueryset = IvrModel.objects.filter(phone__phone_number=phone_number).values('ivr_option', 'option_type', 'option_value')

	for option in ivrQueryset:
		ivr_message += '. Press %d for %s' %(count, option['ivr_option'])
		ivr_options[count] = dict(option_type = option['option_type'], option_value = option['option_value'])
		count += 1

	# print ivr_message
	return ivr_message, ivr_options


