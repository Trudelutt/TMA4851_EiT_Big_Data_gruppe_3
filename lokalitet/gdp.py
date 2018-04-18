import numpy as np
import csv
import pandas as pd
import math
import pycountry
from scipy.stats import norm
import time
from openpyxl import load_workbook


avs=pd.read_csv('testgdp.csv', sep=',',header=None)
avs = avs.values
