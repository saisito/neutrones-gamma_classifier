# Project

ML aplications in Water Cherenkov Detector

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
    {"id": "1ngBJDS2nR2g0X1eYIpRc4A9AG17CrYTe", "name": "Ambe/fondo_ambe_plomo_30cm_nogps_1970_01_01_01h00.dat"},
    {"id": "17HjDZCe0aWUHeV7iqYSX2FDWF1U96x7k", "name": "AmBe/fondo_ambe_parafinapuraplomo2bloques_30cm_880t1_nogps_1970_01_01_01h00.dat"},
    {"id": "1vTUrvm11CXtjweLyzNsiXWUi7OknUgE1", "name": "AmBe/fondo_ambe_desnuda_30cm_880t1_nogps_1970_01_01_00h00.dat"},
    {"id": "1hL343azbJf2WBNdvIn60-MhlbFsFgZlc", "name": "AmBe/fondo_ambe_cadmioparafinaborada_30cm_880t1_nogps_1970_01_01_02h00.dat"},
    {"id": "1ofxET2MSL1DCedaPAnJyYK-iNOK67AkP", "name": "AmBe/ambe_plomo_30cm_880t1_nogps_1970_01_01_01h00.dat"},
    {"id": "1gJv9FPWCrN_vDwSRhXIDJGPwicE0HRBR", "name": "AmBe/ambe_parafinapuraplomo2bloques_30cm_880t1_nogps_1970_01_01_01h00.dat"},
    {"id": "18uftyzsP6ssM2kmBKO96fIp74dS5G-s2", "name": "AmBe/ambe_desnuda_30cm_880t1_nogps_1970_01_01_00h00.dat"},
    {"id": "1ZAXvR3OMOQvjmCoa-p-O8spagY96tUeC", "name": "AmBe/ambe_cadmioparafinaborada_30cm_880t1_nogps_1970_01_01_02h00.dat"},
]

if not os.path.exists('AmBe'):
    os.makedirs('AmBe')

for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    gdown.download(url, output, quiet=False)

print("All files have been downloaded")


