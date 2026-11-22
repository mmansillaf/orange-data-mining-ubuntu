import Orange

# Cargar dataset de prueba integrado
data = Orange.data.Table("iris")
print(f"Dataset cargado: {len(data)} filas, {len(data.domain.attributes)} atributos")
print(f"Objetivo: {data.domain.class_var.name}")

# Entrenar un clasificador (Tree y Random Forest)
tree = Orange.classification.TreeLearner()(data)
rf = Orange.classification.RandomForestLearner()(data)

# Evaluación cruzada (5-fold)
cv = Orange.evaluation.CrossValidation(k=5)
res = cv(data, [Orange.classification.TreeLearner(), Orange.classification.RandomForestLearner()])
print(f"Exactitud (CA) Arbol: {Orange.evaluation.CA(res)[0]:.4f}")
print(f"Exactitud (CA) Random Forest: {Orange.evaluation.CA(res)[1]:.4f}")
