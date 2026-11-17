def ensinar():
    pergunta = input("Digite a pergunta:").strip().lower()
    resposta = input("Digite a resposta:").strip().lower()

    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta} - {resposta}\n")

def conversar():
    fala = input("você: ").strip().lower()
    encontrou = False

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(" - ")
                if len(dados) == 2:
                    pergunta, resposta = dados
                    if fala == pergunta:
                        print(f"Bot: {resposta}")
                        encontrou = True
                        break
