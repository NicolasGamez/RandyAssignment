from Weighted_Graph import *
G = Weighted_Graph("G.txt")


V_T = {0}                       #Setting up tree
E_T= []
T = (V_T,E_T)

def c(edge):                    #Finds the cost of an edgeset
    return G.edge_dict()[edge]


def incident_edges(T):          #Find the edges that are touching
    temp_edges = []
    for e in G.edge_set():
        for v in T[0]:
            if v in e and e not in T[1]:
                temp_edges.append(e)
                
    return temp_edges

def valid_edges(T):             #Finds the edges that are not used
    edges = incident_edges(T)
    temp_edges = []
    for e in edges:
        if e[0] not in T[0] or e[1] not in T[0]:
            temp_edges.append(e)
    return temp_edges

def min_valid_edges(G,T):       #Finds the lowest cost of the valid edge sets 
    edges = valid_edges(T)
    costs = []                  #List to store the costs of each valid edge set
    minimum_edges=[]            #List to store the corresponding edge set
    e=0
    for i in edges:             #Builds Cost list and Minimum_edges simultaneously
        costs.append(c(edges[e]))
        minimum_edges.append(edges[e])
        e+=1
    minimum = min(costs)         #Finds the minimum value of the cost List
    j=0
 
    for x in costs:              #Finds the corresponding edgeset in Minimum_edges
        if minimum == costs[j]:
            return minimum_edges[j]
            break
        j+=1
