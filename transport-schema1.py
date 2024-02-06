# mini projet - schema 1: Schema centré

import numpy as np
import matplotlib.pyplot as plt


# ----------------------------
# Données
# ----------------------------

# Uo
def uO(x):
    if (3 <= x <= 4):
        return 1
    return 0
    
# Dimenssions(Longeur) de la barre
L = 10

# Vitesse
a = 2

# Nombre de neuds
N = 200

# Pas du maillage
dx = L / (N-1)

# Maillage de la barre
x = np.linspace(0, L, N)

# Conditions initiale
U = np.array([uO(x[i]) for i in range(N)])

# Temps
temps = 0
tempsArret = 4.5

# pas de temps
dt = 0.1
lamba = (dt * a)/dx
Unew = np.zeros(N)
Uexa = np.zeros(N)

    
# ----------------------------
# Solution exacte
# ----------------------------

def u_exacte(x, t):
    y = (x - (a*t)) % L
    return np.where((3 <= y) & (y <= 4), 1, 0)

# ----------------------------
# Modelisation
# ----------------------------

while (temps < tempsArret):
    for i in range(1, N-1):
        # Schema centré
        Unew[i] = U[i] - (lamba/2)*(U[i+1] - U[i-1]) 

    # Solution exacte
    Uexa = u_exacte(x, temps)
    
    
    Unew[0] = Unew[N-2]
    Unew[N-1] = Unew[N-2]
    temps += dt
    U = Unew.copy()
    
    # Plot
    plt.figure(figsize=(17,10))
    plt.ylim(-3, 3)
    plt.plot(x, U, "-or", label=f"Solution approchée, N={N}, t={temps}s")
    plt.plot(x, Uexa, "-b", label="Solution exacte")
    plt.legend(loc='upper right')
    plt.grid()
    plt.pause(0.01)
    
# ----------------------------
# Erreur du schema
# ----------------------------

diff = Uexa - Unew
err = np.linalg.norm(diff, ord=1)
print(err)

