val = [60, 100, 120]
wt = [10, 20, 10]
W = 50
n = len(val)
def knap(w, val_arr, wt_arr, n):
	if n == 0 or w == 0:
		return 0
	if wt_arr[n-1] > w:
		return knap(w,val_arr, wt_arr, n-1)
	else:
		return max(val_arr[n-1] + knap(w- wt_arr[n-1] ,val_arr, wt_arr, n-1), knap(w,val_arr, wt_arr, n-1))

def knap_iterative():
	pass
# print knap(W, val, wt, n)