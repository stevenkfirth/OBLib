# -*- coding: utf-8 -*-

import unittest
import pandas as pd


class Test_Model(unittest.TestCase):
    ""
    
    def test___init__(self):
        ""
        from OBLib import Model
        from OBLib.Model import Inputs
        m=Model()
        self.assertIsInstance(m,
                              Model)
        self.assertIsInstance(m.inputs,
                              Inputs)
        
        
    def test_run(self):
        ""
        from OBLib import Model
        from OBLib.Model import Outputs
        m=Model()
        result=m.run()
        self.assertIsInstance(result,
                              Outputs)
        
        
        
class Test_Inputs(unittest.TestCase):
    ""
    
    def test_set_timestamps(self):
        ""
        from OBLib import Model
        m=Model()
        m.inputs.set_timestamps(start=(2021,1,1),
                                freq='H',
                                periods=24)
        self.assertEqual(m.inputs.timestamps.tolist(),
                         pd.date_range(start=pd.Timestamp(2021,1,1),
                                       freq='H',
                                       periods=24).tolist())
        
    
    def test_timestamps(self):
        ""
        from OBLib import Model
        m=Model()
        m.inputs.timestamps=pd.date_range(start=pd.Timestamp(2021,1,1),
                                          freq='H',
                                          periods=24)
        self.assertEqual(m.inputs.timestamps.tolist(),
                         pd.date_range(start=pd.Timestamp(2021,1,1),
                                       freq='H',
                                       periods=24).tolist())
        
        
        
if __name__=='__main__':
    
    unittest.main()