#Pregunara Nro 4
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, KBinsDiscretizer, StandardScaler

# 1. Cargar el archivo CSV con los datos
# Cambia esta ruta a la ubicación de tu archivo
ruta_archivo = 'Steam_2024_bestRevenue_1500.csv'
datos_steam = pd.read_csv(ruta_archivo)

# 2. Seleccionamos algunas columnas para el preprocesamiento
# 'copiesSold', 'revenue', 'reviewScore', 'publisherClass', 'price' son las columnas que trabajaremos
datos_seleccionados = datos_steam[['copiesSold', 'revenue', 'reviewScore', 'publisherClass', 'price']]

# 3. OneHotEncoder - Convierte la columna 'publisherClass' en varias columnas binarias (una por cada categoría)
onehot_encoder = OneHotEncoder(sparse_output=False)  # Esto transforma la columna en varias columnas binarias
publisher_class_codificado = onehot_encoder.fit_transform(datos_seleccionados[['publisherClass']])

# 4. LabelEncoder - Convierte las categorías de 'publisherClass' en números (0, 1, 2, etc.)
label_encoder = LabelEncoder()
publisher_class_label_codificado = label_encoder.fit_transform(datos_seleccionados['publisherClass'])

# 5. Discretización - Dividimos los valores de 'copiesSold' en 4 grupos diferentes
discretizer = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform')  # Separamos en 4 grupos
copies_sold_discretizado = discretizer.fit_transform(datos_seleccionados[['copiesSold']])

# 6. Normalización - Escalamos 'revenue' y 'price' para que sus valores estén en un rango similar
escalador = StandardScaler()
valores_escalados = escalador.fit_transform(datos_seleccionados[['revenue', 'price']])

# 7. Convertimos todo a DataFrames para juntar todo en una sola tabla
# Convertimos 'publisherClass' con OneHotEncoder a DataFrame
publisher_class_codificado_df = pd.DataFrame(publisher_class_codificado, columns=onehot_encoder.get_feature_names_out(['publisherClass']))
# Convertimos la versión de LabelEncoder a DataFrame
publisher_class_label_codificado_df = pd.DataFrame(publisher_class_label_codificado, columns=['publisherClass_label_codificado'])
# Convertimos los valores discretizados de 'copiesSold' a DataFrame
copies_sold_discretizado_df = pd.DataFrame(copies_sold_discretizado, columns=['copiesSold_discretizado'])
# Convertimos los valores escalados de 'revenue' y 'price' a DataFrame
valores_escalados_df = pd.DataFrame(valores_escalados, columns=['revenue_escalado', 'price_escalado'])

# 8. Unimos todos los resultados en un solo DataFrame para tener los datos procesados
datos_procesados = pd.concat([publisher_class_codificado_df, publisher_class_label_codificado_df,
                               copies_sold_discretizado_df, valores_escalados_df], axis=1)

# 9. Mostramos el resultado final del preprocesamiento
print(datos_procesados)
