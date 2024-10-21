import sys

def fibo(number):
    x = [0,1]
    i = 2
    add = 0

    if number == 1 or number == 0:
        return 1
    
    while(add <= number):
        add = x[i-1] + x[i-2]
        if add <= number:
            if add == number:
                return 1
            x.append(x[i-1] + x[i-2])
        i += 1

    return 0

if len(sys.argv) != 2:
    print("Para usar o código faça: python3 q1.py <número>")
    sys.exit(1)
          

numero_escolhido = int(sys.argv[1])

if fibo(numero_escolhido):
    print(f"{numero_escolhido} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_escolhido} não pertence à sequência de Fibonacci.")
