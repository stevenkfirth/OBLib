# -*- coding: utf-8 -*-

import unittest

from OBLib import Model, DeterministicModel
from OBLib import ScheduleModel
from OBLib import SAP2012ThermostatModel

import pandas as pd






class Test_ScheduleModel(unittest.TestCase):
    ""
    
    def test_run_all_days(self):
        ""
        m=ScheduleModel()
        m.inputs.set_timestamps(start=(2021,1,1),freq='H',periods=24*7)
        
        # constant 0
        m.inputs.all_days=[0]
        result=m.run()
        self.assertEqual(result.data['result'],
                         [0]*24*7)
        
        
        
    
            
        
        
if __name__=='__main__':
    
    
    
    unittest.main()