import os, sys
from datetime import datetime

# artifact -> pipeline folder -> timestamp -> output

def get_currrent_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_currrent_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"

# ML_PROJECT_NEW_FULL/DATA_DIR/DATA_DIR_KEY

ARTIFACT_DIR_KEY = "Artifact"

# Data Ingestion related variable
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_RAW_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY ="test.csv"

# Data Transformmation related variables

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESS_DIR = "processor"
DATA_TRANSFORMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"

# artifacts/data_transformation/ processor->processor.pkl and transformation ->train.csv and test.csv

# Model Training

MODEL_TRAINER_KEY = "model_trainer"
MODEL_OBJECT = "model.pkl"
