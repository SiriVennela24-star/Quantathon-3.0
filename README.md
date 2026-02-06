# Quantum Hardware Health Monitor (QHHM)

Real-time Quantum Hardware Health Monitor that imports quantum calibration data from the IBM Quantum API, analyzes hardware health parameters, computes a health score, applies error mitigation strategies on benchmark circuits, and displays before vs after results on a Streamlit dashboard.

## Folder Structure

```text
QHHM/
├── app.py                     # Streamlit dashboard
├── config.py                  # Settings (backend, shots)
├── calibration_api.py         # Fetch calibration data from IBM API
├── health_metrics.py          # Compute health score
├── mitigation.py              # Define mitigation strategies and apply them
├── circuits.py                # Benchmark quantum circuits
├── execution.py               # Run circuits on simulator with optional noise
├── visualization.py           # Plot before/after graphs
├── requirements.txt
└── README.md
```

## 1. Install Dependencies

From inside the `QHHM` folder:

```bash
pip install -r requirements.txt
```

(or equivalently)

```bash
pip install qiskit qiskit-aer qiskit-ibm-provider streamlit matplotlib numpy
```

## 2. Save IBM Quantum API Token (only once)

You must have an IBM Quantum account. Then save your token locally (replace `YOUR_TOKEN_HERE`):

```bash
qiskit-ibm-provider save-account --token YOUR_TOKEN_HERE
```

This stores credentials so `IBMProvider()` in `calibration_api.py` can authenticate.

## 3. Configuration

Edit `config.py` if needed:

- `IBM_BACKEND`: name of the backend from your IBM Quantum account (e.g. a real hardware backend).
- `DEFAULT_SHOTS`: default number of shots used by the simulator.

By default, the backend is set to `ibmq_qasm_simulator`.

## 4. Running the Dashboard

From inside the `QHHM` directory:

```bash
streamlit run app.py
```

Your browser should open the **Quantum Hardware Health Monitor (QHHM)** dashboard. Click **"Import Calibration Data & Analyze Hardware"** to:

- Fetch current calibration data from the configured IBM backend.
- Compute an aggregate error rate and health score.
- Select an automatic mitigation strategy.
- Simulate an improved error rate and health score after mitigation.
- View before/after comparisons and the benchmark circuit.
