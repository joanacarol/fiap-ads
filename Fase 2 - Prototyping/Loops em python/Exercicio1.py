#1. Você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos. Como não estudamos listas neste capítulo, você não deve se preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final.

qnt_alimentos = int(input("Quantos alimentos você consumiu hoje?"))
i = 0
calorias_consumidas = 0
while i < int(qnt_alimentos):
    i += 1
    calorias = int(input(f"Informe a quantidade de calorias da refeição {i}: "))
    calorias_consumidas += calorias
print(f"Total calorias consumidas {calorias_consumidas}")    