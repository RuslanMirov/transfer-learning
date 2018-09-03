"""
Created on Mon Sep  3 16:21:51 2018

@author: Ruslan
"""

class Configuration:
    def __init__(self):
        self.feature_extraction_epochs = 10 
        self.fine_tuning_epochs = 20
        self.epochs_without_transfer_learning = 100
        self.batch_size = 30
        self.data_dir = "data/training"
        self.val_dir = "data/validation"