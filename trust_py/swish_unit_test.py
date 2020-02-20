"""

"""

import swish_analyze
import numpy as np
import unittest


class TestModel(unittest.TestCase):
 
    def test_data(self,X_train,y_train,X_test,y_test):
	    self.assertEqual(X_train.shape[0], len(y_train))
	    self.assertEqual(X_test.shape[0], len(y_test))



class TestModel(unittest.TestCase):
    def __init__(self,X_train,y_train,X_test,y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def test_data(self):
	    self.assertEqual(self.X_train.shape[0], len(self.y_train))
	    self.assertEqual(self.X_test.shape[0], len(self.y_test))

    

if __name__ == '__main__':
    X_train = np.random.random((250,200))
    y_train = np.random.randint(2, size=250)
    X_test = np.random.random((100,200))
    y_test = np.random.randint(2, size=100)    
        
    unittest.main()
    
    suite = unittest.TestSuite()
    suite.addTest(TestModel(X_train,y_train,X_test,y_test))
    unittest.TextTestRunner().run(suite)
