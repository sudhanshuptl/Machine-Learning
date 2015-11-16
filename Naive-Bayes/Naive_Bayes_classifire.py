__auther__='Sudhanshu Patel'
#Classify Iris data Using Naive Bayes
#An Example Of Supervised Learning

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import numpy as np

#{{ Getting Iris Dataset
data=load_iris()
X=data.data #input Features
Y=data.target #Class of corresponding Input
#}}

if __name__=='__main__':
    # clsf == classifire :)
    clsf=GaussianNB()
    #{{training our classifire using Naive_bayes
    #!for IRis data Classification

    clsf.fit(X,Y)

    #}}

    # Test fot All data
    print '''  _______Input_______\
            __Real Class__\
            Prediction class '''
    pred=[]
    for i in range(len(X)):
        pred.append(clsf.predict(X[i])) #storing Pred result
        print X[i],'\t\t\t',Y[i],'\t\t\t',pred[-1]

    from sklearn.metrics import accuracy_score
    print "Accuracy Test Using accuracy_score function"
    pred=np.array(pred)
    print accuracy_score(pred,Y)*100,'%  Wow _/\_ Not Bad'
