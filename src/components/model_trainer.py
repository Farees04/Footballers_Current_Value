import os
import sys
from dataclasses import dataclass
from sklearn.metrics import r2_score
import xgboost as xg
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import pandas as pd


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Split training and test input data")
            target = "current_value"
            X_train = train_df.drop(target,axis=1)
            y_train= train_df[target]
            X_test = test_df.drop(target,axis=1)
            y_test = test_df[target]

            
    
            # 'learning_rate': 0.1 'n_estimators': 200
            
            logging.info(f"Best found model on both training and testing dataset")
            X_train["position"] = X_train["position"].astype("category")
            X_test["position"] = X_test["position"].astype("category")
            dtrain_reg = xg.DMatrix(X_train, enable_categorical=True)
            dtest_reg = xg.DMatrix(X_test, enable_categorical=True)
            params = {"objective": "reg:squarederror",'n_estimators': 200,'learning_rate': 0.1  }
            n = 100
            model = xg.train(
            params=params,
            dtrain=dtrain_reg,
            num_boost_round=n,)
            y_pred = model.predict(dtest_reg)
            score = r2_score(y_test, y_pred)*100
            print(" Accuracy of the model is %.2f" %score)
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )   
            return score
            



            
        except Exception as e:
            raise CustomException(e,sys)