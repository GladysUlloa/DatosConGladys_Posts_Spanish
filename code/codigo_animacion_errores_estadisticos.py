# CREACIÓN DE LA GRÁFICA ANIMADA DE LOS ERRORES ESTADÍSTICOS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D  # Para 3D scatter

sns.set(style="whitegrid")

fig = plt.figure(figsize=(15, 18))

# Crear subplots 3D y 2D combinados
ax1 = fig.add_subplot(3, 2, 1)  # histograma normal vs sesgado (2D)
ax2 = fig.add_subplot(3, 2, 2)  # boxplot varianzas similares (2D)
ax3 = fig.add_subplot(3, 2, 3)  # boxplot varianzas diferentes (2D)
ax4 = fig.add_subplot(3, 2, 4, projection='3d')  # multicolinealidad (3D scatter)
ax5 = fig.add_subplot(3, 2, 5)  # tamaño muestra (KDE 2D)
ax6 = fig.add_subplot(3, 2, 6, projection='3d')  # correlación vs causalidad (3D scatter)

# Datos
np.random.seed(0)

normal_data = np.random.normal(loc=0, scale=1, size=1000)
skewed_data = np.random.exponential(scale=1, size=1000)
bins = np.linspace(min(np.min(normal_data), np.min(skewed_data)),
                   max(np.max(normal_data), np.max(skewed_data)), 30)
normal_hist, _ = np.histogram(normal_data, bins=bins)
skewed_hist, _ = np.histogram(skewed_data, bins=bins)

group1 = np.random.normal(loc=5, scale=1, size=100)
group2_equal_var = np.random.normal(loc=5, scale=1.2, size=100)
group2_unequal_var = np.random.normal(loc=5, scale=3.5, size=100)
df_equal = pd.DataFrame({'Grupo': ['A']*100 + ['B']*100,
                         'Valor': np.concatenate([group1, group2_equal_var])})
df_unequal = pd.DataFrame({'Grupo': ['A']*100 + ['B']*100,
                           'Valor': np.concatenate([group1, group2_unequal_var])})

size = 100
X1 = np.random.normal(0,1,size)
X2 = X1 * 0.9 + np.random.normal(0, 0.1, size)
Y = 2*X1 + np.random.normal(0, 1, size)
Z1 = X1 + np.random.normal(0,0.1,size)  # eje z para 3D

means_small = [np.mean(np.random.normal(0,1,10)) for _ in range(200)]
means_large = [np.mean(np.random.normal(0,1,100)) for _ in range(200)]

Z = np.random.normal(0,1,size)
X = Z + np.random.normal(0, 0.1, size)
Y_corr = Z + np.random.normal(0, 0.1, size)
Z_corr = Z + np.random.normal(0, 0.1, size)

def init():
    for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
        ax.clear()
    return []

def update(frame):
    for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
        ax.clear()

    # 1. Histogramas
    ax1.bar(bins[:-1], normal_hist * frame/30, width=np.diff(bins),
            alpha=0.8, label='Normal', align='edge',
            color='#1f77b4', edgecolor='black', linewidth=1)
    ax1.bar(bins[:-1], skewed_hist * frame/30, width=np.diff(bins),
            alpha=0.8, label='No Normal (Sesgada)', align='edge', bottom=normal_hist * frame/30,
            color='#ff7f0e', edgecolor='black', linewidth=1)
    ax1.set_title('1. Distribuciones: Normal vs No Normal', fontsize=14, fontweight='bold')
    ax1.legend()

    # 2a. Boxplot varianzas similares
    if frame >= 10:
        sns.boxplot(x='Grupo', y='Valor', data=df_equal, ax=ax2,
                    palette=['#2ca02c', '#98df8a'], linewidth=2)
        ax2.set_title('2a. Varianzas similares', fontsize=14, fontweight='bold')

    # 2b. Boxplot varianzas diferentes
    if frame >= 10:
        sns.boxplot(x='Grupo', y='Valor', data=df_unequal, ax=ax3,
                    palette=['#d62728', '#ff9896'], linewidth=2)
        ax3.set_title('2b. Varianzas muy diferentes', fontsize=14, fontweight='bold')

    # 3. Multicolinealidad 3D scatter
    n_points = min(frame*4, size)
    ax4.scatter(X1[:n_points], Y[:n_points], Z1[:n_points],
                c='#9467bd', edgecolor='black', s=60, alpha=0.8, label='X1 vs Y')
    ax4.scatter(X2[:n_points], Y[:n_points], Z1[:n_points],
                c='#8c564b', edgecolor='black', s=60, alpha=0.8, label='X2 vs Y')
    ax4.set_title('3. Multicolinealidad (3D)', fontsize=14, fontweight='bold')
    ax4.legend()
    ax4.set_xlabel('X1 / X2')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Z (profundidad)')

    # 4. Tamaño muestra KDE
    alpha_val = min(frame/30, 1)
    sns.kdeplot(means_small, ax=ax5, label='n=10 (alta varianza)', alpha=alpha_val, color='#17becf', linewidth=3)
    sns.kdeplot(means_large, ax=ax5, label='n=100 (menor varianza)', alpha=alpha_val, color='#bcbd22', linewidth=3)
    ax5.set_title('4. Variabilidad media según tamaño muestra', fontsize=14, fontweight='bold')
    ax5.legend()

    # 5. Correlación vs causalidad 3D scatter
    n_points_corr = min(frame*4, size)
    ax6.scatter(X[:n_points_corr], Y_corr[:n_points_corr], Z_corr[:n_points_corr],
                c='#e377c2', edgecolor='black', s=60, alpha=0.8)
    ax6.set_title('5. Correlación no implica causalidad (3D)', fontsize=14, fontweight='bold')
    ax6.set_xlabel('X')
    ax6.set_ylabel('Y')
    ax6.set_zlabel('Z (variable oculta)')

    plt.tight_layout()
    return []

ani = FuncAnimation(fig, update, frames=30, init_func=init, blit=False, interval=150)

# Guardar el gif en directorio actual
writer = PillowWriter(fps=10)
ani.save("errores_estadisticos_animacion.gif", writer=writer)

plt.close()
