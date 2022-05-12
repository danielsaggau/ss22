import arff
import numpy as np
import scikit-learn
dataset = arff.load(open('sat12_all_feature_values.arff'))
data = np.array(dataset['data'])
