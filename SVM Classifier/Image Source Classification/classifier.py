# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:33:32 2015

@author: Sudhanshu Patel 
"""

import xlrd
import numpy as np
from sklearn.svm import SVC
import datetime
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
# Data Files
Test_file_name='featurevectors_NONIQM_new.xls'
Train_File_name='featurevectors_NONIQM_new.xls'
def excel_data(filename,Train=True):
    book = xlrd.open_workbook(filename)
 
    # print number of sheets
    print book.nsheets
 
    # print sheet names
    print book.sheet_names()
 
    # get the first worksheet
    feature=[]
    target=[]
    if Train:
        first_sheet = book.sheet_by_index(0)
        for row in range(1,140):
            temp=[]
            for col in range(11):
                try:
                    temp.append(float(first_sheet.cell(row,col).value))
                except:
                    print 'first_sheet.cell(row,col)',first_sheet.cell(row,col),row,col
            feature.append(temp)
            target.append(1)
        Second_sheet = book.sheet_by_index(1)
        for row in range(1,140):
            temp=[]
            for col in range(11):
                temp.append(float(Second_sheet.cell(row,col).value))
            feature.append(temp)
            target.append(2)
        third_sheet = book.sheet_by_index(2)
        for row in range(1,140):
            temp=[]
            for col in range(11):
                temp.append(float(third_sheet.cell(row,col).value))
            feature.append(temp)
            target.append(3)
                            
    else:
        first_sheet = book.sheet_by_index(0)
        for row in range(110,143):
            temp=[]
            for col in range(11):
                temp.append(float(first_sheet.cell(row,col).value))
            feature.append(temp)
            target.append(1)
        Second_sheet = book.sheet_by_index(1)
        for row in range(110,143):
            temp=[]
            for col in range(11):
                temp.append(float(Second_sheet.cell(row,col).value))
            feature.append(temp)
            target.append(2)
        third_sheet = book.sheet_by_index(2)
        for row in range(110,143):
            temp=[]
            for col in range(11):
                temp.append(float(third_sheet.cell(row,col).value))
            feature.append(temp)
            target.append(3)
    return  np.array(feature),np.array(target)
'''
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
    #input Feature & output label
    X,Y = excel_data(Train_File_name)
    X_norm=X_normalized = normalize(X, norm='l2')

    #Draw(Y,X)
    
    #Now Create & Train Our Classifier
    clsf=SVC(kernel='rbf',gamma=1,C=1) #SVM Classier
    print 'Training Started ..'
    a = datetime.datetime.now()
    clsf.fit(X_norm, Y)
    b=datetime.datetime.now()
    print 'Training Is completed, Time taken for training :',b-a
    
    #Now Load Testing dataset
    P,Q=excel_data(Test_file_name)
    
    # Print Accuracy Test
    prediction=clsf.predict(P)
    from sklearn.metrics import accuracy_score
    print 'Accuracy Check ',accuracy_score(prediction,Q)*100,'%  Wow _/\_ that is GOOD :)'
    #print 'real Output,   predicted Output,     freatures'
    #for i in range(50):
    #    print Q[i],'             ',prediction[i]
    
