# Daemon Technical Assessment

The purpose of this project is to show some basic data transforms applied to an opensource IMDB data set.
Two transformations are done namely: 
- A. Fetch top 15 movies with a minimum of 100 votes. Please note that
ranking is calculated by formula: (numVotes /
averageNumberOfVotes) * averageRating
- B. List of the title of these top 15 movies

## Getting Started

### Dependencies

* Insure you have a python virtual environment installed on your machine. Use either conda or venv.
* The project was completed using Windows 10, and this will affect the way the program runs on other machines because of the specific directory naming conventions.
* Python version 3.8 or higher installed on your machine.
* Please ensure that you have also installed pip, which is a Python package manager.
* Make sure that Jupyter Notebooks are installed on your machine.

### Installing

* Activate your virtual environment using your preferred method.
* ```pip install -r requirements.txt```

### Executing program

* Step 1: Refer to the Jupyter notebook in the 'src' directory named "data_exploration_and_optimizations". This script is employed to investigate and enhance our data prior to its consumption by the main function. Run 
```jupyter-notebook```
* Step 2: Check test cases ```python -m unittest -v Test_Cases.DataTransformTestCases```
* Step 3: Run ```python main.py```

### Relevant output

