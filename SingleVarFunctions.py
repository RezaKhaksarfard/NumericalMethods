#Parametric models with one input and one ouput

import numpy as np

def Func1( x, params ):
    return params[ 0 ] + params[ 1 ] * np.power( x, 3 )