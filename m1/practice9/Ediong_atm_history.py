def view_history():
    # TODO 2: Try to open transactions.txt in read mode.
    # TODO 3: Read all lines from the file.
    # TODO 4: Return the lines to the caller.
    # TODO 5: Handle FileNotFoundError.
    # If the file does not exist, return an empty list.
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()

        return lines

    except FileNotFoundError:
        return []

""" 
######### Learning Signature ######### 
Programmed by: Kevin Paolo Ediong
Date Submitted: September 4, 2026
""" 