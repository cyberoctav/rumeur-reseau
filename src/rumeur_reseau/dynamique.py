import numpy as np 
import matplotlib.pyplot as plt




def simuler(A, p_transmission, p_saturation, p_oubli, source, pas_max, trace = False):
    assert pas_max > 0, "pas_max doit être supérieur à 0"
    tableau = None 
    n = A.shape[0]
    etats = np.zeros(n)
    if source is None:
        source = np.random.randint(0,n)
    etats[source] = 1
    deja_entendu=np.zeros(n)
    deja_entendu[source]=True 
    pas = 0
    if trace :
        tableau = np.zeros((pas_max+1,n))
        tableau[0] = etats
    for j in range(pas_max):
        propagateur = np.where(etats == 1)[0] # récupère un tableau des indices des propagateurs
        if propagateur.size == 0 :
            break
        for i in propagateur:
            voisins = A[i].indices # récupère un tableau des indices des voisins du propagateur i
            for v in voisins:
                if etats[v] == 0: # si le voisin est ignorant
                    if np.random.rand() < p_transmission: # transmission de la rumeur
                        etats[v] = 1
                        deja_entendu[v] = True
            if np.random.rand() < p_saturation: # saturation du propagateur
                etats[i] = 2
        for p in np.where(etats == 2)[0]: # pour chaque propagateur saturé
            if np.random.rand() < p_oubli: # oubli de la rumeur
                etats[p] = 0
        if trace : 
            tableau[pas] = etats
        pas += 1

    return int(deja_entendu.sum()), pas, (propagateur.size == 0), etats, tableau 


def simuler_dementi(A, p_transmission, p_saturation, p_oubli, p_dementi, source, source_dementi, pas_max, trace = False):
    assert pas_max > 0, "pas_max doit être supérieur à 0"
    tableau = None 
    n = A.shape[0]
    etats = np.zeros(n)
    if source is None:
        source = np.random.randint(0,n)
    if source_dementi is None:
        source_dementi = np.random.randint(0,n)
        while source_dementi == source:
            source_dementi = np.random.randint(0,n)
    etats[source] = 1
    deja_entendu=np.zeros(n)
    deja_entendu[source]=True 
    deja_dementi = np.zeros(n)
    deja_dementi[source_dementi]=True
    etats[source_dementi] = 3
    pas = 0
    if trace :
        tableau = np.zeros((pas_max+1,n))
        tableau[0] = etats
    for j in range(pas_max):
        propagateur = np.where(etats == 1)[0] # récupère un tableau des indices des propagateurs
        if propagateur.size == 0 :
            break
        for i in propagateur:
            voisins = A[i].indices # récupère un tableau des indices des voisins du propagateur i
            for v in voisins:
                if etats[v] == 0: # si le voisin est ignorant
                    if np.random.rand() < p_transmission: # transmission de la rumeur
                        etats[v] = 1
                        deja_entendu[v] = True
            if np.random.rand() < p_saturation: # saturation du propagateur
                etats[i] = 2
        sature = np.where(etats == 2)[0]
        for p in sature: # pour chaque propagateur saturé
            if np.random.rand() < p_oubli: # oubli de la rumeur
                etats[p] = 0
        dementi = np.where(etats == 3)[0]
        for k in dementi: 
            voisins = A[k].indices 
            for v in voisins :
                if etats[v] == 2 :
                    if np.random.rand() < p_dementi : 
                        etats[v] = 3
            if np.random.rand() < p_saturation: # saturation du propagateur
                etats[k] = 4

        if trace : 
            tableau[pas] = etats
        pas += 1
    
    return int(deja_entendu.sum()), int(deja_dementi.sum()), pas, (propagateur.size == 0), etats, tableau 
