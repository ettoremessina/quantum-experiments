q = QuantumRegister(5, 'q')
c = ClassicalRegister(5, 'c')
circuit = QuantumCircuit(q, c)

circuit.reset(q[0])
circuit.reset(q[1])
circuit.reset(q[2])
circuit.reset(q[3])
circuit.reset(q[4])

circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2])
circuit.h(q[3])
circuit.h(q[4])

circuit.measure(q, c)

