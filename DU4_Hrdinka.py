# Řešení úloh DU4 (Hrdinka)


# Jednodušší úkol
age = 18
money = 30
beer_price = 30

if age >= 18:
    if money >= 30:
        print('Můžeš si koupit pivo.')
        balance = money - beer_price
        print('Zůstatek peněz na účtu je po koupi ' + str(balance) + ' Kč.')
    else:
        print('Nemůžeš si koupit pivo. Máš nedostatek peněz na účtu.')
else:
    print('Nemůžeš si koupit pivo. Není ti 18 let.')


# Složitější úkol
ticket_price = 45

age = input("Zadejte věk: ")

for i in range(4):
    try:
        val = float(age)
        if float(age) < 0:
            age = float(input("Věk neexistuje. Zadejte věk znovu: "))
        else:
            break
    except ValueError:
        age = input("To není číslo. Zadejte věk znovu: ")

try:
    val = float(age)
except ValueError:
    print("Zadali jste požadavek 5x špatně. Nemáte nárok na lístek. Jděte pěšky.")
    exit()

age = float(age)

tram_employee = str(input("Jste zaměstnancem tramvajové služby? (ANO/NE): "))
while tram_employee.upper() not in ["ANO","NE"]:
    tram_employee = str(input("Chybné zadání. Jste zaměstnancem tramvajové služby? Zadejte buď ANO nebo NE: "))
tram_employee = tram_employee.upper()

if age < 18:
    if age < 12:
        ticket_price = 0
    else:
        ticket_price = ticket_price * 0.5
elif age > 65:
    if tram_employee == "ANO":
        ticket_price = 0
    else:
        ticket_price = ticket_price * 0.3
else:
    if tram_employee == "ANO":
        if age > 55:
            ticket_price = 0
        else:
            ticket_price = ticket_price * 0.8

print('Jízdenka stojí ' + str(ticket_price) + ' Kč.')