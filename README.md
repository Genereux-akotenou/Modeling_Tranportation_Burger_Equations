# Modeling_Tranportation_Burger_Equations
#### Étude et application de quelques schémas aux différences finies pour deux lois de conservation
On souhaite étudier, appliquer et voir le comportement de quelques schémas aux différences finies pour deux équations relevant de lois de conservation 1D définies sur un domaine Ω = [0, L].

# Contribution
- Saturné AYIDEGNON
- Généreux AKOTENOU

<!-- On souhaite étudier, appliquer et voir le comportement de quelques schémas aux différences finies pour deux équations relevant de lois de conservation 1D définies sur un domaine Ω = [0, L].

#### 1. Equation de transport
On considère tout d’abord l’équation de transport soumise à des conditions aux limites périodiques :

$
\begin{cases}
\frac{\partial u}{\partial t} + a \frac{\partial u}{\partial x} = 0 \quad \forall x \in (0, L), \forall t > 0 \\
u(x, t = 0) = u_0(x) \quad \forall x \in [0, L] \\
u(0, t) = u(L, t), \frac{\partial u}{\partial x}(L, t) = 0 \quad \forall t > 0
\end{cases}
$

1. A l’aide de la méthode des caractéristiques, déterminer la solution exacte $u(x, t)$ du problème.

2. Étudier la consistance, la stabilité et la convergence de chacun des schémas numériques suivants :
   - Schéma 1 (centré) : $u_{n+1,j} - u_{n,j} \frac{\Delta t}{2} + a \frac{u_{n,j+1} - u_{n,j-1}}{2\Delta x} = 0$
   - Schéma 2 (décentré) : $u_{n+1,j} - u_{n,j} \frac{\Delta t}{2} + a \frac{u_{n,j} - u_{n,j-1}}{\Delta x} = 0$ si $a > 0$, $u_{n+1,j} - u_{n,j} \frac{\Delta t}{2} + a \frac{u_{n,j+1} - u_{n,j}}{\Delta x} = 0$ si $a < 0$
   - Schéma 3 (Lax-Friedrichs) : $u_{n+1,j} - \frac{1}{2}(u_{n,j-1} + u_{n,j+1}) \frac{\Delta t}{2} + a \frac{u_{n,j+1} - u_{n,j-1}}{2\Delta x} = 0$
   - Schéma 4 (Lax-Wendroff) : $u_{n+1,j} - u_{n,j} \frac{\Delta t}{2} + a \frac{u_{n,j+1} - u_{n,j-1}}{2\Delta x} - \frac{a^2}{2}\Delta t \left(\frac{u_{n,j-1} - 2u_{n,j} + u_{n,j+1}}{\Delta x^2}\right) = 0$

3. Implémenter chacun des schémas numériques pour évaluer la solution approchée, puis comparer cette solution avec la solution exacte. (Tracer les solutions aux temps physiques $t_1 = 2.5$ s et $t_2 = 4.5$ s en testant sur deux maillages différents formés de $N = 100$ et $N = 200$ points. Interpréter les résultats.

4. Évaluer l’erreur en norme $L^1$ de la solution numérique obtenue par chaque schéma au temps $t_1 = 2.5$ s et pour $N = 100$. Interpréter.

##### Données :
$L = 10$ m , $a = 2$ m/s , $u_0(x) = 1$ pour $3$ m ≤ $x$ ≤ $4$ m et $0$ ailleurs.
Nombre de Courant : $CFL = 0.8$.

#### 2. Equation de Burgers
On considère maintenant l’équation de Burgers suivante :

$
\begin{cases}
\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = 0 \quad \forall x \in (0, L), \forall t > 0 \\
u(x, t = 0) = u_0(x) \quad \forall x \in [0, L] \\
\frac{\partial u}{\partial x}(0, t) = \frac{\partial u}{\partial x}(L, t) = 0 \quad \forall t > 0
\end{cases}
$

5. Reprendre les questions 1), 3) et 4).

##### Données :
$L = 6$ m , $u_0(x) = 0.4$ pour $x < 2$ m et $0.1$ ailleurs. $CFL = 0.8$. -->
