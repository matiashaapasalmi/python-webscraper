import requests;
import json;
from datetime import datetime, timedelta;

bus_stop = input("Enter bus stop id: ");

now = datetime.now()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#The html data file from bus Rimmi is respons
url = "http://data.itsfactory.fi/journeys/api/1/journeys?stopPointId=" + bus_stop + "&";
#0-6 0 monday, 6 sunday
today = now.weekday();
url = url + "dayTypes=" + weekdays[today];

busses = [];

for x in range(60):
    now = now + timedelta(minutes=1);


    depart_time = now.strftime("%H:%M");

    newurl = url + "&departureTime=" + depart_time;

    respons = requests.get(newurl);

    text = respons.text;

    data = json.loads(text);
    if data["status"] == "fail":
      print("Invalid stop id");
      break;

    if len(data["body"]) > 0:
      busses = busses + data["body"];
    

if len(busses) < 1:
  print("No data found");

for bus in busses:
  print(bus["departureTime"], "   ", bus["headSign"]);
