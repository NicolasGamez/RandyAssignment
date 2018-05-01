'''
from Weighted_Graph.classes.WG import Weighted_Graph
from Weighted_Graph.functions.Prims_functions import min_valid_edge
from Weighted_Graph.functions.general_weighted_functions import c
'''
from GroupAssignment import *
from Weighted_Graph import *


def Prims(file , initial_vertex = 0,show = False, cost = False):
    G = Weighted_Graph(file)
    

    if show == True:
        G.draw_graph()
        
    T=({initial_vertex}, [])
    while T[0] != G.vertex_set():
        if show == True:
            G.draw_subgraph(T)
        e = min_valid_edge(G,T)
        T[1].append(e)
        for v in e:
            T[0].add(v)
            
    if show == True:
        G.draw_subgraph(T)
        
    if cost == True:
        cost = 0
        for e in T[1]:
            cost += c(G,e)
        return "Optimal Spanning Tree cost" + str(cost)
    return T

Prims('graph.txt')
