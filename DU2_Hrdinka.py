# Řešení úloh DU2 (Hrdinka)

# Úloha 1
name = "Daniel"
surname = "Hrdinka"
full_name = name + " " + surname
print(full_name)
language = "Python"
character = language[0]
print(character)

# Úloha 2
fstring_full_name = f"{name} {surname}"
print(fstring_full_name)
name = "Martin"
age = 30
name_length = len(name)
name_upper = name.upper()
print(f"{name_upper} , vek: {age}, pocet znaku: {name_length}")
print("{} , vek: {}, pocet znaku: {}".format(name_upper, age, name_length))
new_name = name_upper.replace("T","M",1)
print(new_name)

# Úloha 3
x = round(5.74,1)
print(x)
x1 = 2**3
x2 = pow(2,3)
print(x1)
print(x2)
x = 5
y = 6
z = 10
result = x + y - z
result2 = result ** 2
result3 = result2 - 10
print(result)
print(result2)
print(result3)