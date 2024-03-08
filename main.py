# Zad.1
# ulubione_sporty = ["piłka nożna", "koszykówka", "pływanie", "tenis"]
#
# ulubione_sporty_odwrocone = ulubione_sporty[::-1]
#
# mniej_lubiane_sporty = ["bieganie", "szachy"]
# ulubione_sporty_odwrocone.extend(mniej_lubiane_sporty)
#
# print("Odwrócona lista z dodanymi mniej lubianymi sportami:", ulubione_sporty_odwrocone)


# Zad.2
# skroty = {
#     "np.": "na przykład",
#     "itd.": "i tak dalej",
#     "itp.": "i tym podobne",
#     "tzn.": "to znaczy",
#     "wg": "według",
#     "red.": "redaktor",
#     "tj.": "to jest",
#     "r.": "rok",
#     "dz.": "dziennik",
#     "mgr": "magister",
#     "lic.": "licencjat",
#     "św.": "święty",
#     "wg.": "według",
#     "ur.": "urodzony",
#     "str.": "strona",
#     "kard.": "kardynał",
#     "bp": "biskup",
#     "ul.": "ulica",
#     "nr": "numer",
#     "w.": "wieku",
#     "godz.": "godzina",
# }
#
# for skrot, rozwinięcie in skroty.items():
#     print(f"{skrot}: {rozwinięcie}")

# Zad.3
# ulubione_gry = {
#     "The Witcher 3": "RPG",
#     "Counter-Strike 2": "FPS",
#     "The Legend of Zelda: Breath of the Wild": "Action-Adventure",
#     "Minecraft": "Sandbox",
#     "Overwatch": "FPS",
#     "Rocket League": "Sports",
# }
#
# liczba_gier = len(ulubione_gry)
#
# print("Ulubione gry komputerowe:")
# for gra, gatunek in ulubione_gry.items():
#     print(f"{gra} - {gatunek}")
#
# print(f"Liczba ulubionych gier komputerowych: {liczba_gier}")

# Zad.4
# zdanie = input("Podaj swoje wymyślone zdanie: ")
#
# liczba_a = zdanie.count('a')
#
# print("Liczba wystąpień litery 'a' w podanym zdaniu:", liczba_a)


# Zad.5
# import sys
#
# sys.stdout.write("Podaj pierwszą liczbę całkowitą (a): ")
# sys.stdout.flush()
# a = int(sys.stdin.readline())
#
# sys.stdout.write("Podaj drugą liczbę całkowitą (b): ")
# sys.stdout.flush()
# b = int(sys.stdin.readline())
#
# sys.stdout.write("Podaj trzecią liczbę całkowitą (c): ")
# sys.stdout.flush()
# c = int(sys.stdin.readline())
#
# wynik = a ** b + c
#
# sys.stdout.write("Wynik obliczenia a^b + c wynosi: ")
# sys.stdout.write(str(wynik))
# sys.stdout.write("\n")
# sys.stdout.flush()


# Zad.6
# a = int(input("Podaj pierwszą liczbę całkowitą (a): "))
# b = int(input("Podaj drugą liczbę całkowitą (b): "))
# c = int(input("Podaj trzecią liczbę całkowitą (c): "))
#
# if a >= b:
#     if a >= c:
#         print("Największa liczba to:", a)
#     else:
#         print("Największa liczba to:", c)
# elif b >= c:
#     print("Największa liczba to:", b)
# else:
#     print("Największa liczba to:", c)

# Zad.7
# lista_liczb = [1, 2.5, 3, 4.7, 5]
#
# for liczba in lista_liczb:
#     kwadrat = liczba ** 2
#     print(f"Kwadrat liczby {liczba} wynosi: {kwadrat}")

# Zad.8
# parzyste = []
# liczba_wprowadzonych = 0
#
# print("Podaj 10 różnych liczb:")
#
# while liczba_wprowadzonych < 10:
#     liczba = int(input(f"Podaj {liczba_wprowadzonych + 1}. liczbę: "))
#     if liczba % 2 == 0:
#         parzyste.append(liczba)
#     liczba_wprowadzonych += 1
#
# print("Liczby parzyste spośród wprowadzonych to:")
# for liczba in parzyste:
#     print(liczba)

# Zad.9
# import math
# try:
#     liczba = float(input("Podaj liczbę, z której chcesz obliczyć pierwiastek kwadratowy: "))
#
#     if liczba < 0:
#         raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej.")
#
#     pierwiastek = math.sqrt(liczba)
#     print(f"Pierwiastek kwadratowy z {liczba} wynosi: {pierwiastek}")
#
# except ValueError as ve:
#     print(f"Błąd: {ve}")





