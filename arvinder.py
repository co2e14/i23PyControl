#!/bin/env dls-python

 

'''Control script for motion ioc of I23 cryo-gripper.
'''

 

from pkg_resources import require

require('cothread==2.11')

 

 

# Channel Access python functions: caget, caput and camonitor

# Documentation here: http://www.cs.diamond.ac.uk/docs/docshome/cothread/index.html

# and externally visible here: http://controls.diamond.ac.uk/downloads/python/cothread/2-11-beta/docs/html/index.html

import cothread

from cothread.catools import *

 

 

# get some PV variables

x_readback = caget("BL23I-MO-GRIP-02:X.RBV")

y_readback = caget("BL23I-MO-GRIP-02:Y.RBV")

z_readback = caget("BL23I-MO-GRIP-02:Z.RBV")

grip_readback = caget("BL23I-MO-GRIP-02:GRP.RBV")

 

 

# print the readback values as a float, decimal, string, and integer

print "x, y, z, grip = %f, %d, %s, %i" % (x_readback, y_readback, z_readback, grip_readback)

 

 

def repeat_moves(axis_pv, n_moves, first_pos, second_pos, time_to_move=5, check_limits=True):

    '''caput two values alternately to a pv repeatedly

    axis_pv:        name of the pv

    n_moves:        positive number of repetitions

    first_pos:      first value to send to pv

    second_pos:     second value to send to pv

    time_to_move:   seconds to wait for caput to finish (move can finish early, so overestimate is good)

    check_limits:   defaults to True, check positions to move to are within limits

    '''

 

    # make sure n_moves is a positive number

    assert(n_moves > 0)

 

    # check limits

    if check_limits:

 

        # get motor limits

        lolimit = caget(axis_pv+".LLM")

        hilimit = caget(axis_pv+".HLM")

 

        # check move positions are within limits

        assert(first_pos < hilimit)

        assert(first_pos > lolimit)

        assert(second_pos < hilimit)

        assert(second_pos > lolimit)

 

    # list of readback positions after every caput

    readback_positions = []

 

    # loop through the n_moves

    for x in range(n_moves):

 

        status = caput(axis_pv+'.VAL', first_pos, wait=True, timeout=time_to_move)

        # print status.ok # returns True if caput move was successful

        first_readback_pos = caget(axis_pv+".RBV")

        status = caput(axis_pv+'.VAL', second_pos, wait=True, timeout=time_to_move)

        second_readback_pos = caget(axis_pv+".RBV")

 

        # record the first and second readback positions to the positions list

        readback_positions.append(first_readback_pos)

        readback_positions.append(second_readback_pos)

 

        # print to terminal the progress of the repeated moves

        print "%i\t%f\t%f" % (x, first_readback_pos, second_readback_pos)

 

    # return the positions list

    return readback_positions

 

 

# do the repeat moves, and get a list of the axis positions after each move

list_pos = repeat_moves("XFZ39520:MOTOR", 3, 20, 0, 10)

 

print "number of positions is ", len(list_pos)
