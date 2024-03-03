n = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))

fibonacci_sequence = [0, 1]

if n <= 0:
    print("Nenhum termo válido foi solicitado.")
elif n == 1:
    print("Os primeiros 1 número da sequência de Fibonacci é:")
    print(fibonacci_sequence[0])
elif n == 2:
    print("Os primeiros 2 números da sequência de Fibonacci são:")
    print(fibonacci_sequence)
else:
    print("Os primeiros", n, "números da sequência de Fibonacci são:")
    for _ in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    print(fibonacci_sequence)
