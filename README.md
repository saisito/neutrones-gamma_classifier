# Project

ML aplications in Water Cherenkov Detector. Currently, all functionalities and analyses are contained within the `process.ipynb` file.

## Download Files

This project contains large data files that are not stored directly in the repository due to their size. To download the original files, please follow the instructions below:

1. Ensure you have `gdown` installed. If not, you can install it using `pip`:

    ```sh
    pip install gdown
    ```

2. Run the `download_files.py` script to download the files from Google Drive:

    ```sh
    python download_files.py
    ```

   This script will download all the required files into the `data/` directory.

## Script Details

The `download_files.py` script includes a list of Google Drive file IDs and their respective output filenames. The script uses these IDs to download the files and save them in the specified directory. Below is the content of the `download_files.py` script:

```python
import gdown
import os

files = [
    {"id": "17OZ-F1nk55n4eSi1Vt-mx0ca4xkXAwHZ", "name": "AmBe_cdparafb.dat"},
    {"id": "1cCsaeiXucjjPJbJGTY1Ks5PfxiQdmz_Z", "name": "AmBe_desnuda.dat"},
    {"id": "1dpx1jDNWDwzfayRgZ1WiQJuSDFyiS_KK", "name": "AmBe_plomo(10cm).dat"},
    {"id": "1cfn6VZ2-sRI2lFwcCBdoesQKpNukNhTD", "name": "fondo_AmBe_cdparafb.dat"},
    {"id": "140tUN1M4vtvS9jn6h_ZVpowiltiKA_bx", "name": "fondo_AmBe_desnuda.dat"},
    {"id": "1c4beBXSOPdcFQ_FX20V342n-vLb36Dxo", "name": "fondo_AmBe_plomo(10cm).dat"},
]

# Crear la carpeta 'AmBe' si no existe
if not os.path.exists('AmBe'):
    os.makedirs('AmBe')

# Descargar los archivos
for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    
    # Crear la ruta completa para guardar el archivo
    output_path = os.path.join('AmBe', output)
    
    # Descargar el archivo
    gdown.download(url, output_path, quiet=False)

print("All files have been downloaded")





