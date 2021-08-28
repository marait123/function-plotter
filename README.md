# function-plotter

# installation and setup
* you must make sure you have python3.7
* install the dependencies using `pip install requirements.tx`

# project Structure
    .
    ├── plotter                   # this folder includes the plotter main app and its utilities
        ├── plotter.py           # this file has the Window dialog of the app
        ├── utils.py           # this file includes some utility functions like errorDialog and others.
        ├── test_plotter.py           # this file can be run with pytest it uses pytestqt
        ├── test_utils.py           # this file can be run with pytest it uses pytest
    ├── images  # screenshots of testing and documentation
    └── requirements.txt    # this file includes the dependencies used to run the project
    └── README.md


# running
* after installing the requirements you can run the code using `python .\plotter\plotter.py`
# images


## drawing x^2
![ x2 image ](https://github.com/marait123/function-plotter/blob/main/images/x2.JPG)

## drawing x^3+3*x+500...
![ x3 image ](https://github.com/marait123/function-plotter/blob/main/images/x3.JPG)

## error when adding invalid formulae (expression)
![ error image ](https://github.com/marait123/function-plotter/blob/main/images/error1.JPG)



# testing
* you can run the gui testing pytest-qt using `pytest  .\plotter\test_plotter.py`
* you can run the utils testing pytest using `pytest .\plotter\test_utils.py`
* or you can run both by running testing.ps1 script
![ testing image ](https://github.com/marait123/function-plotter/blob/main/images/testing.JPG)
