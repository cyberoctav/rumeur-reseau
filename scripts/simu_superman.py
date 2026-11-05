from math import *
import numpy as np
from sknetwork.data import erdos_renyi
from sknetwork.visualization import visualize_graph
from IPython.display import SVG, display


n = 100
p1 = 0.3 # probabilités de transmettre la rumeur
p2 = 0.3 # probabilités de dementir la rumeur
k = 1 # nombre de personne propagateur et de superman au départ
s = 100 # nombre de simulation

p_graphe = 4

Tbis = np.random.normal(4,sqrt(2),n)
T = np.zeros(n)
for i in range(n):
    if int(Tbis[i]) <=0 : 
        Tbis[i] = 1
    elif int(Tbis[i]) >=4 :    
        Tbis[i] = 4
        
    T[i] = int(Tbis[i])


# 0 : ignorant
# 1 : propagateur
# 2 : propagateur saturé
# 3 : superman
# 4 : superman saturé



S = np.zeros(n)
a = np.random.choice(n, 2, replace=False)
S[a[0]] = 1
S[a[1]] = 3

# S : statut des personnes


P = np.zeros([2,n])
for i in range(n):
    P[0,i] = S[i]
    P[1,i] = T[i]


G = erdos_renyi(n, p_graphe / n)

# while np.sum(P[0, :] == 1) > 0: pour tester jusqu'a plus de propagateur
for z in range(s):

    propagateurs = np.where(P[0, :] == 1)[0]

    for j in propagateurs:

        v1 = G[j].indices
        for i in v1:

            if P[0,i] == 0:
                X = np.random.random()
                if X < p1 and k < n:
                    
                    P[0,i] = 1

        P[1,j] = P[1,j] - 1

        if P[0,j] == 1 and P[1,j] == 0:
                P[0,j] = 2


    superman = np.where(P[0, :] == 3)[0]
    for j in superman:
    
        v1 = G[j].indices
        for i in v1:
            if P[0,i] == 0:
                X = np.random.random()
                if X < p2 and k < n:
                        
                    P[0,i] = 3
            
        P[1,j] = P[1,j] - 1
            
        if P[0,j] == 3 and P[1,j] == 0:
            P[0,j] = 4
                 


print(np.sum(P[0,:] == 4))
print(np.sum(P[0,:] == 3))
print(np.sum(P[0,:] == 2))
print(np.sum(P[0,:] == 1))
print(np.sum(P[0,:] == 0))

image = visualize_graph(
    G,
    labels=P[0, :].astype(int),
    label_colors=['lightgray', 'red', 'orange','blue','green'],
    node_size=7,
    width=650,
    height=450
)

display(SVG(image))