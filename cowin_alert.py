import sys
from datetime import datetime
from pytz import timezone
from datetime import timedelta
import requests

covin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
exotel_url = "https://{api_key}:{api_token}@api.exotel.com/v1/Accounts/{sid}/Calls/connect.json"

now_asia = datetime.now(timezone("UTC")).astimezone(timezone("Asia/Kolkata"))
date_format = "%d-%m-%Y"

min_age_limit = 18

def _cowin_fetch_slots(pincode, date):
	params = {"pincode": pincode, "date": date.strftime(date_format)}
	response = requests.get(covin_url, params=params).json()
	return response

def _get_center(pincode, days):
	for day in range(days):
		response = _cowin_fetch_slots(pincode, now_asia  + timedelta(days=day))
		for center in response.get("centers", []):
			for session in center.get("sessions", []):
				if session.get("min_age_limit", 18) <= min_age_limit and session.get("available_capacity", 0) > 0:
					return center
	return None

def _notify_exotel_call(api_key, api_token, sid, from_number, to_number, caller_id):
	url = exotel_url.format(api_key=api_key, api_token=api_token, sid=sid)
	data = {"From": from_number, "To": to_number, "CallerId": caller_id}
	print(requests.post(url, data=data))

def main():
	args = sys.argv
	pincode, days = str(int(sys.argv[1])), int(sys.argv[2])
	center = _get_center(pincode, days)
	if center:
		print(center)
		api_key, api_token, sid = sys.argv[3], sys.argv[4], sys.argv[5]
		from_number, to_number, caller_id = sys.argv[6], sys.argv[7], sys.argv[8]
		_notify_exotel_call(api_key, api_token, sid, from_number, to_number, caller_id)

if __name__ == "__main__":
	main()
