from qiskit import QuantumCircuit


def benchmark_circuit():
    """Define a simple 2-qubit benchmark circuit using H and CX with measurements."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc
