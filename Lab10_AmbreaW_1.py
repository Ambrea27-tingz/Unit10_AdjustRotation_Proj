""" 
Ambrea Williams

Lab10_AmbreaW_1.py

Date: July 5th, 2025

Creating a function representing the degrees of a rotation

Description: This function needs to be able to accept integers, return the 
input vaue adjusted for full rotations, and raise an exception for non-numeric input.
"""

def adjust_rotation(degrees):
  
    """
    Adjusts the input degrees to be within the range of 0 to 360.
    
    Parameters:
    degrees (int or float): The input degrees to be adjusted.
    Returns:
    int: The adjusted degrees within the range of 0 to 360.
    
    Raises a ValueError: If the input is not a numeric value.
    """

    try: 
        degrees = float(degrees)
    except (ValueError,TypeError):
        raise ValueError("Input must be a numeric value.")
    else:
       return degrees % 360
