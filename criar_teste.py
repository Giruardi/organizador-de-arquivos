from pathlib import Path

pasta = Path("teste")
pasta.mkdir(exist_ok=True)

nomes = ["foto1.jpg", "foto2.png", "relatorio.pdf", "notas.txt", "musica.mp3", "contrato.pdf" , "FBI.docx" , "limpador.txt"]

for nome in nomes:
    (pasta / nome).touch()