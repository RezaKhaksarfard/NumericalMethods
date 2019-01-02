from GradientDescent import GradientDescent
from NewtonsMethod import NewtonsMethod

def GetMinimizer( minimizerName ):
    if minimizerName == 'GD':
        return GradientDescent()
    elif minimizerName == 'Newton':
        return NewtonsMethod()