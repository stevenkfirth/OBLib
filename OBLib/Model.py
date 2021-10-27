# -*- coding: utf-8 -*-

import pandas as pd



class Model():
    """Abstract model class.
    This is the top-level class and should not be used directly.
    Instead this class is inherited by other more specialised model classes.
    
    """
    
    def __init__(self):
        ""
        self._inputs=Inputs()
        
        
    def run(self):
        """Runs the model.
        
        This is an abstract method and should be overloaded by subclasses.
        
        :returns: The model outputs.
        :rtype: Outputs
        
        """
        outputs=Outputs()
        
        # timestamps passed from inputs to outputs
        outputs._timestamps=self._inputs._timestamps
        
        # CALCULATIONS HERE
        
        return outputs
        
    
    @property
    def inputs(self):
        """The model inputs. Access this object to change the model inputs.  
        
        Read-only property.
        
        :rtype: Inputs
        
        """
        return self._inputs
    
        
    
class Inputs():
    """Abstract model inputs class.
    This is the top-level class and should not be used directly.
    Instead this class is inherited by other more specialised model inputs classes.
    
    """
    
    def __init__(self):
        ""
        
        self._timestamps=None
    
    
    def set_timestamps(self,
                       start=None,
                       end=None,
                       *args,
                       **kwargs):
        """Convenience method to set the `timestamps` property.
        
        :param start: The start timestamp (optional)
        :type start: tuple
        :param end: The end timestamp (optional)
        :type end: tuple
        
        The remaining input arguments here are passed to the `pandas.date_range` method. 
        See the pandas documentation for details.
        
        Typcial inputs might be:
        
        * start=(2021,1,1,0,0) (i.e. 1st January 2021)
        * freq='H' (for hourly intervals)
        * periods=24 (to generate 1 day of hourly intervals)        
        
        :rtype: pandas.DatetimeIndex
        
        """
        if not start is None:
            start=pd.Timestamp(*start)
        if not end is None:
            end=pd.Timestamp(*end)
            
        
        self._timestamps=pd.date_range(start=start,
                                       end=end,
                                       *args,
                                       **kwargs)
        return self._timestamps
    
    
    @property
    def timestamps(self):
        """The input timestamps.      
        Model predictions will be made for each timestamp.
        
        Read / write property.
        
        :rtype: pandas.DatetimeIndex
        
        """
        return self._timestamps
    
    
    @timestamps.setter
    def timestamps(self,value):
        ""
        self._timestamps=value
    
    
    
class Outputs():
    """Abstract model outputs class.
    This is the top-level class and should not be used directly.
    Instead this class is inherited by other more specialised model outputs classes.
    
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
        """The outputs timestamps.      
       
        Read-only property.
        
        :rtype: pandas.DatetimeIndex
        
        """
        return self._timestamps
    
    
    @property
    def data(self):
        """The model predictions.
        
        Read-only property.
        
        :returns: A dictionary of the model results.
            Key-value pairs are: keys -> the name of the quantity or variable; 
            values -> a list of the model predictions (this list aligns with the 
            output timestamps).
        
        :rtype: dict
        
        """
        return self._data
    
    
    @property
    def df(self):
        """A Pandas dataframe of the timestamps and data.
        
        Read-only property.
        
        :returns: A dataframe with: index -> timestamps; 
            columns -> 'data' keys; values -> `data` values.
        
        :rtype: pandas.DataFrame
        
        """
        return pd.DataFrame(index=self.timestamps,
                            data=self.data)
        
        


