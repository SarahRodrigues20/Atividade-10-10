faixa1 = 0

faixa2 = 0

faixa3 = 0

faixa4 = 0

faixa5 = 0

for i in range(1, 9):

   print('Informe a idade a pessoa', i+1,)

   idade=int(input())


   if (idade<=15):

       faixa1 +=1

   elif (idade>=16 and idade<=30):

       faixa2 +=1

   elif (idade>=31 and idade<=45):

       faixa3 +=1

   elif (idade>=46 and idade<=60):

       faixa4+=1

   elif (idade>60):

       faixa5+=1

       

print("Pessoas na faixa etária até 15 anos:", faixa1)

print("Pessoas na faixa etária de 16 a 30 anos:", faixa2)

print("Pessoas na faixa etária de 31 a 45 anos:", faixa3)

print("Pessoas na faixa etária de 46 a 60 anos:", faixa4)

print("Pessoas na faixa acima de 60 anos:", faixa5)

porcentagem1 = (faixa1/8)*100

porcentagem2 = (faixa5/8)*100

print("O número de pessoas na faixa etária até 15 anos é de", porcentagem1,'%')

print("O número de pessoas na faixa etária acima de 60", porcentagem2,'%')