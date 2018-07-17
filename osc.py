from math import sqrt
from math import sin
from math import pi
import matplotlib.pyplot as plt
import numpy as np

N = 600


class Osc:
    """ Oscillation class: computes various approximations for the motion
    of the pendulum and plots the results in a graph"""
    def __init__(self, angle, length):
        self.angle = angle
        self.length = length
        self.theta_1 = np.zeros(N)
        self.theta_2 = np.zeros(N)
        self.theta_cos = np.zeros(N)

    def aperiod(self):
        """ Approximate series solution for the period of the oscillation
            taken from wikipedia see section:
            Power series solution for the elliptic integral
            https://en.wikipedia.org/wiki/Pendulum_(mathematics) """
        f2 = 1.0 / 16.0
        f4 = 11.0 / 3072.0
        f6 = 173.0 / 737280.0
        f8 = 22931.0 / 1321205760.0
        f10 = 1319183.0 / 951268147200.0
        f12 = 233526463.0 / 2009078326886400.0
        a2 = self.angle * self.angle
        a4 = a2 * a2
        a6 = a4 * a2
        a8 = a4 * a4
        a10 = a6 * a4
        a12 = a6 * a6
        Tf = 1.0 + f2 * a2 + f4 * a4 + f6 * a6
        Tf += f8 * a8 + f10 * a10 + f12 * a12
        T0 = 2.0 * pi * sqrt(self.length / 9.8)
        print('The estimated period from the 12th order series '
              'is %f seconds' % (T0 * Tf))
        print('This is an increase on the harmonic period of %f '
              'by a factor of %f' % (T0, Tf))
        self.trajectory(T0, Tf)

    def trajectory(self, T0, Tf):
        """ computes the trajectory for the pendulum 3 different ways
        firstly a naive approximation assuming the motion to be sinusoidal
        secondly a numerical solution using the Verlet quadrature
        thirdly the same with half the time step"""
        self.T1 = T0 * Tf
        delt = (3.0 * self.T1) / float(N)
        self.ta = np.arange(0, (3.0 * self.T1), delt)
        omega = 2.0 * pi / self.T1
        a0 = self.angle * 180.0 / pi
        self.theta_cos = a0 * np.cos(omega * self.ta)
        th = self.angle
        thd = 0.0
        fac = 180.0 / pi
        for i in range(0, N):
            self.theta_1[i] = fac * th
            (th, thd) = self.verlet(th, thd, 0.001, delt)
        th = self.angle
        thd = 0.0
        for i in range(0, N):
            self.theta_2[i] = fac * th
            (th, thd) = self.verlet(th, thd, 0.0005, delt)

    def verlet(self, theta, thetad, dt, delt):
        """integrates the motion between 2 adjacent points on the graph
        using the Verlet quadrature
        see: https://en.wikipedia.org/wiki/Verlet_integration#Velocity_Verlet
        """
        ns = delt / dt
        ns = int(ns)
        dt = delt / float(ns)
        x = theta
        v = thetad
        fac = -9.8 / self.length
        a = fac * sin(x)
        for i in range(0, ns):
            vh = v + 0.5 * a * dt
            x = x + vh * dt
            a = fac * sin(x)
            v = vh + 0.5 * a * dt
        return (x, v)

    def display(self):
        """ creates a graph of the pendulum's trajectory for the
        three approximations which have been used """
        plt.plot(self.ta, self.theta_cos, label='sinusoidal')
        plt.plot(self.ta, self.theta_1, label='dt = 0.001')
        plt.plot(self.ta, self.theta_2, label='dt = 0.0005')
        plt.legend(loc='center left')
        plt.xlabel('t')
        plt.ylabel('theta (degrees)')
        plt.title('pendulum position (angle in degrees) as a function of time')
        plt.grid(True)
        input('\npress enter to continue and view a graph of how the '
              'pendulum\'s\nangle varies with time\n')
        fig = plt.gcf()
        fig.canvas.set_window_title('time graph')
        plt.show()
