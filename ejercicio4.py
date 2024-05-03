import pandas as pd

calificaciones = [
    {"nombre": "Juan", "matematicas": 85, "ciencias": 90, "historia": 75},
    {"nombre": "María", "matematicas": 70, "ciencias": 80, "historia": 85},
    {"nombre": "Pedro", "matematicas": 95, "ciencias": 75, "historia": 90},
    {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia": 80},
    {"nombre": "Luis", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Sofía", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Elena", "matematicas": 70, "ciencias": 75, "historia": 85},
    {"nombre": "Javier", "matematicas": 80, "ciencias": 85, "historia": 90},
    {"nombre": "Laura", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Diego", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Paula", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Carmen", "matematicas": 70, "ciencias": 75, "historia": 85},
]

df = pd.DataFrame(calificaciones)

print(df)

#se calcula el promedio de cada materia y luego se imprime su resultado

cantidadMatematica = df['matematicas'].value_counts().sum()

promedioMatematica = df['matematicas'].sum()/cantidadMatematica

print("\nPromedio matematicas: ", promedioMatematica)

cantidadCiencias = df['ciencias'].value_counts().sum()

promedioCiencias = df['ciencias'].sum()/cantidadCiencias

print("\nPromedio ciencias: ",promedioCiencias)

cantidadHistoria = df['historia'].value_counts().sum()

promedioHistoria = df['historia'].sum()/cantidadHistoria

print("\nPromedio historia: ",promedioHistoria)

# se encuentra a los estudiantes con las calificaciones más altas en cada asignatura

mejoresMatematicas = df.loc[df['matematicas'].idxmax()]

print("\nMejor calificación en Matemáticas:",mejoresMatematicas)

mejoresCiencias = df.loc[df['ciencias'].idxmax()]

print("\nMejor calificación en Ciencias:",mejoresCiencias)

mejoresHistoria = df.loc[df['historia'].idxmax()]

print("\nMejor calificación en Historia:",mejoresHistoria)


# se calcula el porcentaje de estudiantes que aprobaron cada asignatura y luego se imprime su resultado
aprobadosMatematicas = df[df['matematicas'] >= 60].shape[0] / df.shape[0] * 100

print("\nPorcentaje de estudiantes que aprobaron matematicas:", aprobadosMatematicas,"%")

aprobadosCiencias = df[df['ciencias'] >= 60].shape[0] / df.shape[0] * 100

print("\nPorcentaje de estudiantes que aprobaron ciencias:", aprobadosCiencias,"%")

aprobadosHistoria = df[df['historia'] >= 60].shape[0] / df.shape[0] * 100

print("\nPorcentaje de estudiantes que aprobaron historia:", aprobadosHistoria,"%")

#se crea otro dataframe donde se visualizan 2 columnas una de nombre del estudiante y otra del promedio de notas de las materias

df['promedio'] = df[['matematicas', 'ciencias', 'historia']].mean(axis=1)

df_promedio = df[['nombre', 'promedio']]

print("\n",df_promedio)
