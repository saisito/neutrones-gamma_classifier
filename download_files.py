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
