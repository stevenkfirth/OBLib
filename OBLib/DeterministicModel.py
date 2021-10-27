# -*- coding: utf-8 -*-

from .Model import Model, Inputs, Outputs


import pandas as pd
import numpy as np



class DeterministicModel(Model):
    """Abstract model class.
    This is an abstract class for all deterministic models and should not be used directly.
    Instead this class is inherited by other more specialised model classes.
    
    """
    
    def __init__(self):
        ""
        self._inputs=DeterministicInputs()
        
    
DeterministicModel.inputs.__doc__=DeterministicModel.inputs.__doc__.replace(
    'Inputs',
    'DeterministicInputs')
           
DeterministicModel.run.__doc__=DeterministicModel.run.__doc__.replace(
    'Outputs',
    'DeterministicOutputs')
    
       
    
class DeterministicInputs(Inputs):
    """Abstract deterministic model inputs class.
    This should not be used directly.
    Instead this class is inherited by other more specialised model inputs classes.
    
    """
    
    
    
    
class DeterministicOutputs(Outputs):
    """Abstract deterministic model outputs class.
    This should not be used directly.
    Instead this class is inherited by other more specialised model outputs classes.
    
    """
    
    
