# 🧪📉 ¿QUÉ ES EL P-VALOR (Y POR QUÉ ES TAN IMPORTANTE)? 🧪📉

En análisis de datos y estadística, tomar decisiones basadas en evidencia —y no solo en intuición— es fundamental.  
Aquí entra el **p-valor**, una herramienta estadística clave para evaluar si los patrones observados en los datos podrían haberse generado por azar.

---

## 🔎 ¿QUÉ ES EL P-VALOR?

El **p-valor** es la **probabilidad** de obtener un resultado tan extremo como el observado (o más), **suponiendo que la hipótesis nula sea cierta**.

> Es decir, nos indica cuán compatibles son nuestros datos con un escenario donde “nada ha cambiado” o “no hay efecto real”.

---

## 🎯 ¿PARA QUÉ SE UTILIZA?

En la práctica, el p-valor se usa para:

✅ Evaluar si un nuevo modelo mejora significativamente frente al anterior.  
✅ Validar si una política, tratamiento o intervención tiene un efecto real.  
✅ Comparar grupos (clientes, pacientes, procesos) en contextos de negocio, salud, industria, etc.  
✅ Respaldar decisiones basadas en evidencia: A/B testing, ensayos clínicos, experimentos, etc.

---

## 🔖 ¿CÓMO SE USA?

📌 Si el p-valor es **pequeño** (por ejemplo, menor a 0.05), indica que el resultado es poco probable bajo la hipótesis nula. → Hay evidencia para **rechazarla**.  
📌 Si el p-valor es **grande**, los datos no son tan sorprendentes bajo la hipótesis nula. → **No se rechaza** la hipótesis.

> 💡 Un p-valor pequeño sugiere que los datos observados difícilmente ocurrirían si no hubiera ningún efecto o diferencia real.

---

## 🚫 ¿QUÉ NO ES EL P-VALOR?

❌ No es la probabilidad de que la hipótesis sea cierta o falsa.  
❌ No te dice si un efecto es importante o útil en la práctica.  
❌ No sustituye el juicio estadístico ni el conocimiento del contexto.

---

## 📊 ¿POR QUÉ ES TAN ÚTIL EN CIENCIA DE DATOS?

Porque nos ayuda a:

☑ Evaluar si los resultados de un modelo o experimento son **estadísticamente significativos**.  
☑ Evitar caer en conclusiones impulsivas o sesgadas.  
☑ Respaldar decisiones con **rigurosidad cuantitativa**.

🎯 Desde A/B testing en productos hasta validación de modelos predictivos, el p-valor conecta la **estadística** con la **toma de decisiones basada en datos**.

---

## 🎞️ Visualización del p-valor

![Visualización p-valor](P-Valor.gif)

Puedes ver o descargar el GIF aquí:  
👉 [P-Valor.gif](P-Valor.gif)

📌 **Descripción**:  
Esta animación muestra una **distribución normal** donde el área roja representa la probabilidad (p-valor) de obtener un valor tan extremo como **z = 1.96** bajo la hipótesis nula.  
El área azul refleja la simetría de la cola opuesta. Es ideal para visualizar cómo tomamos decisiones estadísticas con base en la rareza de los datos observados.

🎬 Puedes encontrar el código fuente de esta animación aquí:  
👉 [`code/manim_pvalor.py`](code/manim_pvalor.py)

---

## ▶️ ¿Cómo generar esta animación?

Instala las dependencias:

```bash
pip install -r requirements.txt
