#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:10:42 2024

@author: westonlarhette
"""
## Simple code to find final position of object with kinematics equation s = 0.5at^2
print('Enter the acceleration, ensuring it is in m/s^2:')
a = float(input())
print('Enter the time that the object travels for, ensuring it is in units of seconds:')
t = float(input())
s = float(0.5*a*(t**2))
s = str(s)
print('The final position of the object is ' + s, 'meters')


## Code that takes velocity v from the user and prints the maximum height
## a ball reaches when it is thrown upward
g = 9.8
print('Enter the velocity of a the ball, in m/s')
v = float(input())
h = float(-(v**2)/(2*-g))
h = str(h)
print('The maximum height the ball reaches is ' + h, 'meters')


## A box of mass m is sliding on a surface with a coefficient of kinetic friction u.
## Write a code that takes m and u from the user and prints the force of friction
## acting on the box. Assume acceleration due to gravity g 9.8 m/s^2
import numpy
cos = numpy.cos
g = 9.8
print('Enter the mass of the box in kg')
m = float(input())
print('Enter the coefficient of kinetic friction')
u = float(input())
print('Enter the angle that the incline makes with the horizontal')
theta = float(input())
F = float(u*m*g*cos(theta))
F = str(F)
print('The force of friction acting on the box is ' + F, 'Newtons')