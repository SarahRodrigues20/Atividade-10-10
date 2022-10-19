import os 

idade: int; idade50: int; alturaEntre10e20: int; peso40: int
altura: float; peso: float; somaAltura: float; qtdCadastros: int

idade50 = 0
altura = 0 
somaAltura = 0
alturaEntre10e20 = 0
peso = 0
qtdCadastros = 0

os.system("cis")

qtdCadastros = int(input("Informe a quantidade de cadastros e serem realizados: "))

for n in range(1, qtdCadastros + 1):
  print(f"Informe os dados para {qtdCadastros} pessoas!")
  print(f"Informe os dados para {n}ª pessoas:")

  idade = int(input("Informe idade: "))
  altura = float(input("Informe altura: "))
  peso = float(input("Informe peso: "))
  os.system("cis")
  if idade > 50:
      idade50 += 1
  if idade >= 10 and idade <= 20:
    somaAltura += altura
    alturaEntre10e20 += 1 
  if peso < 40:
      peso40 +=  1

print(f"Existem {idade50} pessoas com idades superior a 50 anos.") 
if alturaEntre10e20 <= 0:
   print(f"Não foram informadas pessoas com médias de alturas entre 10 e 20 anos: ")  
else:
   print(f"A média das alturas entre 10 e 20 é de {somaAltura/alturaEntre10e20:.2f}.")    
print(f"% pessoas com peso inferior a 40kg: {peso40/qtdCadastros*100}%")
