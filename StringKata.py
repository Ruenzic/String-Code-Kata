def test():
    assert(add("") == 0)
    assert(add("5") == 5)
    assert(add("1,2") == 3)
    assert(add("1\n2") == 3)
    assert(add("//*\n1*2") == 3)
    try:
        add("-1,-2")
    except ValueError as e:
        assert(str(e) == "negatives not supported -1, -2")

    assert(add("1001,5") == 5)
    try:
        add("-1001,-2")
    except ValueError as e:
        assert(str(e) == "negatives not supported -1001, -2")

    assert(add("//[***]\n1***2") == 3)
    assert(add("//[*][;]\n1*2;3") == 6)
    assert(add("//[***][;;]\n1***2;;3") == 6)
    assert(add("//[***][;;][%]\n1***2;;3%1") == 7)


    print("all tests passed")



def add(numberString):
    if len(numberString) == 0: return 0
    else:
        temp = getDelims(numberString)
        delims = temp[0]
        numberString = temp[1]
        numbers = split(delims,numberString)
        return sum(numbers)


def getDelims(numberString):
    delims = []
    length = 0
    if numberString[0:2] == "//":
        if numberString[2] == "[":
            delim = ""
            record = False
            for i in range (0,len(numberString)):
                if numberString[i-1] == "[":
                    record = True
                elif numberString[i] == "]":
                    record = False
                if record:
                    delim += numberString[i]
                elif record == False and len(delim) != 0:
                    delims.append(delim)
                    length += len(delim)
                    delim = ""

            numberString = numberString[3 + 2*len(delims) + length:]
        else:
            delims.append(numberString[2])
            numberString = numberString[4:]
    else: delims.append(',')



    return [delims,numberString]



def split(delims,numberString):
    numbers = numberString.split('\n')
    for delim in delims:
        final = []
        for num in numbers:
            final += num.split(delim)
        numbers = final

    return numbers


def sum(numbers):
    total = 0
    negatives = []
    for num in numbers:
        if len(num) > 0:
            if num[0] == "-":
                negatives.append(num)
            elif int(num) < 1000:
                total += int(num)
    if len(negatives) == 0:
        return total
    else: raise ValueError("negatives not supported " + ', '.join(negatives))






test()