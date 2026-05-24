# ============================================================
# PROGRAMA DE CIENCIA DE DATOS
# CURSO: ESTADÍSTICA DESCRIPTIVA Y VISUALIZACIÓN DE DATOS
# ============================================================

# ------------------------------------------------------------
# TEMA:
# Análisis Descriptivo del Rendimiento Académico de Estudiantes
# utilizando R Studio
# ------------------------------------------------------------

# ------------------------------------------------------------
# AUTOR:
# PhD(c).Gladys Choque Ulloa
# ------------------------------------------------------------

# ------------------------------------------------------------
# PROYECTO:
# Aplicación de técnicas de estadística descriptiva y
# visualización de datos en un contexto educativo
# ------------------------------------------------------------

# ------------------------------------------------------------
# DATASET:
# Student Academic Performance Dataset
#
# Descripción:
# Dataset enfocado en factores que afectan el rendimiento
# académico de estudiantes:
# - Horas de estudio
# - Asistencia
# - Motivación
# - Recursos educativos
# - Calidad docente
# - Sueño
# - Puntajes previos
# - Factores familiares
# entre otros.
# ------------------------------------------------------------

# ------------------------------------------------------------
# OBJETIVO GENERAL:
# Analizar descriptivamente el rendimiento académico de
# estudiantes mediante medidas estadísticas y visualización
# de datos utilizando R Studio.
# ------------------------------------------------------------

# ------------------------------------------------------------
# OBJETIVOS ESPECÍFICOS:
# 1. Calcular medidas de tendencia central.
# 2. Calcular medidas de dispersión.
# 3. Construir tablas de frecuencia.
# 4. Elaborar histogramas, boxplots y scatterplots.
# 5. Analizar correlaciones mediante mapas de calor.
# 6. Interpretar resultados estadísticos.
# ------------------------------------------------------------

# ============================================================
# 1. INSTALACIÓN DE LIBRERÍAS
# ============================================================

# Instalar paquetes (solo la primera vez)

install.packages("tidyverse")
install.packages("ggplot2")
install.packages("corrplot")
install.packages("dplyr")

# ============================================================
# 2. CARGA DE LIBRERÍAS
# ============================================================

library(readr)
library(tidyverse)
library(ggplot2)
library(corrplot)
library(dplyr)

# ============================================================
# 3. CARGA DEL DATASET
# ============================================================

# IMPORTANTE:
# Colocar el archivo CSV en el mismo directorio del proyecto
# o especificar la ruta completa.

datos <- read_csv("C:/Users/Usuario/Downloads/StudentPerformanceFactors.csv")
view(datos)

# ============================================================
# 4. EXPLORACIÓN INICIAL DEL DATASET
# ============================================================

# Primeras filas
head(datos)

# Últimas filas
tail(datos)

# Estructura del dataset
str(datos)

# Dimensiones
dim(datos)

# Nombres de variables
colnames(datos)

# Resumen estadístico
summary(datos)

# ============================================================
# 5. LIMPIEZA BÁSICA DE DATOS
# ============================================================

# Verificar valores nulos
colSums(is.na(datos))

# ============================================================
# 6. MEDIDAS DE TENDENCIA CENTRAL
# ============================================================

# ------------------------------------------------------------
# MEDIA
# ------------------------------------------------------------

media_exam <- mean(datos$Exam_Score)

cat("Media del puntaje final:", media_exam, "\n")

# ------------------------------------------------------------
# MEDIANA
# ------------------------------------------------------------

mediana_exam <- median(datos$Exam_Score)

cat("Mediana del puntaje final:", mediana_exam, "\n")

# ------------------------------------------------------------
# MODA
# ------------------------------------------------------------

moda_exam <- names(sort(table(datos$Exam_Score),
                        decreasing = TRUE))[1]

cat("Moda del puntaje final:", moda_exam, "\n")

# ============================================================
# 7. MEDIDAS DE DISPERSIÓN
# ============================================================

# ------------------------------------------------------------
# RANGO
# ------------------------------------------------------------

rango_exam <- range(datos$Exam_Score)

cat("Rango del puntaje final:\n")
print(rango_exam)

# ------------------------------------------------------------
# VARIANZA
# ------------------------------------------------------------

varianza_exam <- var(datos$Exam_Score)

cat("Varianza:", varianza_exam, "\n")

# ------------------------------------------------------------
# DESVIACIÓN ESTÁNDAR
# ------------------------------------------------------------

desviacion_exam <- sd(datos$Exam_Score)

cat("Desviación estándar:", desviacion_exam, "\n")

# ============================================================
# 8. TABLAS DE FRECUENCIA
# ============================================================

# ------------------------------------------------------------
# FRECUENCIA ABSOLUTA
# ------------------------------------------------------------

