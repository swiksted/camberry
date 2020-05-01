from picamera import PiCamera
from time import sleep
from  datetime import datetime

# Set up camera module
camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(15)

# Get datestamp for file
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%m-%Y_%H%M%S")
file_path = '/home/pi/images/'+timestampStr+'.jpg' 

# Take picture 
camera.capture(file_path)
camera.stop_preview()