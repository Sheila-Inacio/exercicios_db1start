mensagem = "A soma dos numeros digitados são: "
a = input("Digite o primeiro numero: ")
b = input("Digite o segundo numero: ")
if not a.isnumeric():
    print("Voce não digitou um numero, para primeira variavel")

if not b.isnumeric():
    print("Voce não digitou um numero, para segunda variavel")

if a.isnumeric() and b.isnumeric():
    resultado = int(a) + int(b)
    print(mensagem, resultado)