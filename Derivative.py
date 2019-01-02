# Numerical First and Second Derivatives 

import numpy as np

class NumericalDerivative( ):
    
    def __init__( self ):
        self.__delta = 0.001 # The small change in variable for derivative calculation

    # First derivative calculation by central difference method        
    def CentralDiff( self, func, params, i ):
        paramsPlus = params.copy()
        paramsPlus[ i ] += self.__delta

        paramsMinus = params.copy()
        paramsMinus[ i ] -= self.__delta
        
        der = ( func( paramsPlus ) - func( paramsMinus ) ) / ( 2 * self.__delta )
        
        return der
        
    # First derivative calculation by backward difference method        
    def BackwardDiff( self, func, params, i ):
        paramsMinus = params.copy()
        paramsMinus[ i ] -= self.__delta
        
        der = ( func( params ) - func( paramsMinus ) ) / self.__delta
        
        return der
        
    # First derivative calculation by forward difference method        
    def ForwardDiff( self, func, params, i ):
        paramsPlus = params.copy()
        paramsPlus[ i ] += self.__delta

        der = ( func( paramsPlus ) - func( params ) ) / self.__delta
        
        return der
        
    # Second derivative calculation        
    def SecondDer( self, func, params, i ):
        paramsPlus = params.copy()
        paramsPlus[ i ] += self.__delta

        paramsMinus = params.copy()
        paramsMinus[ i ] -= self.__delta
        
        der = ( func( paramsPlus ) - 2 * func( params ) + func( paramsMinus ) ) / np.power( self.__delta, 2 )
        
        return der
        