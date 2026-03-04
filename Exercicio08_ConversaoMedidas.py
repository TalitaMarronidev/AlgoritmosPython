#8) Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas. 
#Ex:  
#Digite uma distância em metros: 185.72 
#A distância de 85.7m corresponde a: 
#0.18572Km 
#1.8572Hm 
#18.572Dam 
#1857.2dm 
#18572.0cm 
#185720.0mm 


num = float(input('Informe uma distância em metros:'))

km = num / 1000
Hm = num / 100
Dam = num / 10
dm = int(num * 10)
cm = int(num * 100)
mm = int(num * 1000)

print(f'A distância de {num} metros em km é de: {km}')
print(f'A distância de {num} metros em Hm é de: {Hm}')
print(f'A distância de {num} metros em Dam é de: {Dam}')
print(f'A distância de {num} metros em dm é de: {dm}')
print(f'A distância de {num} metros em cm é de: {cm}')
print(f'A distância de {num} metros em mm é de: {mm}')