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
 
# ターミナル対応
import matplotlib
 
def setting():
	#ファイル名をリスト化
	list_i=[1,2,5,8]
	list_j=list(range( 9,11,1))
	filename=list()
	for i in list_i:
		for j in list_j:
			filename.append(f'{i}-{j}.csv')
	
	#リストやフレームの準備
	df_x = pd.DataFrame()
	df_y = pd.DataFrame()
	count_list=list()
	ind_l=list(range(9,11))
	col_l=[1,2,5,8]
	spread_l=list(range(0,80,10))
	j=10
	number=list()
	pred_list=[]
	spread_list=[]
	height_list=[]
	min_list=[]
	ans_list=[1]*10+[5]*10+[6]*10+[7]*10
	
	for i, filename_csv in enumerate(filename):
		j=j+1
		tmp_df = np.loadtxt(filename_csv)
	#閾値設定
	fname="normal.csv"
	normal_df = np.loadtxt(fname)
	line=max(normal_df)	
	
	#メイン処理の中身
	for i, filename_csv in enumerate(filename):
		j=j+1
		number.append(str(j))
		tmp_df = np.loadtxt(filename_csv)
		
		start = 0
		N=len(tmp_df)
		
		#特徴量抽出
		o=N//10
		maxid = signal.argrelmax(tmp_df, order=o) #最大値
		freq = np.linspace(start, start+N, N)
		
		#ピーク値のIDの変形
		max_array=np.array(maxid)
		size=len(freq[maxid])
		array = np.array(max_array).reshape(size, 1)

		
		#山の個数カウント
		#カウントした波形のarray作成
		k=0
		spread=0
		height=0
		array1=np.array([0])
		array1=np.delete(array1,0)
		new_array=np.array([0])
		for i in array:
			if(tmp_df[i]>line):
				k=k+1
				if(k==1):
					new_array=np.append(array1,i)
				else:
					new_array=np.append(new_array,i)
		
		
		#XとYのフレーム化
		x=freq[new_array]
		y=tmp_df[new_array]
		temp_x=pd.DataFrame(x)
		df_x = pd.concat([df_x, temp_x], axis=1)
		temp_y=pd.DataFrame(y)
		df_y = pd.concat([df_y, temp_y], axis=1)
		
		
		if(k==0):
			gesture=8
		elif(k==1):
			gesture=1
			min_list.append(y)
		#k=2の場合に幅（spread）と高さ（height）の計算
		elif(k==2):
			new_x=sorted(x,reverse=True)
			new_y=sorted(y,reverse=True)
			spread=new_x[0]-new_x[1]
			height=new_y[0]-new_y[1]
			min_list.append(new_y[1])
		
		#k>2の場合の幅と高さの計算（一応）
		elif(k>2):
			new_x=sorted(x,reverse=True)
			new_y=sorted(y,reverse=True)
			while True:
				c=-1
				if(k==2):
					break
				for i in new_array:
					c=c+1
					if(new_y[k-1]==tmp_df[i]):
						k=k-1
						new_array=np.delete(new_array,c)
						break	
			x=freq[new_array]
			y=tmp_df[new_array]
			new_x=sorted(x,reverse=True)
			new_y=sorted(y,reverse=True)
			spread=new_x[0]-new_x[1]
			height=new_y[0]-new_y[1]
			min_list.append(new_y[1])

	center=(min(min_list)+line)/2
	return center-line

 
def load_tsdata(thre):
	#ファイル名をリスト化
	list_i=[1,2,5,8]
	list_j=list(range( 1,9,1))
	filename=list()
	for i in list_i:
		for j in list_j:
			filename.append(f'{i}-{j}.csv')
	
	#リストやフレームの準備
	df_x = pd.DataFrame()
	df_y = pd.DataFrame()
	count_list=list()
	ind_l=list(range(1,9))
	col_l=[1,2,5,8]
	spread_l=list(range(0,32,8))
	j=10
	number=list()
	pred_list=[]
	spread_list=[]
	height_list=[]
	min_list=[]
	ans_list=[1]*8+[2]*8+[5]*8+[8]*8
	
	for i, filename_csv in enumerate(filename):
		j=j+1
		tmp_df = np.loadtxt(filename_csv)
	#閾値設定
	fname="normal.csv"
	normal_df = np.loadtxt(fname)
	line=max(normal_df)+thre
	
	
	
	
	#メイン処理の中身
	for i, filename_csv in enumerate(filename):
		j=j+1
		number.append(str(j))
		tmp_df = np.loadtxt(filename_csv)
		
		start = 0
		N=len(tmp_df)
		
		#特徴量抽出
		o=N//10
		maxid = signal.argrelmax(tmp_df, order=o) #最大値
		freq = np.linspace(start, start+N, N)
		
		#ピーク値のIDの変形
		max_array=np.array(maxid)
		size=len(freq[maxid])
		array = np.array(max_array).reshape(size, 1)

		
		#山の個数カウント
		#カウントした波形のarray作成
		k=0
		spread=0
		height=0
		array1=np.array([0])
		array1=np.delete(array1,0)
		new_array=np.array([0])
		for i in array:
			if(tmp_df[i]>line):
				k=k+1
				if(k==1):
					new_array=np.append(array1,i)
				else:
					new_array=np.append(new_array,i)
		
		
		#XとYのフレーム化
		x=freq[new_array]
		y=tmp_df[new_array]
		temp_x=pd.DataFrame(x)
		df_x = pd.concat([df_x, temp_x], axis=1)
		temp_y=pd.DataFrame(y)
		df_y = pd.concat([df_y, temp_y], axis=1)
		
		
		if(k==0):
			gesture=8
		elif(k==1):
			gesture=1
			min_list.append(y)
		#k=2の場合に幅（spread）と高さ（height）の計算
		elif(k==2):
			new_x=sorted(x,reverse=True)
			new_y=sorted(y,reverse=True)
			spread=new_x[0]-new_x[1]
			height=new_y[0]-new_y[1]
			min_list.append(new_y[1])
		
		#k>2の場合の幅と高さの計算（一応）
		elif(k>2):
			new_x=sorted(x,reverse=True)
			new_y=sorted(y,reverse=True)
			while True:
				c=-1
				if(k==2):
					break
				for i in new_array:
					c=c+1
					if(new_y[k-1]==tmp_df[i]):
						k=k-1
						new_array=np.delete(new_array,c)
						break	
			x=freq[new_array]
			y=tmp_df[new_array]
			new_x=sorted(x,reverse=True)
			new_y=sorted(y,reverse=True)
			spread=new_x[0]-new_x[1]
			height=new_y[0]-new_y[1]
			min_list.append(new_y[1])

		
		#幅と高さによってラベルを与える
		if(k>=2):
			if(spread<80):
				spread_judge=0
			elif(spread>=80):
				spread_judge=1
