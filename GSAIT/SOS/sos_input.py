
class sos_input():
    def __init__(self):
        sos_input.sos_dict = {}
        sos_input.EPSILON = 1e-8
        sos_input.ITERMAX = 100_000 # Confession: I learned how to do this on tiktok
        sos_input.STEPSIZE = 0.001
        sos_input.METHOD="gradient-descent"
        sos_input.CONSTRAINED=True
    
    def read(self, filename):
        pass

    def write(self, gui):
        pass

