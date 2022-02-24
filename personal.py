import os

def main():
	os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one/first")
	print(os.getcwd())
	from one.first import ex_margin
	ans_list,pred_list = ex_margin.main()
	return ans_list,pred_list

def main2():
	os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one/first")
	from one.first import margin
	thre = margin.main()
	os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one/secound")
	print(os.getcwd())
	from one.secound import ex_margin
	ans_list,pred_list = ex_margin.main(thre)
	return ans_list,pred_list

def main3():
	os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one/first")
	from one.first import margin
	thre = margin.main()
	os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one/third")
	print(os.getcwd())
	from one.third import ex_margin
	ans_list,pred_list = ex_margin.main(thre)
	return ans_list,pred_list
	
def main4():
	os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one/first")
	from one.first import margin
	thre = margin.main()
	os.chdir("/Users/ogawaryoma/Desktop/PEAK/interval/one/fourth")
	print(os.getcwd())
	from one.fourth import ex_margin
	ans_list,pred_list = ex_margin.main(thre)
	return ans_list,pred_list
