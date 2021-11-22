import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self._pankki_mock = Mock()
        self._viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self._viitegeneraattori_mock.uusi.side_effect = [42, 43, 44]

        self._varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 3
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "härkis", 4)
            if tuote_id == 3:
                return Tuote(3, "kulta", 2)

        # otetaan toteutukset käyttöön
        self._varasto_mock.saldo.side_effect = varasto_saldo
        self._varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self._kauppa = Kauppa(self._varasto_mock, self._pankki_mock, self._viitegeneraattori_mock)
        
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostos_missa_kaksi_eri_tuottetta_paattyy_pankin_metodin_tilisiirron_kutsulla_oikeilla_parametreilla(self):
        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(2)
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 9)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostos_missa_kaksi_kpl_samaa_tuottetta_paattyy_pankin_metodin_tilisiirron_kutsulla_oikeilla_parametreilla(self):
        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostos_missa_toinen_tuote_loppu_paattyy_pankin_metodin_tilisiirron_kutsulla_oikeilla_parametreilla(self):
        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(3)
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_aloita_asiointi_nollaa_ostoskorin(self):
        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(3)
        self._kauppa.aloita_asiointi()
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 0)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_ostokselle(self):
        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.aloita_asiointi()
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 0)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.aloita_asiointi()
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 43, "12345", "33333-44455", 0)

        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.aloita_asiointi()
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 44, "12345", "33333-44455", 0)

        self.assertEqual(self._viitegeneraattori_mock.uusi.call_count, 3)

    def test_tuotteen_poisto_ostoskorista_vahentaa_ostosumman(self):
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(2)
        self._kauppa.poista_korista(1)
        self._kauppa.tilimaksu("pekka", "12345")

        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 4)

    def test_tuotteen_poisto_ostoskorista_palauttaa_sen_varastoon(self):
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(2)
        self._kauppa.poista_korista(1)

        self._varasto_mock.palauta_varastoon.assert_called()

    def test_tuotteen_poisto_ostoskorista_palauttaa_oikean_tuotteen_varastoon(self):
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(2)
        self._kauppa.poista_korista(1)

        self._varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))
