# auto
self drive car tensorFlow and python tornado web server
hardward: raspberry and adafruit motor hat
motor api: adafruit motor hat api

raspberry server send live images to python tornado client 

client use tensorflow to recognize images

there are 3 options:
  -- forward
  -- turn left
  -- turn right
then send back response to raspberry server 
then triger motor api to response for next step.

