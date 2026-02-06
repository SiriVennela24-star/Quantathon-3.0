def prepare_comparison(before_error: float, after_error: float, before_health: float, after_health: float) -> dict:
    """Package before/after error and health metrics for downstream use."""

    return {
        "before": {"error_rate": before_error, "health_score": before_health},
        "after": {"error_rate": after_error, "health_score": after_health},
    }
