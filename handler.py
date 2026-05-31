import joblib
import numpy as np
from pydantic import BaseModel

class InputData(BaseModel):
    area_sqft: float = 0.0

class Handler:
    def __init__(self):
        self.model = None
        self.scaler = None

    def load_model(self):
        tools = joblib.load('artifacts/machine_learning_tools.pkl')
        self.model, self.scaler = tools['model'], tools['scaler']


    def predict(self, input_data: InputData):
        input_array = np.array(input_data.area_sqft).reshape(1, -1)
        input_scaled = self.scaler.transform(input_array)
        prediction = self.model.predict(input_scaled)
        return prediction[0]