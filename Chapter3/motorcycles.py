motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')

print(motorcycles)

print(motorcycles + ['triumph'])

print(motorcycles)

motos = []

motos.append('honda')
motos.append('yamaha')
motos.append('suzuki')

print(motos)

motos.insert(0, 'indian')
print(motos)

del motos[2]

print(motos)

popped_moto = motos.pop()

print(popped_moto.title())

last_owned = motos.pop()

print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motos.pop(0)

print(f"The first bike I owned was a {first_owned.title()}.")

motos = ['honda', 'indian', 'suzuki', 'ducati', 'suzuki', 'suzuki']

print(motos)

motos.remove('suzuki')

print(motos)