s = 'azcbobobegghakl'

workingSequentialString = ""
sequentialString = ""
stringIsInSequence = True

for i in range(0, len(s)):
    
	#print "Start of string: index " + str(i)
	
	substring = s[i:]
	
	#print "substring: " + substring
	
	stringIsInSequence = True
	workingSequentialString = ""
	
	
	substringLength = len(s[i:])
	
	#print "length of substring: " + str(substringLength)
	#print "number of tests: " + str(substringLength - 1)
	
	for j in range(0, substringLength):
		if j == 0:
			workingSequentialString = substring[0]
		#print "value of character " + str(substring[j]) + ": " + str(ord(substring[j]))
		#print "value of workingSequentialString: " + workingSequentialString
		if j > 0 and ord(substring[j]) < ord(substring[j-1]):
			#print "Test false"
			stringIsInSequence = False
		if (j > 0) and stringIsInSequence == True:
			workingSequentialString = workingSequentialString + substring[j]
			
	if len(workingSequentialString) > len(sequentialString):
		sequentialString = workingSequentialString
	
	#print "-------\n"
	

#print "_________________"
print sequentialString