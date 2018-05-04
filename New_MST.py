from Weighted_Graph import *
from prims_functions import *
from prims import *

G = Weighted_Graph("G.txt")

#Setting up tree
V_T = {0}
E_T= []
T = (V_T,E_T)

print(Prims('G.txt', show = True, cost = True))
