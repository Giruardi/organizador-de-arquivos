from pathlib import Path

pasta = Path("teste2")
numero = 1

for arquivo in pasta.iterdir():
    novo_nome = f"viagem_{numero:02d}{arquivo.suffix}"
    if arquivo.suffix == ".jpg":
        arquivo.rename(pasta / novo_nome)
        numero += 1