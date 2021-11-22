from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self._ostokset:
            maara += ostos.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        index = self._loyda_tuote_ostoksista(lisattava)
        if not index == None:
            self._ostokset[index].muuta_lukumaaraa(1)
        else:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        index = self._loyda_tuote_ostoksista(poistettava)
        if not index == None:
            self._ostokset[index].muuta_lukumaaraa(-1)
            if self._ostokset[index].lukumaara() == 0:
                del self._ostokset[index]

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
    
    def _loyda_tuote_ostoksista(self, tuote):
        index = 0
        for ostos in self._ostokset:
            print(ostos.tuotteen_nimi(), tuote.nimi())
            if ostos.tuotteen_nimi() == tuote.nimi():
                return index
            index += 1
        return None
