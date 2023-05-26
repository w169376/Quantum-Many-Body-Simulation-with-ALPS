import numpy as np

# Define the size of the lattice
L = 10

# Define the coupling constant
J = 1.0

# Define the temperature
T = 2.0

# Initialize the lattice with random spins
lattice = np.random.choice([-1, 1], size=(L, L))

# Define the Hamiltonian
def hamiltonian(lattice):
    return -J * np.sum(
        lattice * (np.roll(lattice, 1, axis=0) + np.roll(lattice, 1, axis=1))
    )

# Define the Monte Carlo step
def monte_carlo_step(lattice, beta):
    for i in range(L):
        for j in range(L):
            delta_E = 2 * J * lattice[i, j] * (
                lattice[(i+1)%L, j] + lattice[i-1, j] +
                lattice[i, (j+1)%L] + lattice[i, j-1]
            )
            if delta_E < 0 or np.random.rand() < np.exp(-beta * delta_E):
                lattice[i, j] *= -1

# Run the Monte Carlo simulation
beta = 1.0 / T
for step in range(10000):
    monte_carlo_step(lattice, beta)
