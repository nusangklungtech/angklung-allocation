"""
Parser file to parse excel files
"""
import numpy as np
import pandas as pd

def read_file(filename):
    """
    Reads the excel file and returns a numpy array
    """
    workbook = pd.read_excel(filename, sheet_name=None, header=None)
    return workbook

def parse_to_array(workbook):
    """
    Parses the excel file into a numpy array
    """
    # Get the number of sheets
    num_sheets = len(workbook.keys())
    # Get the number of rows
    num_rows = len(workbook[0].index)
    # Get the number of columns
    num_cols = len(workbook[0].columns)
    # Create a numpy array with the correct dimensions
    array = np.zeros((num_sheets, num_rows, num_cols))
    # Populate the array
    for sheet in workbook.keys():
        array[int(sheet)] = workbook[sheet].values
    return array

def process_excel_file(filename: str, rows: int, cols: int):
    workbook = read_file(filename)
    array = parse_to_array(workbook)
    return array