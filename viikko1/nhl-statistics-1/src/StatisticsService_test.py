import unittest
from enum import Enum
from statistics_service import StatisticsService
from player import Player

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_found(self):
        result = self.stats.search("Semenko")

        self.assertEqual(result.name, "Semenko")

    def test_search_not_found(self):
        result = self.stats.search("asd")

        self.assertEqual(result, None)

    def test_team(self):
        result = self.stats.team("EDM")

        self.assertEqual([result[0].name, result[1].name, result[2].name], ["Semenko", "Kurri", "Gretzky"])

    def test_top_empty(self):
        result = self.stats.top(2)

        self.assertEqual([result[0].name,result[1].name], ["Gretzky", "Lemieux"])

    def test_top_points(self):
        result = self.stats.top(1, SortBy.POINTS)

        self.assertEqual(result[0].name, "Gretzky")
    
    def test_top_assists(self):
        result = self.stats.top(1, SortBy.ASSISTS)

        self.assertEqual(result[0].name, "Gretzky")
    
    def test_top_goals(self):
        result = self.stats.top(1, SortBy.GOALS)

        self.assertEqual(result[0].name, "Gretzky")
