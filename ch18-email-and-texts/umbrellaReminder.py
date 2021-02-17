#! python3
# umbrellaReminder.py - Each day at 7:30am, the program will text you the daily weather forecast.
#
# NOTES:  Ensure you have a Twilio account, and modify the following variables:
#         1. accountSID: Your twilio SID.
#         2. authToken: Your twilio authentication token.
#         3. myNumber: The mobile number you want the weather forecast to be sent to.
#         4. twilioNumber: The number associated with your twilio account.
#         The program will run for 100 days, and will text the weather forecast at 7:30am.

import requests, bs4, time, datetime
from twilio.rest import Client

# Twilio credentials and your phone number.
accountSID = 'your-account-sid'
authToken  = 'your-account-token'
myNumber = 'your-twilio-number'
twilioNumber = 'your-mobile-number'
twilioClient = Client(accountSID, authToken)

# Webscrape today's weather forecast from weather.gov and send it as a text message to your number.
def getWeatherToday():
    res = requests.get('https://forecast.weather.gov/MapClick.php?zoneid=NYZ052&zflg=1')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    weatherToday = soup.select('#detailed-forecast-body > div:nth-child(1) > div.col-sm-10.forecast-text')
    weatherToday = weatherToday[0].getText()
    print(weatherToday)

    message = twilioClient.messages.create(body=weatherToday, from_=twilioNumber, to=myNumber)

# This is the first time the program will send the text/run the getWeatherToday function.
firstAlarmDate = datetime.datetime(2021, 1, 24, 7, 30)

# Run for a hundred days following the first alarm date. Will run the getWeatherToday function once every day.
while datetime.datetime.now() < firstAlarmDate:
    time.sleep(1)
for day in range(100):
    getWeatherToday()
    time.sleep(86400)


