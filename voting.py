import numpy as np
import os
from joblib import dump
from sklearn.ensemble import VotingClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from catboost import CatBoostClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

# Función para cargar los datos desde múltiples archivos
def cargar_datos(archivos_neutrones, archivos_gammas):
    """
    Carga y procesa datos de archivos de neutrones y gammas.
    Args:
        archivos_neutrones (list of str): Lista de rutas de archivos que contienen datos de neutrones.
        archivos_gammas (list of str): Lista de rutas de archivos que contienen datos de gammas.
    Returns:
        tuple: Una tupla que contiene:
            - data (numpy.ndarray): Arreglo con los datos combinados de neutrones y gammas.
            - labels (numpy.ndarray): Arreglo con las etiquetas correspondientes (1 para neutrones, 0 para gammas).
    """
    pulsos_neutrones = []
    pulsos_gammas = []
    
    # Cargar datos de neutrones
    for archivo in archivos_neutrones:
        datos = np.loadtxt(archivo, delimiter=',')
        pulsos_neutrones.append(datos)
    
    # Cargar datos de gammas
    for archivo in archivos_gammas:
        datos = np.loadtxt(archivo, delimiter=',')
        pulsos_gammas.append(datos)
    
    # Concatenar todos los pulsos de neutrones y gammas
    pulsos_neutrones = np.vstack(pulsos_neutrones)
    pulsos_gammas = np.vstack(pulsos_gammas)
    
    # Crear etiquetas (1 para neutrones, 0 para gammas)
    labels = np.array([1] * pulsos_neutrones.shape[0] + [0] * pulsos_gammas.shape[0])
    
    # Combinar los pulsos en un solo arreglo
    data = np.vstack((pulsos_neutrones, pulsos_gammas))
    
    return data, labels

archivos_neutrones = ['AmBe_plomo_random/fuente_pulsos.csv']  
archivos_gammas = ['AmBe_cdparafinab_random/fuente_pulsos.csv']

# Cargar los datos
data, labels = cargar_datos(archivos_neutrones, archivos_gammas)

# Dividir los datos en conjunto de entrenamiento y prueba 20-80
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Filtrar por las caracteristicas mas importantes
selected_features = [7, 8, 9, 10, 13] 
X_train = X_train[:, selected_features]
X_test = X_test[:, selected_features]

# Clasiciadores de mayor accuracy
classifiers = {
    "CatBoost": CatBoostClassifier(silent=True),
    "LightGBM": LGBMClassifier(force_col_wise=True, verbose=-1,),
    "RandomForest": RandomForestClassifier(),
    "GradientBoosting": GradientBoostingClassifier(),
    "XGBoost": XGBClassifier()
}

# Crear el VotingClassifier
voting_clf = VotingClassifier(estimators=list(classifiers.items()), voting='soft')

param_dist = {
    'CatBoost__iterations': [100, 200, 300],
    'CatBoost__learning_rate': [0.01, 0.1, 0.2],
    'CatBoost__depth': [4, 6, 8],

    'LightGBM__num_leaves': [31, 63, 127],
    'LightGBM__learning_rate': [0.01, 0.1, 0.2],
    'LightGBM__n_estimators': [100, 200, 300],
    'LightGBM__max_depth': [-1, 5, 10],

    'RandomForest__n_estimators': [100, 200, 300],
    'RandomForest__max_depth': [5, 10, 15],

    'GradientBoosting__n_estimators': [100, 200, 300],
    'GradientBoosting__learning_rate': [0.01, 0.1, 0.2],
    'GradientBoosting__max_depth': [3, 5, 7],

    'XGBoost__max_depth': [3, 5, 7],
    'XGBoost__learning_rate': [0.01, 0.1, 0.2],
    'XGBoost__n_estimators': [100, 200, 300],
    'XGBoost__reg_alpha': [0, 0.1, 0.5],
    'XGBoost__reg_lambda': [1, 1.5, 2]
}


# RandomSearch tranqui para no explotar la compu :)
random_search = RandomizedSearchCV(
    estimator=voting_clf, 
    param_distributions=param_dist, 
    n_iter=50,  # Número de iteraciones para explorar el espacio de hiperparámetros
    scoring='accuracy', 
    cv=5,  # Validación cruzada
    random_state=42, 
    n_jobs=4  
)

random_search.fit(X_train, y_train)

voting_clf = random_search.best_estimator_

model_dir = 'models'
model_filename = 'voting_classifier_model.joblib'

# Crear la carpeta si no existe
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Guardar el modelo en la carpeta models
dump(voting_clf, os.path.join(model_dir, model_filename))

print(f"Modelo guardado en {os.path.join(model_dir, model_filename)}")
