import numpy as np 
import pandas as pd

# Use this function if you want the Cayley table printed in your terminal. 
def ints_mod_print(n): 
    if type(n) is not int: 
        raise TypeError(f"{n} is not a valid input. Inputs must be integers.")
    elif n <= 0: 
        raise ValueError(f"{n} is not a valid input. Inputs must be positive integers.")
    
    # The math of the Cayley table: 
    cayley = np.ones((n, n), dtype = int)
    for row_ent in range(n): 
        for col_ent in range(n): 
            cayley[row_ent][col_ent] = (row_ent + col_ent) % n

    # The formatting to make the table more readable: 
    col_width, operation = 2, "+"
    header = f"{operation:>{col_width}} | " + " ".join(f"{element:>{col_width}}" for element in range(n)) 
    # ^ Initializes the header row as "+ | [elements in Z_n]" with spacing defined via col_width (right-aligned). 
    separate = "-" * len(header)
    print(header)
    print(separate)

    for i, row_label in enumerate(range(n)): 
        row_str = " ".join(f"{val:>{col_width}}" for val in cayley[i]) 
        # ^ Initializes the rows of the Cayley table as "[element] | [result after operation]" with spacing defined via col_width (right-aligned). 
        print(f"{row_label:>{col_width}} | {row_str}")

def cayley_math(n): 
    cayley = np.ones((n, n), dtype = int)
    for row_ent in range(n): 
        for col_ent in range(n): 
            cayley[row_ent][col_ent] = (row_ent + col_ent) % n
    return cayley

# Use this function if you want the Cayley table in the form of a markdown file (automatically written). 
def ints_mod_markdown(n):
    if type(n) is not int: 
        raise TypeError(f"{n} is not a valid input. Inputs must be integers.")
    elif n <= 0: 
        raise ValueError(f"{n} is not a valid input. Inputs must be positive integers.")
    
    df = pd.DataFrame(data = cayley_math(n), index = range(n), columns = range(n))
    with open(f"Z_{n}_Cayley_Table.md", "w") as f: 
        f.write(df.to_markdown())