from urllib.request import urlopen
import json
import time
import board
import neopixel

apikey="YOUNEEDYOUROWNKEYHERE" # get a key from https://developer.forecast.io/register
lati ="52.11394"  #find your latitude and longitude from google maps. 
longi = "0.08045"

#function that colours in the strip given the colour and the range
def goColour(strip, green, red, blue, start, end):
    for i in range(start, end+1):
        strip[i] = (red, green, blue)
        strip.show()

#setup the strip
strip = neopixel.NeoPixel(board.D18, 240)

try:
    goColour(strip, 0, 0, 0, 0, 239) #clear the strip
    oldTemp = 0

    #get the data from the api website
    url="https://api.forecast.io/forecast/"+apikey+"/"+lati+","+longi+"?units=si"

    #in case the Internet is not working: try it but then use the oldTemp just in case
    try:
        meteo=urlopen(url).read()
        meteo = meteo.decode('utf-8')
        weather = json.loads(meteo)
        currentTemp = weather['currently']['temperature']
    except IOError:
        currentTemp = oldTemp

    oldTemp = currentTemp #set oldTemp to last known temperature

    #let's colour! It's always going to be < 0, white:
    goColour(strip, 255, 255, 255, 0,34)  #white

    if currentTemp > 0:
        goColour(strip, 0, 0, 255, 35, 69)  # blue
    if currentTemp > 5:
        goColour(strip, 0, 255, 255, 70, 99)  # purple
    if currentTemp > 10:
        goColour(strip, 255, 0, 0, 100, 134) # green
    if currentTemp > 15:
        goColour(strip, 255, 255, 0, 135, 169)  # yellow
    if currentTemp > 20:
        goColour(strip, 100, 255, 0, 170, 209)  #orange
    if currentTemp > 25: #will this ever happen in Yorkshire??
        goColour(strip, 0, 255, 0, 210, 239)  # Red                  
	
except KeyboardInterrupt:
	print("Exit")
	goColour(strip, 0,0,0, 0, 240)
