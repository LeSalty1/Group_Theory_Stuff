import numpy as np

def dihedral_reps(n): 
    rotations = [rot for rot in range(1, n)]
    reflections = [ref for ref in range(1, n)]
    #TO-DO: 
        # Need to somehow define the rotations (i.e., r, r^2, etc.)
        # Need somehoe differentiate the reflections (s_1, s_2, etc.)
        # Need to define some sort of valid multiplication structure between them 
        # Need to also figure out how the multiplication works between the functions.  
        # Implement a visual showing the polygon in question. 
            # Visual needs to include the rotations and reflections 
        # Include a Cayley table for the group. 

order = input("Which dihedral group would you like to represent (type out the order):\n")
while True: 
    # Need to figure out how to check for inputs    
    if int(order) <= 5 or int(order) % 2 != 1: 
        print("That is not a valid dihedral group! Try again.")
    elif int(order) % 2 == 0: 
        dihedral_reps(order)
    else: 
        print("That's just nonsense...")
        break 
