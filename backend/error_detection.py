def detect_errors(error_rate: float, fidelity: float, thresholds=None) -> dict:
    """Detect whether error rate and fidelity cross simple thresholds."""

    if thresholds is None:
        thresholds = {"error": 0.08, "fidelity": 0.9}

    alerts: dict = {}
    if error_rate > thresholds["error"]:
        alerts["error_rate"] = True
    if fidelity < thresholds["fidelity"]:
        alerts["fidelity"] = True
    return alerts
