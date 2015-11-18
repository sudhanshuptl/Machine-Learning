
import csv
import numpy as np
from sklearn.svm import SVC
import datetime
import matplotlib.pyplot as plt

# Data Files
Test_file_name='test.csv'
Train_File_name='train.csv'

#Create Dataset
def parse_csv(datafile):
    data=[]
    with open(datafile,'rb') as sd:
        r=csv.DictReader(sd)
        for line in r:
            data.append(line)
        return data
def create_dataset(dataset, Train=True):
    # Carete Feature & Label array
    feature=[]
    target=[]
    #calculating Avg Age and emb
    emb,freq,ide=dict(),dict(),0
    avgAge,count=0,0
    for data in dataset:
        if data['Age'] !='':
            try:
                avgAge+=float(data['Age'])
                count+=1
            except:
                print 'Eror, ',data['Age']
        if data['Embarked'] not in emb:
            emb[data['Embarked']]=ide
            ide+=1
            freq[data['Embarked']] = 1
        else:
            freq[data['Embarked']] +=1
    #find Max Frequent mbarked class
    val=max(freq.values())
    for key in freq:
        if freq[key]==val:
            Barked=key
            break
    del freq,val


    avgAge=avgAge/count
    
    for data in dataset:
        if Train:
            target.append(int(data['Survived']))
        else:
            target.append(int(data['PassengerId']))
        temp=[]
        #temp.append(int(data['PassengerId']))
        temp.append(int(data['Pclass']))
        temp.append(int(data['SibSp']))
        temp.append(int(data['Parch']))
        temp.append(float(data['Fare'])/240)
        if data['Sex']=='male':
            temp.append(1)
        else:
            temp.append(0)
        if data['Age']=='':
            temp.append(avgAge)
        else:
            temp.append(float(data['Age']))
        feature.append(temp)
        if data['Embarked'] !='':
            temp.append(emb[data['Embarked']])
        else:
            temp.append(emb[Barked])
    
    return np.array(feature),np.array(target)

if __name__=='__main__':
    parse_data=parse_csv(Train_File_name)
    
    #input Feature & output label
    X,Y = create_dataset(parse_data)
    #for i in range(len(X)):
    #    print X[i],Y[i]

    #Draw(Y,X)
    
    #Now Create & Train Our Classifier
    clsf=SVC(kernel='rbf',gamma=10,C=1) #SVM Classier
    print 'Training Started ..'
    a = datetime.datetime.now()
    clsf.fit(X, Y)
    b=datetime.datetime.now()
    print 'Training Is completed, Time taken for training :',b-a
    
    #Now Load Testing dataset
    parse_data=parse_csv(Test_file_name,)
    P,Q= create_dataset(parse_data,Train=False)
    
    # Print Accuracy Test
    prediction=clsf.predict(P)
    #for i in range(len(P)):
    #    print P[i],prediction[i]
    
    # Write Results in file
    with open('result.csv', 'w') as csvfile:
        fieldnames = ['PassengerId', 'Survived']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(P)):
            writer.writerow({'PassengerId': Q[i], 'Survived': prediction[i]})
