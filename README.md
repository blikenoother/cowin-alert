# CoWIN 💉 🔈📲

Simple python script which monitors slots availability and triggeres notification via call (Exotel free trial)

## Run code
  - [Try Free trail on Exotel and signup](https://my.exotel.com/auth/register). Just after signup, make sure to misscall on given number as instructed to verify your number
  - make sure you have python3.5+ version installed
  - `pip3 install requests`
  - `pip3 install pytz`
  - clone the code or download just `cowin_alert.py` file
  - `python3 cowin_alert.py {pincode} {days} {exotel_api_key} {exotel_api_token} {exotel_sid} {from_number} {to_number} {exotel_caller_id}`

### Params
  - `pincode` pincode which you want to monitor (Eg: 122001)
  - `days` number of days to check slots for, if you pass `7` then this script will fetch data from now() to now() + 7 days and check slots availability
  - `exotel_api_key` login to the exotel developer dashboard and find your "API KEY (USERNAME)" [here](https://my.exotel.com/apisettings/site#api-credentials) 
  - `exotel_api_token` login to the exotel developer dashboard and find your "API TOKEN (PASSWORD)" [here](https://my.exotel.com/apisettings/site#api-credentials) 
  - `exotel_sid` login to the exotel developer dashboard and find your "Account sid" [here](https://my.exotel.com/apisettings/site#api-credentials) 
  - `from_number` number on which 1st call should be connected, usually your 10 digit mobile number, you need to append 0 (Eg: 099xxxxxxxx). Also make sure this number is added into the Exotel users and verifeid by giving miss call. This limitation is only for Exotel Free trial account.
  - `to_number` number on which 2nd call should be connected, usually your 10 digit mobile number, you need to append 0 (Eg: 099xxxxxxxx). Also make sure this number is added into the Exotel users and verifeid by giving miss call. This limitation is only for Exotel Free trial account.
  - `exotel_caller_id` login to the exotel developer dashboard and find ExoPhone. The link to ExoPhone will be `https://my.exotel.com/{exotel_sid}/numbers` (Eg: 079480xxxxx)
 
### Run this script periodically
- make sure you have a system on cloud or a system which is running 24x7 and has internet connection
- you can go for aws/azure or any similar cloud and launch instance within their free tier
- check if python3 is stalled or you can installed by following [this article](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) or google it
- the following commands are for linux machine to schedule cron job
- `crontab -e` this will open a file which contains list of all cron jobs
- append following line to the file
- `*/30 * * * * python3 /{path-of-code}/cowin_alert.py 122001 5 EXOTEL_API_KEY_HERE EXOTEL_API_TOKEN_HERE EXOTEL_SID_HERE 099xxxxxxxx 099xxxxxxxx 079480xxxxx >> /{log-path}/cowin_alert.log`
- make sure to change `{path-of-code}` & `{log-path}` according
- verify cron job with command `crontab -l`

##### Request 🙏
Make sure to crawl the API generously, I have used 30min interval in above example. Crawling too frequently may land you in legal trouble. I hope developer community will use this script responsibly.

