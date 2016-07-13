s = 'azcbobobegghakl'

count = 0
threeCharStringCount = len(s)-2

for i in range(0, threeCharStringCount):
    print i
    print s[i:i+3]
    if s[i:i+3] == "bob":
        count += 1
        print "yep"
    else:
        print "nope"

print "Number of times bob occurs is: " + str(count)