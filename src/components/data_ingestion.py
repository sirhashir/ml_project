#used to read the data source from a particular dataset
#first localdataset

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#there should be some inputs that are required by data ingestion component
#where to save the test data
#where to save the train data

@dataclass #we wil be able to directly define class variable
class DataIngestionConfig: #any input we require will be given thorugh this class
    pass

