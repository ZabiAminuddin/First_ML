import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from exceptions import CustomException
from logger import logging
from components.data_transformation import DataTransformation
from components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "rawdata.csv")

class DataIngestion:
    def __init__(self):
        self.initiation_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Initiated Data Ingestion method")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("reading data from stud")
            os.makedirs(os.path.dirname(self.initiation_config.train_data_path),exist_ok=True)

            df.to_csv(self.initiation_config.raw_data_path, index=False, header=True)

            train_set, test_set=train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.initiation_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.initiation_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion completed")

            return(

                self.initiation_config.train_data_path,
                self.initiation_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_tranformation = DataTransformation()
    data_tranformation.initiate_data_transformation(train_data, test_data)
    