from Weighted_Graph import *
from prims_functions import *
from prims import *

G = Weighted_Graph("G.txt")

print(Prims('G.txt', show = True, cost = True))
