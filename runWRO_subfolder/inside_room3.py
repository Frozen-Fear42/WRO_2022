from runWRO_subfolder.variable_initiation import *
from runWRO_subfolder import inside_room1,inside_room2,inside_room4,lundary_sorting,dropping,starting_room
def pid_line(proportional_gain = 1.4,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 20:

        # Calculate the deviation from the threshold.

        deviation = right_sensor.reflection() - left_sensor.reflection()

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

def lift(rotation=160,angle=200):
    large_motor.run_angle(rotation,angle,then=Stop.BRAKE)

def ls_following(proportional_gain = 1.4,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 30:

        # Calculate the deviation from the threshold.

        deviation = left_sensor.reflection() - 30

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

def rs_following(proportional_gain = 1.4,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 30:

        # Calculate the deviation from the threshold.

        deviation = 30 - right_sensor.reflection()

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.stop()
        right_motor.run(100)
    robot.stop()
    left_motor.brake()
    right_motor.brake()


def inside_room():
    #pid
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(50)

    pid_line(0.5,200)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-2)

    wait(300)


    #turn to room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-94)

    #move straight
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(300)

    turn_to_lundary()

    #lift first lundary
    lift(300,-280)
    lift(300,280)


def drop_water(water_position):
    inside_room()
    return(Dropping.drop_water_position(water_position))

def game():
    inside_room()
    
    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(67)

    #move to ball
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-121.5)


    #lift ball
    lift(350,-170)

    #move to drop in basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(60)

    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(95)

    #move to basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-147)

    #drop ball
    lift(350,110)

    #move away from basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(128)

    #move out of bottle
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-62)

    #out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(250)

    lift(350,50)

    ls_following(proportional_gain=0, drive_speed=100)
    rs_following(proportional_gain=0, drive_speed=100)


def turn_to_lundary():

    #turn to bottle
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(94.5)

    #move back to pick bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-50)