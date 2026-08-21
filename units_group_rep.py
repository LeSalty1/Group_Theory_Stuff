import numpy as np 
import sympy as sp
import math
import pandas as pd 

def units_mod_print(n): 
    if type(n) is not int: 
        raise TypeError(f"{n} is not a valid input. Valid inputs must be positive integers greater than 1.")
    elif n <= 1: 
        raise ValueError(f"{n} is not a valid input. Valid inputs must be positive integers greater than 1.")

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

def units_mod_markdown(n): 
    if type(n) is not int: 
        raise TypeError(f"{n} is not a valid input. Valid inputs must be positive integers greater than 1.")
    elif n <= 1: 
        raise ValueError(f"{n} is not a valid input. Valid inputs must be positive integers greater than 1.")
    if sp.isprime(n): 
        elements = [numb for numb in range(1, n)] # Clearly if n is prime, then any positive integer less than it is coprime. 
    else: 
        elements = [numb for numb in range(1, n) if math.gcd(numb , n) ==  1]
    cayley = np.ones((len(elements), len(elements)), dtype = int)
    for row_ent in range(len(elements)): 
        for col_ent in range(len(elements)): 
            cayley[row_ent][col_ent] = (elements[row_ent] * elements[col_ent]) % n

    df = pd.DataFrame(data = cayley, index = elements, columns = elements)
    with open(f"U({n})_Cayley_Table.md", "w") as f: 
        f.write(df.to_markdown())