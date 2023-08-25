"""
Angklung Allocation System
Version 1.0.0
Author: Jason Christopher

This is the main file for the Angklung Allocation System.
Will take in an excel file and prints the allocation.
Further development would require a GUI.
"""
import numpy as np
import pandas as pd

from utils.parser import process_excel_file

def main():
    print("Angklung Allocation System - Version 1.0.0")
    print("------------------------------------------------------------------")

    # Get the filename
    filename = input("Enter the filename: ")
    # Get the number of rows
    rows = int(input("Enter the number of rows: "))
    # Get the number of columns
    cols = int(input("Enter the number of columns: "))
    
    # Read the file
    array = process_excel_file(filename, rows, cols)
    # Read beat separation
    beat_separation = int(input("Enter the beat separation: "))

    # Process array
    