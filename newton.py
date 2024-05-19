import numpy as np

def diode_current(Vd, Is, n, Vt):
    return Is * (np.exp(Vd / (n * Vt)) - 1)

def f(V, Is, n, Vt, Vs, R):
    I, Vd = V
    return np.array([Vs - I * R - Vd, I - diode_current(Vd, Is, n, Vt)])

def jacobian(V, Is, n, Vt, R):
    I, Vd = V
    dIdVd = Is * np.exp(Vd / (n * Vt)) / (n * Vt)
    return np.array([[-R, -1], [1, -dIdVd]])

def newtons_method(f, jacobian, V0, Is, n, Vt, Vs, R, tol=1e-10, max_iter=100):
    V = V0
    for _ in range(max_iter):
        F = f(V, Is, n, Vt, Vs, R)
        J = jacobian(V, Is, n, Vt, R)
        delta_V = np.linalg.solve(J, -F)
        V += delta_V
        if np.linalg.norm(delta_V) < tol:
            break
    return V

# Parameters
Is = 1e-14
n = 1.2
Vt = 26e-3
Vs = 5
R = 1000

# Initial guess
V0 = np.array([0.001, 0.7])

# Solve using Newton's Method
solution = newtons_method(f, jacobian, V0, Is, n, Vt, Vs, R)
I, Vd = solution
print(f"Current through the diode: {I:.6f} A")
print(f"Voltage across the diode: {Vd:.6f} V")
