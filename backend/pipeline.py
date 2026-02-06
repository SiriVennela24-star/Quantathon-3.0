from typing import Optional

from .calibration import fetch_calibration_data
from .metrics import compute_health
from .benchmark import create_benchmark_circuit, run_benchmark_circuit
from .error_detection import detect_errors
from .mitigation import decide_mitigation, simulate_mitigation
from .comparison import prepare_comparison


def run_backend_pipeline(api_key: Optional[str] = None) -> dict:
    """End-to-end backend pipeline for the QHHM dashboard.

    The pipeline is driven by a user-provided API key, which determines the
    synthetic calibration fingerprint and therefore all downstream metrics and
    visualizations.
    """

    # 1️⃣ Fetch Calibration Data (key-dependent synthetic data)
    calib = fetch_calibration_data(api_key=api_key)

    # 2️⃣ Compute Health Score
    error_rate, health_score = compute_health(calib)

    # 3️⃣ Benchmark Circuit and simple fidelity proxy
    qc = create_benchmark_circuit()
    counts = run_benchmark_circuit()
    fidelity = max(0.0, min(1.0, 1.0 - error_rate))

    # 4️⃣ Detect Errors
    alerts = detect_errors(error_rate, fidelity)

    # 5️⃣ Decide Mitigation and simulate improvement
    strategy = decide_mitigation(error_rate)
    improved_error = simulate_mitigation(error_rate)
    improved_health = min(health_score + 20, 100.0)

    # 6️⃣ Prepare Comparison
    results = prepare_comparison(error_rate, improved_error, health_score, improved_health)

    return {
        "calibration": calib,
        "health_score": health_score,
        "error_rate": error_rate,
        "fidelity": fidelity,
        "alerts": alerts,
        "mitigation_strategy": strategy,
        "results": results,
        "benchmark_counts": counts,
    }
