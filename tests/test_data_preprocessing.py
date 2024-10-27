
import unittest
import pandas as pd
from src import data_preprocessing

class TestDataPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        df = pd.DataFrame({"feature1": [1, None, 3], "feature2": [2, 3, None]})
        data_preprocessing.preprocess_data(df)
        self.assertFalse(df.isnull().values.any())

if __name__ == "__main__":
    unittest.main()