# 			if(height<new_y[1]*0.8):
# 				height_judge=0
# 			elif(height>=new_y[1]*0.8):
# 				if(y[0]>y[1]):
# 					height_judge=1
# 				elif(y[0]<y[1]):
# 					height_judge=2
			
		
		#ジェスチャ判定
		if(k>=2):
			if(spread_judge==0):
# 				if(height_judge==0):
					gesture=2
# 				elif(height_judge==1):
# 					gesture=3
# 				else:
# 					gesture=4
			else:
# 				if(height_judge==0):
					gesture=5
# 				elif(height_judge==1):
# 					gesture=6
# 				else:
# 					gesture=7
		pred_list.append(gesture)
		spread_list.append(spread)
		height_list.append(height)
		
		
		#カウントした個数をフレーム化
	count_list.append(k)
	df_count=pd.DataFrame(pred_list)
	df_ans=pd.DataFrame(ans_list)
	df_count=df_count.T
	
	#高さと幅のデータフレーム
	df_spread=pd.DataFrame(spread_list)
	df_height=pd.DataFrame(height_list)
	b = df_spread.to_numpy().reshape(4,8)
	c = df_height.to_numpy().reshape(4,8)
	df_spread= pd.DataFrame(b, columns=ind_l, index=col_l)
	df_height= pd.DataFrame(c, columns=ind_l, index=col_l)
	df_spread=df_spread.T
	df_height=df_height.T

#各ジェスチャごとの正解率のフレーム
	accuracy_list=list()
	for i in spread_l:
		j=i+8
		sam_count_l=pred_list[i:j]
		sam_ans_l=ans_list[i:j]
		accuracy=accuracy_score(sam_ans_l, sam_count_l)
		accuracy_list.append(accuracy)
	
	#データフレームの詳細
	a = df_count.to_numpy().reshape(4,8)
	df_count= pd.DataFrame(a, columns=ind_l, index=col_l)
	df_count=df_count.T
	df_accuracy=pd.DataFrame(accuracy_list,index=col_l,columns=['accuracy'])
	df_accuracy=df_accuracy.T
	df_c=pd.concat([df_count,df_accuracy])
	
	#保存データフレームの作成
	df_x.columns=number
	df_y.columns=number
	df_x.to_csv('peak_X.csv')
	df_y.to_csv('peak_Y.csv')
	df_c.to_csv('peak_gesture.csv')
	df_spread.to_csv('peak_spread.csv')
	df_height.to_csv('peak_height.csv')
	
	#各データの表示
	cm = confusion_matrix(ans_list, pred_list)
	print('混同行列(confusion matrix)')
	print(cm)
	print('正解率(accuracy)')
	print(accuracy_score(ans_list, pred_list))
	print('適合率(precision)')
	prec=precision_score(ans_list, pred_list,average=None)
	print(prec)
	print('全体適合率')
	print(precision_score(ans_list, pred_list,average='macro'))
	print('再現率(recall)')
	reca=recall_score(ans_list, pred_list,average=None)
	print(reca)
	print('全体再現率')
	print(recall_score(ans_list, pred_list,average='macro'))
	print('F値(F-measure)')
	fsco=f1_score(ans_list, pred_list,average=None)
	print(fsco)
	print('全体F値')
	print(f1_score(ans_list, pred_list,average='macro'))
	
	#csv保存
	para_x=list(range(1,5,1))
	para_y=list(range(1,5,1))
	para=np.stack([accuracy_list,reca,prec,fsco])
	index=['accuracy','recall','precision','F-measur']
	para_df = pd.DataFrame(data=para, index=index, columns=para_x, dtype='float')
	conf= pd.DataFrame(cm,index=para_x,columns=para_y)
	df_v = pd.concat([conf, para_df])
	df_v.to_csv("peak_CM.csv")

	return ans_list,pred_list
	
def main():
	thre=setting()
	print(thre)
	ans_list,pred_list = load_tsdata(thre)
	return ans_list,pred_list
 
if __name__ == '__main__':
	main()
