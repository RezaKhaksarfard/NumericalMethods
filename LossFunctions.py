# Loss Funcitons

import numpy as np

def SSE( params, func, xData, yData ): #Sum of squared errors
    loss = sum( [ np.power( func( x, params ) - y, 2 ) for ( x, y ) in zip( xData, yData ) ] )
    return loss