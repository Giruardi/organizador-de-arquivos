from pathlib import Path
import shutil

pasta = Path("teste")

for nome in ["PDFs", "Imagens", "Documentos", "Outros"]:
    (pasta / nome).mkdir(exist_ok=True)

for arquivo in list(pasta.iterdir()):
    if arquivo.is_file():
        if arquivo.suffix == ".pdf":
            shutil.move(arquivo, pasta / "PDFs" / arquivo.name)
        elif arquivo.suffix in [".jpg", ".png"]:
            shutil.move(arquivo, pasta / "Imagens" / arquivo.name)
        elif arquivo.suffix in [".docx" , ".txt"]:
            shutil.move(arquivo, pasta / "Documentos" / arquivo.name)
        else:
            shutil.move(arquivo, pasta / "Outros" / arquivo.name)