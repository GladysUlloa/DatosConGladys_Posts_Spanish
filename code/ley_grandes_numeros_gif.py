import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import imageio
import os

# Configuración estética
sns.set(style="whitegrid")
plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 16

# Crear carpeta temporal para imágenes
if not os.path.exists("frames"):
    os.makedirs("frames")

# Parámetros
mu = 50       # media poblacional
sigma = 10    # desviación estándar
sample_size = 1000  # total de datos simulados
samples = np.random.normal(mu, sigma, sample_size)

# Inicializar lista para guardar imágenes
filenames = []

# Crear imágenes para cada tamaño de muestra incremental (fluido)
for n in range(10, sample_size+1, 5):  # paso más pequeño para animación continua
    sample_mean = np.mean(samples[:n])

    plt.figure(figsize=(8, 5))

    # Histograma con bordes y estética suave
    sns.histplot(samples[:n],
                 bins=30,
                 kde=True,
                 color="#4C72B0",
                 edgecolor="black",  # borde de las barras
                 linewidth=0.5,
                 alpha=0.7)

    # Línea de la media poblacional
    plt.axvline(mu, color='green', linestyle='--', linewidth=2, label=f'Media poblacional: {mu}')

    # Línea de la media de la muestra actual
    plt.axvline(sample_mean, color='red', linestyle='-', linewidth=2, label=f'Media muestra (n={n}): {sample_mean:.2f}')

    # Estética del gráfico
    plt.title("Ley de los Grandes Números", fontsize=18)
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.legend(loc="upper right", fontsize=10)
    plt.tight_layout()

    # Guardar frame
    filename = f"frames/frame_{n}.png"
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

# Crear GIF continuo
with imageio.get_writer("ley_grandes_numeros.gif", mode='I', duration=0.04) as writer:  # velocidad más suave
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Eliminar frames intermedios
for filename in filenames:
    os.remove(filename)

print("✅ GIF generado con animación continua: ley_grandes_numeros.gif")
