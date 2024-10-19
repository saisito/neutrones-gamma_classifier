import numpy as np
import matplotlib.pyplot as plt
import glob
import random
import re
import os
import csv

def save_filtered_data_all(file_list, charge_range, output_dir):
    """
    Filters and saves segmented data from input files based on a charge range.
    Args:
        file_list (list of str): A list containing two file paths. The first file is assumed to be the source data (fuente) 
                                 and the second file is the background data (fondo).
        charge_range (tuple of int): A tuple containing two integers that define the lower and upper bounds of the charge range.
        output_dir (str): The directory where the filtered data will be saved.
    Returns:
        None
    The function reads data from the provided files, segments it into chunks of 32, filters these segments based on the 
    provided charge range, and saves the filtered segments into CSV files in the specified output directory. The source 
    data is saved as "fuente_pulsos.csv" and the background data is saved as "fondo_pulsos.csv".
    """
    fuente_data, fondo_data = [], []
    fuente_file, fondo_file = file_list
    for file, data_list in zip([fuente_file, fondo_file], [fuente_data, fondo_data]):
        data = np.loadtxt(file, np.int32, usecols=0)
        num_segments = len(data) // 32
        new_data = data[:num_segments * 32].reshape(-1, 32)

        for subsegment in new_data:
            if charge_range[0] < np.sum(subsegment) < charge_range[1]:
                data_list.append(subsegment)
        
    # Guardar los resultados en el directorio de salida
    os.makedirs(output_dir, exist_ok=True)
    if fuente_data:
        np.savetxt(os.path.join(output_dir, "fuente_pulsos.csv"), np.array(fuente_data), delimiter=',', fmt='%d')
    if fondo_data:
        np.savetxt(os.path.join(output_dir, "fondo_pulsos.csv"), np.array(fondo_data), delimiter=',', fmt='%d')
    
    print(f"Datos guardados en {output_dir}")

def save_filtered_data_random(file_list, charge_range, output_dir, sample_size):
    """
    Filters and saves random samples of data segments based on a charge range.
    Parameters:
    file_list (list of str): List containing the paths to the source and background data files.
    charge_range (tuple of int): Tuple specifying the minimum and maximum charge range for filtering segments.
    output_dir (str): Directory where the filtered data will be saved.
    sample_size (int): Number of samples to randomly select from the filtered data.
    Returns:
    None
    The function reads data from the provided files, filters the segments based on the specified charge range,
    randomly samples the filtered segments, and saves the results to the specified output directory.
    """
    fuente_data, fondo_data = [], []
    fuente_file, fondo_file = file_list
    for file, data_list in zip([fuente_file, fondo_file], [fuente_data, fondo_data]):
        data = np.loadtxt(file, np.int32, usecols=0)
        num_segments = len(data) // 32
        new_data = data[:num_segments * 32].reshape(-1, 32)

        for subsegment in new_data:
            if charge_range[0] < np.sum(subsegment) < charge_range[1]: 
                data_list.append(subsegment)
        
    # Si el tamaño de la muestra es mayor que los datos disponibles, se usa todo el conjunto
    fuente_sample = random.sample(fuente_data, min(sample_size, len(fuente_data)))
    fondo_sample = random.sample(fondo_data, min(sample_size, len(fondo_data)))

    # Guardar los resultados en el directorio de salida
    os.makedirs(output_dir, exist_ok=True)
    if fuente_sample:
        np.savetxt(os.path.join(output_dir, "fuente_pulsos.csv"), np.array(fuente_sample), delimiter=',', fmt='%d')
    if fondo_sample:
        np.savetxt(os.path.join(output_dir, "fondo_pulsos.csv"), np.array(fondo_sample), delimiter=',', fmt='%d')
    
    print(f"Datos guardados en {output_dir}")


file_list_AmBe_desnuda = sorted(glob.glob('AmBe/*desnuda*'))
file_list_AmBe_plomo = sorted(glob.glob('AmBe/*plomo(10cm)*'))
file_list_AmBe_cdparafinab = sorted(glob.glob('AmBe/*cdparafb*'))

charge_thresholds_AmBe = (4000, 8000) 

# Una muestra aleatoria del intervalo de carga
save_filtered_data_random(file_list_AmBe_desnuda, charge_thresholds_AmBe, "AmBe_desnuda_random", 100000)
# Todo el intervalo de carga
save_filtered_data_all(file_list_AmBe_desnuda, charge_thresholds_AmBe, "AmBe_desnuda")

# Una muestra aleatoria del intervalo de carga
save_filtered_data_random(file_list_AmBe_plomo, charge_thresholds_AmBe, "AmBe_plomo_random", 100000) 
# Todo el intervalo de carga
save_filtered_data_all(file_list_AmBe_plomo, charge_thresholds_AmBe, "AmBe_plomo") 

# Una muestra aleatoria del intervalo de carga
save_filtered_data_random(file_list_AmBe_cdparafinab, charge_thresholds_AmBe, "AmBe_cdparafinab_random", 100000)
save_filtered_data_all(file_list_AmBe_cdparafinab, charge_thresholds_AmBe, "AmBe_cdparafinab") # Todo el intervalo de carga


