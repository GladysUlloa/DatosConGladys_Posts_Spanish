import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Datos distribuciones
n_binom, p_binom = 10, 0.5
x_binom = np.arange(0, n_binom + 1)
y_binom = [round(math.comb(n_binom, k) * (p_binom ** k) * ((1 - p_binom) ** (n_binom - k)), 2) for k in x_binom]

mu_pois = 3
x_pois = np.arange(0, 11)
y_pois = [round((mu_pois ** k) * math.exp(-mu_pois) / math.factorial(k), 2) for k in x_pois]

p_geo = 0.3
x_geo = np.arange(1, 11)
y_geo = [round((1 - p_geo) ** (k - 1) * p_geo, 2) for k in x_geo]

N, K, n_sample = 50, 20, 10
x_hiper = list(range(max(0, n_sample - (N - K)), min(K, n_sample) + 1))
y_hiper = [round((math.comb(K, k) * math.comb(N - K, n_sample - k)) / math.comb(N, n_sample), 2) for k in x_hiper]

r, p_nb = 3, 0.3
x_nb = np.arange(r, 21)
y_nb = [round(math.comb(k - 1, r - 1) * (p_nb ** r) * ((1 - p_nb) ** (k - r)), 2) for k in x_nb]

x_norm = np.linspace(-4, 4, 100)
y_norm = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_norm ** 2)

fig, axs = plt.subplots(2, 3, figsize=(18, 10), dpi=200)
fig.suptitle('Distribuciones de Probabilidad', fontsize=22, fontweight='bold')

titles = [
    "Binomial (n=10, p=0.5)",
    "Poisson (μ=3)",
    "Geométrica (p=0.3)",
    "Hipergeométrica (N=50, K=20, n=10)",
    "Binomial Negativa (r=3, p=0.3)",
    "Normal estándar (0,1)"
]

x_labels = [
    "Número de éxitos",
    "Número de eventos",
    "Ensayos hasta éxito",
    "Éxitos en muestra",
    "Ensayos hasta r éxitos",
    "Valores"
]

colors = [
    (0.2, 0.4, 0.7, 0.6),
    (1.0, 0.6, 0.2, 0.6),
    (0.7, 0.2, 0.3, 0.6),
    (0.9, 0.8, 0.3, 0.6),
    (0.3, 0.7, 0.4, 0.6),
    (0.5, 0.4, 0.7, 1.0)
]

def animate(frame):
    max_frames = 30
    
    frame_binom = min(frame, len(x_binom))
    frame_pois = min(frame, len(x_pois))
    frame_geo = min(frame, len(x_geo))
    frame_hiper = min(frame, len(x_hiper))
    frame_nb = min(frame, len(x_nb))
    frame_norm = min(frame*4, len(x_norm))
    
    axs[0,0].clear()
    axs[0,0].bar(
        x_binom[:frame_binom], y_binom[:frame_binom],
        color=colors[0], edgecolor='black', linewidth=1, alpha=0.7
    )
    axs[0,0].set_title(titles[0], fontsize=14, fontweight='medium')
    axs[0,0].set_xlabel(x_labels[0], fontsize=12)
    axs[0,0].set_ylabel('Probabilidad', fontsize=12)
    axs[0,0].set_ylim(0, max(y_binom)*1.2)
    axs[0,0].grid(True, alpha=0.3)
    axs[0,0].set_facecolor('#fafafa')

    axs[0,1].clear()
    axs[0,1].bar(
        x_pois[:frame_pois], y_pois[:frame_pois],
        color=colors[1], edgecolor='black', linewidth=1, alpha=0.7
    )
    axs[0,1].set_title(titles[1], fontsize=14, fontweight='medium')
    axs[0,1].set_xlabel(x_labels[1], fontsize=12)
    axs[0,1].set_ylabel('Probabilidad', fontsize=12)
    axs[0,1].set_ylim(0, max(y_pois)*1.2)
    axs[0,1].grid(True, alpha=0.3)
    axs[0,1].set_facecolor('#fafafa')

    axs[0,2].clear()
    axs[0,2].bar(
        x_geo[:frame_geo], y_geo[:frame_geo],
        color=colors[2], edgecolor='black', linewidth=1, alpha=0.7
    )
    axs[0,2].set_title(titles[2], fontsize=14, fontweight='medium')
    axs[0,2].set_xlabel(x_labels[2], fontsize=12)
    axs[0,2].set_ylabel('Probabilidad', fontsize=12)
    axs[0,2].set_ylim(0, max(y_geo)*1.2)
    axs[0,2].grid(True, alpha=0.3)
    axs[0,2].set_facecolor('#fafafa')

    axs[1,0].clear()
    axs[1,0].bar(
        x_hiper[:frame_hiper], y_hiper[:frame_hiper],
        color=colors[3], edgecolor='black', linewidth=1, alpha=0.7
    )
    axs[1,0].set_title(titles[3], fontsize=14, fontweight='medium')
    axs[1,0].set_xlabel(x_labels[3], fontsize=12)
    axs[1,0].set_ylabel('Probabilidad', fontsize=12)
    axs[1,0].set_ylim(0, max(y_hiper)*1.2)
    axs[1,0].grid(True, alpha=0.3)
    axs[1,0].set_facecolor('#fafafa')

    axs[1,1].clear()
    axs[1,1].bar(
        x_nb[:frame_nb], y_nb[:frame_nb],
        color=colors[4], edgecolor='black', linewidth=1, alpha=0.7
    )
    axs[1,1].set_title(titles[4], fontsize=14, fontweight='medium')
    axs[1,1].set_xlabel(x_labels[4], fontsize=12)
    axs[1,1].set_ylabel('Probabilidad', fontsize=12)
    axs[1,1].set_ylim(0, max(y_nb)*1.2)
    axs[1,1].grid(True, alpha=0.3)
    axs[1,1].set_facecolor('#fafafa')

    axs[1,2].clear()
    axs[1,2].plot(
        x_norm[:frame_norm], y_norm[:frame_norm],
        color=colors[5], lw=2.5
    )
    axs[1,2].set_title(titles[5], fontsize=14, fontweight='medium')
    axs[1,2].set_xlabel(x_labels[5], fontsize=12)
    axs[1,2].set_ylabel('Probabilidad', fontsize=12)
    axs[1,2].set_ylim(0, max(y_norm)*1.2)
    axs[1,2].grid(True, alpha=0.3)
    axs[1,2].set_facecolor('#fafafa')

ani = animation.FuncAnimation(fig, animate, frames=30, interval=150, repeat=False)

ani.save('distribuciones_animadas_profesional_nitido_mejorado.gif', writer='pillow', fps=10, dpi=200)

print("Animación guardada como 'distribuciones_animadas_profesional_nitido_mejorado.gif'")
plt.close()
