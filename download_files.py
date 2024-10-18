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

