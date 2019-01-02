import unittest

import LossFunctions
import SingleVarFunctions

class TestLossFunctions( unittest.TestCase ):

    def testAlmostEqual( self ):
        func = SingleVarFunctions.Func1 #Parametric Model
    
        #Input Data
        xData = [ -2, -1, 0, 1, 2 ]
        yData = [ func( x, [ 2, 3 ] ) for x in xData ]
        
        #Initialize model parameters
        params = [ 2, 3 ]
        
        self.assertAlmostEqual( LossFunctions.SSE( params, func, xData, yData ),  0.0 )
        
    def testNotAlmostEqual( self ):
        func = SingleVarFunctions.Func1 #Parametric Model
    
        #Input Data
        xData = [ -2, -1, 0, 1, 2 ]
        yData = [ func( x, [ 2, 3 ] ) for x in xData ]
        
        #Initialize model parameters
        params = [ 1, 3 ]
        
        self.assertNotAlmostEqual( LossFunctions.SSE( params, func, xData, yData ),  0.0 )