import odrive
from odrive.enums import *
import time
import keyboard

#----------program for testing odrive---------#
#----wait motor calibrate, it will auto run---# 

#---parameter---#
MAX_SPEED = 100
KP_VALUE  = 30
KI_VALUE  = 0.25
BANDWIDTH = 2500
RAMP_RATE = 100
POS_GAIN = 35

#-------------setup-------------#
address_motor = odrive.find_any()
print("reset position...")
address_motor.axis0.motor.config.current_control_bandwidth = BANDWIDTH
address_motor.axis0.controller.config.vel_gain = KP_VALUE
address_motor.axis0.controller.config.vel_integrator_gain = KI_VALUE 
address_motor.axis0.controller.config.vel_ramp_rate = RAMP_RATE
address_motor.axis0.controller.config.vel_limit = MAX_SPEED
address_motor.axis0.controller.config.pos_gain = POS_GAIN
address_motor.axis0.controller.config.control_mode = ControlMode.POSITION_CONTROL
address_motor.axis0.controller.input_pos = 0
time.sleep(2)
print("changing mode...")
address_motor.axis0.controller.config.input_mode = InputMode.VEL_RAMP
address_motor.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
address_motor.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
time.sleep(2)
print("SETUP DONE!")
time.sleep(1)

#--starting speed--#
velocity_motor = 10

#---run---#
while True:
    if keyboard.is_pressed("h"):    # PRESS KEYBOARD BUTTON 'h' FOR TURNING OFF ODRIVE MOTOR
        velocity_motor = 0
    elif keyboard.is_pressed("p"):  # PRESS KEYBOARD BUTTON 'p' FOR TURNING ON ODRIVE MOTOR CW
        velocity_motor = 75
    elif keyboard.is_pressed("o"):  # PRESS KEYBOARD BUTTON 'o' FOR TURNING ON ODRIVE MOTOR CCW
        velocity_motor = -75
    elif keyboard.is_pressed("l"):  # PRESS KEYBOARD BUTTON 'l' FOR TURNING ON ODRIVE MOTOR CW SEQUENTIAL
        velocity_motor = 0
        while velocity_motor < 100:
            velocity_motor += 1
            time.sleep(1)
    elif keyboard.is_pressed("k"):  # PRESS KEYBOARD BUTTON 'k' FOR TURNING ON ODRIVE MOTOR CCW SEQUENTIAL
        velocity_motor = 0
        while velocity_motor > -100:
            velocity_motor -= 1
            time.sleep(1)

    if address_motor.axis0.current_state == 1:
        print("RESET MOTOR ERROR...")
        address_motor.clear_errors()
        address_motor.axis0.requested_state = 8
    else:
        print("STARTING MOTOR...")
        address_motor.axis0.controller.input_vel = velocity_motor
