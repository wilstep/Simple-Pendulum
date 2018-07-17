from front import FrontEnd
from osc import Osc

""" Runs the classes FrontEnd and Osc """

ob = FrontEnd()
ob.intro()
ob.my_input()
ob.summary()
ob.display()
my_osc = Osc(ob.angle, ob.length)
my_osc.aperiod()
my_osc.display()
