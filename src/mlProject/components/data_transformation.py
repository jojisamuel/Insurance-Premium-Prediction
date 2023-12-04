import os
from mlProject import logger
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    



    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        # Preprocess the data (encode categorical variables)
        le_sex = LabelEncoder()
        le_smoker = LabelEncoder()
        le_region = LabelEncoder()

        data['sex'] = le_sex.fit_transform(data['sex'])
        data['smoker'] = le_smoker.fit_transform(data['smoker'])
        data['region'] = le_region.fit_transform(data['region'])

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        