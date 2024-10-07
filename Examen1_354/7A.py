import random
from deap import base, creator, tools

# Definir la función de evaluación como minimizar la función x^(2x) - 1
def eval_func(individual):
    # Convertir binario a decimal
    x = int("".join(map(str, individual)), 2)
    return (x ** (2 * x) - 1,)

# Crear los tipos de fitness y el individuo en DEAP
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Configurar el toolbox
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)  # Gen aleatorio
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 8)  # Individuos de 8 bits
toolbox.register("population", tools.initRepeat, list, toolbox.individual)  # Población de individuos

# Registro de operadores
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxOnePoint)  # Cruce de un punto (como punto de división)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.125)  # Mutación de un bit
toolbox.register("select", tools.selTournament, tournsize=3)  # Selección por torneo

# Inicializar la población inicial basada en decimales convertidos a binario
poblacion_decimal = [1, 21, 30, 16, 26, 8, 21, 15, 22, 14, 13, 4]
poblacion_binaria = [creator.Individual([int(bit) for bit in format(num, '08b')]) for num in poblacion_decimal]

# Parámetros del Algoritmo Genético
num_generaciones = 3
tamano_poblacion = len(poblacion_binaria)
probabilidad_cruce = 0.7
probabilidad_mutacion = 0.2

# Algoritmo Genético
for generacion in range(num_generaciones):
    # Selección
    offspring = toolbox.select(poblacion_binaria, len(poblacion_binaria))
    offspring = list(map(toolbox.clone, offspring))

    # Aplicar cruce y mutación
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < probabilidad_cruce:
            toolbox.mate(child1, child2)
            del child1.fitness.values, child2.fitness.values

    for mutant in offspring:
        if random.random() < probabilidad_mutacion:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluar la aptitud de los individuos
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # Reemplazar la población antigua por la nueva
    poblacion_binaria[:] = offspring

    # Resultados de la generación actual
    poblacion_decimal_final = [int("".join(map(str, ind)), 2) for ind in poblacion_binaria]
    print(f"Generación {generacion + 1}:")
    print("Población final en decimal:", poblacion_decimal_final)
    print("-" * 40)

