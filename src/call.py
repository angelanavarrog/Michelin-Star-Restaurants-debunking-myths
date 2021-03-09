import pandas as pd
import numpy as np


def normalize(s):
# Function to replace vowels accented by the same unaccented vowels.

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

def convert_str():

    total_values = []
    for i in range(len(total_values)):
        myVal = total_values[i].replace(".", "")
        total_values[i] = int(myVal)
        return total_values

