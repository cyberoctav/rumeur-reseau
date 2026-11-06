from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sknetwork.data import erdos_renyi, linear_graph

from rumeur_reseau.dynamique import simuler

FIGURES = Path(__file__).resolve().parent.parent / "figures"
FIGURES.mkdir(exist_ok=True)


def histogramme_distribution_finale(A, nom, p_transmission, p_saturation, p_oubli, pas_max, nb_simulations):
    """Simule le modèle simulation de propagation sur le graphe A et affiche l'histogramme pour savoir si celui-ci s'arrête ou non"""
    resultats = []
    for k in range(nb_simulations):
        entendu = simuler(A, p_transmission, p_saturation, p_oubli, source=None, pas_max=pas_max, trace = False)[0]
        resultats.append(entendu)
    n = A.shape[0]
    plt.hist(resultats, bins=np.arange(0.5, n + 1.5), density=True)
    plt.xlabel('Résultat de la simulation')
    plt.ylabel('Fréquence')
    plt.title(f'Histogramme de la propagation sur {nb_simulations} simulations')
    plt.savefig(FIGURES / f"histogramme_{nom}.pdf", bbox_inches='tight')
    plt.close()

histogramme_distribution_finale(erdos_renyi(100, 4 / 100), "erdos_renyi", p_transmission=0.3, p_saturation=0.2, p_oubli=0.1, pas_max=100, nb_simulations=1000)
histogramme_distribution_finale(linear_graph(100), "linear_graph", p_transmission=0.6, p_saturation=0.2, p_oubli=0.1, pas_max=100, nb_simulations=1000)