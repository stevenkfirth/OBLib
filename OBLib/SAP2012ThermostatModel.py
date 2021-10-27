# -*- coding: utf-8 -*-

from .Model import Model, Outputs
from .ScheduleModel import ScheduleModel




class SAP2012ThermostatModel(ScheduleModel):
    """
    """
    
    def __init__(self):
        ""
        ScheduleModel.__init__(self)
        
        self._inputs.all_days=[0]*8+[21]*8+[0]*8
        
    