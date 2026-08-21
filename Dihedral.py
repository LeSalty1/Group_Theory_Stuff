import numpy as np
import sympy as sp

# def rotation_rotation(r1, r2, rot_cap): -> implementing mutliplication between 2 rotations 
# rot_cap defined as order//2

def dihedral_reps(n): 
    r_var = sp.symbols('r')
    rotations = [r_var**i for i in range(1, n//2)] 
    # Our convention is that r**(order/2) represents multiplicative identity e. 
    reflections = sp.symbols(f's1:{n//2 + 1}')
    identity = sp.symbols('e')
    print("Rotations:", rotations, '\n' + 
          "Reflections:", reflections)
    
    #TO-DO: 
        # Need to define some sort of valid multiplication structure between them 
            # Break this down into rotation-rotation, rotation-reflection and reflection-reflection to later put them together into a more generalized function. 
        # Need to also figure out how the multiplication works between the functions.  
        # Implement a visual showing the polygon in question. 
            # Visual needs to include the rotations and reflections 
        # Include a Cayley table for the group. 
while True: 
    order = input("Which dihedral group would you like to represent (type out the order):\n")
    try: 
        int(order)
        break 
    except ValueError: 
        print("Well that's just nonsense.")
if int(order) <= 5 or int(order) % 2 == 1: 
    print("That is not a valid dihedral group! Try again.")
elif int(order) % 2 == 0: 
    dihedral_reps(int(order))
