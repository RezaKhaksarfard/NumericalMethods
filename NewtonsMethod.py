# Newton's Method
 
from Derivative import NumericalDerivative
from MinimizerABC import MinimizerABC 

class NewtonsMethod( MinimizerABC ):
    
    def Minimize( self, func, params ):
        totalDiff = 1.0e6
        
        derObj = NumericalDerivative() # Derivate calculation object

        nParams = len( params )
        delta = [ 0.0 ] * nParams
        nIter = 0
        while totalDiff > self.ep:
            totalDiff = 0
            
            for i in range( nParams ):
                firstDer = derObj.CentralDiff( func, params, i )
                secondDer = derObj.SecondDer( func, params, i )
                delta[ i ] = -firstDer / secondDer
                totalDiff += abs( delta[ i ] )
                
            for i in range( nParams ):
                params[ i ] += delta[ i ]
                
            nIter += 1

        return params