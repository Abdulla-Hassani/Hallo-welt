robotsazi
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()
arm_motor=Motor(Port.B, Direction.COUNTERCLOCKWISE,[8,40])
greifer_motor= Motor(Port.C)
arm_motor.control.limits(speed=20, acceleration=100)
left_motor= Motor(Port.D)
right_motor= Motor(Port.A)
robot= DriveBase(left_motor,right_motor,wheel_diameter=55, axle_track=130)
color_sensor=ColorSensor(Port.S4)
Black=10
White=50
midnumber=(Black+White)/2
DRIVE_SPEED=80
PROPOTIONAL_GAIN=1.2
light_sensor = LightSensor(Port.S2)
ultrasonic_sensor=UltrasonicSensor(Port.S3)
arm_motor.run_time(100,1000)
arm_motor.run(10)
while light_sensor.reflection()<30:
    wait(10)
arm_motor.reset_angle(0)
arm_motor.hold()
greifer_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
greifer_motor.reset_angle(0)
greifer_motor.run_target(30,-70)
def robot_pick(position):
    arm_motor.run_target(50,-10)
    greifer_motor.run_until_stalled(200,then=Stop.HOLD, duty_limit=50)
    arm_motor.run_target(60,0)
def robot_release(position):
    arm_motor.run_target(50, 30)
    greifer_motor.run_target(100,-70)
    arm_motor.run_target(60,0)

UP = 40
DOWN = -30
while True:
    if ultrasonic_sensor.distance()<100:
        robot_pick(UP)
        wait(10)
        continue
    # elif ultrasonic_sensor.distance()>100:
    #     robot_release(DOWN)
    #     robot_pick(UP)
    #     robot_release(DOWN)

    elif ultrasonic_sensor.distance()>100:
        deviation=color_sensor.reflection()-midnumber
        turn_rate=PROPOTIONAL_GAIN*deviation
        robot.drive(DRIVE_SPEED,turn_rate)
    if color_sensor.reflection()>30:
        robot.stop()
        right_motor.brake()
        left_motor.brake()
