
import numbers

class Osake:
    def __init__(self, nimi, ostohinta, maara):

        lista = []
        self.nimi = nimi
        lista.append(self.nimi)
        self.ostohinta = ostohinta
        lista.append(self.ostohinta)
        self.maara = maara
        lista.append(self.maara)



        @property
        def nimi(self):
            return self._nimi
        @nimi.setter
        def nimi(self, value):
            self._nimi = value

        @property
        def ostohinta(self):
            return self._ostohinta
        @ostohinta.setter
        def ostohinta(self, value):
            if value < 0:
                value = 0
            self._ostohinta = value

        @property
        def maara(self):
            return self._maara
        @maara.setter
        def maara(self, value):
            if value < 0:
                value = 0
            self._maara = value

    

        
    
    def laske_tuotto_yhdelle_vuodelle(self, kasvuprosentti, ostohinta):

        return ostohinta * (kasvuprosentti / 100)


    def tulosta_arvo(self, kasvuprosentti, vuodet):


        potti = (1 + kasvuprosentti / 100) * (self.ostohinta * self.maara)
        korkoaKorolle = self.ostohinta * self.maara * (1 + kasvuprosentti / 100) ** vuodet
        tuotto = korkoaKorolle - (self.ostohinta * self.maara)
        kokopotti = korkoaKorolle + tuotto

        #lasketuotto = self.laske_tuotto_yhdelle_vuodelle(self, kasvuprosentti, vuodet)
        arvo = self.maara * self.ostohinta

        print("Osakkeen potin arvo on {:.2f} ja tuotto {:.2f}".format(korkoaKorolle, tuotto))
        kokopotti = 0
        for i in range(vuodet):
            
            arvo += self.laske_tuotto_yhdelle_vuodelle(kasvuprosentti, self.ostohinta)
            
        return korkoaKorolle
        



        
    
if __name__ == "__main__":

    lista = []
    while True:

        
        nimi = input("Anna osakkeen nimi: ")
            
        ostohinta = float(input("Anna osakkeen ostohinta/kpl: "))
            
        maara = int(input("Anna ostettujen osakkeiden lukumäärä: "))

        lista.append(Osake(nimi, ostohinta, maara))
        osake = Osake(nimi, ostohinta, maara)

        valinta = input("Lisää osakkeita (k/e)? ")
        print()
        if valinta == "k" or valinta == "K":
            continue
        elif valinta == "e" or valinta == "E":

            kasvuprosentti = int(input("Anna kasvuprosentti: "))
            vuodet = int(input("Anna vuodet: "))
            print()
            break

    osake.tulosta_arvo(kasvuprosentti, vuodet)
    potti = 0

    for i in lista:
        print(f"{i.nimi} {i.maara} {i.ostohinta}")

        
        potti += i.tulosta_arvo(kasvuprosentti, vuodet)
        
    print("Koko potin arvo on: {:.2f}".format(potti))