frecuencia_motivacion <- table(datos$Motivation_Level)

cat("Frecuencia absoluta:\n")
print(frecuencia_motivacion)

# ------------------------------------------------------------
# FRECUENCIA RELATIVA
# ------------------------------------------------------------

frecuencia_relativa <- prop.table(frecuencia_motivacion)

cat("Frecuencia relativa:\n")
print(frecuencia_relativa)

# ============================================================
# 9. HISTOGRAMA
# ============================================================

ggplot(datos, aes(x = Exam_Score)) +
  
  geom_histogram(
    binwidth = 2,
    fill = "skyblue",
    color = "black"
  ) +
  
  labs(
    title = "Distribución de Puntajes del Examen",
    x = "Puntaje Final",
    y = "Frecuencia"
  ) +
  
  theme_minimal()

# ============================================================
# 10. BOXPLOT
# ============================================================

ggplot(datos,
       aes(x = Motivation_Level,
           y = Exam_Score,
           fill = Motivation_Level)) +
  
  geom_boxplot() +
  
  labs(
    title = "Puntaje Final según Nivel de Motivación",
    x = "Nivel de Motivación",
    y = "Puntaje Final"
  ) +
  
  theme_minimal()

# ============================================================
# 11. SCATTERPLOT
# ============================================================

ggplot(datos,
       aes(x = Hours_Studied,
           y = Exam_Score)) +
  
  geom_point(
    color = "blue",
    alpha = 0.5
  ) +
  
  geom_smooth(
    method = "lm",
    color = "red"
  ) +
  
  labs(
    title = "Horas de Estudio vs Puntaje Final",
    x = "Horas de Estudio",
    y = "Puntaje Final"
  ) +
  
  theme_minimal()

# ============================================================
# 12. ANÁLISIS DE CORRELACIÓN
# ============================================================

# Seleccionar variables numéricas

numericas <- datos %>%
  select(
    Hours_Studied,
    Attendance,
    Sleep_Hours,
    Previous_Scores,
    Tutoring_Sessions,
    Physical_Activity,
    Exam_Score
  )

# ------------------------------------------------------------
# MATRIZ DE CORRELACIÓN
# ------------------------------------------------------------

correlacion <- cor(numericas)

cat("Matriz de correlación:\n")
print(correlacion)

# ============================================================
# 13. MAPA DE CALOR
# ============================================================

corrplot(
  correlacion,
  method = "color",
  type = "upper",
  addCoef.col = "black",
  tl.col = "black",
  number.cex = 0.7
)

# ============================================================
# 14. INTERPRETACIÓN BÁSICA
# ============================================================

cat("\n")
cat("==================================================\n")
cat("INTERPRETACIÓN GENERAL\n")
cat("==================================================\n")

cat("\n")

cat("- La media representa el promedio general de notas.\n")

cat("- La mediana representa el valor central.\n")

cat("- La desviación estándar muestra la dispersión.\n")

cat("- El histograma permite observar la distribución.\n")

cat("- El boxplot ayuda a detectar valores atípicos.\n")

cat("- El scatterplot permite analizar relaciones.\n")

cat("- El mapa de calor muestra correlaciones entre variables.\n")

cat("\n")

cat("Ejemplo:\n")

cat("Si la correlación entre Hours_Studied y Exam_Score\n")
cat("es positiva, entonces mayores horas de estudio\n")
cat("podrían asociarse con mejores resultados académicos.\n")

# ============================================================
# 15. PREGUNTAS PARA LOS ESTUDIANTES
# ============================================================

cat("\n")
cat("==================================================\n")
cat("PREGUNTAS DE ANÁLISIS\n")
cat("==================================================\n")

cat("\n")

cat("1. ¿Qué variable tiene mayor correlación con Exam_Score?\n")

cat("2. ¿Existen valores atípicos en los puntajes?\n")

cat("3. ¿Qué nivel de motivación presenta mejores notas?\n")

cat("4. ¿Las horas de estudio influyen en el rendimiento?\n")

cat("5. ¿La asistencia parece afectar el puntaje final?\n")

# ============================================================
# 16. CONCLUSIÓN
# ============================================================

cat("\n")
cat("==================================================\n")
cat("CONCLUSIÓN GENERAL\n")
cat("==================================================\n")

cat("\n")

cat("El análisis descriptivo permitió identificar patrones\n")
cat("importantes en el rendimiento académico estudiantil.\n")

cat("Variables como horas de estudio, asistencia y\n")
cat("puntajes previos presentan relación con el desempeño.\n")

cat("Las visualizaciones facilitan la interpretación de\n")
cat("los datos y ayudan en la toma de decisiones.\n")

# ============================================================
# FIN DEL PROYECTO
# ============================================================

