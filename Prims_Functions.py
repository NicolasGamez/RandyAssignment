from Weighted_Graph import *
G = Weighted_Graph("G.txt")

V_T = {0}
E_T= []
T = (V_T,E_T)

G.draw_graph()

# Prints Cost of edge

def c(edge):
    return G.edge_dict()[edge]

#print("The cost of edge (1,5) is ", c((1,5)))
#print("Initial Tree is:", T)

# Find Incident edges

def incident_edges(T):
    temp_edges = []
    for e in G.edge_set():
        for v in T[0]:
            if v in e and e not in T[1]:
                temp_edges.append(e)
                
    return temp_edges

# Find Valid edges

def valid_edges(T):
    edges = incident_edges(T)
    temp_edges = []
    for e in edges:
        if e[0] not in T[0] and e[1] not in T[0]:
            edges.append(e)
    return edges
