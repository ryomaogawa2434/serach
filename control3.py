import os
import wave
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one")
from one import personal
ans_list,pred_list=personal.main3()
sum_ans_list=ans_list
sum_pred_list=pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/two")
from two import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/three")
from three import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/four")
from four import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/five")
from five import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/Six")
from Six import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/seven")
from seven import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/eight")
from eight import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/nine")
from nine import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/ten")
from ten import personal
ans_list,pred_list=personal.main3()
sum_ans_list=sum_ans_list+ans_list
sum_pred_list=sum_pred_list+pred_list

print("\n")
print("全体総合")
cm = confusion_matrix(sum_ans_list,sum_pred_list)
print('混同行列(confusion matrix)')
print(cm)
print('正解率')
acu=recall_score(sum_ans_list,sum_pred_list,average=None)
print(acu)
print('全体正解率(accuracy)')
print(accuracy_score(sum_ans_list,sum_pred_list))
acu_all=accuracy_score(sum_ans_list,sum_pred_list)
print('適合率(precision)')
prec=precision_score(sum_ans_list,sum_pred_list,average=None)
print(prec)
print('全体適合率')
print(precision_score(sum_ans_list,sum_pred_list,average='macro'))
prec_all=precision_score(sum_ans_list,sum_pred_list,average='macro')
print('再現率(recall)')
reca=recall_score(sum_ans_list,sum_pred_list,average=None)
print(reca)
print('全体再現率')
print(recall_score(sum_ans_list,sum_pred_list,average='macro'))
reca_all=recall_score(sum_ans_list,sum_pred_list,average='macro')
print('F値(F-measure)')
fsco=f1_score(sum_ans_list,sum_pred_list,average=None)
print(fsco)
print('全体F値')
print(f1_score(sum_ans_list,sum_pred_list,average='macro'))
fsco_all=f1_score(sum_ans_list,sum_pred_list,average='macro')

para_x=list(range(1,5,1))
para_y=list(range(1,5,1))
para=np.stack([acu,reca,prec,fsco])
para_all=np.stack([acu_all,reca_all,prec_all,fsco_all])
index=["accuracy",'recall','precision','F-measur']
para_df = pd.DataFrame(data=para, index=index, columns=para_x, dtype='float')
conf= pd.DataFrame(cm,index=para_x,columns=para_y)
df_v = pd.concat([conf, para_df])
os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval")
df_v.to_csv("Result3.csv")
with open('Result3.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(para_all)
