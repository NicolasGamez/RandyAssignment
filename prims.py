from Weighted_Graph import *
from prims_functions import *

G = Weighted_Graph("G.txt")

#Setting up tree
V_T = {0}
E_T= []

T = (V_T,E_T)

def Prims(file , initial_vertex = 0,show = False, cost = False):
    G = Weighted_Graph(file)
    
    if show == True:
        G.draw_graph()
        
    T=({initial_vertex}, [])
    while T[0] != G.vertex_set():
        if show == True:
            G.draw_subgraph(T)
        e = min_valid_edges(G,T)
        T[1].append(e)
        for v in e:
            T[0].add(v)
            
    if show == True:
        G.draw_subgraph(T)
        
    if cost == True:
        cost = 0
        for e in T[1]:
            cost += c(e)
        print( "Optimal Spanning Tree cost: " + str(cost))
    return T


