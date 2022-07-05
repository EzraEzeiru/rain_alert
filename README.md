# rain_alert
This is a rain alert application. It make use of the open weather api to collect weather data for every new day. 

• main.py: Makes a get request to the open weather api to collect weather data for that day based on your latitude and longitude specified in the app. 
It then compares the weather ID from the json data returned from the api to the standard rainy day ID which is 700. If the weather ID from the Abi is a above 700, it means is going to rain and a message is sent to the user via twilio.

• play.py: it has nothing to do with the application. Just a file where I practiced dictionary comprehension.
