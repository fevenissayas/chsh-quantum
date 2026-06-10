# CHSH Game — Quantum vs Classical Correlation

This repository implements the CHSH game in **Qiskit**. It demonstrates that quantum entanglement produces stronger correlations than any classical strategy.

## How It Works

- **Classical strategy** — both players always output 0. Wins 75% of the time.
- **Quantum strategy** — Alice and Bob share a Bell state $|\Phi^+\rangle$ and measure in rotated bases depending on their inputs. Wins ~85.4% of the time, exceeding the classical bound and violating Bell's inequality.

## Getting Started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 chsh_game.py          # run core simulation
```

## Files

- `chsh_game.py` — core game logic (classical & quantum strategies)
- `chsh_game.ipynb` — evaluation matrices, CHSH correlation analysis, and plots
