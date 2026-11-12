# Verification Notes

This folder records the evidence actually supplied in the conversation.

| Check | Captured result | Interpretation |
|---|---|---|
| Pylint | 10.00/10 | Above the handout's >9.5 target at the time captured. |
| Bandit | B404, subprocess import | Warning was present in the screenshot. The remote-publish helper was later removed; rescan to verify. |
| Flake8 | Seven E501 findings; earlier W293 finding | Formatting violations were present in the screenshots. A clean final scan is not evidenced. |
| Unit tests | 7 tests, OK | All seven tests shown in the screenshot passed. |
| Program run | Four matches printed; top-two query returned True | Demonstration completed successfully. |

## Before reports
The screenshots supplied do not contain complete, legible before-fix outputs for all three tools. Therefore no invented before reports are included. Generate genuine before reports from the preserved original assigned file if available.

## Commands for a final local verification
```powershell
python -m pylint tournament_scoreboard.py
python -m bandit -r tournament_scoreboard.py
python -m flake8 tournament_scoreboard.py
python -m unittest discover -s tests -v
```

Do not describe Bandit or Flake8 as clean unless these commands are run against the final source and their actual output is saved.
