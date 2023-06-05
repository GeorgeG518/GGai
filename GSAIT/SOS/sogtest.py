import objective_function
import numpy as np

class sog_test(objective_function.objective_function):
    def __init__(self, num_cv, initial_values):
        super().__init__(num_cv, initial_values)

    def pre_process(self):
        print("sog test pre process")

a=sog_test(10, np.zeros(10))
a.post_process()
a.pre_process()
