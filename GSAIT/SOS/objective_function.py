import numpy as np

class objective_function():
    """
    Abstract base class for objective function classes defined by the user
    """
    def __init__(self,num_cv, iv=None):
        """
        This will require some thinking because the contructor doesn't have any sort
        of input file taken into account.
        """
        self.control_variable_count=num_cv
        if iv is None:
            iv=np.zeros(len(self.control_variable_count)) # TODO: fix to constraints
        self.initial_values = iv

    def pre_process(self):
        print("Abstract pre_process")

    def post_process(self):
        print("Abstract post_process")

    def gradient(self, point):
        print("Abstract gradient")

    def evaluate(self,point):
        print("Abstract evaluate")
