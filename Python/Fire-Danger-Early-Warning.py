#!/bin/python3
  
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

R = [255, 0, 0]
B = [0, 0, 0]
Y = [255, 255, 0]
W = [255, 255, 255]
G = [0, 255, 0]

warning = [
  W, W, W, B, B, W, W, W,
  W, W, B, Y, Y, B, W, W,
  W, B, Y, R, Y, Y, B, W,
  B, Y, Y, R, Y, Y, Y, B,
  B, Y, Y, Y, Y, Y, Y, B,
  W, B, Y, R, Y, Y, B, W,
  W, W, B, Y, Y, B, W, W,
  W, W, W, B, B, W, W, W
  ]
  
noWarning = [
  W, W, W, W, W, W, W, W,
  W, W, W, W, W, W, W, G,
  W, W, W, W, W, W, G, G,
  W, W, W, W, W, G, G, W,
  W, W, W, W, G, G, W, W,
  G, W, W, G, G, W, W, W,
  G, G, G, G, W, W, W, W,
  W, G, G, W, W, W, W, W
  ]


while True:
  temperature = sense.temperature
  humidity = sense.humidity
  if (temperature < 20 and humidity > 50):
    sense.set_pixels(noWarning)
  else:
    sense.set_pixels(warning)