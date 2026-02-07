# Quantum Hardware Health Monitor (QHHM)  
**Team:** Qubit Queens  

---

## **Project Overview**
The **Quantum Hardware Health Monitor (QHHM)** is an interactive, modular dashboard designed to simulate and visualize the health of quantum hardware, specifically targeting **Noisy Intermediate-Scale Quantum (NISQ)** devices. It allows users to monitor qubit calibration, gate errors, readout errors, and overall hardware health without needing access to physical quantum computers.  

QHHM provides **educational insights, prototyping capabilities, and operational readiness assessment** for quantum applications, making it easier to understand how errors affect algorithms and how mitigation strategies can improve hardware performance.

---

## **Motivation / Problem Statement**
Running quantum algorithms on NISQ devices is challenging due to:
- Qubit decoherence (T1/T2 times)  
- Gate and readout errors  
- Instability of hardware over time  

Quantum developers need a **reliable way to monitor hardware health** before running algorithms, to reduce wasted runtime and improve results. QHHM simulates this monitoring process with synthetic, API-key seeded calibration data, providing insights on hardware readiness.

---

## **Project Objectives**
- Simulate NISQ hardware behavior using deterministic calibration data  
- Calculate key metrics: **error rate, health score, fidelity**  
- Predict and visualize the impact of **mitigation strategies**  
- Provide **interactive visualizations** for easier understanding of hardware health  
- Serve as a **prototype operations dashboard** for quantum engineers  

---

## **Technology Stack**
- **Python 3.10+** – Core programming language  
- **Streamlit** – Interactive dashboard UI  
- **Qiskit** – Quantum circuit simulation and execution  
- **NumPy** – Synthetic calibration data generation and calculations  
- **Matplotlib** – Visualizations (bar charts, gauges)  
- **Optional:** IBM Quantum API for live hardware integration in future  

---

## **Project Architecture**
QHHM follows a **three-layer architecture**:

**1. Input Layer**  
- User provides **API key**  
- Synthetic qubit calibration data (T1, T2, gate/readout errors)  
- Benchmark quantum circuit definition  

**2. Backend Layer**  
- Generate key-dependent calibration data  
- Compute metrics: **error rate, health score, fidelity**  
- Detect errors & generate alerts  
- Simulate benchmark circuit execution  
- Apply and simulate **mitigation strategies**  
- Prepare before/after metrics for comparison  

**3. Frontend Layer (Streamlit UI)**  
- Accepts API key input  
- Displays:
  - Current hardware metrics  
  - After-mitigation metrics  
  - Alerts and benchmark counts  
  - Interactive visualizations (charts, gauges, comparisons)  

**Visual Suggestion:** Include the **animated dashboard diagram** or **Input → Process → Output infographic**.

---

## **Project Workflow**
1. User enters API key → Backend generates synthetic calibration data.  
2. Compute **error rate, health score, and fidelity** from calibration.  
3. Simulate benchmark quantum circuit → Extract outcomes.  
4. Detect errors → Suggest mitigation strategies (measurement correction, circuit optimization).  
5. Display metrics and visualizations in Streamlit UI.  
6. Show **before vs after mitigation** comparison for better understanding.

---

## **Inputs & Outputs**

| **Input** | **Output** |
|-----------|------------|
| API Key | Hardware health score (before & after) |
| Synthetic calibration data (T1/T2, gate errors, readout errors) | Error alerts & mitigation suggestions |
| Benchmark quantum circuit | Interactive visualizations: bar charts, gauges, comparison panels |
| Thresholds for error/fidelity | Educational insights into qubit behavior |

---

## **Expected Outcomes**
- Deterministic hardware health scores based on API key  
- Error alerts highlighting problematic qubits or gates  
- Predicted effects of mitigation strategies (before/after metrics)  
- Interactive visualizations for developers and learners  
- A teaching tool for understanding NISQ device behavior  

**Visuals:** Use the **Expected Outcomes infographic** or **dashboard diagrams**.

---

## **Applications**
1. **Educational Tool** – Learn about qubit errors, decoherence, and mitigation strategies.  
2. **Prototype Operations Dashboard** – Track simulated quantum hardware health before running real algorithms.  
3. **Algorithm Readiness Assessment** – Decide if a backend is suitable for executing quantum workloads safely.  

---

## **Advantages & Disadvantages**
**Advantages:**  
- Modular design allows **future integration with real IBM Quantum devices**  
- Fast, reproducible **simulations without physical hardware**  
- Interactive **visualizations** help understand hardware health  
- Helps **educational and prototyping purposes**

**Disadvantages:**  
- Not connected to **live hardware yet**  
- Mitigation predictions are **simulated**, not executed on real devices  
- Cannot fully capture **all physical noise and drift** present in real NISQ systems  

---

## **How Qiskit is Used**
- `QuantumCircuit()` – Define benchmark circuit  
- `Aer.get_backend('qasm_simulator')` + `execute()` – Run simulation  
- `result.get_counts()` – Extract outcome counts  
- Metrics are computed using synthetic calibration data  
- Circuit diagram displayed in UI for visual explanation  

---

## **How to Run QHHM in VS Code**

1. **Clone the repository:**  
```bash
git clone https://github.com/your-username/QHHM.git
cd QHHM

Create a virtual environment:

python -m venv venv
# Activate:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py
