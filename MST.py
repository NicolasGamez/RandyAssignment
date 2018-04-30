#Not really sure, I believe is for determining which algorithm the user wants?
#Not finished

from Weighted_Graph import *
from prims.py import *

def MST(textfile, show = False, cost = False):
    return Prims(textfile, show, cost)
