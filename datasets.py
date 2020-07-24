import os
import pandas as pd

class RawData(object):
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.TrainData = {}
        self.TestData = {}

    def list_data(self, folder=""):
        return os.listdir(self.base_dir + "/" + folder)

    def load_data(self):
        raise NotImplemented()


class WingRawData(RawData):
    def load_data(self):
        self.TrainData["base"] = pd.read_csv(self.base_dir+"/train/train_base.csv")
        self.TestData["base"] = pd.read_csv(self.base_dir+"/test/test_base.csv")




class TrainDataset(object):
    def split(self):
        pass

    def to_lgb(self):
        pass

    def to_xgb(self):
        pass

    def to_np(self):
        pass


class TestDataset(object):

    def to_lgb(self):
        pass

    def to_xgb(self):
        pass

    def to_np(self):
        pass