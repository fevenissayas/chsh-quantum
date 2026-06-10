# CHSH Game — Quantum vs Classical Correlation

A Qiskit implementation of the CHSH game, demonstrating how quantum entanglement produces stronger-than-classical correlations.

## The Game

- Referee sends random bits $x$ to Alice and $y$ to Bob.
- Alice outputs $a$, Bob outputs $b$.
- **Win condition**: $a \oplus b = x \land y$

| Strategy | P(win) | CHSH value $S$ |
|----------|--------|----------------|
| Classical (deterministic) | 0.75 | 2.0 |
| Quantum (Bell state) | $\cos^2(\pi/8) \approx 0.854$ | $2\sqrt{2} \approx 2.828$ |

Classical correlations are bounded by $|S| \leq 2$ (Bell's theorem). Quantum entanglement reaches $|S| = 2\sqrt{2}$ (Tsirelson's bound), violating the classical limit.

## Usage

```bash
# Install
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run script
python3 chsh_game.py

# Or run the notebook with full evaluation & plots
jupyter notebook chsh_game.ipynb
```

## Files

| File | Description |
|------|-------------|
| `chsh_game.py` | Core game logic (classical & quantum strategies) |
| `chsh_game.ipynb` | Notebook with evaluation matrices, CHSH analysis, and plots |
| `requirements.txt` | Python dependencies |
