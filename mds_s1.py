"""TechVick_GonnaWin"""
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

testKag=pd.read_csv("D:/Vikulp_imp_ambitions/machine_learning/kaggle/mds/test.csv")
train=pd.read_csv("D:/Vikulp_imp_ambitions/machine_learning/kaggle/mds/train.csv")
sample_submission=pd.read_csv("D:/Vikulp_imp_ambitions/machine_learning/kaggle/mds/sample_submission.csv")

column=['X0','X1','X2','X3','X4','X5','X6','X8']
for i in column:
    input = train[[i]]
    output = []
    for k in input[i]:
        num=sum([ord(j) for j in k],0)
        number = num-96
        output.append(number)
    output=[int(m) for m in output]
    df = pd.DataFrame(np.array(output).reshape(4209,1), columns = list("a"))
    train[i]=df['a']

target1 = train["y"].values

train.pop('y')
train.pop('ID')


feature1 = train
regr_1=DecisionTreeRegressor(max_depth=2)
regr_1.fit(feature1,target1)


column=['X0','X1','X2','X3','X4','X5','X6','X8']
for i in column:
    input = testKag[[i]]
    output = []
    for k in input[i]:
        num=sum([ord(j) for j in k],0)
        number = num-96
        output.append(number)
    output=[int(m) for m in output]
    df = pd.DataFrame(np.array(output).reshape(4209,1), columns = list("a"))
    testKag[i]=df['a']

id=testKag['ID']
testKag.pop('ID')
feature2 = testKag
y_1=regr_1.predict(feature2)
data_frame = pd.DataFrame(id,columns=['ID'])
data_frame['y'] = pd.Series(y_1, index=data_frame.index)
data_frame['ID'] = data_frame["ID"].astype(int)
np.savetxt('submission.csv',data_frame,delimiter=',')



