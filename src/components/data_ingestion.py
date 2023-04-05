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
    train_data_path: str=os.path.join('artifacts',"train.csv")# artifact is folder;  #data ingestion will save everything on this path
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # as sson as we call this, the three path above will be saved in the ingestion_config class variable
    
    def initiate_data_ingestion(self): #use to write code to read from databases
        logging.info("Entered the data ingestion method/component...")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")
        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) #so that we can also save it using rawdatapath

            logging.info("Train Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=40)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
        