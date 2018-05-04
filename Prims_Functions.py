from Weighted_Graph import *
G = Weighted_Graph("G.txt")
#Setting up tree
V_T = {0}
E_T= []

T = (V_T,E_T)

def c(edge):
    return G.edge_dict()[edge]


def incident_edges(T):
    temp_edges = []
    for e in G.edge_set():
        for v in T[0]:
            if v in e and e not in T[1]:
                temp_edges.append(e)
                
    return temp_edges

def valid_edges(T):
    edges = incident_edges(T)
    temp_edges = []
    for e in edges:
        if e[0] not in T[0] or e[1] not in T[0]:
            temp_edges.append(e)
    return temp_edges

def min_valid_edges(G,T):
    edges = valid_edges(T)
    cost = []
    minimum_edges=[]
    e=0
    #print('minimum edges start', minimum_edges )
    for i in edges:
        #print(c(edges[e]))
        cost.append(c(edges[e]))
        minimum_edges.append(edges[e])
        e+=1
    #print(min(cost))
    #print('minimum edges end', minimum_edges )
    #print('cost', cost)
    minimum = min(cost)
    j=0
    
    for x in cost:
        if minimum == cost[j]:
            return minimum_edges[j]
            break
        j+=1
        
    
    
'''    for x in cost:
        if cost[j] == minimum:
            minimum_edges=[]
'''

#print(min_valid_edges(G,T))
