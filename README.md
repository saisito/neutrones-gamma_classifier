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
    {"id": "1cWmr7C3Ox0cK6wL5tr3PiDqEjd7X0iap", "name": "Ambe/AmBe_cdparafb.dat"},
    {"id": "1zP-XywxZPinYCqDIOiGDJVFFVFC5driP", "name": "AmBe/AmBe_desnuda.dat"},
    {"id": "1e8snPLFctL00qOLpH4u19wonhSISV7OF", "name": "AmBe/AmBe_plomo(10cm).dat"},
    {"id": "16dxS3s9cxaUUxMKb38fe2ldsqkHUvgdy", "name": "AmBe/fondo_AmBe_cdparafb.dat"},
    {"id": "1hKX2MDz0HU5yrvSax_uAY3TGOOjLKBMZ", "name": "AmBe/fondo_AmBe_desnuda.dat"},
    {"id": "1wUPnZEpWPSPATU8YDUdXvozL0u-HFBA5", "name": "AmBe/fondo_AmBe_plomo(10cm).dat"},
]

if not os.path.exists('AmBe'):
    os.makedirs('AmBe')

for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    gdown.download(url, output, quiet=False)

print("All files have been downloaded")


