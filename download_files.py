import gdown
import os

files = [
    {"id": "1cWmr7C3Ox0cK6wL5tr3PiDqEjd7X0iap", "name": "AmBe/AmBe_cdparafb.dat"},
    {"id": "1zP-XywxZPinYCqDIOiGDJVFFVFC5driP", "name": "AmBe/AmBe_desnuda.dat"},
    {"id": "1e8snPLFctL00qOLpH4u19wonhSISV7OF", "name": "AmBe/AmBe_plomo(10cm).dat"},
    {"id": "16dxS3s9cxaUUxMKb38fe2ldsqkHUvgdy", "name": "AmBe/fondo_AmBe_cdparafb.dat"},
    {"id": "1hKX2MDz0HU5yrvSax_uAY3TGOOjLKBMZ", "name": "AmBe/fondo_AmBe_desnuda.dat"},
    {"id": "1wUPnZEpWPSPATU8YDUdXvozL0u-HFBA5", "name": "AmBe/fondo_AmBe_plomo(10cm).dat"},
]

# Crear la carpeta AmBe si no existe
if not os.path.exists('AmBe'):
    os.makedirs('AmBe')

# Descargar los archivos
for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    
    output_path = os.path.join('AmBe', output)
    
    gdown.download(url, output_path, quiet=False)

print("All files have been downloaded")
