import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Ruta del archivo que cargaste
ruta_archivo = 'C:/Users/Administrador/Desktop/Steam_2024_bestRevenue_1500.csv'  # Cambia esta ruta a la ubicación de tu archivo

# Cargar el dataset completo
datos_steam = pd.read_csv(ruta_archivo)

# Selección de las columnas relevantes
datos_seleccionados = datos_steam[['copiesSold', 'revenue', 'reviewScore']]

# Obtener media, mediana y moda para cada columna seleccionada
media = datos_seleccionados.mean()
mediana = datos_seleccionados.median()
moda = datos_seleccionados.mode().iloc[0]  # Devuelve la primera moda si hay más de una

# Mostrar los resultados
print("Media:\n", media)
print("\nMediana:\n", mediana)
print("\nModa:\n", moda)

# Gráfico de diagrama de cajas y bigotes
plt.figure(figsize=(10, 6))
plt.boxplot([datos_seleccionados['copiesSold'], datos_seleccionados['revenue'], datos_seleccionados['reviewScore']],
            labels=['Copias Vendidas', 'Ingresos', 'Puntuación de Reseñas'])
plt.title('Diagrama de Cajas y Bigotes de Copias Vendidas, Ingresos y Puntuación de Reseñas')
plt.ylabel('Valores')
plt.grid(True)
plt.show()
