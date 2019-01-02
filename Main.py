import numpy as np
from functools import partial

import SingleVarFunctions
import LossFunctions
import MinimizerFactory

if __name__ == '__main__':
    
    #Parametric Model
    func = SingleVarFunctions.Func1
    
    #Input Data
    xData = [ -2, -1, 0, 1, 2 ]
    randList = np.random.uniform( -0.01, 0.01, size = len( xData ) )
    yData = [ func( x, [ 2, 3 ] ) + r for ( x, r ) in zip( xData, randList ) ]
    
    #Loss function to minimize
    lossFunc = LossFunctions.SSE
    
    #Freeze function, inputs and outputs
    lossFunc = partial( lossFunc, func = func, xData = xData, yData = yData )
    
    #Minimize
    minimizer = MinimizerFactory.GetMinimizer('Newton')
    
    params = minimizer.Minimize( lossFunc, [ 1, 1 ] )
    print( params )