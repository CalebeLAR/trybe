from faker import Faker

faker = Faker()

print(faker.name())
print(faker.name())
print(faker.name())
print(faker.name())


faker = Faker()
Faker.seed(0)  # repare que usamos a classe 'Faker', e não a instância 'faker'
# O restante do código permanece igual
print(faker.name())
print(faker.name())
print(faker.name())
print(faker.name())

faker = Faker(locale='pt_BR')

print(faker.name())
print(faker.phone_number())
print(faker.cpf())