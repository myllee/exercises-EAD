valor = int(input("Digite um valor inteiro: "))

print(f"Tabuada de {valor}:")
for i in range(1, 11):
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")
