# -*- coding: utf-8 -*-


from .DeterministicModel import DeterministicModel, DeterministicInputs, \
                                DeterministicOutputs


import pandas as pd
import numpy as np



class ScheduleModel(DeterministicModel):
    """
    """
    
    def __init__(self):
        ""
        self._inputs=ScheduleInputs()
        
    
        
    def run(self):
        """Runs the model.
        
        :returns: The model outputs.
        :rtype: ScheduleOutputs
        
        """
        
        outputs=DeterministicOutputs()
        outputs._timestamps=self._inputs.timestamps
        
        if not self._inputs.all_days is None:
            
            data=self._get_profile_values(self._inputs.all_days,
                                          outputs.timestamps)
            
            outputs._data['result']=data
        
        return outputs
           

    def _get_profile_values(self,
                            schedule_values,
                            timestamps):
        """
        """
        interval=int(24*60*60/len(schedule_values)) # in seconds
        #print(interval)
        schedule_times=list(range(interval,86400+interval,interval))
        #print(schedule_times)
        #print(schedule_values)
    
        x=((timestamps-timestamps.normalize())
           /pd.Timedelta(seconds=1)).astype(int).tolist() 
            # timestamps in seconds after midnight
        #print(x)
    
        y=np.searchsorted(schedule_times, x) # indices for schedule_values list
        #print(y)
        
        values=[schedule_values[x] for x in y]
        #print(values)
        
        return values
        
    
ScheduleModel.inputs.__doc__=ScheduleModel.inputs.__doc__.replace(
    'DeterministicInputs',
    'ScheduleInputs')
           

    
 
class ScheduleInputs(DeterministicInputs):
    """
    """
    
    def __init__(self):
        ""
        DeterministicInputs.__init__(self)
        self._all_days=None
        
        
    @property
    def all_days(self):
        ""
        return self._all_days
    
    @all_days.setter
    def all_days(self,value):
        ""
        # validation check here...
        self._all_days=value
    
 
    
class ScheduleOutputs(DeterministicOutputs):
    """
    """
    
    
