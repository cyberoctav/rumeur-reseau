from pathlib import Path

from rumeur_reseau.dynamique import simuler_dementi
from sknetwork.data import albert_barabasi
from sknetwork.visualization import visualize_graph
from sknetwork.embedding import Spring
import numpy as np 
#paramètres
p_transmission = 0.3
p_dementi  = 0.2
p_oubli = 0.1
p_saturation = 0.2
p_saturation_dementi = 0.3
pas_max = 50
n = 100


FIGURES = Path(__file__).resolve().parent.parent / "figures"
FIGURES.mkdir(exist_ok=True)

def figure_evolution_sociaux(A, nom, p_transmission, p_saturation, p_saturation_dementi, p_oubli, p_dementi, pas_max):
    dossier = FIGURES/ nom
    dossier.mkdir(parents = True, exist_ok=True)
    for ancien in dossier.glob("*.svg"):
        ancien.unlink()
    spring = Spring()
    positions = spring.fit_transform(A)
    degres = np.argsort([int(A.indptr[i+1]-A.indptr[i]) for i in range(A.shape[0])])
    source_rumeur = degres[-1]
    print(source_rumeur)
    source_dementi = degres[-2]
    print(source_dementi)
    tableau = simuler_dementi(A, p_transmission, p_saturation, p_oubli, p_dementi, p_saturation_dementi, source_rumeur, source_dementi, pas_max, trace=True)[5]
    for i in range(len(tableau)):
        image = visualize_graph(
            A, 
            position = positions,
            labels = tableau[i].astype(int),
            label_colors=['lightgray', 'red', 'orange', 'green', 'purple'], # gris clair : ignorant, rouge : propagateur, orange : propagateur saturé, vert : démenti, violet : démenti saturé
            node_size=7,
            width=650,
            height=450
        )
        chemin = dossier / f"pas_{i}.svg"
        chemin.write_text((image))

figure_evolution_sociaux(albert_barabasi(n,2), "albert_barabasi",p_transmission, p_saturation, p_oubli, p_dementi, p_saturation_dementi, pas_max)
