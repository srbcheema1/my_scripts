# -*- coding: utf-8 -*-
# author: pBouillon (https://github.com/pBouillon)

'''
    Small code sample using the HC-SR04 sensor and a LED
    after setup, light up a LED when something move 
    in front of the sensor
'''

import RPi.GPIO
from RPi.GPIO import BCM
from RPi.GPIO import HIGH
from RPi.GPIO import IN
from RPi.GPIO import LOW
from RPi.GPIO import OUT
from RPi.GPIO import cleanup
from RPi.GPIO import input
from RPi.GPIO import output
from RPi.GPIO import setmode
from RPi.GPIO import setup
from RPi.GPIO import setwarnings

import time
from time import sleep
from time import time


'''Delays and temporisations
'''
DELAY_ALARM = 2
DELAY_DETEC = .0001
DELAY_EXEC  = .0001
DELAY_SETUP = .0005
'''Pins
'''
PIN_LED     = 25
PIN_ECHO    = 7
PIN_TRIGGER = 8
'''Ressources
'''
DETECTION_BOUND  = 20
CM_CONVERTOR     = 17150
MAX_DIST         = 450
MIN_DIST         = 2
VERIFICATIONS    = 5


def alarm() :
    '''Light up the LED
    
    On alarm, light up the led
    '''
    output (PIN_LED, HIGH) 
    print('pass')
    sleep (DELAY_ALARM)
    output (PIN_LED, LOW)
    
def blink (iterations, delay) :
    for x in range (iterations):
        output (PIN_LED, HIGH)
        sleep  (delay)
        output (PIN_LED, LOW)
        sleep  (delay)

def destroy() :
    '''Clean every PINs
    '''
    cleanup ()

def get_dist() :
    '''Get the distance
    
    Returns:
        Distance in cm
    '''
    output (PIN_TRIGGER, False)
    sleep  (DELAY_SETUP)

    output (PIN_TRIGGER, True)
    sleep  (DELAY_EXEC)
    output (PIN_TRIGGER, False)

    while not input (PIN_ECHO):
        pulse_start = time()

    while input (PIN_ECHO):
        pulse_end  = time()

    distance = (pulse_end - pulse_start) * CM_CONVERTOR
    distance = round (distance, 2)
    
    if not MIN_DIST < distance < MAX_DIST:
        distance = 0
        
    return distance

def setup_env() :
    '''set up the PINs
    
    Disabble warnings in case of pins already 
        in use due to another program before
    '''
    setwarnings (False)
    
    setmode (BCM)
    setup (PIN_LED,     OUT)
    setup (PIN_TRIGGER, OUT)
    setup (PIN_ECHO,    IN )

def setup_dist() :
    '''Calibrate the distance
    
    Makes the led blinking while setup
    Then turn off the led
    '''
    data = []
    for x in range (15) :
        blink(4, .05)    
        data.append(get_dist())
        print('x: ', x,' -- current: ',data[x])
    
    delta = 0.0
    for x in range(int(3*len(data)/4), len (data)):
        if not delta :
            delta = data[x] - data[x-1]
        else:
            delta += data[x] - data[x-1]
            delta /= 2
            
    print('delta: ',delta)
    if not -1 < delta < 1 :
        return -1
                
    print ('Calibrate around ',data[0],' cm')
    return sum (data[int(3*len(data)/4):]) / float (len (data[int(3*len(data)/4):]))
            
def verify_alarm(dist) :
    '''Check VERIFICATION time if something pass
    '''
    delta   = .0
    a_count =  0
    
    for x in range (VERIFICATIONS) :
        delta = dist - get_dist()
        if not delta < DETECTION_BOUND :
            a_count += 1
        else:
            a_count -= 1
            
    if a_count > 0 :
        alarm()

def watch(dist) :
    '''Call alarm() on passage
    '''
    blink(1, 1)
    print ('Operationnal\n')
    while True:
        delta = dist - get_dist()
        if not delta < DETECTION_BOUND :
            verify_alarm(dist)
        sleep (DELAY_DETEC)

if __name__ == '__main__':
    try :
        print ('Intitiating ...\n')
        setup_env ()
        
        print ('Calibrating ...\n')
        watched_dist = -1
        while not watched_dist + 1:
            watched_dist = setup_dist()
        print('\nwatched dist: ',watched_dist,'\n')
        
        print ('Proceding\n')
        watch (watched_dist)
        
    except KeyboardInterrupt :
        print ('\nKeyboard interruption, cleaning pins...\n')
    
    except Exception as e:
        print ('\nAn error occurred, aborting...\n',e,'\n')
    finally:
        destroy ()
        exit  ()