import hashlib
import numpy as np


def get_calibration_data(api_key: str | None = None):
    """Return synthetic calibration data instead of querying an IBM provider.

    If an API key is provided, use it to seed a local RNG so that the
    calibration "fingerprint" is stable for that key. Different keys will
    therefore produce different (but repeatable) health statistics and graphs.
    """

    # Build a per-key RNG so that results depend on the provided API key.
    if api_key:
        # Derive a 32-bit seed from the first 8 hex chars of a SHA-256 digest.
        digest = hashlib.sha256(api_key.encode("utf-8")).hexdigest()[:8]
        seed = int(digest, 16)
        rng = np.random.default_rng(seed)
    else:
        rng = np.random.default_rng()

    # Number of qubits to simulate
    num_qubits = 8

    # T1/T2 in microseconds – draw from reasonable ranges
    t1 = rng.uniform(50, 120, size=num_qubits).tolist()
    t2 = rng.uniform(40, 110, size=num_qubits).tolist()

    # Readout error per qubit (0 = perfect, ~0.1 = noisy)
    readout_error = rng.uniform(0.0, 0.08, size=num_qubits).tolist()

    # Single-qubit gate errors and two-qubit (CX) gate errors
    gate_error = rng.uniform(0.0, 0.03, size=num_qubits).tolist()

    # For CX we simulate errors per pair; just generate the same count as qubits
    cnot_error = rng.uniform(0.0, 0.05, size=num_qubits).tolist()

    data = {
        "t1": t1,
        "t2": t2,
        "readout_error": readout_error,
        "gate_error": gate_error,
        "cnot_error": cnot_error,
    }

    return data
