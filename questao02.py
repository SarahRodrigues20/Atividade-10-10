precoIngresso: float
despesas: float
lugro: float
qtdIngressos: int

precoIngresso = 5.00
qtdIngresso = 120
despesas = 200.00

while precoIngresso >= 1.00:
    lucro = qtdIngresso * precoIngresso - despesas
print(f"|Preço: \t\t |R$ {precoIngresso:.2f}")
print(f"|Lucro: \t\t |R$ {lucro:.2f}")
print(f"|Ingressos vendidos: \t |{qtdIngresso}")
print("----------------------------------")

precoIngressos = precoIngresso - 0.50
qtdIngresso = qtdIngresso + 26
