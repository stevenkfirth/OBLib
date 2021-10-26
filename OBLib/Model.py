# -*- coding: utf-8 -*-

import pandas as pd



class Model():
    """Abstract model class
    """
    
    def __init__(self):
        """
        """
        
        
        
    def _generate_timestamps(self,
                             start=None,
                             end=None,
                             freq=None,
                             periods=None):
        """
        """
        timestamps=pd.date_range(start=start,
                                 end=end,
                                 freq=freq,
                                 periods=periods)
        return timestamps
        
        
    
    
    
class Output():
    """Abstract outputs class
    """
    
    def __init__(self):
        """
        """
        self._timestamps=None # ->pd.DatetimeIndex
        self._data={} # key -> data name; value-> np.array etc.
        
        
    
    def __repr__(self):
        ""
        return ("%s" % self.__class__.__name__
                + "("
                + "timestamps=%s" % self.timestamps
                + ", "
                + "data=%s" % self.data
                + ")"
                )
    
    @property
    def timestamps(self):
        ""
        return self._timestamps
    
    
    @property
    def data(self):
        ""
        return self._data
    
    
    @property
    def df(self):
        ""
        return pd.DataFrame(index=self.timestamps,
                            data=self.data)
        
        


