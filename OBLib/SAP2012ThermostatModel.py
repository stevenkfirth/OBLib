# -*- coding: utf-8 -*-

from .ScheduleModel import ScheduleModel


class SAP2012ThermostatModel(ScheduleModel):
    """Class representing the thermostat model in SAP2012.
    
    SAP2012 is the energy calculation methodology used in the UK for building
    regulation compliance of domestic buildings.
    See `<https://www.bregroup.com/sap/standard-assessment-procedure-sap-2012/>`_
    
    This model predicts the 'living area' heating period as given in Table 9 
    of the SAP2012 document. This is:
        
    * On weekdays, the heating is on at times 07:00-09:00 and 16:00-23:00
      with a thermostat temperature of 21 degC.
    * On weekends, the heating is on at time 07:00-23:00 with a
      thermostat temperature of 21 degC.
      
    When the heating is off, an assumed thermostat setpoint of -100 degC is used.
    
    .. rubric:: Code Example
    
    .. code-block:: python
           
       >>> from OBLib import SAP2012ThermostatModel
       >>> model=SAP2012ThermostatModel()
       >>> model.inputs.set_timestamps(start=(2021,1,1),
       >>>                             freq='H',
       >>>                             periods=24*7)
       >>> result=model.run()
       
    
    
    """
    
    def __init__(self):
        ""
        ScheduleModel.__init__(self)
        
        self._inputs.weekdays=[-100]*7+[21]*2+[-100]*7+[21]*7+[-100]*1
        self._inputs.weekends=[-100]*7+[21]*16+[-100]*1
        
    
    
    