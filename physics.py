
"""
SOME PHYSICS REUSABLE FUNCTIONS

"""
import datetime

# physics

# Speed and Velocity


def speed_input():
    distance = int(input("Enter the distance"))
    time = int(input("Enter th etime"))
    return distance / time


def speed(distance, time):

    return distance / time


def velocity():
    displacement = int(input("Enter the displacement"))
    time = int(input("Enter th etime"))
    return displacement / time


def time():
    return datetime.datetime.now()


def time_from():
    distance = float(input("Enter the distance/displacement"))
    speed = float(input("Enter the speed/velocity"))
    # speed = d/t time
    return distance / speed


def distance_from():
    " Gives you the distance from time and velocity"

    time = float(input("Enter the time"))
    speed = float(input("Enter the speed/velocity"))
    # s=d/t => d= s x t
    return time * speed


def momentum():
    mass = float(input("ENter the mass"))
    velocity = float(input("ENter the velocity"))
    return mass*velocity
