#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This is on my Desktop/ASTR-400B-Repository
#This is the Read function that opens the MW_000.txt file and reads line 1 and line 2. It is reading in and splitting up total particles and the label.
#Inputs: filename
#Outputs: time (Myr), particle_num (any integer to total number of particles), data (an array of the rest of the data)

import numpy as np
import astropy.units as u

def Read(filename):
    #Reading the first line
    file = open(filename,'r') #opens file
    line1 = file.readline() #reads line 1
    label,value = line1.split() #splits label and value apart at the space
    time = float(value)*u.Myr #value is still a string and want it to be a number, so it is converted to a float
    
    #Reading the second line
    line2 = file.readline() #reads line 2
    label,value = line2.split() #splits label and value apart at the space
    particle_num = int(value) #no units here
    
    file.close()
    
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3) #creates an array from the text file
    
    return time, particle_num, data



