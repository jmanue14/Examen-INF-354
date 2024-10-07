import numpy as np

# Población inicial en formato decimal, consistente con los datos de la imagen proporcionada
poblacion_decimal = [1, 21, 30, 16, 26, 8, 21, 15, 22, 14, 13, 4]

# Convertir la población inicial de decimal a binario de 8 bits
poblacion = np.array([list(map(int, format(individuo, '08b'))) for individuo in poblacion_decimal])

# Función para cruzar dos padres en un punto de división
def cruzar(padre1, padre2, punto_division):
    hijo1 = np.concatenate([padre1[:punto_division], padre2[punto_division:]])
    hijo2 = np.concatenate([padre2[:punto_division], padre1[punto_division:]])
    return hijo1, hijo2

# Función para mutar el antepenúltimo bit de un individuo
def mutar(individuo):
    bit_pos = 5  # antepenúltimo bit
    individuo[bit_pos] = 1 - individuo[bit_pos]  # alternar entre 0 y 1
    return individuo

# Parámetros para cada generación
puntos_division = [4, 4, 3]  # Punto de cruce para cada generación

# Realizar el proceso para 3 generaciones
for generacion in range(3):
    nueva_poblacion = []
    
    # Realizar cruces en pares sucesivos
    for i in range(0, len(poblacion), 2):
        padre1, padre2 = poblacion[i], poblacion[i+1]
        hijo1, hijo2 = cruzar(padre1, padre2, puntos_division[generacion])
        nueva_poblacion.extend([hijo1, hijo2])
    
    # Aplicar mutación a cada hijo
    poblacion_mutada = [mutar(individuo.copy()) for individuo in nueva_poblacion]
    
    # Convertir la población mutada de binario a decimal
    poblacion_final_decimal = [int(''.join(map(str, individuo)), 2) for individuo in poblacion_mutada]
    
    # Actualizar la población para la siguiente generación
    poblacion = np.array(poblacion_mutada)
    
    # Mostrar resultados de la generación actual
    print(f"Generación {generacion + 1}:")
    print("Población final en decimal:", poblacion_final_decimal)
    print("-" * 40)
