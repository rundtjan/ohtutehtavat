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

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavara(self):
        kauramaito = Tuote("Kauramaito", 3)
        self.kori.lisaa_tuote(kauramaito)
        kaurakerma = Tuote("Kaurakerma", 3)
        self.kori.lisaa_tuote(kaurakerma)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
