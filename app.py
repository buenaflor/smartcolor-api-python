from flask import Flask, jsonify, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

redPin = 13
greenPin = 15
bluePin = 16

RGB = [redPin,greenPin,bluePin]
for pin in RGB:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

app = Flask(__name__)

def set_rgb_color(red, green, blue):
    GPIO.output(redPin, red)
    GPIO.output(greenPin, green)
    GPIO.output(bluePin, blue)

@app.route('/', methods=['GET'])
def index():
    set_rgb_color(1,0,1)
    return jsonify({'message': 'it works'})

@app.route('/api/ledpower', methods=['GET'])
def return_ledstatus():
    if GPIO.input(redPin) == 0 and GPIO.input(greenPin) == 0 and GPIO.input(bluePin) == 0:
        return jsonify({'ledOn': False})
    else:
        return jsonify({'ledOn': True})
    
@app.route('/api/single_color', methods=['POST'])
def single_color():
    print("gettin requests")
    print(request.json['red'])
    response = {
            'red': request.json['red'],
            'green': request.json['green'],
            'blue': request.json['blue']
        }
    red = response['red']
    green = response['green']
    blue = response['blue']
    
    return jsonify({'successful': green})

@app.route('/api/ledpower', methods=['POST'])
def return_power():
    print("turning off or on")
    action = {'ledOn': request.json['ledOn']}
    ledOn = action['ledOn']
    if ledOn == True:
       set_rgb_color(1, 1, 1)
       return jsonify({'ledOn': True})
    else:
       set_rgb_color(0, 0, 0)
       return jsonify({'ledOn': False})

if __name__ == '__main__':
     app.run(host='192.168.0.241', port=3000, debug=True)