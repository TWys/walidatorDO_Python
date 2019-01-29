nrDO = input('Podaj numer dowodu osobistego: ')
nrDO = [n for n in nrDO]

# Sprawdzenie czy numer ma odpowiednią długość
if len(nrDO) != 9:
    print('Numer niepoprawny')
    quit()

i = 0
while i < 3:
    # Zmiana małych liter na wielkie (jeżeli wpisano małe)
    if 96 < ord(nrDO[i]) < 123:
        nrDO[i] = chr(ord(nrDO[i])-32)
        print(nrDO[i])
    # Sprawdzenie czy 3 pierwsze znaki to litery
    if ord(nrDO[i]) < 65 or ord(nrDO[i]) > 90:
        print('Numer niepoprawny')
        quit()
    i += 1

# Sprawdzenie czy znaki od 4 do 9 to cyfry
while i < len(nrDO):
    try:
        nrDO[i] = int(nrDO[i])
    except ValueError:
        print('Numer niepoprawny')
        quit()
    i += 1

# Obliczenie sumy kontrolnej
chcksum = (ord(nrDO[0])-55) * 7 + (ord(nrDO[1])-55) * 3 + (ord(nrDO[2])-55) + nrDO[3] * 9 + nrDO[4] * 7 + nrDO[5] * 3 \
          + nrDO[6] + nrDO[7] * 7 + nrDO[8] * 3

# Sprawdzenie czy reszta z dzielenia sumy kontrolnej przez 10 daje 0- jeśli tak- numer jest poprawny
if chcksum % 10 != 0:
    print('Numer niepoprawny')
    quit()
else:
    print('Numer poprawny')
