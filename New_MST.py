# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:36:40 2018

@author: rakix
"""

from Prim import Prims
from Kruskals import Kruskals 

def MST(textfile, solver = 'Prims', , cost = False, show = False):
    if solcer == 'Kruskals':
        return Kruskals(textfile, cost, show)
    else:
        return Prims(textfile, cost, show)
