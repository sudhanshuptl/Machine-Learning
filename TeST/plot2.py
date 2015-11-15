__auther__='Sudhanshu Patel'
import sklearn.datasets as data
from sklearn.svm import SVC
import numpy as np

# Get digits Dataset****
data=data.load_digits()
X=data.data #feature vector
Y=data.target #Label Vector
# **************************

#** Plot
import matplotlib.pyplot as plt
for x, y in zip(X, Y):
    plt.scatter( x, y, color='b' ) 
plt.show()
if __name__=='__main__':
    pass
    
