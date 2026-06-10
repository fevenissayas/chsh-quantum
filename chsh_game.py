"""
CHSH Game: quantum entanglement advantage over classical correlation.
"""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer


def classical_strategy(trials: int = 100_000) -> float:
    """Best classical strategy: both always output 0."""
    wins = 0
    rng = np.random.default_rng()
    for _ in range(trials):
        x = int(rng.integers(0, 2))
        y = int(rng.integers(0, 2))
        a = b = 0
        if (a ^ b) == (x & y):
            wins += 1
    return wins / trials


def quantum_circuit(x: int, y: int) -> QuantumCircuit:
    """Build CHSH circuit for inputs x, y."""
    qr = QuantumRegister(2, "q")
    cr = ClassicalRegister(2, "c")
    qc = QuantumCircuit(qr, cr)

    qc.h(qr[0])
    qc.cx(qr[0], qr[1])

    if x == 0:
        qc.ry(0, qr[0])
    else:
        qc.ry(-np.pi / 2, qr[0])

    if y == 0:
        qc.ry(-np.pi / 4, qr[1])
    else:
        qc.ry(np.pi / 4, qr[1])

    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])
    return qc


def quantum_strategy(trials: int = 10_000) -> float:
    """Quantum strategy using Bell states and optimal measurements."""
    backend = Aer.get_backend("qasm_simulator")
    shots = max(1, trials // 4)
    wins = 0
    total = 0

    for x in (0, 1):
        for y in (0, 1):
            qc = quantum_circuit(x, y)
            result = backend.run(qc, shots=shots).result()
            counts = result.get_counts()

            for bitstring, count in counts.items():
                a = int(bitstring[1])
                b = int(bitstring[0])
                if (a ^ b) == (x & y):
                    wins += count
                total += count

    return wins / total


if __name__ == "__main__":
    n = 80_000

    print("CHSH Game")
    print("=" * 40)
    p_cls = classical_strategy(n)
    p_qnt = quantum_strategy(n)
    p_opt = np.cos(np.pi / 8) ** 2

    print(f"Classical winning probability: {p_cls:.4f}  (expected 0.7500)")
    print(f"Quantum  winning probability:  {p_qnt:.4f}  (expected ~0.8536)")
    print(f"Theoretical quantum bound:      {p_opt:.4f}")
