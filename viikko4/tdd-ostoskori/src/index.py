# testikoodi tänne jos tarvetta

from ostoskori import Ostoskori
from tuote import Tuote

def main():
    kori = Ostoskori()
    kauramaito = Tuote("Kauramaito", 3)
    kori.lisaa_tuote(kauramaito)
    kauramaito = Tuote("Kauramaito", 3)
    kori.lisaa_tuote(kauramaito)
    print(str(kori.ostokset()))

if __name__ == "__main__":
    main()