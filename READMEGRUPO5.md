 # Readme

 ## Supervivientes del accidente TITANIC

### Descripcion 
 Este proyecto tiene como objetivo investigar y visualizar los datos relacionados con el hundimiento del Titanic, una de las mayores tragedias marítimas de la historia. Se explorarán factores como las características de los pasajeros (edad, sexo, clase social), la ubicación de las cabinas, y su relación con la supervivencia.

--Cambios Alex

# 🌌 Análisis Titanic

Bienvenido a **Análisis Titanic**, un proyecto diseñado para realizar análisis estadísticos de un conjunto de datos — el legendario Titanic. Este proyecto también tiene como objetivo reforzar prácticas de control de versiones con Git y GitHub. 🚀

---

## 🔍 Objetivos del Proyecto

1. Realizar análisis estadísticos del archivo CSV con información de los pasajeros del Titanic.
2. Visualizar patrones y tendencias a partir de los datos.
3. Practicar técnicas de versionado de código con Git y GitHub.

---

¿Que os parece el cambio chic@s?
>>>>>>> 3d340bbba9fcf1f6b1dd9a2c1b7b05b95aa481b5

-- cambios miguel 
## 1.

El objetivo principal de este análisis es comprender qué factores influyeron en la supervivencia de los pasajeros del Titanic. Al examinar los datos de los supervivientes, podemos identificar patrones y tendencias que nos permitan responder preguntas como:

¿Qué características compartían los supervivientes? Edad, sexo, clase social, etc.
¿Existió alguna relación entre la ubicación en el barco y la supervivencia?
¿Influyó la tarifa del pasaje en las posibilidades de sobrevivir?
¿Hubo alguna diferencia en la supervivencia entre los diferentes puertos de embarque?


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = pd.read_csv('titanic.csv')

# Análisis exploratorio
sns.countplot(x='Survived', data=data)
plt.title('Distribución de la Supervivencia')
plt.show()

# Comparación de la supervivencia por sexo
sns.barplot(x='Sex', y='Survived', data=data)
plt.title('Tasa de Supervivencia por Sexo')
plt.show()
````
