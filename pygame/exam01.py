import random
j = ["골목길","집","산","편의점"]
m = ["커터칼","가위","송곳","벽돌"]
b = ["정재민","정재성","박율","박사온"]
d = 0
s = 0
g = 0


d = random.choice(j) 
s = random.choice(m)
g = random.choice(b) 
print(f"{d}이 {s}에서 {g}로 죽임 ")