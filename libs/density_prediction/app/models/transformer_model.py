from pathlib import Path

import torch

class TransformerModel:
    def __init__(self, model_path: Path):
         self.model = "TransformerModel" # self.load_model(model_path=model_path) # TODO

    def load_model(self, model_path):
        """Load pretrained model or custom model."""
        return torch.load(model_path)

    def predict(self, input_data):
        """Model inference logic. TODO"""
        with torch.no_grad():
            # return self.model(input_data)
            return f"Model prediction for input[:10]: {input_data[:10]}"
