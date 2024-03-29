# mini projet - schema 2: Décentré amont

import numpy as np
import matplotlib.pyplot as plt

    
# ----------------------------
# Données
# ----------------------------

# U0
def uO(x):
    if x < 2:
        return 0.4
    return 0.1

# Dimenssions(Longeur) de la barre
L = 6

# Nombre de neuds
N = 200

# Nombre de Courant
CFL = 0.8

# Pas du maillage
dx = L / (N-1)

# Maillage de la barre
x = np.linspace(0, L, N)

# Conditions initiales
U = np.array([uO(x[i]) for i in range(N)])

# Temps
temps = 0
tempsArret = 4.5

# init
Unew = np.zeros(N)
Uexa = np.zeros(N)
    
# ----------------------------
# Solution exacte
# ----------------------------

# Solution Exacte
def u_exacte(x, t):
    y = (x - 2) / t
    return np.where(y < 0.25, 0.4, 0.1)

def F(u):
    return (u*u) / 2

# ----------------------------
# Modelisation
# ----------------------------

while (temps < tempsArret):
    # pas de temps
    dt = (CFL * dx) / max(np.abs(U))
    lamba = dt/dx
    
    for i in range(1, N-1):
        # Décentré amont
        Unew[i] = U[i] - lamba*(F(U[i]) - F(U[i-1])) 

    # Solution exacte
    Uexa = u_exacte(x, temps)
    
    
    Unew[0] = Unew[1]
    Unew[N-1] = Unew[N-2]
    
    temps += dt
    U = Unew.copy()

    
    # Plot
    plt.figure(figsize=(17,10))
    plt.ylim(-0.5, 1)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.plot(x, U, "-r", label=f"Solution approchée, N={N}, t={round(temps, 4)}s")
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


