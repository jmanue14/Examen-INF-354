#5      Con el uso de librerías realiza en Python los mismos preprocesamiento del punto 3.
import pandas as pd
import numpy as np

# 1. Cargar el archivo CSV con los datos del dataset original
ruta_archivo = 'Steam_2024_bestRevenue_1500.csv'
datos_steam = pd.read_csv(ruta_archivo)

# 2. Seleccionar las columnas numéricas que queremos normalizar y usar para las penalizaciones
# Usaremos 'copiesSold', 'revenue' y 'price' como las características de ejemplo
X = datos_steam[['copiesSold', 'revenue', 'price']].to_numpy()  # Convertimos a array numpy para manipular más fácilmente

# 3. Normalización sin librerías (Restar la media y dividir entre la desviación estándar)
def normalizar(X):
    media = X.mean(axis=0)  # Media de cada columna
    desviacion = X.std(axis=0)  # Desviación estándar de cada columna
    X_normalizado = (X - media) / desviacion  # Normalizar los datos
    return X_normalizado

# 4. Implementación de la penalización L1 (Suma de los valores absolutos de los coeficientes)
def penalizacion_L1(coeficientes):
    return np.sum(np.abs(coeficientes))  # Suma de los valores absolutos

# 5. Implementación de la penalización L2 (Suma de los cuadrados de los coeficientes)
def penalizacion_L2(coeficientes):
    return np.sum(coeficientes ** 2)  # Suma de los cuadrados

# 6. Normalizamos los datos del dataset
X_normalizado = normalizar(X)

# Supongamos que estos son los coeficientes de un modelo (los puedes cambiar por coeficientes reales si lo deseas)
# Por simplicidad, aquí estamos generando unos coeficientes aleatorios como ejemplo
coeficientes = np.array([0.5, -0.2, 0.3])  # Estos serían los "coeficientes" del modelo de regresión

# 7. Calculamos las penalizaciones L1 y L2 usando los coeficientes
penalizacion_l1 = penalizacion_L1(coeficientes)
penalizacion_l2 = penalizacion_L2(coeficientes)

# Mostramos los resultados
print("Datos normalizados:\n", X_normalizado[:5])  # Mostrar solo las primeras 5 filas
print("Penalización L1:", penalizacion_l1)
print("Penalización L2:", penalizacion_l2)
