import math

def roundNum2(input):
    print input
    output = map(lambda x: math.floor(x), input)
    print output
    print 'sum(input):', sum(input), ' '
    remain = int(round(sum(input)) - sum(output))
    print remain
    it = sorted(enumerate(input), key=lambda x: x[1] - math.floor(x[1]))
    for _ in xrange(remain):
        output[it.pop()[0]] += 1
    return output

def roundNum(input):
    output=map(lambda x: math.floor(x), input)
    print output
    diff=round(sum(input))-sum(output)
    rd=sorted(enumerate(input), key=lambda x: x[1]-math.floor(x[1]))

    for i in range(int(diff)):
        output[rd.pop()[0]]+=1

    return output




s=[30.3, 2.4, 3.5]

rst=roundNum(s)
print rst

