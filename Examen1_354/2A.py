import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo que cargaste
ruta_archivo = 'C:/Users/Administrador/Desktop/Steam_2024_bestRevenue_1500.csv'  # Cambia esta ruta a la ubicación de tu archivo

# Cargar el dataset completo
datos_steam = pd.read_csv(ruta_archivo)

# Función para calcular percentiles y cuartiles sin usar librerías
def calcular_percentiles_cuartiles(datos, percentil):
    datos_ordenados = sorted(datos)
    indice = (percentil / 100) * (len(datos_ordenados) - 1)
    inferior = int(indice)
    superior = inferior + 1
    peso = indice - inferior
    return datos_ordenados[inferior] * (1 - peso) + datos_ordenados[superior] * peso

# Recalcular percentiles y cuartiles para el dataset completo
percentiles_cuartiles = {col: {
    'Percentil 25': calcular_percentiles_cuartiles(datos_steam[col].dropna(), 25),
    'Percentil 50 (Mediana)': calcular_percentiles_cuartiles(datos_steam[col].dropna(), 50),
    'Percentil 75': calcular_percentiles_cuartiles(datos_steam[col].dropna(), 75)
} for col in datos_steam.select_dtypes(include=['float64', 'int64']).columns}  # Solo columnas numéricas

# Convertir los resultados en un DataFrame para visualizarlos
percentiles_cuartiles_df = pd.DataFrame(percentiles_cuartiles)

# Ajustar la configuración de pandas para mostrar todas las columnas
pd.set_option('display.max_columns', None)  # Muestra todas las columnas
pd.set_option('display.width', None)        # Ajusta el ancho para que no se corte la salida

# Mostrar los percentiles y cuartiles en la consola
print("Percentiles y Cuartiles del Dataset:")
print(percentiles_cuartiles_df)

# Graficar distribuciones
plt.figure(figsize=(12, 6))

# Gráfico para 'revenue' (ingresos), que probablemente sigue una distribución gaussiana
plt.subplot(1, 2, 1)
plt.hist(datos_steam['revenue'], bins=30, color='blue', alpha=0.7, range=(0, 2e7))  # Ajusta el rango para que sea visible
plt.title('Distribución de Ingresos (Posiblemente Gaussiana)')
plt.xlabel('Ingresos')
plt.ylabel('Frecuencia')

# Gráfico para 'copiesSold' (copias vendidas), que podría seguir una distribución Poisson
plt.subplot(1, 2, 2)
plt.hist(datos_steam['copiesSold'], bins=30, color='green', alpha=0.7, range=(0, 1e6))  # Ajusta el rango para que sea visible
plt.title('Distribución de Copias Vendidas (Posiblemente Poisson)')
plt.xlabel('Copias Vendidas')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()


# Graficar distribuciones
plt.figure(figsize=(12, 6))

# Gráfico para 'revenue' (ingresos), que probablemente sigue una distribución gaussiana
plt.subplot(1, 2, 1)
plt.hist(datos_steam['revenue'], bins=30, color='blue', alpha=0.7, range=(0, 2e7))  # Ajusta el rango para que sea visible
plt.title('Distribución de Ingresos (Posiblemente Gaussiana)')
plt.xlabel('Ingresos')
plt.ylabel('Frecuencia')

# Gráfico para 'copiesSold' (copias vendidas), que podría seguir una distribución Poisson
plt.subplot(1, 2, 2)
plt.hist(datos_steam['copiesSold'], bins=30, color='green', alpha=0.7, range=(0, 1e6))  # Ajusta el rango para que sea visible
plt.title('Distribución de Copias Vendidas (Posiblemente Poisson)')
plt.xlabel('Copias Vendidas')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()
