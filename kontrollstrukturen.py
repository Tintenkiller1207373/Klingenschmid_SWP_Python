alter = 16

if alter >= 18:
    print("Du bist volljährig.")
elif alter >= 14:
    print("Du bist Jugendlicher.")
else:
    print("Du bist ein Kind.")

for i in range(1, 6):
    print(i)

zahl = 3

while zahl > 0:
    print("Countdown:", zahl)
    zahl = zahl - 1

print("Start!")

for zahl in range(1, 10):
    if zahl == 5:
        print("5 gefunden – Abbruch!")
        break
    print(zahl)

for zahl in range(1, 6):
    if zahl == 3:
        pass
    else:
        print(zahl)

eingaben = ["2", "abc", "0"]

for eingabe in eingaben:
    print("Eingabe:", eingabe)
    try:
        zahl = int(eingabe)
        ergebnis = 10 / zahl
        print("  Ergebnis:", ergebnis)
    except ValueError:
        print("  Das war keine Zahl!")
    except ZeroDivisionError:
        print("  Durch 0 teilen geht nicht!")
