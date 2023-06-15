# Import necessary libraries
import pyalps
import numpy as np
import matplotlib.pyplot as plt # Plotting library
# Define the parameters for your model  and simulation
params = pyalps.Parameters()    # Create a parameter object
params['LATTICE'] = "square lattice"  # Define the lattice type 
params['T'] = 1.0  # Set the temperature
params['L'] = 10  # Set the linear size of the lattice  
params['J'] = 1.0  # Set the exchange interaction strength          
params['SWEEPS'] = 10000  # Set the number of Monte Carlo sweeps        
params['THERMALIZATION'] = 1000  # Set the number of thermalization steps
params['UPDATE'] = "local"  # Set the update method to local updates    
params['MODEL'] = "Ising"  # Set the model type
# Run the simulation        
input_file = pyalps.writeInputFiles('ising',params)  # Write the input file for spinmc          
res = pyalps.runApplication('spinmc',input_file,Tmin=5,writexml=True)  # Run the Monte Carlo simulation
# Analyze the results
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='ising'),'|Magnetization|')  # Load the simulation results
magnetization = np.array([d.y[0] for d in data])  # Extract the magnetization data
plt.plot(magnetization)  # Plot the magnetization data
plt.show()  # Show the plot
