# -*- coding: utf-8 -*-


from .DeterministicModel import DeterministicModel, DeterministicInputs, \
                                DeterministicOutputs


import pandas as pd
import numpy as np



class ScheduleModel(DeterministicModel):
    """The ScheduleModel class.
    
    This is a deterministic model which makes predictions based on a series
    of fixed 'daily profiles'.
    
    This is similar to the approach taken to specify schedules in many
    building simulation tools.
    
    """
    
    def __init__(self):
        ""
        self._inputs=ScheduleInputs()
        
    
        
    def run(self):
        """Runs the model.
        
        :returns: The model outputs.
        :rtype: ScheduleOutputs
        
        """
        
        outputs=ScheduleOutputs()
        outputs._timestamps=self._inputs.timestamps
        
        # all days
        if not self._inputs.all_days is None:
            
            data=self._get_profile_values(self._inputs.all_days,
                                          outputs.timestamps)
            
            outputs._data['result']=data
        
        # weekends
        
        
        
        # weekdays
        
        
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
    """Inputs to the `ScheduleModel` class.
    
    The inputs are formed of a series of 'day profiles'.
    
    A day profile is a list of numbers which represents the schedule for a day:
    For example:
        
    * [21] represents a constant value of 21 throughout the day.
    * [5,12,5] represents a value of 5 for the first 8 hours, followed by
      a value of 21 for the next 8 hours, with a final value of 8 for the 
      remaining 8 hours.
    * [5]*8 + [12]*8 + [5]*8 represents the same profile as [5,12,5]
    
    Day profile lists can be set to the following attributes. These attributes 
    are applied in the order below when creating the final predicted values.
        
    * `all_days`: This day profile is applied to all days.
    * `weekdays`: This day profile is applied to weekdays (Monday to Friday) only.
    * `weekends`: This day profile is applied to weekends (Saturday and Sunday) only.
     
    
    """
    
    def __init__(self):
        ""
        DeterministicInputs.__init__(self)
        self._all_days=[np.nan]
        self._weekdays=None
        self._weekends=None
        
        
    @property
    def all_days(self):
        """A day schedule to be applied to all days.
        
        Default value is [np.nan].
        
        Read/write property.
        
        :rtype: tuple or list
        
        """
        return self._all_days
    
    
    @all_days.setter
    def all_days(self,value):
        ""
        self._all_days=value
        
    
    @property
    def weekdays(self):
        """A day schedule to be applied to weekdays (Monday to Friday).
        
        Read/write property.
        
        :rtype: tuple or list
        
        """
        return self._weekdays
    
    
    @weekdays.setter
    def weekdays(self,value):
        ""
        self._weekdays=value
        
        
    @property
    def weekends(self):
        """A day schedule to be applied to weekends (Saturday and Sunday).
        
        Read/write property.
        
        :rtype: tuple or list
        
        """
        return self._weekends
    
    
    @weekends.setter
    def weekends(self,value):
        ""
        self._weekends=value
    
 
    
class ScheduleOutputs(DeterministicOutputs):
    """Outputs of the `ScheduleModel` class.
    """
    
    
