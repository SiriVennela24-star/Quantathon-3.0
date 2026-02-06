import streamlit as st

from backend import run_backend_pipeline
from visualization import (
    plot_comparison,
    health_speedometer_before,
    health_speedometer_after,
)
from circuits import benchmark_circuit


st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        background-image:
            radial-gradient(circle at 15% 20%, rgba(250, 204, 21, 0.18), transparent 55%),
            radial-gradient(circle at 80% 10%, rgba(250, 204, 21, 0.12), transparent 55%),
            radial-gradient(circle at 10% 80%, rgba(234, 179, 8, 0.18), transparent 55%),
            linear-gradient(135deg, rgba(24, 24, 27, 1), rgba(0, 0, 0, 1));
        background-attachment: fixed;
    }

    .block-container {
        padding-top: 2rem;
        border-left: 1px solid rgba(250, 204, 21, 0.12);
        border-right: 1px solid rgba(250, 204, 21, 0.12);
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.9);
    }

    h1, h2, h3, h4, h5, h6,
    p, span, label, div, .stMetric label {
        font-family: "Times New Roman", Times, serif;
        color: #facc15; /* yellow */
    }

    h1 {
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    h2, h3 {
        border-bottom: 1px solid rgba(250, 204, 21, 0.2);
        padding-bottom: 0.2rem;
        margin-bottom: 0.6rem;
    }

    /* Buttons */
    .stButton>button {
        background-color: #000000;
        color: #facc15;
        border: 1px solid #facc15;
        border-radius: 999px;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #facc15;
        color: #000000;
    }

    /* Code block (circuit) styling */
    pre, code {
        color: #facc15 !important;
        background-color: #111111 !important;
        border-left: 2px solid rgba(250, 204, 21, 0.6);
    }

    /* Subtle corner ornaments */
    .block-container::before,
    .block-container::after {
        content: "";
        position: fixed;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        border: 1px dashed rgba(250, 204, 21, 0.25);
        box-shadow: 0 0 12px rgba(250, 204, 21, 0.25);
        z-index: -1;
    }
    .block-container::before {
        top: 12%;
        left: -2%;
    }
    .block-container::after {
        bottom: 10%;
        right: -2%;
    }

    /* Vertical side accents to fill empty space */
    .side-accent-left,
    .side-accent-right {
        position: fixed;
        top: 15%;
        bottom: 15%;
        width: 2px;
        background: linear-gradient(
            to bottom,
            rgba(250, 204, 21, 0.0),
            rgba(250, 204, 21, 0.4),
            rgba(250, 204, 21, 0.0)
        );
        box-shadow: 0 0 14px rgba(250, 204, 21, 0.35);
        z-index: -1;
    }
    .side-accent-left {
        left: 3%;
    }
    .side-accent-right {
        right: 3%;
    }

    .side-orbit {
        position: fixed;
        width: 130px;
        height: 130px;
        border-radius: 50%;
        border: 1px solid rgba(250, 204, 21, 0.24);
        box-shadow: 0 0 22px rgba(250, 204, 21, 0.3);
        z-index: -1;
    }
    .side-orbit.left-top {
        top: 8%;
        left: -3%;
    }
    .side-orbit.right-bottom {
        bottom: 6%;
        right: -3%;
    }

    .quantum-bookmark {
        position: fixed;
        top: 0;
        right: 1.5rem;
        background: linear-gradient(135deg, #facc15, #eab308);
        padding: 0.6rem 1.2rem;
        border-radius: 0 0 10px 10px;
        color: #000000;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8);
        z-index: 9999;
    }
    .quantum-bookmark-secondary {
        position: fixed;
        top: 3.2rem;
        right: 1.5rem;
        background: linear-gradient(135deg, #0f172a, #020617);
        padding: 0.4rem 1rem;
        border-radius: 0 0 8px 8px;
        color: #facc15;
        font-size: 0.8rem;
        border-top: 1px solid #facc15;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8);
        z-index: 9998;
    }
    .quantum-bookmark-tertiary {
        position: fixed;
        top: 0;
        left: 1.5rem;
        background: linear-gradient(135deg, #020617, #111827);
        padding: 0.6rem 1.1rem;
        border-radius: 0 0 10px 10px;
        color: #facc15;
        font-size: 0.85rem;
        border-bottom: 1px solid #facc15;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 1);
        z-index: 9999;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    </style>
    <div class="quantum-bookmark">Quantum Computer · Health Monitor</div>
    <div class="quantum-bookmark-secondary">Superposition · Entanglement · Error Rates</div>
    <div class="quantum-bookmark-tertiary">NISQ Hardware · Advanced Monitoring</div>
    <div class="side-accent-left"></div>
    <div class="side-accent-right"></div>
    <div class="side-orbit left-top"></div>
    <div class="side-orbit right-bottom"></div>
    """,
    unsafe_allow_html=True,
)


st.title("Quantum Hardware Health Monitor (QHHM)")

st.write(
    "Monitor IBM Quantum backend calibration data, compute a hardware health score, "
    "and simulate the effect of automatic error mitigation strategies on benchmark circuits."
)

# API key input + action button side by side
input_col, button_col = st.columns([3, 1])
with input_col:
    api_key = st.text_input(
        "IBM API Key",
        type="password",
        placeholder="Paste your IBM Quantum API key here",
    )
with button_col:
    run_analysis = st.button("Import Calibration Data & Analyze Hardware")

if run_analysis:
    with st.spinner("Running backend pipeline..."):
        backend_data = run_backend_pipeline(api_key=api_key)

    calib = backend_data["calibration"]
    error_rate = backend_data["error_rate"]
    health = backend_data["health_score"]
    fidelity = backend_data["fidelity"]
    alerts = backend_data["alerts"]
    strategy = backend_data["mitigation_strategy"]
    comparison = backend_data["results"]
    benchmark_counts = backend_data["benchmark_counts"]

    improved_error = comparison["after"]["error_rate"]
    improved_health = comparison["after"]["health_score"]

    # Show raw calibration parameters that were derived from the API key
    with st.expander("Calibration parameters derived from API key", expanded=False):
        st.write("T1 times (µs):", calib["t1"])
        st.write("T2 times (µs):", calib["t2"])
        st.write("Readout error per qubit:", calib["readout_error"])
        st.write("Single-qubit gate error per qubit:", calib["gate_error"])
        st.write("CNOT gate error per pair:", calib["cnot_error"])

    # Current vs After Mitigation side by side
    col_current, col_after = st.columns(2)

    with col_current:
        st.subheader("Current Hardware Status")
        st.metric("Error Rate", error_rate)
        st.metric("Health Score", f"{health}%")
        st.metric("Fidelity (proxy)", f"{fidelity:.3f}")

    with col_after:
        st.subheader("After Mitigation (Simulated)")
        st.metric("After Fix - Error Rate", improved_error)
        st.metric("After Fix - Health Score", f"{improved_health}%")
        st.write("**Selected Mitigation Strategy:**", strategy)

    # Alerts and benchmark counts
    with st.expander("Backend alerts and benchmark counts", expanded=False):
        st.write("Alerts:", alerts)
        st.write("Benchmark counts:", benchmark_counts)

    # Optionally, show the benchmark circuit (structure is static)
    qc = benchmark_circuit()
    st.write("Benchmark circuit:")
    # Use Qiskit's text drawer instead of the removed QuantumCircuit.qasm() API
    circuit_diagram = qc.draw(output="text")
    st.code(str(circuit_diagram), language="text")

    # Plot before vs after
    st.subheader("Visual Comparison")
    fig = plot_comparison(error_rate, improved_error, health, improved_health)
    st.pyplot(fig, clear_figure=True)

    # Speedometer-style gauges for health scores (before / after)
    st.subheader("Health Score Speedometers")
    gauge_before_col, gauge_after_col = st.columns(2)
    with gauge_before_col:
        st.markdown("**Before Health Score**")
        gauge_before = health_speedometer_before(health)
        st.pyplot(gauge_before, clear_figure=True)
    with gauge_after_col:
        st.markdown("**After Health Score**")
        gauge_after = health_speedometer_after(improved_health)
        st.pyplot(gauge_after, clear_figure=True)
