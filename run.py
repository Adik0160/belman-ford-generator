i = 1
wezelDict = {}
skrypt = ""
while(True): #Węzeł
    wezel = input()
    if wezel == '0':
        break
    wezelDict[wezel] = "wezel"+str(i)
    i += 1
print(wezelDict)
for key in wezelDict:
    skrypt += wezelDict[key] + "=Wezel('" + key + "')\r\n"

i = 1
while(True): #krawędź
    wartosc = 0.0
    pierwszy = input("pierwszy " + str(i) +"> ")
    if pierwszy == '0':
        break
    drugi = input("drugi " + str(i) +"> ")
    while(True):
            try:
                dlugosc = float(input("długość od " + pierwszy + " do " + drugi + "; nr. " + str(i) + ">> "))
                if dlugosc == 0.0:
                    break
                mnoznik = float(input("mnożnik " + pierwszy + " do " + drugi + "; nr. " + str(i) + ">> "))      
            except:
                print("tylko liczby byq, wpisuejmy dane od nowa")
                dlugosc = 0
                mnoznik = 0
                wartosc = 0 #dane od nowa
            wartosc += dlugosc*mnoznik*20
    try:
        skrypt += "krawedz" + str(i) + "=Krawedz(" + str(wartosc) + "," + wezelDict[pierwszy] + "," + wezelDict[drugi] + ")\r\n"
        i += 1
    except:
        print("luźno byku popraw to")       

skrypt += "wierzchołkiLista={"
for wierzcholki in wezelDict:
    skrypt += wezelDict[wierzcholki] + ","
skrypt += "}\r\n"

skrypt += "krawedzieLista={"
for krawiedzie in range(1,i,1):
    if krawiedzie != 1:
        skrypt += ","
    skrypt += "krawedz"+ str(krawiedzie)
skrypt += "}\r\n"

print(skrypt)