"""
Front end for Oscillator program
"""

from math import sqrt
from math import acos
from math import pi
import matplotlib.pyplot as plt
import numpy as np


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('That is not a valid number.')


class FrontEnd:
    """ Front end class """
    def __init__(self):
        self.length = 0.0
        self.init_y = 0.0
        self.init_x = 0.0
        self.angle = 0.0

    """ brief description of what the program does for the user """
    def intro(self):
        print('This program computes and plots the motion of '
              'a simple pendulum.')
        print('This is done firstly using the simple harmonic motion '
              'approximation\nand secondly it is done numerically\n')
        print('In the limit where both the numerical time step size'
              '\nand the oscillation amplitude are large')
        print('the results should coincide for both methods.\n\n\n')

    """ this method collects all of the data from the user """
    def my_input(self):
        print('Input the length for your pendulum, from 0.1m up to 2m')
        while True:
            self.length = input_float('')
            if(self.length > 2.0 or self.length < 0.1):
                print('No: the length for your pendulum'
                      ' must be from 0.1 to 2m')
            else:
                break
        print('\nInput the initial height of your pendulum, '
              'between %f and %f' % (-self.length, self.length))
        while True:
            self.init_y = input_float('')
            if(self.init_y >= self.length
               or self.init_y <= -self.length):
                print('No: the initial height for your pendulum '
                      'must be between %f to %f' % (-self.length, self.length))
            else:
                break
        """ Use Pythagoras' theorem to get the initial x position """
        self.init_x = self.length * self.length\
            - self.init_y * self.init_y
        self.init_x = -sqrt(self.init_x)
        self.angle = acos(self.init_y / self.length) - pi

    """ This method prints out a summary of all the parameters which have been
        determined from the user input """
    def summary(self):
        print
        print('\nThe length of your pendulum is %fm' % self.length)
        print('The initial height (y coordinate) for your pendulum'
              ' is % f' % self.init_y)
        print('The initial horizontal displacement of your oscillator '
              '(the initial x coordinate) is %f' % self.init_x)
        print('The initial angle of your oscillator is %f radians\n'
              'or %f degrees' % (self.angle, (self.angle / pi * 180.0)))

    """ This method displays the chosen starting position of the pendulum """
    def display(self):
        rad = 0.05 * self.length
        x = np.array([0.0, self.init_x])
        y = np.array([0.0, self.init_y])
        radp = rad + self.length * 0.025
        plt.xlim(-self.length - radp, self.length + radp)
        plt.ylim(-self.length - radp, self.length + radp)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Initial (stationary) pendulum position')
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')
        input('\npress enter to continue and view a graph of how the '
              'pendulum\nis initially set with zero momentum '
              '(i.e. it is initially stationary)\n')
        fig = plt.gcf()
        ax = fig.gca()
        circle = plt.Circle((self.init_x, self.init_y), rad, color='blue')
        ax.add_artist(circle)
        fig.canvas.set_window_title('initial graph')
        plt.show()
