from calculadora import soma, sub, mult, div

def testar():
    assert soma(2, 2) == 4
    assert sub(5, 3) == 2
    assert mult(3, 3) == 9
    assert div(10, 2) == 5

    print("Todos os testes passaram com sucesso!")

testar()