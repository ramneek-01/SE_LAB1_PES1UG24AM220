"""Tournament scoreboard used for the Lab 5 static-analysis exercise."""

import os
import random
import tempfile

POINTS = {"win": 3, "draw": 1, "loss": 0}
teams = {}
matches = []


def add_team(team_name, players=None):
    """Register a team and initialise its statistics."""
    if not team_name or not team_name.strip():
        raise ValueError("Team name cannot be empty.")
    if team_name in teams:
        raise ValueError("Team already exists.")
    teams[team_name] = {
        "played": 0, "won": 0, "drawn": 0, "lost": 0,
        "gf": 0, "ga": 0, "players": list(players) if players else [],
    }


def match_result(home_goals, away_goals):
    """Return the match result from the home team's perspective."""
    if home_goals < 0 or away_goals < 0:
        raise ValueError("Goals cannot be negative.")
    if home_goals > away_goals:
        return "home"
    if home_goals < away_goals:
        return "away"
    return "draw"


def record_match(home, away, home_goals, away_goals):
    """Record a match and update both teams' statistics."""
    if home == away:
        raise ValueError("A team cannot play itself.")
    if home not in teams or away not in teams:
        raise KeyError("Both teams must be registered.")
    result = match_result(home_goals, away_goals)
    for team, scored, conceded in (
        (home, home_goals, away_goals), (away, away_goals, home_goals)
    ):
        stats = teams[team]
        stats["played"] += 1
        stats["gf"] += scored
        stats["ga"] += conceded
    if result == "draw":
        teams[home]["drawn"] += 1
        teams[away]["drawn"] += 1
    else:
        winner, loser = (home, away) if result == "home" else (away, home)
        teams[winner]["won"] += 1
        teams[loser]["lost"] += 1
    matches.append((home, away, home_goals, away_goals))


def points(team_name):
    """Return league points for a team."""
    stats = teams[team_name]
    return stats["won"] * POINTS["win"] + stats["drawn"] * POINTS["draw"]


def goal_difference(team_name):
    """Return goals scored minus goals conceded."""
    stats = teams[team_name]
    return stats["gf"] - stats["ga"]


def league_table():
    """Return team names sorted by points and goal difference."""
    return sorted(
        teams,
        key=lambda name: (points(name), goal_difference(name)),
        reverse=True,
    )


def is_top_two(team_name):
    """Return whether a registered team is in the top two."""
    return team_name in league_table()[:2]


def toss_coin():
    """Simulate a fair coin toss."""
    return random.choice(("Heads", "Tails"))


def table_file_path():
    """Create a temporary JSON file safely and return its path."""
    with tempfile.NamedTemporaryFile(
        suffix=".json", prefix="league_table_", delete=False
    ) as temporary_file:
        return temporary_file.name


def publish_table(server):
    """Publish the table to a remote host."""
    os.system("scp table.json " + server + ":/var/www/")


def main():
    """Run the sample tournament and print the league table."""
    for name in ("Royal Strikers", "City Rovers", "Lake United", "Hill Warriors"):
        add_team(name)
    print("Toss:", toss_coin())
    record_match("Royal Strikers", "City Rovers", 2, 1)
    record_match("Lake United", "Hill Warriors", 0, 0)
    record_match("City Rovers", "Lake United", 3, 2)
    record_match("Hill Warriors", "Royal Strikers", 1, 1)
    print("Pos Team Played Won Drawn Lost Pts")
    for position, name in enumerate(league_table(), 1):
        stats = teams[name]
        print(position, name, stats["played"], stats["won"], stats["drawn"],
              stats["lost"], points(name))
    print("Is City Rovers in the top two?", is_top_two("City Rovers"))
    print("Matches played:", len(matches))


if __name__ == "__main__":
    main()
