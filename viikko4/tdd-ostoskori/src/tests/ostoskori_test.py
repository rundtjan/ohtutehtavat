import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteen(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(3, self.kori.hinta())

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavara(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        kaurakerma = Tuote("Kaurakerma", 3)
        self.kori.lisaa_tuote(kaurakerma)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_oikein(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        kaurakerma = Tuote("Kaurakerma", 3)
        self.kori.lisaa_tuote(kaurakerma)
        self.assertEqual(6, self.kori.hinta())

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavara(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_oikein(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(6, self.kori.hinta())

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_oikea_ostos(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Kauramaito")

    def test_kahden_erin_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        kaurakerma = Tuote("Kaurakerma", 3)
        self.kori.lisaa_tuote(kaurakerma)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_oikea_ostos_ja_kaksi_kpl(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Kauramaito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_jos_korissa_kaksi_samaa_tuotetta_ja_toinen_poistetaan_koriin_jaa_ostos_jossa_yksi_tuote(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.poista_tuote(kauramaito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_yhden_tuotteen_lisaamisen_ja_poistamisen_jalkeen_kori_on_tyhja(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.poista_tuote(kauramaito)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
