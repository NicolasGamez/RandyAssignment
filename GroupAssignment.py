from Weighted_Graph import *

G = Weighted_Graph("G.txt")

G.draw_graph()

def c(edge):
    return G.edge_dict()[edge]

print("The cost of edge (1,5) is ", c((1,5)))

V_T = {0}
E_T= []

T = (V_T,E_T)

#print("Initial Tree is:", T)

# Find Incident edges
def incident_edges(T):
    temp_edges = []
    for e in G.edge_set():
        for v in T[0]:
            if v in e and e not in T[1]:
                temp_edges.append(e)
                
    return temp_edges
'''
V_T = (0,2,3)
E_T = (0,2),(2,3)
T = (V_T,E_T)

print (incident_edges(T))
'''
# Find Valid edges

def valid_edges(T):
    edges = incident_edges(T)
    temp_edges = []
    for e in edges:
        if e[0] not in T[0] and e[1] not in T[0]:
            edges.append(e)
    return edges

V_T = (0,2,3,4) 
E_T = [(0,2),(2,3),(2,4)]
T = (V_T,E_T)

#print(valid_edges(T))
print (incident_edges(T))

