import numpy as np 

def ints_mod(n): 
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

# Below code only necessary when testing function, feel free to remove in your own implentations. 
while True: 
    mod_order = input("Enter the order for the integer modulo n group you wish to represent: ")
    try: 
        int(mod_order)
        break 
    except ValueError: 
        print("Well that's just nonsense (single integer required)!")
    if mod_order <= 0: 
        print("Such a group does not exist")
ints_mod(int(mod_order))