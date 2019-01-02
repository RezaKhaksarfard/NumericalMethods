import unittest
from functools import partial

import MinimizerFactory
import SingleVarFunctions
import LossFunctions

class TestSingleVarFunctions( unittest.TestCase ):

    @classmethod
    def setUpClass( cls ):
        cls.__minimizer = MinimizerFactory.GetMinimizer( 'Newton' )


    def testMinimizeAlmostEqual( self ):
        
        #Parametric Model
        func = SingleVarFunctions.Func1 #Parametric Model
        
        #Input Data
        xData = [ -2, -1, 0, 1, 2 ]
        yData = [ func( x, [ 2, 3 ] ) for x in xData ]
        
        #Loss function to minimize
        lossFunc = LossFunctions.SSE
        
        #Freeze function, inputs and outputs
        lossFunc = partial( lossFunc, func = func, xData = xData, yData = yData )
        
        #Minimize
        paramsCalcluated = self.__minimizer.Minimize( lossFunc, [ 1, 1 ] )        
        
        paramsBase = [ 2, 3 ]
        for p1, p2 in zip( paramsCalcluated, paramsBase ):
            self.assertAlmostEqual( p1, p2, places = 3 )