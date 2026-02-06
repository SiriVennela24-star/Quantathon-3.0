from circuits import benchmark_circuit
from execution import run_circuit


def create_benchmark_circuit():
    """Return the benchmark circuit used in the dashboard."""
    return benchmark_circuit()


def run_benchmark_circuit(noise_model=None, shots: int = 1024):
    """Run the benchmark circuit using the existing execution helper."""
    qc = create_benchmark_circuit()
    return run_circuit(qc, noise_model=noise_model, shots=shots)
