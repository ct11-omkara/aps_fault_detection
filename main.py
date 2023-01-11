#=========================================OLD CODE=========================================
# import pymongo

# # Provide the mongodb localhost url to connect python to mongodb.
# client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
# # Database Name
# dataBase = client["neurolabDB"]

# # Collection  Name
# collection = dataBase['Products']

# # Sample data
# d = {'companyName': 'iNeuron',
#      'product': 'Affordable AI',
#      'courseOffered': 'Machine Learning with Deployment'}

# # Insert above records in the collection
# rec = collection.insert_one(d)

# # Lets Verify all the record at once present in the record with all the fields
# all_record = collection.find()

# # Printing all records present in the collection
# for idx, record in enumerate(all_record):
#      print(f"{idx}: {record}")

#=========================================Logger & Exception check=========================================

# from sensor.logger import logging
# from sensor.exception import SensorException
# import sys, os

# def test_logger_and_exception ():
#      try:
#           logging.info("Starting the test_logger_and_exception")
#           result = 3/0
#           print(result)
#           logging.info("Stopping the test_logger_and_exception")
#      except Exception as e:
#           logging.debug(str(e))

#           raise SensorException(e, sys)

# if __name__ == "__main__":
#      try:
#           test_logger_and_exception()
#      except Exception as e:
#           print(e)


#=========================================utils/get_collection_as_dataframe=========================================

# from sensor.utils import get_collection_as_dataframe
# import sys, os

# if __name__ == "__main__":
#      try:
#           get_collection_as_dataframe(database_name="aps", collection_name="sensor")
#      except Exception as e:
#           print(e)

#=========================================config_entity.DataIngestionConfig testing=========================================

# from sensor.entity import config_entity
# import sys, os

# if __name__ == "__main__":
#      try:
#           training_pipeline_config = config_entity.TrainingPipelineConfig()
#           data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
#           print(data_ingestion_config.to_dict())
#      except Exception as e:
#           print(e)

#=========================================components.data_ingestion.py (training & testing split) testing=========================================

# from sensor.entity import config_entity
# from sensor.components import data_ingestion
# import sys, os

# if __name__ == "__main__":
#      try:
#           training_pipeline_config = config_entity.TrainingPipelineConfig()
#           data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
#           print(data_ingestion_config.to_dict())
#           data_ingestion = data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
#           print(data_ingestion.initiate_data_ingestion())
          
#      except Exception as e:
#           print(e)


#=========================================components.data_validation.py (validation) testing=========================================

# from sensor.entity import config_entity
# from sensor.components.data_ingestion import DataIngestion
# from sensor.components.data_validation import DataValidation
# import sys, os

# if __name__ == "__main__":
#      try:
#           training_pipeline_config = config_entity.TrainingPipelineConfig()
#           data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
#           print(data_ingestion_config.to_dict())
#           data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
#           data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

#           data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
#           data_validation = DataValidation(data_validation_config=data_validation_config, 
#                                            data_ingestion_artifact=data_ingestion_artifact)
#           data_validation_artifact = data_validation.initiate_data_validation()           
          
#      except Exception as e:
#           print(e)


#=========================================components.data_trainer.py (trainer) testing=========================================

# from sensor.entity import config_entity
# from sensor.components.data_ingestion import DataIngestion
# from sensor.components.data_validation import DataValidation
# from sensor.components.data_transformation import DataTransformation
# from sensor.components.model_trainer import ModelTrainer
# import sys, os

# if __name__ == "__main__":
#      try:
#           training_pipeline_config = config_entity.TrainingPipelineConfig()

#           #Data ingestion
#           data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
#           print(data_ingestion_config.to_dict())
#           data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
#           data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

#           #Data validation
#           data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
#           data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
#           data_validation_artifact = data_validation.initiate_data_validation()     


#           #Data transformation
#           data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)      
#           data_transformation = DataTransformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
#           data_transformation_artifact = data_transformation.initiate_data_transformation()


#           #Model trainer
#           model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
#           model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
#           model_trainer_artifact = model_trainer.initiate_model_trainer()
          
