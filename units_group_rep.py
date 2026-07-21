import numpy as np 
import sympy as sp
import math

def units_mod(n): 
    # The math of the Cayley table: 
    if sp.isprime(n): 
        elements = [numb for numb in range(1, n)] # Clearly if n is prime, then any positive integer less than it is coprime. 
    else: 
        elements = [numb for numb in range(1, n) if math.gcd(numb , n) ==  1]
    cayley = np.ones((len(elements), len(elements)), dtype = int)
    for row_ent in range(len(elements)): 
        for col_ent in range(len(elements)): 
            cayley[row_ent][col_ent] = (elements[row_ent] * elements[col_ent]) % n

    # The formatting to make the table more readable: 
    col_width, operation = 3, "*"
    header = f"{operation:>{col_width}} | " + " ".join(f"{element:>{col_width}}" for element in elements)
    # ^ Initializes the header row as "+ | [elements in Z_n]" with spacing defined via col_width (center-aligned). 
    separate = "-" * len(header)
    print(header)
    print(separate)
    for i, element in zip(range(len(elements)), elements): 
        row_str = " ".join(f"{val:>{col_width}}" for val in cayley[i]) 
        # ^ Initializes the rows of the Cayley table as "[element] | [result after operation]" with spacing defined via col_width (center-aligned). 
        print(f"{element:>{col_width}} | {row_str}")

# Below code only necessary when testing function, feel free to remove in your own implentations. 
while True: 
    mod_order = input("Enter the number that you want the group of units of: ")
    try: 
        int(mod_order)
        break 
    except ValueError: 
        print("Well that's just nonsense (single integer required)!")
    if mod_order <= 1: 
        print("Such a group does not exist")
units_mod(int(mod_order))