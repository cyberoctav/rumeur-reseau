
from pathlib import Path
import numpy as np
from sknetwork.data import erdos_renyi, linear_graph
from sknetwork.visualization import visualize_graph
from sknetwork.embedding import Spring

from rumeur_reseau.dynamique import simuler

FIGURES = Path(__file__).resolve().parent.parent / "figures"
FIGURES.mkdir(exist_ok=True)

#paramètres
p_transmission = 0.3
p_oubli = 0.1
p_saturation = 0.2
pas_max = 100
n = 30
p = 4


def figure_simuler_modele(A, nom, p_transmission, p_saturation, p_oubli, pas_max):
    spring = Spring()
    positions = spring.fit_transform(A)
    etats = simuler(A, p_transmission, p_saturation, p_oubli, source=None, pas_max=pas_max, trace = False)[3]
    image = visualize_graph(
        A,
        position=positions,
        labels=etats.astype(int),
        label_colors=['lightgray', 'red', 'orange'], # gris clair pour ignorant, rouge pour propagateur, orange pour saturé
        node_size=7,
        width=650,
        height=450
    )

    chemin = FIGURES / f"{nom}.svg"
    chemin.write_text((image))


figure_simuler_modele(erdos_renyi(n, p / n), "erdos_renyi", p_transmission, p_saturation, p_oubli, pas_max)
figure_simuler_modele(linear_graph(n), "linear_graph", p_transmission, p_saturation, p_oubli, pas_max)



def figure_simuler_modele_trace(A, nom, p_transmission, p_saturation, p_oubli, pas_max, trace):
    spring = Spring()
    positions = spring.fit_transform(A)
    nb_entendus, pas_effectues, propagation_terminee, etats, tableau = simuler(A, p_transmission, p_saturation, p_oubli, source=None, pas_max=pas_max, trace = trace)
    for i in range(len(tableau)):
        image = visualize_graph(
            A,
            position=positions,
            labels=tableau[i].astype(int),
            label_colors=['lightgray', 'red', 'orange'], # gris clair pour ignorant, rouge pour propagateur, orange pour saturé
            node_size=7,
            width=650,
            height=450
        )

        chemin = FIGURES / f"{nom}_{i}.svg"
        chemin.write_text((image))



figure_simuler_modele_trace(erdos_renyi(n, p / n), "erdos_renyi_trace", p_transmission, p_saturation, p_oubli, pas_max, trace = True)
figure_simuler_modele_trace(linear_graph(n), "linear_graph_trace", p_transmission, p_saturation, p_oubli, pas_max, trace = True)