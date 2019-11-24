q = QuantumRegister(5, 'q')
c = ClassicalRegister(5, 'c')
circuit = QuantumCircuit(q, c)

circuit.h(q[1])
circuit.h(q[2])
circuit.h(q[3])
circuit.h(q[4])
circuit.h(q[2])
circuit.h(q[3])
circuit.h(q[4])
circuit.h(q[3])
circuit.h(q[4])
circuit.h(q[4])

circuit.measure(q, c)

