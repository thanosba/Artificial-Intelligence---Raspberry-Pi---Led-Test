import time
import RPi.GPIO as GPIO
from pyswip import Functor, Variable, Query, call

assertz = Functor(“assertz”, 1)
father = Functor(“father”, 2)

# Add facts to a dynamic database
call(assertz(father(“thanos”,”john”)))
call(assertz(father(“thanos”,”gina”)))

# Setup an iterative query session
X = Variable()
q = Query(father(“thanos”,X))
while q.nextSolution():
    print “Hello,”, X.value
    if X.value == “john”:          # Lite LED #5 if john is a child of thanos
        GPIO.output(5,GPIO.HIGH)
        time.sleep(6)
        GPIO.output(5,GPIO.LOW)
    if X.value == “gina”:          # Lite LED #18 if gina is a child of thanos
        GPIO.output(18,GPIO.HIGH)
        time.sleep(6)
        GPIO.output(18,GPIO.LOW)

