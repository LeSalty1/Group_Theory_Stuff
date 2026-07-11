import numpy as np

def dihedral_reps(n): 
    rotations = [rot for rot in range(1, n)]
    reflections = [ref for ref in range(1, n)]


order = input("Which dihedral group would you like to represent (type out the order):\n")
while True: 
    if int(order) <= 5 or int(order) % 2 != 1: 
        print("That is not a valid dihedral group! Try again.")
    elif int(order) % 2 == 0: 
        dihedral_reps(order)
    else: 
        print("That's just nonsense...")
        break 
