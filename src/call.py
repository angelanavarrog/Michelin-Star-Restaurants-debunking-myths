import pandas as pd
import numpy as np

# Functions defined and used during cleanings

def normalize(s):
    """ Function to replace vowels accented by the same unaccented vowels.
    input: words with accented words
    output: words unaccentedd vowels.
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def convert_str(element):
    """Function to convert object data to int when needed."""

    x = element.replace(".","")
    number = float(x)
    return  number

