import numpy as np
from sos_input import sos_input
class optimization_method():
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
        """
        Value property that returns the value at a point
        """
        return np.copy(self.current_value)

    def pre_process(self):
        """
        Abstract method that can be overridden to perform any necessary pre-processing steps
        """
        return

    def post_process(self):
        """
        Abstract method that can be overridden to perform any necessary post-processing steps
        """
        return
        
    def evaluate(self,point):
        """
        Required by the user to evaluate. Preferably needs to be something that can be evaluate 
        fast.
        """
        raise NotImplementedError("You must implement an evaluate function in a class that inherits from optimize_function")

    def update(self,new_point):
        """
        IN:
            new_point: 1darray representing new point

        Might be worth caching previous points here so that way you can evaluate faster
        """
        self.current_value=new_point

class gradient_method(optimization_method):
    def __init__(self,num_cv, iv=None):
        super().__init__(num_cv, iv)

    def gradient(self, point=None):
        """
        Can be overridden to user's needs. Returns a 1d array of partial derivatives
        """
        arr_partial_derivatives=np.zeros(self.control_variable_count,dtype=np.float64)
        if point is None: 
            point=self.current_value
        # TODO: need to cache points, would make sense
        current_evaluated=self.evaluate(point)
        for each in range(point.shape[0]):
            copy=np.copy(point)
            copy[each]=point[each]+sos_input.STEPSIZE
            arr_partial_derivatives[each]= (self.evaluate(copy)-current_evaluated)/sos_input.STEPSIZE

        if sos_input.METHOD=='gradient-descent':
            return -arr_partial_derivatives
        elif sos_input.METHOD=='gradient-ascent':
            return arr_partial_derivatives