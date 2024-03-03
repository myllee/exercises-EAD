metros = float(input("Digite a medida em metros: "))
centimetros = 0

for i in range(int(metros)):
    centimetros += 100

print(f"{metros} metros equivalem a {centimetros} centímetros.")