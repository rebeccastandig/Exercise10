mylist = [5,3,1,2,4,8,7,6]


def merge_sort(mylist):
	if len(mylist) <= 1:
		return mylist
	else:
		list1 = mylist[:(len(mylist)/2)]
		list2 = mylist[(len(mylist)/2):]
		list1 = merge_sort(list1)
		list2 = merge_sort(list2)
		newlist = []
		while len(list1) != 0 and len(list2) != 0:
			if list1[0] > list2[0]:
				newlist.append(list2.pop(0))
			else:
				newlist.append(list1.pop(0))
		if len(list1) > 0:
			newlist = newlist + list1
		else:
			newlist = newlist + list2
	return newlist

print merge_sort(mylist)