"""Basic unit tests for the tournament scoreboard."""

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tournament_scoreboard.py"
SPEC = importlib.util.spec_from_file_location("scoreboard", MODULE_PATH)
scoreboard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scoreboard)


class ScoreboardTests(unittest.TestCase):
    def setUp(self):
        scoreboard.teams.clear()
        scoreboard.matches.clear()

    def test_default_player_lists_are_independent(self):
        scoreboard.add_team("A")
        scoreboard.add_team("B")
        scoreboard.teams["A"]["players"].append("Player 1")
        self.assertEqual(scoreboard.teams["B"]["players"], [])

    def test_draw_awards_one_point_each(self):
        scoreboard.add_team("A")
        scoreboard.add_team("B")
        scoreboard.record_match("A", "B", 1, 1)
        self.assertEqual(scoreboard.points("A"), 1)
        self.assertEqual(scoreboard.points("B"), 1)

    def test_negative_score_is_rejected(self):
        with self.assertRaises(ValueError):
            scoreboard.match_result(-1, 0)

    def test_duplicate_team_is_rejected(self):
        scoreboard.add_team("A")
        with self.assertRaises(ValueError):
            scoreboard.add_team("A")

    def test_unknown_team_is_rejected(self):
        scoreboard.add_team("A")
        with self.assertRaises(KeyError):
            scoreboard.record_match("A", "B", 0, 0)

    def test_top_two_handles_small_leagues(self):
        scoreboard.add_team("A")
        self.assertTrue(scoreboard.is_top_two("A"))
        self.assertFalse(scoreboard.is_top_two("missing"))

    def test_match_updates_stats_and_points(self):
        scoreboard.add_team("A")
        scoreboard.add_team("B")
        scoreboard.record_match("A", "B", 2, 1)
        self.assertEqual(scoreboard.points("A"), 3)
        self.assertEqual(scoreboard.goal_difference("A"), 1)


if __name__ == "__main__":
    unittest.main()
