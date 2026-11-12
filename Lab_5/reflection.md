# Lab 5 — Reflection

**Student:** Ramneek Gautam  
**SRN:** PES1UG24AM220

The uploaded three-page lab handout asks for reflection answers but does not include the exact reflection-question wording. These are general reflections on the exercise, not answers to unseen prescribed questions.

1. **What is static code analysis?**  
   Static code analysis inspects source code without executing it to identify potential defects, insecure patterns and style violations.

2. **What did the tools check?**  
   Pylint evaluates code quality and likely programming mistakes. Bandit identifies common Python security risks. Flake8 checks style and formatting conventions.

3. **What changes were made?**  
   The scoreboard was updated to avoid a mutable default argument, validate teams and scores, use safer temporary-file creation, remove a hard-coded credential, protect demo execution with a main guard, and remove the unused remote-publish helper that depended on subprocess.

4. **What was learned?**  
   A program can produce the expected demonstration output and still contain security, correctness or maintainability problems. Static analysis helps make these issues visible, but each finding must be understood and verified rather than merely suppressed.

**Evidence limitation:** The screenshots show Pylint 10.00/10 and seven passing tests. They also show a Bandit B404 warning and Flake8 E501/W293 findings. A fresh complete scan after the final source changes is not included in the evidence.
