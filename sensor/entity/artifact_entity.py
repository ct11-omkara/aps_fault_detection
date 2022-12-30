from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str
# class DataIngestionArtifact:...

@dataclass
class DataValidationArtifact:
    report_file_path:str
# class DataValidationArtifact:...

@dataclass
class DataTransformationArtifact:
    transform_object_path:str
    transformed_train_path:str
    transformed_test_path:str
    target_encoder_path:str
# class DataTransformationArtifact:...


@dataclass
class ModelTrainerArtifact:
    model_path:str 
    f1_train_score:float 
    f1_test_score:float


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    improved_accuracy:float

    
class ModelPusherArtifact:...