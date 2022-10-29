import config
import pickle
import json
import numpy as np

class Iris():
    def __init__(self, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm	):
        self.SepalLengthCm	= SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb")	as f:
            self.model = pickle.load(f)

        
        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    
    def get_predicted_class(self):
        self.load_model()

        test_arr = np.zeros(len(self.json_data['columns']))
        
        test_arr[0] = self.SepalLengthCm
        test_arr[1] = self.SepalWidthCm
        test_arr[2] = self.PetalLengthCm
        test_arr[3] = self.PetalWidthCm 
        print("Test array is:", test_arr)

        pred_class = self.model.predict([test_arr])
        return pred_class

