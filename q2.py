import sys

def verificar(string):
    caracteres = list(string)
    qtd_as = 0
    for letra in caracteres:
        if letra == 'a' or letra == 'A':
            qtd_as += 1
    return qtd_as

if len(sys.argv) != 2:
    print("Para usar o código faça: python3 q2.py <string>")
    sys.exit(1)

string = sys.argv[1]

print(f"A quantidade de As é de: {verificar(string)}")
