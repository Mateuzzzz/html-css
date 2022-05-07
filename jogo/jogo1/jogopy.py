import random

jogadores = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"]
funcoes = ["assassino", "engenheiro", "cozinheiro", "lixeiro", "policial", "xerife",
           "programador", "zumbi", "cientista", "médico"]

"""Escolhendo os jogadores es suas funções"""

f1 = random.choice(funcoes)
funcoes.remove(f1)

f2 = random.choice(funcoes)
funcoes.remove(f2)

f3 = random.choice(funcoes)
funcoes.remove(f3)

f4 = random.choice(funcoes)
funcoes.remove(f4)

f5 = random.choice(funcoes)
funcoes.remove(f5)

f6 = random.choice(funcoes)
funcoes.remove(f6)

f7 = random.choice(funcoes)
funcoes.remove(f7)

f8 = random.choice(funcoes)
funcoes.remove(f8)

f9 = random.choice(funcoes)
funcoes.remove(f9)

f10 = random.choice(funcoes)
funcoes.remove(f10)

"""Dizer a função de cada jogador"""

print(f"p1 = {f1}")
print(f"p2 = {f2}")
print(f"p3 = {f3}")
print(f"p4 = {f4}")
print(f"p5 = {f5}")
print(f"p6 = {f6}")
print(f"p7 = {f7}")
print(f"p8 = {f8}")
print(f"p9 = {f9}")
print(f"p10 = {f10}")
