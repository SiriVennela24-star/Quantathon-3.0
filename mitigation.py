def mitigation_strategy(error_rate: float) -> str:
    """Return a textual description of the mitigation strategy based on error rate."""
    if error_rate > 0.15:
        return "Measurement Mitigation + Circuit Optimization"
    elif error_rate > 0.08:
        return "Measurement Mitigation"
    return "No Mitigation Required"


def apply_mitigation(error_rate: float) -> float:
    """Simulate an improved error rate after mitigation is applied."""
    improved_error = error_rate * 0.4
    return round(improved_error, 3)
