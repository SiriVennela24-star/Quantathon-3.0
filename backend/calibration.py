import hashlib
from typing import Optional

import numpy as np


def fetch_calibration_data(api_key: Optional[str] = None, num_qubits: int = 8) -> dict:
    """Generate synthetic calibration data, keyed by a user-provided API key.

    This mirrors the behavior used in the main app: the API key seeds a local RNG so
    that each key produces a stable but distinct calibration fingerprint.
    """

    if api_key:
        digest = hashlib.sha256(api_key.encode("utf-8")).hexdigest()[:8]
        seed = int(digest, 16)
        rng = np.random.default_rng(seed)
    else:
        rng = np.random.default_rng()

    # T1/T2 in microseconds – draw from reasonable ranges
    t1 = rng.uniform(50, 120, size=num_qubits).tolist()
    t2 = rng.uniform(40, 110, size=num_qubits).tolist()

    # Readout error per qubit (0 = perfect, ~0.1 = noisy)
    readout_error = rng.uniform(0.0, 0.08, size=num_qubits).tolist()

    # Single-qubit gate errors and two-qubit (CX) gate errors
    gate_error = rng.uniform(0.0, 0.03, size=num_qubits).tolist()

    # For CX we simulate errors per pair; just generate the same count as qubits
    cnot_error = rng.uniform(0.0, 0.05, size=num_qubits).tolist()

    return {
        "t1": t1,
        "t2": t2,
        "readout_error": readout_error,
        "gate_error": gate_error,
        "cnot_error": cnot_error,
    }
