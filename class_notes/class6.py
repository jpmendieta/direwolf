# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:39:49 2015

@author: jp
"""

import pandas as pd

flowers = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header= None, names=['sLength','sWidth','pLength','pWidth','species'])
