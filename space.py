import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder
import pyttsx3

# Retrieve the names of all astronauts currently in the space station

engine = pyttsx3.init() ## loads the engine for text to speech

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
a=open("iss.txt", "w")
a.write("There are currently "+str(result["number"])+" astronauts on the ISS \n")
people=result["people"]
for p in people:
    a.write(p["name"] + "- on board")

g = geocoder.ip("me")
a.write ("\n Your current Lat/Long is: " + str(g.latlng))
a.close()
with open('iss.txt') as f:
    for line in f:
        print (line)
        engine.say(line)
        engine.runAndWait()


screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.gif")

screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)

while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    lat = float(lat)
    lon = float(lon)
    print("\nLatitude:", str(lat))
    print("Longitude:", str(lon))

    iss.goto(lon, lat)

    time.sleep(5)
