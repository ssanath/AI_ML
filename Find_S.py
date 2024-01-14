# Find S
import pandas as pd
train = pd.read_csv("trainingdata.csv")
train = train.values.tolist()
hypothesis = ['0']*(len(train[0])-1)
for row in train:
    x = row
    if(x[-1] == "Yes"):
        for i in range(len(x)-1):
            if(hypothesis[i] == '0'):
                hypothesis[i] = x[i]
            elif(hypothesis[i] != x[i]):
                hypothesis[i] = '?'
print(hypothesis)
test = pd.read_csv("test.csv")
test = test.values.tolist()
res = []
test_data = []
predicted = []
for i in range(len(test)):
    test_data.append(test[i][-1])
tot_count = len(test_data)
for row in test:
    res = []
    x = row
    for i in range(len(x)-1):
        if(x[i] == hypothesis[i]):
            res.append(x[i])
        else:
            res.append('?')
    if(res == hypothesis):
        predicted.append("Yes")
    else:
        predicted.append("No")
pred_count = 0
for i in range(len(predicted)):
    if(predicted[i] == test_data[i]):
        pred_count += 1
accuracy = pred_count/tot_count
print("Accuracy: ", accuracy)
