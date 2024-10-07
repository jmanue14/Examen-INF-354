import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ruta del archivo que cargaste
ruta_archivo = 'C:/Users/Administrador/Desktop/Steam_2024_bestRevenue_1500.csv'  # Cambia esta ruta a la ubicación de tu archivo

# Cargar el dataset completo
datos_steam = pd.read_csv(ruta_archivo)

# Selección de las columnas relevantes
datos_seleccionados = datos_steam[['copiesSold', 'revenue', 'reviewScore']]

# Gráfico 1: Relación entre 'copiesSold' y 'revenue'
plt.figure(figsize=(10, 6))
plt.scatter(datos_seleccionados['copiesSold'], datos_seleccionados['revenue'], alpha=0.5, color='blue')
plt.title('Relación entre Copias Vendidas y Ingresos')
plt.xlabel('Copias Vendidas')
plt.ylabel('Ingresos')
plt.grid(True)
plt.show()

# Gráfico 2: Relación entre 'reviewScore' y 'copiesSold'
plt.figure(figsize=(10, 6))
plt.scatter(datos_seleccionados['reviewScore'], datos_seleccionados['copiesSold'], alpha=0.5, color='green')
plt.title('Relación entre Puntuación de Reseñas y Copias Vendidas')
plt.xlabel('Puntuación de Reseñas')
plt.ylabel('Copias Vendidas')
plt.grid(True)
plt.show()

# Gráfico 3: Mapa de calor para las correlaciones entre las tres columnas sin seaborn
plt.figure(figsize=(8, 6))
correlacion = datos_seleccionados.corr()

# Mapa de calor con matplotlib
plt.imshow(correlacion, cmap='coolwarm', interpolation='none')
plt.colorbar()

# Añadir etiquetas a los ejes
plt.xticks(np.arange(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(np.arange(len(correlacion.columns)), correlacion.columns)

plt.title('Mapa de Calor de Correlaciones entre Copias Vendidas, Ingresos y Puntuación de Reseñas')
plt.show()
