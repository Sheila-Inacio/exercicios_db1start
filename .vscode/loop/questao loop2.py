bimestre = 4
nota = 0
for x in range(bimestre):
    nota += float(input("Digite sua nota "))
media = nota / bimestre
if media >= 7:
    print(f'Sua média é {media}! Parabéns! ')
else:
    print(f'Sua média é {media}! REPROVADO ')