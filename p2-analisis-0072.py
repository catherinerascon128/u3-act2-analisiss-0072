# importar librerias 
import pandas as pd 
import numpy as np
print("Fuga de Clientes / Churn (Clasificación Binaria) catherine eileen huerta rascon NC = 0072")

clientes = {
    "Cliente": ["michell", "andres", "pedro", "scarr", "iris", "darrel"],
    "Antiguedad_Meses": [2, 36, 12, 12, 48, 1],
    "Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 59.00, 49.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}
df = pd.DataFrame(clientes)
print(df)
print("-+-+-+-+ agrupar por una sola columna +-+-+-+-")
agrupado= df.groupby('Antiguedad_Meses')
print(agrupado)
print("-+-+-+-+ promedio por riesgo de cancelacion +-+-+-+-")
# antiguedad de servicio
print(agrupado['Antiguedad_Meses'].mean())
print("-+-+-+-+ gasto mensual maximo +-+-+-+-")
# maximo de cada servicio
print(agrupado['Gasto_Mensual'].max())
print("-+-+-+-+ agrupar por una sola columna +-+-+-+-")
