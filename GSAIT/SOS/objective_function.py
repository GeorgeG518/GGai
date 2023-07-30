import numpy as np
from sos_input import sos_input
class objective_function():
    """
    Abstract base class for objective function classes defined by the user
    """
    def __init__(self,num_cv, iv=None):
        """
        This will require some thinking because the contructor doesn't have any sort
        of input file taken into account.
        IN:
            num_cv=number of control variables
            iv=initial value
        """
        self.control_variable_count=num_cv
        if iv is None:
            iv=np.zeros(len(self.control_variable_count),dtype=np.float64) # TODO: fix to constraints
        self.current_value = iv

    @property
    def value(self):
        return np.copy(self.current_value)

    def pre_process(self):
        return

    def post_process(self):
        return

    def gradient(self, point=None):

        arr_partial_derivatives=np.zeros(self.control_variable_count,dtype=np.float64)
        if point is None: 
            point=self.current_value
        for each in range(point.shape[0]):
            copy=np.copy(point)
            copy[each]=point[each]+sos_input.STEPSIZE
            arr_partial_derivatives[each]= (self.evaluate(copy)-self.evaluate(point))/sos_input.STEPSIZE

        return arr_partial_derivatives

    def evaluate(self,point):
        """
        Required by the user to evaluate. Preferably needs to be something that can be evaluate 
        fast.
        """
        print("You must implement an evaluate function in a class that inherits from objective_function")

    def update(self,new_point):
        """
        IN:
            new_point: 1darray representing new point

        Might be worth caching previous points here so that way you can evaluate faster
        """
        self.current_value=new_point