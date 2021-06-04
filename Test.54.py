from __future__ import division
import time

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
pwm.set_pwm_freq(60)
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
 
print('Moving servo on channel 0, press Ctrl-C to quit...')
try:
   while True: 
      pwm.set_pwm(0, 0, servo_min) 
      pwm.set_pwm(7, 0, servo_min) 
      pwm.set_pwm(15, 0, servo_min) 
      time.sleep(1) 
      pwm.set_pwm(0, 0, servo_max) 
      pwm.set_pwm(7, 0, servo_max) 
      pwm.set_pwm(15, 0, servo_max) 
      time.sleep(1)
except KeyboardInterrupt:
   pass
