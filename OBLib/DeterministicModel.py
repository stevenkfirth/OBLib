# -*- coding: utf-8 -*-

from .Model import Model, Output


import pandas as pd
import numpy as np



class DeterministicModel(Model):
    """
    """
    
    def __init__(self,
                 all_days=None):
        """
        """
        self.all_days=all_days
        
        
    def __repr__(self):
        ""
        return ("DeterministicModel("
                +"all_days=%s)" % (self._all_days)
                +")"
                )
    
    
    @property
    def all_days(self):
        ""
        return self._all_days
    
    
    @all_days.setter
    def all_days(self,value):
        ""
        # validation check here...
        self._all_days=value
        
        
    def run(self,
            start=None,
            end=None,
            freq=None,
            periods=None):
        """
        
        """
        
        output=DeterministicOutput()
        output._timestamps=self._generate_timestamps(start=start,
                                                     end=end,
                                                     freq=freq,
                                                     periods=periods)
        
        if not self.all_days is None:
            
            data=self._get_profile_values(self.all_days,
                                          output.timestamps)
            
            
        
        
            output._data['profile']=data
        
        return output
           
    
    
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
        
    
    
class DeterministicOutput(Output):
    """
    """
    
    
