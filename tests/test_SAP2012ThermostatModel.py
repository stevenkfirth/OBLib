# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import math


class Test_SAP2012ThermostatModel(unittest.TestCase):
    ""
    
    def test___init__(self):
        ""
        from OBLib import SAP2012ThermostatModel
        from OBLib.ScheduleModel import ScheduleInputs
        m=SAP2012ThermostatModel()
        self.assertIsInstance(m,
                              SAP2012ThermostatModel)
        self.assertIsInstance(m.inputs,
                              ScheduleInputs)
        
        
    def test_run(self):
        ""
        from OBLib import SAP2012ThermostatModel
        from OBLib.ScheduleModel import ScheduleOutputs
        
        m=SAP2012ThermostatModel()
        m.inputs.set_timestamps(start=(2021,1,1),
                                freq='H',
                                periods=24*7)
        result=m.run()
        self.assertIsInstance(result,
                              ScheduleOutputs)
        
        weekday_profile=[-100]*7+[21]*2+[-100]*7+[21]*7+[-100]*1
        weekend_profile=[-100]*7+[21]*16+[-100]*1
        
        self.assertEqual(result.data['result'],
                         weekday_profile*1+weekend_profile*2+weekday_profile*4)
        
        
if __name__=='__main__':
    
    unittest.main()
        
        
        