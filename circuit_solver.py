import numpy as np
from scipy.linalg import lu_factor, lu_solve

class CircuitSolver:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.A = np.zeros((num_nodes, num_nodes))
        self.b = np.zeros(num_nodes)
        self.node_voltages = None

    def add_resistor(self, node1, node2, resistance):
        self.A[node1, node1] += 1 / resistance
        self.A[node1, node2] -= 1 / resistance
        self.A[node2, node1] -= 1 / resistance
        self.A[node2, node2] += 1 / resistance

    def add_voltage_source(self, node, voltage):
        self.b[node] = voltage

    def solve(self):
        # Solve linear system using LU Decomposition
        lu, piv = lu_factor(self.A)
        self.node_voltages = lu_solve((lu, piv), self.b)

    def print_results(self):
        if self.node_voltages is not None:
            print("Node Voltages:")
            for i in range(self.num_nodes):
                print(f"Node {i}: {self.node_voltages[i]} V")
        else:
            print("Solver has not been run yet. Call solve() method first.")

# Example usage:
solver = CircuitSolver(num_nodes=3)

# Add resistors
solver.add_resistor(node1=0, node2=1, resistance=100)
solver.add_resistor(node1=1, node2=2, resistance=200)
solver.add_resistor(node1=0, node2=2, resistance=300)

# Add voltage sources
solver.add_voltage_source(node=0, voltage=5)
solver.add_voltage_source(node=2, voltage=10)

# Solve the circuit
solver.solve()

# Print results
solver.print_results()
