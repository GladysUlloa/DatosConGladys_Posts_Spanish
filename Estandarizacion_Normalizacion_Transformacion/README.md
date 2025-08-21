# 𝗘𝘀𝘁𝗮𝗻𝗱𝗮𝗿𝗶𝘇𝗮𝗰𝗶𝗼́𝗻, 𝗡𝗼𝗿𝗺𝗮𝗹𝗶𝘇𝗮𝗰𝗶𝗼́𝗻 𝘆 𝗧𝗿𝗮𝗻𝘀𝗳𝗼𝗿𝗺𝗮𝗰𝗶𝗼́𝗻 𝗱𝗲 𝗗𝗮𝘁𝗼𝘀: 𝗖𝗼𝗻𝗰𝗲𝗽𝘁𝗼𝘀 𝗖𝗹𝗮𝘃𝗲 𝗲𝗻 𝗖𝗶𝗲𝗻𝗰𝗶𝗮 𝗱𝗲 𝗗𝗮𝘁𝗼𝘀 𝘆 𝗘𝘀𝘁𝗮𝗱𝗶́𝘀𝘁𝗶𝗰𝗮 📊

Cuando trabajamos con datos, una de las primeras preguntas que debemos hacernos es: **¿mis variables están listas para ser analizadas o modeladas?** 🤔

Muchas veces, los datos que recolectamos tienen diferentes escalas, distribuciones o incluso unidades de medida, lo que puede distorsionar los resultados y generar conclusiones poco confiables.

👉 Imagina que comparas estaturas medidas en metros con otras en centímetros, o ingresos expresados en dólares frente a reales. Sin un proceso de estandarización o normalización, el modelo daría más peso a ciertas variables solo por la escala en la que están medidas, no por su importancia real.

Aquí entran en juego tres conceptos que todo profesional de datos debe dominar:

### ✅ Estandarización
Consiste en centrar los datos en torno a la media y ajustarlos según la desviación estándar. Este proceso es crucial cuando trabajamos con algoritmos sensibles a la escala (ejemplo: regresión logística, PCA o máquinas de soporte vectorial).

### ✅ Normalización
Transforma los valores para que estén dentro de un rango fijo, generalmente entre [0,1]. Es muy útil en redes neuronales y métodos basados en distancias (ejemplo: k-means o k-NN), donde las variables con valores grandes podrían dominar el análisis.

### ✅ Transformación
Se aplica cuando necesitamos modificar la forma de la distribución, como en el caso de variables con asimetría o presencia de outliers. Usar logaritmos, raíces cuadradas o Box-Cox permite suavizar estas diferencias y hacer los datos más manejables.

En otras palabras, estos pasos no son simples “preparaciones técnicas”. Son decisiones estratégicas que determinan si nuestro modelo será robusto, interpretativo y capaz de generar valor. Una mala preparación puede llevar a resultados sesgados, baja precisión y conclusiones equivocadas.

## Visualización de los efectos

Aquí puedes ver un ejemplo animado de cómo cambia la distribución de los datos con estandarización, normalización y transformación:
![Gráficas de transformación de datos](https://github.com/GladysUlloa/DatosConGladys_Posts_Spanish/blob/1dc7ef17ecbf681c05d6f34d4851d04f88c3221c/Estandarizacion_Normalizacion_Transformacion/Grafica_de_Estandarizacion_Normalizacion_Transformacion.gif?raw=true)

🚀 La buena práctica es siempre **visualizar antes y después** de aplicar estas técnicas: histogramas, curvas de densidad y boxplots nos permiten comprender cómo cambia la información y verificar si el ajuste cumple con el objetivo.

### En resumen
- ✔ La normalización nivela escalas.  
- ✔ La estandarización centra y ajusta la variabilidad.  
- ✔ La transformación optimiza la distribución.  

Sin estas técnicas, incluso el modelo más avanzado puede fracasar.

---

⚛️ Te invito a leer el artículo completo en mi blog:  
🔗 [Artículo completo](https://goo.su/4llIio)

▶️ Sígueme en mis redes sociales para más contenido de datos:  
🔗 [Datos con Gladys](https://lnkd.in/e6h_BTa3)

---

✍️ Si este contenido te resultó útil, compártelo con tu comunidad.

---

#DataScience #DataVisualization #Statistics #MachineLearning #DatosConGladys
