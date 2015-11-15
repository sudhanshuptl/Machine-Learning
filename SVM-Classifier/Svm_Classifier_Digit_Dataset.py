#SVM Classifier
__auther__='Sudhanshu Patel'
import sklearn.datasets as data
from sklearn.svm import SVC
import numpy as np

# Get digits Dataset****
data=data.load_digits()
X=data.data #feature vector
Y=data.target #Label Vector
# **************************

if __name__=='__main__':
    # clsf = classifier
    clsf=SVC(kernel='rbf',gamma=0.001,C=0.1) #SVM Classier
    # There are other argument like
    # [[[C, cache_size, class_weight, coef0,
    # decision_function_shape, gamma, kernel,
    # max_iter, probability, random_state,shrinking,
    # tol,verbose]]]
    # you can pass in order to custmize your classifier

    # Trainig Classifier  ***
    clsf.fit(X, Y)

    #Now predict values for given classifier
    prediction = clsf.predict(X)

    # 
    print 'printing data for few classification'
    for i in [4,50,200,300,600,700,900,1100,1500,1600,1700,344,1123]:
        print 'Feature : ',X[i],'\t Real Digit :',Y[i],'\tPredicted Digit',prediction[i]
        print '********************************'
    print '\n\n\n'

    # Print Accuracy Test
    from sklearn.metrics import accuracy_score
    print 'Accuracy Check ',accuracy_score(prediction,Y)*100,'%  Wow _/\_ that is GOOD :)'
    

    
    
