# Řešení úloh DU3 (Hrdinka)

books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]

# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
books.extend([{"name": "My Life and Work", "price": 300, "author": "Henry Ford", "publication_year": 2008},
              {"name": "Konstrukce CNC OS", "price": 1300, "author": "Jiří Marek", "publication_year": 2014}])
print(books)

# 2. Změň cenu jedné libovolné knihy. Vypiš list.
books[0]["price"] = 600
print(books)

# 3. Odstraň nějakou knihu. Vypiš list.
books.pop(1)
print(books)

# 4. Vypiš celkový počet knih v listu.
print(len(books))

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
name = input("Zadej název knihy: ")
price = int(input("Zadej cenu knihy: "))
author = input("Zadej autora knihy: ")
publication_year = int(input("Zadej rok vydání knihy: "))
books.append({"name": name, "price": price, "author": author, "publication_year": publication_year})
print(books)