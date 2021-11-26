import copy

def check(a):
    if a == [[]]:
        return (0,0)
    l = len(a[0])
    for i in a:
        if len(i) != l:
            return -1
    return (len(a), l)

def check_s(a):
    if a ==[[]]:
        return 0
    l = len(a)
    for i in a:
        if len(i) != l:
            return -1
    return l

def addtion(a, b):
    global ans
    if check(a) == -1 or check(b) == -1:
        return None
    if check(a) != check(b):
        return None
    temp = addtion_p(a,b)
    save_his(copy.deepcopy(a), copy.deepcopy(b), copy.deepcopy(temp), "addtion")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp

def addtion_p(a,b):
    adt = [len(a[0])*[0]for i in range(len(a))]
    for i in range(len(a)):
        for j in range((len(a[0]))):
           adt[i][j] = a[i][j] + b[i][j]
    return adt

def subtraction(a, b):
    global ans
    if check(a) == -1 or check(b) == -1:
        return None
    if check(a) != check(b):
        return None
    temp = subtraction_p(a,b)
    save_his(copy.deepcopy(a), copy.deepcopy(b), copy.deepcopy(temp), "subtraction")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp

def subtraction_p(a, b):
    sub = [len(a[0])*[0]for i in range(len(a))]
    for i in range(len(a)):
        for j in range((len(a[0]))):
           sub[i][j] = a[i][j] - b[i][j]
    return sub

def multiple(a, b):
    global ans
    if type(a) == int or type(a) == float:
        if check(b) == -1:
            return None
        temp = multiple_p(a, b)
    elif type(b) == int or type(b) == float:
        if check(a) == - 1:
            return None
        temp = multiple_p(b, a)
    else:
        if check(a) == - 1 or check(b) == - 1:
            return None
        if check(a)[1] != check(b)[0] :
            return None
        temp = multiple_p(a, b )
    save_his(copy.deepcopy(a), copy.deepcopy(b), copy.deepcopy(temp), "multiple")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
def multiple_p(a, b) :
    if type(a) == int or type(b) == float:
        res = [len(b[0])*[0]for i in range(len(b))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = b[i][j] * a
    else:
        res = [len(b[0])*[0] for i in range(len(a))]
        for i in range(len(res)):
            for j in range(len(res[i])):
                for k in range(len(a[i])):
                    res[i][j] += a[i][k] * b[k][j]
    return res

def transposed(a):
    global ans
    if check(a) == -1:
        return None
    temp = transposed_p(a)
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "transposed")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
def transposed_p(a) :
    r = len(a)
    c = len(a[0])
    res = [[0 for r in range(r)]for _ in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][i] = a[i][j]
    return res

def minor(a, i, j):
    global ans
    if check(a) == -1:
        return None
    temp = minor_p(a, i - 1, j - 1)
    ans = copy.deepcopy(temp)
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "minor(" + str(i) + ", " + str(j) + ")")
    show(temp)
    return temp
def minor_p(a, i, j):
    temp = []
    for k in a[:i] + a[i + 1:]: 
        temp.append(k[:j] + k[j + 1:])
    return temp

def det(a):
    global ans
    if check_s(a) == -1:
        return None
    temp = det_p(a)
    save_his(copy.deepcopy(a), None, temp, "det")
    ans = temp
    print(temp)
    return temp
def det_p(a):
    if a == [[]]:
        return 1
    if check_s(a) == 1:
        return a[0][0]
    if len(a) == 2:
        return a[0][0]*a[1][1] - (a[1][0] * a[0][1])
    length = len(a) 
    temp = a[1:]
    res = 0
    count = 1
    for i in range(length):
        temp_2 = []
        for j in range(length - 1):
            temp_2.append(temp[j][:i] + temp[j][i + 1:])
        res += count * a[0][i] * det_p(temp_2)
        count *= -1
    return res

def cofactor(a):
    global ans
    if check_s(a) == -1:
        return None
    temp = cofactor_p(a)
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "cofactor")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
def cofactor_p(a):
    res = []
    length = len(a)
    for i in range(length):
        temp = []
        temp_1 = a[:i] + a[i + 1:]
        for j in range(length):
            temp_2 = []
            for k in range(length - 1):
                temp_2.append(temp_1[k][:j] + temp_1[k][j + 1:])
            temp.append(pow(-1, i + j) * det_p(temp_2))
        res.append(temp)
    return res

def adjoint(a):
    global ans
    if check_s(a) == -1:
        return None
    temp = adjoint_p(a)
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "adoint")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
def adjoint_p(a):
    temp = transposed_p(cofactor_p(a))
    return temp

def inverse(a):
    global ans
    if check_s(a) == -1:
        return None
    temp = inverse_p(a)
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "inverse")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
def inverse_p(a):
    temp = multiple_p(1 / det_p(a), adjoint_p(a))
    return temp

ans = None
his = []

def show(a):
    for i in a:
        for j in i:
            print("%.2f" %j , end = "  ")
        print()

def save_his(a, b, r, k):
    global his
    if b == None: 
        dic1 = {"a" : a, "res" : r, "k" : k} 
    else:
        dic1 = {"a" : a, "b" : b, "res" : r, "k" : k} 
    his.insert(0, dic1)
    if(len(his) == 11):
        his.pop(10)

def show_his():
    global his
    for i in range(len(his)):
        print(i + 1,"번째:")
        print("a : ", end = "") 
        if type(his[i]["a"]) == list:
            print()
            show(his[i]["a"])
        else:
            print(i["a"])
        if len(his[i]) == 4:
            print("b : ", end = "")
            if type(his[i]["b"]) == list:
                print()
                show(his[i]["b"])
            else:
                print(his[i]["b"])
        print("res : ", end = "")
        if type(his[i]["res"]) == list:
            print()
            show(his[i]["res"])
        else:
            print(his[i]["res"])
        print("계산 : " + his[i]["k"])
        print()
