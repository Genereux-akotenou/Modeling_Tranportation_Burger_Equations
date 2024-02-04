# mini projet - schema 3: Lax-Friedrich

import numpy as np
import matplotlib.pyplot as plt

    
# ----------------------------
# Données
# ----------------------------

# U0
def uO(x):
    if (3 <= x <= 4):
        return 1
    return 0

# Dimenssions(Longeur) de la barre
L = 10

# Vitesse
a = 2

# Nombre de neuds
N = 100

# Nombre de Courant
CFL = 0.8

# Pas du maillage
dx = L / (N-1)

# Maillage de la barre
x = np.linspace(0, L, N)
print(x)

# Conditions limites
U = np.array([uO(x[i]) for i in range(N)])

# Temps
temps = 0
tempsArret = 2.5

# pas de temps
dt = (dx * CFL) / a
lamba = (dt * a)/dx
Unew = np.zeros(N)
Uexa = np.zeros(N)


    
# ----------------------------
# Solution exacte
# ----------------------------

# Solution Exacte
def u_exacte(x, t):
    y = (x - (a*t)) % L
    return np.where((3 <= y) & (y <= 4), 1, 0)

# ----------------------------
# Modelisation
# ----------------------------

while (temps < tempsArret):
    for i in range(1, N-1):        
        # Schema de Lax-Friedrich
        Unew[i] = (U[i-1] + U[i+1])/2 - (lamba/2)*(U[i+1] - U[i-1]) 
        
    # Solution exacte
    Uexa = u_exacte(x, temps)
    
    
    Unew[0] = Unew[N-1]
    Unew[N-1] = Unew[N-2]
    
    temps += dt
    U = Unew.copy()

    
    # Plot
    plt.figure(figsize=(20,12))
    plt.ylim(-3, 3)
    plt.plot(x, U, "-r", label=f"Solution approchée, N={N}, t={tempsArret}s")
    plt.plot(x, Uexa, "-b", label="Solution exacte")
    plt.legend(loc='upper right')
    plt.grid()
    plt.pause(0.1)
    
    
    

# ----------------------------
# Erreur du schema
# ----------------------------

diff = Uexa - Unew
err = np.linalg.norm(diff, ord=1)
print(err)