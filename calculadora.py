historico = []

def salvar(operacao, resultado):
    historico.append({
        "operacao": operacao,
        "resultado": resultado
    })

def listar():
    if not historico:
        print("Nenhum cálculo realizado ainda.")
    else:
        for i, item in enumerate(historico):
            print(i, item["operacao"], "=", item["resultado"])

def deletar(indice):
    if 0 <= indice < len(historico):
        historico.pop(indice)
        print("Item removido com sucesso.")
    else:
        print("Índice inválido.")

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def executar_calculadora():
    while True:
        print("\n1-Somar 2-Subtrair 3-Multiplicar 4-Dividir")
        print("5-Ver Histórico 6-Excluir do Histórico 7-Sair")

        op = input("Escolha: ")

        if op == "7":
            print("Encerrando...")
            break

        elif op == "5":
            listar()

        elif op == "6":
            listar()
            try:
                indice = int(input("Digite o índice para excluir: "))
                deletar(indice)
            except:
                print("Entrada inválida")

        elif op in ["1", "2", "3", "4"]:
            try:
                a = float(input("Número 1: "))
                b = float(input("Número 2: "))
            except:
                print("Digite apenas números!")
                continue

            if op == "1":
                r = soma(a, b)
                salvar(f"{a} + {b}", r)
                print("Resultado:", r)

            elif op == "2":
                r = sub(a, b)
                salvar(f"{a} - {b}", r)
                print("Resultado:", r)

            elif op == "3":
                r = mult(a, b)
                salvar(f"{a} * {b}", r)
                print("Resultado:", r)

            elif op == "4":
                r = div(a, b)
                print("Resultado:", r)
                if b != 0:
                    salvar(f"{a} / {b}", r)

        else:
            print("Opção inválida!")


# ESSA LINHA É A CHAVE
if __name__ == "__main__":
    executar_calculadora()