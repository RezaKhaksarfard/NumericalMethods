import unittest

import SingleVarFunctions

class TestSingleVarFunctions( unittest.TestCase ):

    def testAlmostEqual( self ):
        self.assertAlmostEqual( SingleVarFunctions.Func1( 1, [ 2, 3 ] ),  5.0 )
        
    def testNotAlmostEqual( self ):
        self.assertNotAlmostEqual( SingleVarFunctions.Func1( 2, [ 3, 4 ] ),  0.0 )