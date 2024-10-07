import numpy as np
import pandas as pd

# Configuración para la generación de datos
np.random.seed(42)  # Para garantizar la reproducibilidad
n_articulos = 100  # Número de artículos
peso_maximo = 100  # Peso máximo que puede llevar la mochila

# Generar datos aleatorios para los artículos
pesos = np.random.randint(1, 10, n_articulos)  # Pesos entre 1 y 10
valores = np.random.randint(10, 100, n_articulos)  # Valores entre 10 y 100

# Crear un DataFrame para los artículos
articulos = pd.DataFrame({
    'peso': pesos,
    'valor': valores
})
articulos['valor_por_peso'] = articulos['valor'] / articulos['peso']  # Calcular valor por unidad de peso

# Ordenar los artículos por valor por unidad de peso en orden descendente
articulos_ordenados = articulos.sort_values(by='valor_por_peso', ascending=False)

# Función para seleccionar artículos usando un enfoque voraz
def mochila_voraz(articulos, peso_maximo):
    peso_total = 0
    valor_total = 0
    articulos_elegidos = []
    
    for _, articulo in articulos.iterrows():
        if peso_total + articulo['peso'] <= peso_maximo:
            articulos_elegidos.append(articulo)
            peso_total += articulo['peso']
            valor_total += articulo['valor']
    
    return articulos_elegidos, valor_total, peso_total

# Ejecutar el algoritmo voraz
articulos_elegidos, valor_total, peso_total = mochila_voraz(articulos_ordenados, peso_maximo)

# Mostrar los resultados
print(f"Valor Total: {valor_total}")
print(f"Peso Total: {peso_total}")
print("Artículos Elegidos:")
print(pd.DataFrame(articulos_elegidos))
