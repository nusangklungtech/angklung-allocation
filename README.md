# Angklung Allocation Algorithm (AAA)
Version 1.0.0 <br>

## Overview

This repository serves as the codebase for the Angklung Allocation Algorithm for NUS Angklung Ensemble. The application is planned to be functional by Q3 of 2023, and hopes to help the conductors in determining the distribution of angklungs while avoiding overlaps and maximising load distribution.

Version 1.0.0 serves the following features:
- Parsing of conductor's partiture from `.xlsx` format
- Performing the allocation algorithm (graph coloring) in recommending the minimum number of users required
- Performing the allocation algorithm (graph coloring) given a specific number of users

Version 1.0.0 is planned to have a **command-line interface** with no knowledge base / no database connection. Future iterations would definitely be planned, bearing in mind the possibility of storing past allocation data in a database that is accessible anytime, as well as having an interactive GUI for better user experience.

## Acknowledgement

This project is made possible due to the groundbreaking research by Salindeho and Baskoro (2019) on the following journal:

Salindeho, B. M., &amp; Baskoro, E. T. (2019). Graph coloring for determining angklung distribution. 
Journal of Physics: Conference Series, 1277(1), 012033. https://doi.org/10.1088/1742-6596/1277/1/012033 

## Setup and Installation

1. Clone the repository if you haven't done so. Here is a CLI implementation

```
git clone https://github.com/nusangklungtech/angklung-allocation.git
```

2. Ensure that you have a Python installation on your computer. If you do not have a Python installation, please download it from the following [link](https://www.python.org/downloads/). We recommend Python versions 3.8 or higher.

3. (Optional) We recommend setting up a virtual environment for this project. To do so, execute the following command

```
python -m venv env
```

(Windows users) Activate your Python virtual environment by running the following command

```
env/scripts/activate
```

(Linux / Mac users) Activate your Python virtual environment by running the following command

```
source env/bin/activate
```

4. Install the necessary packages required. Required packages have been listed under `requirements.txt`. Simply run the following command

```
pip install -r requirements.txt
```

Sidenote: Currently required packages are `numpy` and `pandas`. If you already have these packages (perhaps from your data analytics course?) then you don't need to execute the installation step (for now!)

5. You are good to go! Now, all you need is to run the main python file. Simply

```
python main.py
```

or you can click on the "run" button on your preferred IDE!

## Developer Guide

This is a very quickie developer guide!

The repository currently handles Python files as their raw scripts (well duh ... since it is still a command line interface mode without GUI).

Currently, the code structure is as follows:

- `main.py`: Serves as the entry point of the application
- `utils`: Utility files, especially for the excel parser
- `logic`: Serves as the placeholder for the allocation algorithm.

There is a detailed description on the allocation algorithm that is located under the `logic` folder. Do have a look at that file before continuing the project.

Happy coding!