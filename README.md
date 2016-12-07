# py_gen_data
python project to investigate the use of symbolic execution, Prolog, Python and  to automate production of test data for unit testing

This Project is an investigation into the automatic generation of unit test data for Python 3.5.2
This is a sharing folder with initial code samples to investigate data structures and this is by no means ready to do any testing.

This project is using the ast.py module to perform the initial code parsing into an abstract sytax tree.
This tree is traversed to create the sets of constraints for each path.

The next stages of this coding is to develop the system for communicating to the Prolog interpreter to create the data sets from 
the path constraint sets.
