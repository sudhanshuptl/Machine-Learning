# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:33:32 2015

@author: Sudhanshu Patel 
"""

import csv
import numpy as np
from sklearn.svm import SVC
import datetime
import matplotlib.pyplot as plt

# Data Files
Test_file_name='breast-cancer-test.csv'
Train_File_name='breast-cancer-train.csv'

#Create Dataset
def parse_csv(datafile):
    data=[]
    with open(datafile,'rb') as sd:
        r=csv.DictReader(sd)
        for line in r:
            data.append(line)
        return data
def create_dataset(dataset):
    # Carete Feature & Label array
    feature=[]
    target=[]
    for data in dataset:
        target.append(int(data['Class']))
        temp=[]
        temp.append(int(data['Thickness']))
        temp.append(int(data['Cell_size']))
        temp.append(int(data['Cell_shape']))
        temp.append(int(data['Marg_adhesion']))
        temp.append(int(data['Epi_cell_size']))
        temp.append(int(data['Bare_nuclei']))        
        temp.append(int(data['Bland_cromatin']))
        temp.append(int(data['Norm_nucleoli']))
        temp.append(int(data['Mitoses']))
        feature.append(temp)
    return np.array(feature),np.array(target)
'''
def Draw(pred, features, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], features[ii][2], features[ii][3], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()
'''

if __name__=='__main__':
    parse_data=parse_csv(Train_File_name)
    
    #input Feature & output label
    X,Y = create_dataset(parse_data)

    #Draw(Y,X)
    
    #Now Create & Train Our Classifier
    clsf=SVC(kernel='rbf',gamma=1,C=1) #SVM Classier
    print 'Training Started ..'
    a = datetime.datetime.now()
    clsf.fit(X, Y)
    b=datetime.datetime.now()
    print 'Training Is completed, Time taken for training :',b-a
    
    #Now Load Testing dataset
    parse_data=parse_csv(Test_file_name)
    P,Q= create_dataset(parse_data)
    
    # Print Accuracy Test
    prediction=clsf.predict(P)
    from sklearn.metrics import accuracy_score
    print 'Accuracy Check ',accuracy_score(prediction,Q)*100,'%  Wow _/\_ that is GOOD :)'
    
