# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led = 10 # GPIO number where the led is connected

# Tell the GPIO module to use GPIO numbering used by processor
GPIO.setmode(GPIO.BCM)

# Set GPIO no 11 to output mode
GPIO.setup(led, GPIO.OUT)

# Blink some leds
#while True:
GPIO.output(led, False)
sleep(0.03)  # Sleep for 1 second
GPIO.output(led, True)
sleep(0.03)

# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server

# Function that is ran when a http request comes in
def simple_app(env, start_response):
    
    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/html')] 
    start_response(status, headers)

    # What did the user ask for?
    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
        return "got on"
    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")
        return "got off"
    else:
        print("user asked for something else")
        return "Hello world!"            

# Create a small python server
httpd = make_server("", 8000, simple_app)
print "Serving on port 8000..."
print "You can open this in the browser http://192.168.1.xxx:8000 where xxx is your rpi ip aadress"
print "Or if you run this server on your own computer then http://localhost:8000" 
httpd.serve_forever()

