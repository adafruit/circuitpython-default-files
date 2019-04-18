# Metro M4 AirLift IO demo
# Welcome to CircuitPython 4 :)

import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from adafruit_motor import servo
import neopixel
import busio
import audioio
import pulseio
import simpleio
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_requests as requests
# keyboard support
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

# One pixel connected internally!
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Analog audio output on A0, using two audio files
audio = audioio.AudioOut(board.A0)
audiofiles = ["rimshot.wav", "laugh.wav"]

# Analog input on A1
analog1in = AnalogIn(board.A1)

# Initialize WiFi Module
if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("ESP32 found and in idle mode")
print("Firmware vers.", esp.firmware_version)
print("MAC addr:", [hex(i) for i in esp.MAC_address])

# Digital input with pullup on D2, D3, and D4
buttons = []
for p in [board.D2, board.D3, board.D4]:
    button = DigitalInOut(p)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)

# Servo on D5
# create a PWMOut object on Pin D5
pwm = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm)

# NeoPixel strip (of 16 LEDs) connected on D6
NUMPIXELS = 16
neopixels = neopixel.NeoPixel(board.D6, NUMPIXELS, brightness=0.2, auto_write=False)

# Used if we do HID output, see below
kbd = Keyboard()

######################### HELPERS ##############################

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

def play_file(filename):
    print("")
    print("----------------------------------")
    print("playing file "+filename)
    with open(filename, "rb") as wave_file:
        wave = audioio.WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass
    print("finished")
    print("----------------------------------")

######################### MAIN LOOP ##############################

i = 0
while True:
  if i == 0:
      # Lets to a WiFi SSID scan
      for ap in esp.scan_networks():
          print("\t%s\t\tRSSI: %d" % (str(ap['ssid'], 'utf-8'), ap['rssi']))

  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)

  # also make the neopixels swirl around
  for p in range(NUMPIXELS):
      idx = int ((p * 256 / NUMPIXELS) + i)
      neopixels[p] = wheel(idx & 255)
  neopixels.show()

  # Read analog voltage on A1
  print("A1: %0.2f" % getVoltage(analog1in), end="\t")

  if not buttons[0].value:
      print("Button D2 pressed!", end ="\t")
      # optional! uncomment below & save to have it sent a keypress
      #kbd.press(Keycode.A)
      #kbd.release_all()

  if not buttons[1].value:
      print("Button D3 pressed!", end ="\t")
      play_file(audiofiles[0])

  if not buttons[2].value:
      print("Button D4 pressed!", end ="\t")
      play_file(audiofiles[1])

  # sweep a servo from 0-180 degrees (map from 0-255)
  servo.angle = simpleio.map_range(i, 0, 255, 0, 180)

  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down

  print("")
