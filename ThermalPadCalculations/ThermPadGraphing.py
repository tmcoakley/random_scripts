# ----------------------------------------------------------------------------
# Importing Packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# USER INTERFACE 
#
# I used this website to pull the data points: https://automeris.io/

# Name of file for the deflection vs pressure graph
deflgraph = 'tflex3120.csv'

# Name of file for the thermal impedance vs pressure graph
thermgraph = 'tflexthermal.csv'

# Distance from the chip to whatever you measuring against in mm
chipdist = 1.493

# Thickness of thermal pad in mm
tpthick = 3.05 

# Print out deflection, pressure, thermal impedance 
# True for yes, False for no
printvals = True 

# ----------------------------------------------------------------------------
# Read in data  
#

# Get the deflection data 
dataset1 = pd.read_csv(deflgraph)
df1 = pd.DataFrame(dataset1)

# get the thermal impedance data 
dataset2 = pd.read_csv(thermgraph)
df2 = pd.DataFrame(dataset2)

# Save x and y
defxval = np.array(df1.iloc[:, 0])
defyval = np.array(df1.iloc[:, 1])

impxval = np.array(df2.iloc[:, 0])
impyval = np.array(df2.iloc[:, 1])


# ----------------------------------------------------------------------------
# Calculations  
#

# Calculate deflection as a percentage
deflect = (( (tpthick - chipdist ) / ( tpthick )) * 100 ) 

# Get the pressure based on the calculated deflection 
pressure = (np.interp(deflect, defyval, defxval))

# From the pressure, find the corresponding the thermal impedance
thermimp = (np.interp(pressure, impxval, impyval))    


# ----------------------------------------------------------------------------
# Outputs and graphs  
#

# Printing out all the calculated values
if printvals == True: 
    print("Calculated Values:")
    print("")
    print("Deflection : {:.2f}%".format(deflect))
    print("Pressure : {:.2f} psi".format(pressure))
    print("Thermal Impedance : {:.2f} C*in^2/W".format(thermimp))


# Graph time, yo
# Create two plots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Deflection vs Contact pressure
ax1.plot(defxval, defyval)
ax1.plot(pressure, deflect, 'o', color='black')
ax1.set_xlabel('Contact Pressure (psi)')
ax1.set_ylabel('Deflection (%)')

# Thermal Impedance vs contact pressure
ax2.plot(impxval, impyval)
ax2.plot(pressure, thermimp, 'o', color='black')
ax2.set_xlabel('Contact Pressure (psi)')
ax2.set_ylabel('Thermal Impedance (C*in^2/W)')


# Display the plots
plt.tight_layout()
plt.show()
