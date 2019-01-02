# Gradient Descent
 
from Derivative import NumericalDerivative
from MinimizerABC import MinimizerABC 

class GradientDescent( MinimizerABC ):
    
    def __init__( self ):
        super( GradientDescent, self ).__init__()
        self.__alpha = 0.005 # Learning rate
    
    def Minimize( self, func, params ):
        totalDiff = 1.0e6
        
        derObj = NumericalDerivative() # Derivate calculation object

        nParams = len( params )
        delta = [ 0.0 ] * nParams
        nIter = 0
        while totalDiff > self.ep:
            totalDiff = 0
            
            for i in range( nParams ):
                delta[ i ] = self.__alpha * derObj.CentralDiff( func, params, i )
                totalDiff += abs( delta[ i ] )
            
            for i in range( nParams ):
                params[ i ] -= delta[ i ]
                
            nIter += 1

        return params