#      except Exception as e:
#           print(e)


#=========================================components.data_evaluation.py (evaluation) testing=========================================

# from sensor.entity import config_entity
# from sensor.components.data_ingestion import DataIngestion
# from sensor.components.data_validation import DataValidation
# from sensor.components.data_transformation import DataTransformation
# from sensor.components.model_trainer import ModelTrainer
# from sensor.components.model_evaluation import ModelEvaluation
# import sys, os

# if __name__ == "__main__":
#      try:
#           training_pipeline_config = config_entity.TrainingPipelineConfig()

#           #Data ingestion
#           data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
#           print(data_ingestion_config.to_dict())
#           data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
#           data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

#           #Data validation
#           data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
#           data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
#           data_validation_artifact = data_validation.initiate_data_validation()     


#           #Data transformation
#           data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)      
#           data_transformation = DataTransformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
#           data_transformation_artifact = data_transformation.initiate_data_transformation()


#           #Model trainer
#           model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
#           model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
#           model_trainer_artifact = model_trainer.initiate_model_trainer()


#           #model evaluation
#           model_eval_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
#           model_eval = ModelEvaluation(model_eval_config=model_eval_config, 
#                data_ingestion_artifact=data_ingestion_artifact, 
#                data_transformation_artifact=data_transformation_artifact, 
#                model_trainer_artifact=model_trainer_artifact)
#           model_eval_artifact = model_eval.initiate_model_evaluation()
          
#      except Exception as e:
#           print(e)


#=========================================components.data_pusher.py (pusher) testing=========================================

# from sensor.entity import config_entity
# from sensor.components.data_ingestion import DataIngestion
# from sensor.components.data_validation import DataValidation
# from sensor.components.data_transformation import DataTransformation
# from sensor.components.model_trainer import ModelTrainer
# from sensor.components.model_evaluation import ModelEvaluation
# from sensor.components.model_pusher import ModelPusher
# import sys, os

# if __name__ == "__main__":
#      try:
#           training_pipeline_config = config_entity.TrainingPipelineConfig()

#           #Data ingestion
#           data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
#           print(data_ingestion_config.to_dict())
#           data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
#           data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

#           #Data validation
#           data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
#           data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
#           data_validation_artifact = data_validation.initiate_data_validation()     


#           #Data transformation
#           data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)      
#           data_transformation = DataTransformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
#           data_transformation_artifact = data_transformation.initiate_data_transformation()


#           #Model trainer
#           model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
#           model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
#           model_trainer_artifact = model_trainer.initiate_model_trainer()


#           #model evaluation
#           model_eval_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
#           model_eval = ModelEvaluation(model_eval_config=model_eval_config, 
#                data_ingestion_artifact=data_ingestion_artifact, 
#                data_transformation_artifact=data_transformation_artifact, 
#                model_trainer_artifact=model_trainer_artifact)
#           model_eval_artifact = model_eval.initiate_model_evaluation()


#           #model pusher
#           model_pusher_config = config_entity.ModelPusherConfig(training_pipeline_config)
#           model_pusher = ModelPusher(model_pusher_config=model_pusher_config, 
#                data_transformation_artifact=data_transformation_artifact, 
#                model_trainer_artifact=model_trainer_artifact)
#           model_pusher_artifact = model_pusher.initiate_model_pusher()

          
#      except Exception as e:
#           print(e)


#=========================================OR components.data_pusher.py (pusher) testing=========================================

# from sensor.pipeline.training_pipeline import start_training_pipeline

# print(__name__)
# if __name__ == "__main__":
#      try:
#           start_training_pipeline()          
#      except Exception as e:
#           print(e)

#=========================================OR components.data_pusher.py (pusher) testing=========================================

from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.pipeline.batch_prediction import start_batch_prediction

file_path = '/config/workspace/aps_failure_training_set1.csv'

print(__name__)
if __name__ == "__main__":
     try:
          # start_training_pipeline()  (if model is not trained first time, then uncomment this line, & run it)
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)