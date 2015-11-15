# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:33:32 2015

@author: Sudhanshu Patel 
"""

import csv
import numpy as np
from sklearn.svm import SVC
import datetime

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
        target.append(data['Class'])
        temp=[]
        temp.append(data['Thickness'])
        temp.append(data['Cell_size'])
        temp.append(data['Cell_shape'])
        temp.append(data['Marg_adhesion'])
        temp.append(data['Epi_cell_size'])
        temp.append(data['Bare_nuclei'])        
        temp.append(data['Bland_cromatin'])
        temp.append(data['Norm_nucleoli'])
        temp.append(data['Mitoses'])
        feature.append(temp)
    return np.array(feature),np.array(target)
    
if __name__=='__main__':
    parse_data=parse_csv(Train_File_name)
    
    #input Feature & output label
    X,Y = create_dataset(parse_data)
    
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
    
