import random


def run_circuit(qc, noise_model=None, shots: int = 1024):
    """Simulate running a circuit by returning synthetic counts.

    This avoids relying on qiskit.Aer/execute, which are no longer available at
    the top level in recent qiskit versions. The current Streamlit app does not
    actually call this function, but it is kept for completeness.
    """

    # Generate a fake outcome string with the right number of classical bits
    # based on the circuit's classical registers when available.
    try:
        num_clbits = qc.num_clbits
    except Exception:
        num_clbits = 2

    bitstring = "".join(random.choice("01") for _ in range(num_clbits))
    return {bitstring: shots}
