# Lab 5 — Static Code Analysis: Tournament Scoreboard

**Student:** Ramneek Gautam  
**SRN:** PES1UG24AM220  
**Assigned source:** https://github.com/SETAPESU26/L5_38_tournament_scoreboard

## Files
- `tournament_scoreboard.py`: updated scoreboard implementation
- `issues.md`: issue register and remediation notes
- `reflection.md`: reflection on static analysis
- `reports/`: captured tool output and verification notes
- `tests/`: unit tests

## Run
```powershell
python tournament_scoreboard.py
python -m unittest discover -s tests -v
```

## Evidence status
The screenshots supplied during this work show:
- Pylint: **10.00/10**
- Unit tests: **7 passed**
- Program demonstration: successful
- Bandit: B404 warning for importing `subprocess`
- Flake8: E501 long-line findings and W293 whitespace finding

The source was subsequently updated to remove the remote-publish helper and the `subprocess` dependency. The screenshots pre-date that final source edit. The Flake8 findings shown in the screenshots are recorded as observed; a clean post-edit Flake8 run is **not evidenced**. Do not treat the historical screenshots as proof that all final scans are clean.

The uploaded lab handout requires three commits, before-and-after reports for all three tools, and a Pylint score above 9.5. The available screenshots do not show complete before reports. See `reports/verification_notes.md`.
