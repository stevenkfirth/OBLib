# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import math


class Test_ScheduleModel(unittest.TestCase):
    ""
    
    def test___init__(self):
        ""
        from OBLib import ScheduleModel
        from OBLib.ScheduleModel import ScheduleInputs
        m=ScheduleModel()
        self.assertIsInstance(m,
                              ScheduleModel)
        self.assertIsInstance(m.inputs,
                              ScheduleInputs)
        
        
    def test_run(self):
        ""
        from OBLib import ScheduleModel
        from OBLib.ScheduleModel import ScheduleOutputs
        import numpy as np
        m=ScheduleModel()
        m.inputs.set_timestamps(start=(2021,1,1),
                                freq='H',
                                periods=24)
        
        # no schedule
        result=m.run()
        self.assertIsInstance(result,
                              ScheduleOutputs)
        # the below is needed for lists which contain nan values
        # - as np.nan==np.nan returns False.
        try:
            np.testing.assert_array_equal(result.data['result'],
                                          [np.nan]*24)
        except AssertionError:
            self.fail()
        
        # all_days
        # - constant value
        m.inputs.all_days=[21]
        result=m.run()
        self.assertEqual(result.data['result'],
                         [21]*24)
        # - two values
        m.inputs.all_days=[5,21]
        result=m.run()
        self.assertEqual(result.data['result'],
                         [5]*12+[21]*12)
        # - three values
        m.inputs.all_days=[5,21,5]
        result=m.run()
        self.assertEqual(result.data['result'],
                         [5]*8+[21]*8+[5]*8)
        # - twenty four values
        m.inputs.all_days=[5]*8+[21]*8+[5]*8
        result=m.run()
        self.assertEqual(result.data['result'],
                         [5]*8+[21]*8+[5]*8)
        
        
        # weekdays
        m=ScheduleModel()
        m.inputs.set_timestamps(start=(2021,1,1),
                                freq='H',
                                periods=24*7)
        m.inputs.weekdays=[21]
        result=m.run()
        try:
            np.testing.assert_array_equal(result.data['result'],
                                          [21]*24+[np.nan]*48+[21]*24*4)
        except AssertionError:
            self.fail()
            
        # weekends
        m=ScheduleModel()
        m.inputs.set_timestamps(start=(2021,1,1),
                                freq='H',
                                periods=24*7)
        m.inputs.weekends=[21]
        result=m.run()
        try:
            np.testing.assert_array_equal(result.data['result'],
                                          [np.nan]*24+[21]*48+[np.nan]*24*4)
        except AssertionError:
            self.fail()
        
        
        
if __name__=='__main__':
    
    unittest.main()
        
        
        