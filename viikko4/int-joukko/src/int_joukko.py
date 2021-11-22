KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kasvatuskoko ei kunnossa")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.luvut = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        indeksi = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.luvut[i]:
                indeksi += 1

        if indeksi > 0:
            return True
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.luvut[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.luvut[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.luvut) == 0:
                taulukko_old = self.luvut
                self.luvut = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.luvut)

            return True

        return False

    def poista(self, n):
        indeksi = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.luvut[i]:
                indeksi = i  # siis luku löytyy tuosta kohdasta :D
                self.luvut[indeksi] = self.luvut[self.alkioiden_lkm-1]
                self.luvut[self.alkioiden_lkm-1] = 0
                self.alkioiden_lkm -= 1
                return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.luvut[0:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.luvut[i]) + ", "
            tuotos += str(self.luvut[self.alkioiden_lkm - 1])
            tuotos += "}"
            return tuotos
