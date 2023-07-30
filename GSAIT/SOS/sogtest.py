import objective_function
import numpy as np
from sos_input import sos_input
class custom_func(objective_function.objective_function):
    """
    Going to test simple functions like x**2
    """
    def __init__(self, num_cv, initial_value ):
        super().__init__(num_cv, initial_value)
        return
    
    def evaluate(self,x):
        return np.sin(x)

input=sos_input()
fn=custom_func(1, np.array([-1],dtype=np.float64))

for i in range(input.ITERMAX):
    fn.pre_process()
    step_vector=fn.gradient()
    increment=input.STEPSIZE*step_vector


    fn.update(fn.value+increment)
    print("val:",fn.value)
    fn.post_process()
    if np.abs(np.sum(increment))<=input.EPSILON:
        print("Hill climbing converged!")
        break

print(fn.value)