from abc import ABC, abstractmethod

class MinimizerABC( ABC ):
    
    def __init__( self ):
        self.ep = 1.0e-6 # Small number used for convergence
        
    @abstractmethod
    def Minimize( self, func, params ):
        pass