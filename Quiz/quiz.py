# Problem 4
def isPalindrome(aString):
	newString = ''
	for letter in aString:
		newString = letter + newString
	if newString == aString:
		return True
	return False

# Problem 5
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    for i in range(len(listA)):
    	sum  = sum + (listA[i] * listB[i])
    return sum

#Problem 6
def flatten(aList):
    newList = []
    for item in aList:
        print item
        if isinstance(item, list):
            newList.append(flatten(item))
        newList.append(item)
	return newList

#Problem 7
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    pass


print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])