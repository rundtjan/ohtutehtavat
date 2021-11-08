import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Stubb", "JKL", 6, 22),
            Player("Sipilae", "JKL", 50, 60),
            Player("Kiviniemi",  "KES", 17, 33),
            Player("Soini", "DET", 22, 36),
            Player("Katainen", "EDM", 25, 59)
        ]


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())


    def test_search_loytaa_pelaajan(self):
        player = self.statistics.search("Stubb")
        self.assertEqual(str(player), "Stubb JKL 6 + 22 = 28")

    def test_search_ei_loyda_olematonta_pelaajaa(self):
        player = self.statistics.search("Stubi")
        self.assertIsNone(player)

    def test_team_palauttaa_joukkueen(self):
        team = self.statistics.team("JKL")
        self.assertEqual(len(team), 2)

    def test_hakee_oikean_maaran_topscorers(self):
        topscorers = self.statistics.top_scorers(4)
        self.assertEqual(len(topscorers), 4)

    def test_osaa_jarjestaa_topscorers(self):
        topscorers = self.statistics.top_scorers(4)
        self.assertEqual(topscorers[0].name, "Sipilae")