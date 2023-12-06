from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import * 
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.utils import evaluate_model, save_obj


@dataclass
class ModelTrainerConfig:
    trained_model_fie_path = MODEL_FILE_PATH
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_training(self, train_arr, test_arr):
        try:
            X_train, y_train, X_test, y_test = (train_arr[:,:-1], train_arr[:,-1],
                                                 test_arr[:,:-1], test_arr[:,-1])
            
            models = {
                "XGBRegressor": XGBRegressor(),
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "RandomForestRegressor": RandomForestRegressor(),
                "SVR": SVR()                       
                }
            
            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            
            best_model_score = max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[
                list(model_report.values().index(best_model_score))
            ]
            
            best_model = models[best_model_name]
            
            print(f" Best Model Found, Model Name : {best_model_name}, R2 Score : {best_model_score} ")
            logging.info("Best Model Found, Model Name : {best_model_name}, R2 Score : {best_model_score}")
            
            save_obj(file_path = self.model_trainer_config.trained_model_file_path,
                     obj = best_model)
            
            
        except Exception as e:
            raise CustomException(e, sys)