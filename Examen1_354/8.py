import pandas as pd
import numpy as np

# Generar datos aleatorios para el dataset
np.random.seed(42)  # Para reproducibilidad
n_datos = 500
alturas = np.random.randint(150, 191, n_datos)  # Alturas entre 150 cm y 190 cm
pesos = np.random.randint(50, 101, n_datos)  # Pesos entre 50 kg y 100 kg
tallas = np.random.choice(['Small', 'Medium', 'Large'], n_datos)  # Tallas aleatorias

# Asignar clases en función de la altura
def asignar_clase(altura):
    if altura < 160:
        return 'Bajo'
    elif altura < 180:
        return 'Medio'
    else:
        return 'Alto'

clases = [asignar_clase(altura) for altura in alturas]

# Crear el DataFrame
df = pd.DataFrame({
    'Altura': alturas,
    'Peso': pesos,
    'Talla': tallas,
    'Clase': clases
})

# Funciones para calcular entropía y ganancia de información
def calcular_entropia(clase_col):
    probabilidades = clase_col.value_counts(normalize=True)
    entropia = -np.sum(probabilidades * np.log2(probabilidades))
    return entropia

def calcular_ganancia_informacion(df, feature, target='Clase'):
    entropia_inicial = calcular_entropia(df[target])
    valores = df[feature].unique()
    entropia_condicional = sum((df[feature] == v).mean() * calcular_entropia(df[df[feature] == v][target]) for v in valores)
    return entropia_inicial - entropia_condicional

# Calcular entropía y ganancia de información
entropia_clase = calcular_entropia(df['Clase'])
ganancia_altura = calcular_ganancia_informacion(df, 'Altura')
ganancia_peso = calcular_ganancia_informacion(df, 'Peso')
ganancia_talla = calcular_ganancia_informacion(df, 'Talla')

print(f"Entropía de la Clase: {entropia_clase:.3f}")
print(f"Ganancia de Información - Altura: {ganancia_altura:.3f}")
print(f"Ganancia de Información - Peso: {ganancia_peso:.3f}")
print(f"Ganancia de Información - Talla: {ganancia_talla:.3f}")
