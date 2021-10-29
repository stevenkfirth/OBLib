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
    
    .. rubric:: Code Example
    
    .. code-block:: python
           
       >>> from OBLib import ScheduleModel
       >>> model=ScheduleModel()
       >>> model.inputs.set_timestamps(start=(2021,1,1),
       >>>                             freq='H',
       >>>                             periods=24*7)
       >>> model.inputs.all_days=[21]
       >>> result=model.run()
    
    """
    
    def __init__(self):
        ""
        self._inputs=ScheduleInputs()
        
    
        
    def run(self):
        """Runs the model.
        
        :returns: The model outputs.
        :rtype: ScheduleOutputs
        
        """
        
        # all days data -- default is [np.nan]
        data=self._get_schedule_values(self._inputs._all_days,
                                       self._inputs._timestamps)
        
        # create series with all_days data and timestamps
        s=pd.Series(data=data,
                    index=self._inputs._timestamps)
        
        # weekdays
        if not self._inputs._weekdays is None:
            mask=s.index.weekday<5
            timestamps=s.index[mask]
            data=self._get_schedule_values(self._inputs._weekdays,
                                           timestamps)
            s[mask]=data
        
        # weekends
        if not self._inputs._weekends is None:
            mask=s.index.weekday>4
            timestamps=s.index[mask]
            data=self._get_schedule_values(self._inputs._weekends,
                                           timestamps)
            s[mask]=data
            
        
        # create Outputs object
        outputs=ScheduleOutputs()
        outputs._timestamps=s.index
        
        outputs._data['result']=s.tolist()
        
        return outputs
           

    def _get_schedule_values(self,
                             day_profile,
                             timestamps):
        """This function returns a list of schedule values for a given
        set of timestamps.
        
        :param day_profile: A day profile as defined in `ScheduleInputs`
        :type day_profile: list
        :param timestamps: A set of timestamps
        :type timestamps: pandas.DatetimeIndex
        
        :rtype: list
        
        """
        # calculates the interval of the day profile
        # - in seconds
        # e.g. a day_profile of [21] has an interval of 86400
        # e.g. a day_profile of [5, 21] has an interval of 43200
        interval=int(24*60*60/len(day_profile)) 
        #print(interval)
        
        # calculates the times when the day profile values occur
        # - in seconds past midnight
        # e.g. a day_profile of [21] has a profile_times of [86400]
        # e.g. a day_profile of [5, 21] has a profile_times of [43200,86400]
        profile_times=list(range(interval,86400+interval,interval))
        #print(profile_times)
    
        # converts the timestamps to a list of times after midnight
        # - in seconds past midnight
        x=((timestamps-timestamps.normalize())
           /pd.Timedelta(seconds=1)).astype(int).tolist() 
        #print(x)
    
        # works out where the timestamps values align with the profile_times
        # - this gives a list of indices
        # - the list has the same length as timestamps
        # - each value in the list gives the index to be used for that
        #   timestamp to access the schedule value in the day_profile list.
        y=np.searchsorted(profile_times, x, side='right') 
        #print(y)
        
        # creates a list of schedule values
        # - the list has the same length as timestamps
        values=[day_profile[x] for x in y]
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
    
    
