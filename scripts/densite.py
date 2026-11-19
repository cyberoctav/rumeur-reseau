
from rumeur_reseau.dynamique import simuler
from sknetwork.data import erdos_renyi
import numpy as np
import matplotlib.pyplot as plt


def experience_densite(nb_simu, nb_densites, nb_individus, seuil, p_transmission, p_saturation, source, pas_max, trace = False):
    densites = np.linspace(0, 0.2, nb_densites)
    moyennes_simu = []
    for i in densites:
        simulations = []
        for j in range(nb_simu):
            A = erdos_renyi(nb_individus, i)
            resultat = simuler(
                A, 
                p_transmission, 
                p_saturation, 
                source, 
                pas_max, 
                trace = False
            )
            if resultat[0] / A.shape[0] >= seuil:
                simulations.append(1)
            else:
                simulations.append(0)
        moyennes_simu.append(np.mean(simulations))
    return densites, moyennes_simu

if __name__ == "__main__":
    x, y = experience_densite(
        nb_simu=100,
        nb_densites=20,
        nb_individus=100,
        seuil=0.7,
        p_transmission=0.1,
        p_saturation=0.2,
        source=None,
        pas_max=100
    )

    plt.plot(x, y, marker="o")
    plt.xlabel("Probabilité de connexion")
    plt.ylabel("Probabilité de diffusion large")
    plt.show()

