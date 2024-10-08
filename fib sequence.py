
def fibonacci_check(n):
    fib_sequence = [0, 1]  

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:  
            break
        fib_sequence.append(next_fib)

    print("Sequência de Fibonacci:", fib_sequence)

    if n in fib_sequence:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

try:
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    fibonacci_check(numero)
except ValueError:
    print("Por favor, insira um número inteiro válido.")