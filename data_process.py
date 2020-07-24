from kami.datasets import TrainDataset, TestDataset
from kami.features import FeatureSet
from typing import *

class Processor(object):
    def __int__(self, raw_data, features, ):
        self.raw_data = raw_data
        self.features = features
        self.Train = TrainDataset()
        self.Test = TestDataset()

    def process(self):
        pass