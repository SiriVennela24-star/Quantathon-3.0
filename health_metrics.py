import numpy as np


def compute_health(calib):
    """Compute aggregate error rate and a heuristic health score from calibration data."""
    avg_gate_error = np.mean(calib["gate_error"]) if calib["gate_error"] else 0.0
    avg_readout = np.mean(calib["readout_error"]) if calib["readout_error"] else 0.0
    avg_t1 = np.mean(calib["t1"]) if calib["t1"] else 0.0
    avg_t2 = np.mean(calib["t2"]) if calib["t2"] else 0.0

    error_rate = (avg_gate_error + avg_readout) / 2

    max_t1 = max(calib["t1"]) if calib["t1"] else 1.0
    max_t2 = max(calib["t2"]) if calib["t2"] else 1.0

    health_score = (
        (1 - avg_gate_error) * 30
        + (1 - avg_readout) * 25
        + (avg_t1 / max_t1) * 25
        + (avg_t2 / max_t2) * 20
    )

    return round(error_rate, 3), round(health_score, 1)
