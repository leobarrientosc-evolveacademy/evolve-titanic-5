 # Readme

 ## Supervivientes del accidente TITANIC

### Descripcion 
 Este proyecto tiene como objetivo investigar y visualizar los datos relacionados con el hundimiento del Titanic, una de las mayores tragedias marítimas de la historia. Se explorarán factores como las características de los pasajeros (edad, sexo, clase social), la ubicación de las cabinas, y su relación con la supervivencia.

--Añadido por Alex

# 🌌 Análisis Titanic

Bienvenido a **Análisis Titanic**, un proyecto diseñado para realizar análisis estadísticos de un conjunto de datos — el legendario Titanic. Este proyecto también tiene como objetivo reforzar prácticas de control de versiones con Git y GitHub. 🚀

---

## 🔍 Objetivos del Proyecto

1. Realizar análisis estadísticos del archivo CSV con información de los pasajeros del Titanic.
2. Visualizar patrones y tendencias a partir de los datos.
3. Practicar técnicas de versionado de código con Git y GitHub.

---

## 🔮 Características del Proyecto

- **Lenguaje**: Python
- **Librerías**: 
  - Pandas 
  - Matplotlib 
  - Seaborn
- **Formato de datos**: CSV
- **Análisis**:
  - Supervivencia vs Clase
  - Análisis de género y edad
  - Estadísticas descriptivas de variables importantes

---

## 🔧 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener:

- Python 3.7+
- Librerías instaladas: 
  ```bash
  pip install pandas matplotlib seaborn
  ```

---

## 🚀 Comenzando

Sigue estos pasos para clonar y ejecutar el proyecto:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/analisis-titanic.git
   ```

2. Ve al directorio del proyecto:
   ```bash
   cd analisis-titanic
   ```

3. Ejecuta el script principal:
   ```bash
   python titanic_analysis.py
   ```

---

## 🔢 Estructura del Proyecto

```plaintext
analisis-titanic/
├── data/                # Contiene el archivo CSV del Titanic
├── figures/             # Imágenes generadas por el análisis
├── titanic_analysis.py  # Script principal
├── README.md            # Documentación del proyecto
└── requirements.txt     # Dependencias
```

---

## 📊 Ejemplo de Resultados

### Supervivencia por Clase

![](https://via.placeholder.com/600x300?text=Grafico+1)

### Supervivencia por Género

![](https://via.placeholder.com/600x300?text=Grafico+2)

---

## 🔎 Exploración de Datos

Para explorar el archivo CSV, ejecuta el siguiente código en Python:

```python
import pandas as pd

# Carga los datos
data = pd.read_csv('data/titanic.csv')
print(data.head())
```

---

## 🔧 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el proyecto:

1. Haz un fork de este repositorio.
2. Crea una rama nueva:
   ```bash
   git checkout -b mejora-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Mejora: añadida nueva funcionalidad"
   ```
4. Envía un pull request.

---

## ❤️ Agradecimientos

Este proyecto fue inspirado en el legendario caso del Titanic y el aprendizaje continuo de análisis de datos y prácticas de desarrollo. 🌌

---

## 🔧 Recursos adicionales

- [Documentación de Pandas](https://pandas.pydata.org/)
- [Documentación de Matplotlib](https://matplotlib.org/)
- [Documentación de Seaborn](https://seaborn.pydata.org/)

---

## 🎨 Licencia

Este proyecto está bajo la licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---Añadido por Alex

¿Que os parece el cambio chic@s?
>>>>>>> 3d340bbba9fcf1f6b1dd9a2c1b7b05b95aa481b5

<<<<<<< HEAD

=======
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
>>>>>>> d780503dc39102f216a2decf9a3fb1ae3a228a58
## Buscamos los datos y los ponemos aqui