__auther__='Sudhanshu Patel'
import csv
import numpy as np
from sklearn.svm import SVR
import datetime

# Data Files
Test_file_name='train.csv'
Train_File_name='test.csv'

#Create Dataset
def parse_csv(datafile):
    #create a list of All rows data in json formate
    data=[]
    with open(datafile,'rb') as sd:
        r=csv.DictReader(sd)
        for line in r:
            data.append(line)
        return data
    
def create_dataset(dataset):
    # Create Feature & Label array
    feature=[]
    target=[]
    for data in dataset:
        target.append(int(data['failure']))
        temp=[]
        temp.append(int(data['time']))
        feature.append(temp)
    return np.array(feature),np.array(target)


if __name__=='__main__':
    #parse_data=parse_csv(Train_File_name)
    #X,Y=create_dataset(parse_data)
    
    #input Feature & output label
    failure=[12,15,28,39,53,53,60,60,60,63,68,68,82,91,97,97,102,103,103,104,105,109,109,113,125,126,131,158,165,166,166,173,183,189,193,194,202,204,214,229,230,235,235,237,238,238,239,243,251,253,257,260,263,266,268,271,271,272,274,279,284,288,288,291,293,299,305,308,323,323,327,328,333,336,347,349,369,389,392,393,405,410,411,411,417,435,435,435,435,441,441,453,467,468,488,509,512,517,558,559,573,587,644,644,655,728,734,769,783,994,1064]
    
    Y=[]
    X =[]
    for i in range(1,len(failure)+1):
        X.append([i])
    for fail in failure:
        Y.append(fail)

    #**************    
    #Now Create & Train Our Classifier
    clsf=SVR(kernel='rbf', C=1e2, gamma=0.1)
    print 'Training Started ..'
    clsf.fit(X,Y)
   
    
    #Now Load Testing dataset

    
    # Print Accuracy Test
    print 'TIme           Real failure           predicted failure'
    prediction=clsf.predict(X)
    for i in range(len(X)):
    	print X[i],'           ',Y[i],'          ',prediction[i]

    print 'r-squire Score',clsf.score(X,Y)
