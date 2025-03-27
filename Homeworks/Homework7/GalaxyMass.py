#!/usr/bin/env python
# coding: utf-8

# In[26]:


#This imports the ReadFile program from HW2
from ReadFile import Read

"""This function returns the total mass of any desired galaxy component.
Inputs: name of the file, particle type (1,2,3)
Outputs: total mass of galaxy component in units of 10^12 solar masses
"""

import numpy as np
import astropy.units as u

#This function will return the total mass of any desired galaxy component
def ComponentMass(filename, particle_type):
    time, tot_particle_num, data = Read(filename) #reading contents of the file
    
    #Gives us an index object - all rows with chosen particle type
    index = np.where(data['type']==particle_type)
    
    masses = data[index]["m"] #get's all of the mass of all of the rows for the chosen particle type
    tot_mass = np.sum(masses) #this sums each particle of chosen type together
    tot_mass = np.round(tot_mass/100, 3) #rounding mass to 10^12 sm
    
    return tot_mass