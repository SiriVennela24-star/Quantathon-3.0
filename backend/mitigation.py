def decide_mitigation(error_rate: float) -> str:
    """Choose a simple mitigation strategy based on the error rate."""

    if error_rate > 0.15:
        return "Measurement + Circuit Optimization"
    if error_rate > 0.08:
        return "Measurement Mitigation"
    return "No Mitigation Required"


def simulate_mitigation(error_rate: float) -> float:
    """Simulate the effect of mitigation by scaling the error rate."""

    improved_error = error_rate * 0.4
    return round(improved_error, 3)
