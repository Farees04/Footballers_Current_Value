import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import xgboost as xg


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
           
            model_path =os.path.join('artifacts',"model.pkl")
            model=load_object(file_path=model_path)
            features["position"] = features["position"].astype("category")
            dtrain_reg = xg.DMatrix(features, enable_categorical=True)
            preds=model.predict(dtrain_reg)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        position: str,
        height: float,
        age: float,
        appearance: int,
        goals: float,
        assists: float,
        yellow_cards: float,
        second_yellow_cards: float,
        red_cards: float,
        goals_conceded: float,
        clean_sheets: float,
        minutes_played: int,
        days_injured: int,
        games_injured: int,
        award: int,
        highest_value: int,
       ):
       
        self.position = position

        self.height = height

        self.age = age

        self.appearance = appearance

        self.goals = goals/self.appearance

        self.assists = assists/self.appearance

        self.yellow_cards = yellow_cards/self.appearance

        self.second_yellow_cards = second_yellow_cards/self.appearance

        self.red_cards = red_cards/self.appearance

        self.goals_conceded = goals_conceded/self.appearance

        self.clean_sheets = clean_sheets/self.appearance

        self.minutes_played = minutes_played

        self.days_injured = days_injured

        self.games_injured = games_injured

        self.award = award
        
        self.highest_value = highest_value * 1000000

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "position": [self.position],
                "height": [self.height],
                "age": [self.age],
                "appearance": [self.appearance],
                "goals": [self.goals],
                "assists": [self.assists],
                "yellow cards": [self.yellow_cards],
                "second yellow cards": [self.second_yellow_cards],
                "red cards": [self.red_cards],
                "goals conceded": [self.goals_conceded],
                "clean sheets": [self.clean_sheets],
                "minutes played": [self.minutes_played],
                "days_injured": [self.days_injured],
                "games_injured": [self.games_injured],
                "award": [self.award],
                "highest_value": [self.highest_value]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)