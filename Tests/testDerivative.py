import unittest

from Derivative import NumericalDerivative
import SingleVarFunctions 

class TestDerivative( unittest.TestCase ):

    def setUp( self ):
        self.__derObj = NumericalDerivative() # Derivate calculation object
        
    def testCentralDiffAlmostEqual( self ):
        
        func = lambda x: SingleVarFunctions.Func1( x[ 0 ], [ 2, 3 ] )

        der = self.__derObj.CentralDiff( func, [ 1 ], 0 )
        
        self.assertAlmostEqual( der, 9.0, places = 1 )
        
    def testBackwardDiffAlmostEqual( self ):
        
        func = lambda x: SingleVarFunctions.Func1( x[ 0 ], [ 2, 3 ] )

        der = self.__derObj.BackwardDiff( func, [ 1 ], 0 )
        
        self.assertAlmostEqual( der, 9.0, places = 1 )
        
    def testForwardDiffAlmostEqual( self ):
        
        func = lambda x: SingleVarFunctions.Func1( x[ 0 ], [ 2, 3 ] )

        der = self.__derObj.ForwardDiff( func, [ 1 ], 0 )
        
        self.assertAlmostEqual( der, 9.0, places = 1 )
        
    def testSecondDerAlmostEqual( self ):
        
        func = lambda x: SingleVarFunctions.Func1( x[ 0 ], [ 2, 3 ] )

        der = self.__derObj.SecondDer( func, [ 1 ], 0 )
        
        self.assertAlmostEqual( der, 18.0, places = 1 )