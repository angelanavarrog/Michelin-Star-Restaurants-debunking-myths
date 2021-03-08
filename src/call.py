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


