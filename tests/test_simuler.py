import numpy as np
from sknetwork.data import linear_graph
from rumeur_reseau.dynamique import simuler


def test_ligne_transmission_certaine():
    """Test de la fonction simuler avec une transmission certaine (p_transmission=1) et pas_max=1."""
    A = linear_graph(10)  # Graphe en ligne de 10 nœuds
    p_transmission = 1.0
    p_saturation = 0.0
    p_oubli = 0.0
    source = 0
    pas_max = 5
    nb_entendus, pas_effectues, propagation_terminee, etats = simuler(A, p_transmission, p_saturation, p_oubli, source, pas_max)
    assert nb_entendus == pas_max+1
    assert pas_effectues == pas_max
    assert not propagation_terminee
