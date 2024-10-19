import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import gc

from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
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

# Clasiciadores de mayor accuracy
classifiers = {
    "LGBM": LGBMClassifier(),
    "GB": GradientBoostingClassifier(),
    "RF": RandomForestClassifier(),
    "XGB": XGBClassifier()
}

# Crear el VotingClassifier
voting_clf = VotingClassifier(estimators=list(classifiers.items()), voting='soft')

param_grid = {
    'LGBM__n_estimators': [50, 100, 200],
    'LGBM__learning_rate': [0.01, 0.1, 0.2],
    'LGBM__max_depth': [5, 7, 10],
    'LGBM__num_leaves': [16, 32, 64],
    'LGBM__min_child_samples': [20, 30, 50],
    'LGBM__min_split_gain': [0.0, 0.01, 0.1],
    'LGBM__lambda_l1': [0, 0.1, 0.5],
    'LGBM__lambda_l2': [0, 0.1, 0.5],

    'GB__n_estimators': [50, 100, 200],
    'GB__learning_rate': [0.01, 0.1, 0.2],
    'GB__max_depth': [3, 5, 7],
    
    'RF__n_estimators': [50, 100, 200],
    'RF__max_depth': [None, 10, 20],
    'RF__min_samples_split': [2, 5, 10],
    
    'XGB__n_estimators': [50, 100, 200],
    'XGB__learning_rate': [0.01, 0.1, 0.2],
    'XGB__max_depth': [3, 5, 7]
}

# # Configurar GridSearchCV
grid_search = GridSearchCV(estimator=voting_clf, param_grid=param_grid, 
                           scoring='accuracy', cv=5, verbose=2, n_jobs=-1)

grid_search.fit(X_train, y_train)

voting_clf = grid_search.best_estimator_

import os
from joblib import dump

model_dir = 'models'
model_filename = 'voting_classifier_model.joblib'

# Crear la carpeta si no existe
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Guardar el modelo en la carpeta models
dump(voting_clf, os.path.join(model_dir, model_filename))

print(f"Modelo guardado en {os.path.join(model_dir, model_filename)}")
