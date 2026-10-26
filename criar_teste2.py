from pathlib import Path

pasta = Path("teste2")
pasta.mkdir(exist_ok=True)

nomes = ["IMG_8391.jpg", "foto final (2).jpg", "DSC0045.jpg", "sem nome.jpg", "WhatsApp Image.jpg"]

for nome in nomes:
    (pasta / nome).touch()