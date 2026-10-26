from pathlib import Path

pasta = Path("teste2")

for numero, arquivo in enumerate(pasta.iterdir(), start=1):
    novo_nome = f"viagem_{numero:02d}{arquivo.suffix}"
    arquivo.rename(pasta / novo_nome)