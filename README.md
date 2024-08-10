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

# List of Google Drive file IDs and their corresponding output names
files = [
    {"id": "1Toaeg1spKMOMvFMLRUaFcjH0rRStGQK0", "name": "data/fondo_Co_1200V_170t1_5min.dat"},
    {"id": "1YSUqibib-JbuSJAjgLLqp-pn-GbyJwgv", "name": "data/fondo_10cm_plomo_1200V_170t1_5min.dat"},
    {"id": "18a_Xpv6HfIspJCy1q5FFHE4BL1SJ4MAF", "name": "data/fondo_10cm_noplomo_1200V_170t1_5min.dat"},
    {"id": "1BOnxVzMR0ZX0zUn6hZP1n8YLCKfACcps", "name": "data/Co_1200V_170t1_5min.dat"},
    {"id": "1BsmEN-1ruPRchGM0RLmtCo8cl8vQmhd5", "name": "data/AmBe_30cm_10cm_plomo_1200V_650t1_5min.dat"},
    {"id": "1AT9OqZ95KrGwCKV7Myjt-q_3nSkloNyL", "name": "data/AmBe_30cm_10cm_noplomo_1200V_650t1_5min.dat"},
]

# Create the 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Download each file
for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    gdown.download(url, output, quiet=False)

print("All files have been downloaded.")


