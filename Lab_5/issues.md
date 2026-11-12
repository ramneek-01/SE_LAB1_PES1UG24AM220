# Lab 5 — Static Analysis Issue Register

**Student:** Ramneek Gautam  
**SRN:** PES1UG24AM220  
**Assigned program:** Tournament Scoreboard

| Issue | Category | Evidence / location | Remediation |
|---|---|---|---|
| Mutable default player list | Correctness | Original `addTeam(..., players=[])` | Use `None` and create a new list per team. |
| Shell command construction | Security | Original `os.system("scp ... " + server ...)` | Replaced shell string construction with an argument-list subprocess call, then removed the unused remote-publish helper and subprocess dependency. |
| Insecure temporary path generation | Security | Original `tempfile.mktemp()` | Use `NamedTemporaryFile(delete=False)` to create the temporary file securely. |
| Hard-coded demo credential | Security / maintainability | Original `REFEREE_PASSWORD` constant | Removed the unused hard-coded credential. |
| Import-time execution | Maintainability | Original unconditional `main()` call | Use the `if __name__ == "__main__"` guard. |
| Input validation gaps | Robustness | Team names, team registration and match scores | Reject empty/duplicate teams, negative goals, self-matches and unregistered teams. |
| Pylint findings | Quality | Captured final Pylint output | Final captured score is 10.00/10. |
| Bandit B404 | Security warning | Captured Bandit output flags `subprocess` import | The subprocess-based publishing helper was removed from the final source. A fresh Bandit scan after that removal is not present in the supplied screenshots. |
| Flake8 E501 / W293 | Style | Captured Flake8 output lists long lines and whitespace | Formatting cleanup was attempted. The supplied screenshot still shows E501/W293 findings; a clean final scan is not evidenced. |

## Verification qualification
The issue list distinguishes code-review findings from findings visible in the screenshots. It does not claim that every final tool scan is clean. Re-run the tools against the final committed source to establish final results.
