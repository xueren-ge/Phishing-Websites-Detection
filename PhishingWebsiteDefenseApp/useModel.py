import joblib
from FeatureExtraction import getAttributess

class myModel:
    def __init__(self):
     self.model = joblib.load('./model/xgb_model.pkl')
     self.thresh = 0.5

    def __getFeature(self, url):
        return getAttributess(url)

    def __useModel(self, features):
        return self.model.predict(features)

    def pipeline(self, url):
        features = self.__getFeature(url)
        return self.__useModel(features)
        # return 1 if self.__useModel(features) > self.thresh else 0


if __name__ == '__main__':
    model = myModel()
    print(model.pipeline('https://github.com/masqueraderx'))