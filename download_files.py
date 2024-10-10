import gdown
import os

files = [
    {"id": "1cWmr7C3Ox0cK6wL5tr3PiDqEjd7X0iap", "name": "Ambe/AmBe_cdparafb_650_nogps_2024_10_02_14h00.dat"},
    {"id": "1zP-XywxZPinYCqDIOiGDJVFFVFC5driP", "name": "AmBe/AmBe_desnuda_750_nogps_2024_10_02_14h00.dat"},
    {"id": "1e8snPLFctL00qOLpH4u19wonhSISV7OF", "name": "AmBe/AmBe_plomo(10cm)_440t1_nogps_2024_10_02_13h00.dat"},
    {"id": "16dxS3s9cxaUUxMKb38fe2ldsqkHUvgdy", "name": "AmBe/fondo_AmBe_cdparafb_650_nogps_2024_10_02_14h00.dat"},
    {"id": "1hKX2MDz0HU5yrvSax_uAY3TGOOjLKBMZ", "name": "AmBe/fondo_AmBe_desnuda_750_nogps_2024_10_02_15h00.dat"},
    {"id": "1wUPnZEpWPSPATU8YDUdXvozL0u-HFBA5", "name": "AmBe/fondo_AmBe_plomo(10cm)_440t1_nogps_2024_10_02_14h00.dat"},
]

if not os.path.exists('AmBe'):
    os.makedirs('AmBe')

for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    gdown.download(url, output, quiet=False)

print("All files have been downloaded")
