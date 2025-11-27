import random

n_pessoas = 1000

fila: list[int] = list(range (1, n_pessoas + 1))
random.shuffle(fila)

n_falsos = n_pessoas // 2
falsos: list[int] = set(random.sample(fila, n_falsos))
# custo quadratico 2 N^2
index = 0
while index < len(fila):
    pessoa = fila[index]

    if pessoa in falsos: # o(n)
        del fila[index] # o(n)
    else:
        index += 1

print(fila)
print(falsos)