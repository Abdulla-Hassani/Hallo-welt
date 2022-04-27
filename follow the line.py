#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
robot = DriveBase(right_motor,left_motor,wheel_diameter = 54, axle_track= 200)
light = ColorSensor(Port.S4)
Rot = 50
White = 80
touch_sensor = TouchSensor(Port.S3)
#Eingaben
durchschnitt = (Rot + White )/2
DRIVE_SPEED = 20
PROPORTIONAL_GAIN = 1.2
ev3.speaker.say(" hello friends")


# Write your program here.
while True:
        deviation = light.reflection() - durchschnitt
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
        if touch_sensor.pressed():
          True
          robot.stop()
          left_motor.brake()
          right_motor.brake()
         elif deviation >50:
          robot.stop()
          left_motor.brake()
          right_motor.brake()
          
          
   


