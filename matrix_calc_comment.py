import copy # 리스트의 복사를 위해서 copy.deepcopy()를 사용했습니다.

#ㅡㅡㅡㅡㅡ계산 함수ㅡㅡㅡㅡㅡ

# 1. check 함수(행렬의 형태를 갖추고 있는지 확인하는 함수)
def check(a):
    if a == [[]]:
        return (0,0)
    l = len(a[0])
    for i in a:
        if len(i) != l:
            return -1 # 행렬의 형태를 갖추고 있지 않다면 -1을 반환
    return (len(a), l) # 갖추고 있다면 행의 수와 열의 수를 튜플로 반환

# 2. check_s 함수(정방 행렬의 형태를 갖추고 있는지 확인하는 함수)
def check_s(a):
    if a ==[[]]:
        return 0
    l = len(a)
    for i in a:
        if len(i) != l:
            return -1 # 정방 행렬의 형채를 갖추고 있지 않다면 -1을 반환
    return l # 갖추고 있다면 행의 수 반환

#계산하는 함수는 호출 함수와 계산 함수 둘로 나누어 만들었습니다.

# 3-1. addtion 함수(addtion_p 함수를 호출하는 함수로  사용자가  쉘 모드에서 직접 호출하는 함수)
def addtion(a, b):
    global ans # 전역변수 ans
    if check(a) == -1 or check(b) == -1: # 행렬 확인
        return None
    if check(a) != check(b): # 행렬의 행의 수와 열의 수가 다르면,
        return None # return None
    temp = addtion_p(a,b) # addtion_p(a, b) 호출
    save_his(copy.deepcopy(a), copy.deepcopy(b), copy.deepcopy(temp), "addtion") # his에 계산 정보 저장
    ans = copy.deepcopy(temp) # ans에 temp 저장
    show(temp) # 출력
    return temp # 반환
def addtion_p(a,b):
    adt = [len(a[0])*[0]for i in range(len(a))] # adt라는 2차원 리스트 선언
    for i in range(len(a)):
        for j in range((len(a[0]))):
           adt[i][j] = a[i][j] + b[i][j] # adt에 더한 값을 저장
    return adt # 반환

# 4-1. subtraction 함수(subtraction_p 함수를 호출하는 함수로  사용자가  쉘 모드에서 직접 호출하는 함수)
def subtraction(a, b):
    global ans
    if check(a) == -1 or check(b) == -1: # 행렬 확인
        return None
    if check(a) != check(b): # 행렬의 행의 수와 열의 수가 다르면,
        return None # return None
    temp = subtraction_p(a,b) # subtraction_p(a, b) 호출
    #이하 동일
    save_his(copy.deepcopy(a), copy.deepcopy(b), copy.deepcopy(temp), "subtraction")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
def subtraction_p(a, b):
    sub = [len(a[0])*[0]for i in range(len(a))] # sub라는 2차원 리스트 선언
    for i in range(len(a)):
        for j in range((len(a[0]))):
           sub[i][j] = a[i][j] - b[i][j] # sub에 뺀 값을 저장
    return sub # 반환

# 5-1. multiple 함수(multiple_p 함수를 호출하는 함수로 사용자가 쉘 모드에서 직접 호출하는 함수)
def multiple(a, b):
    global ans
    if type(a) == int or type(a) == float: # a가 숫자라면,
        if check(b) == -1: # b를 확인한 후에,
            return None
        temp = multiple_p(a, b) # multiple__p(a, b)를 호출한다.
    elif type(b) == int or type(b) == float: # b가 숫자라면,
        if check(a) == - 1: # a를 확인한 후에,
            return None
        temp = multiple_p(b, a) # multiple_p(b, a)를 호출한다.
    else:
        if check(a) == - 1 or check(b) == - 1: # 둘 다 정수가 아니라면, a, b를 확인한 후에,
            return None
        if check(a)[1] != check(b)[0] :# a의 열과 b의 행을 확인하고, 
            return None
        temp = multiple_p(a, b )#multiple_p(a, b) 호출
    # 이하 동일
    save_his(copy.deepcopy(a), copy.deepcopy(b), copy.deepcopy(temp), "multiple")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
# 5-2. multiple_p 함수(함수의 곲을 계산 한 값을 반환하는 함수)
def multiple_p(a, b) :
    if type(a) == int or type(a) == float: #a가 숫자라면,
        res = [len(b[0])*[0]for i in range(len(b))] # res을 선언하고
        for i in range(len(res)): #각 행의
            for j in range(len(res[0])): #각 열의 값에
                res[i][j] = b[i][j] * a # a을 곱한 값을 res[i][j]에 저장한다.
    else: #a이 정수가 아니라면,
        res = [len(b[0])*[0] for i in range(len(a))] # res을 선언하고
        for i in range(len(res)):
            for j in range(len(res[i])):
                for k in range(len(a[i])):
                    res[i][j] += a[i][k] * b[k][j] # 각 행과 열에 맞는 값을
    return res # 결과 반환

# 6-1. transposed 함수(transposed_p 함수를 호출하는 함수로 사용자가 쉘 모드에서 직접 호출하는 함수)
def transposed(a):
    global ans
    if check(a) == -1: # 행렬 확인
        return None
    temp = transposed_p(a) # transposed_p(a) 호출
    #이하 동일
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "transposed")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
# 6-2. transposed_p 함수(전치 행렬을 반환하는 함수)
def transposed_p(a) :
    r = len(a) # 행의 길이 저장
    c = len(a[0]) # 열의 길이 저장
    res = [[0 for r in range(r)]for _ in range(c)] # c행 r열의 행렬 선언
    for i in range(r):
        for j in range(c):
            res[j][i] = a[i][j] # 반대되는 값을 저장
    return res # 반환

# 7-1. minor 함수(minor_p 함수를 호출하는 함수로 사용자가 쉘 모드에서 직접 호출하는 함수)
def minor(a, i, j):
    global ans
    if check(a) == -1: # 행렬 확인
        return None
    temp = minor_p(a, i - 1, j - 1) # minor_p(a, i - 1, j - 1) 호출
    #이하 동일
    ans = copy.deepcopy(temp)
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "minor(" + str(i) + ", " + str(j) + ")")
    show(temp)
    return temp
# 7-2. minor_p 함수(소행렬을 반환하는 함수)
def minor_p(a, i, j):
    temp = [] # temp 선언
    for k in a[:i] + a[i + 1:]: 
        temp.append(k[:j] + k[j + 1:]) # temp에 a에서 i 행 j 열을 제외한 부분 저장
    return temp # 반환

# 8-1. det 함수(det_p 함수를 호출하는 함수로 사용자가 쉘 모드에서 직접 호출하는 함수)
def det(a):
    global ans
    if check_s(a) == -1: # 정방 행렬 확인
        return None
    temp = det_p(a) # det_p(a) 호출
    #이하 동일
    save_his(copy.deepcopy(a), None, temp, "det")
    ans = temp
    print(temp)
    return temp
# 8-2. det_p 함수(행렬식을 계산하여 반환하는 함수)
def det_p(a):
    if a == [[]]: # a가 [[]] 이면,
        return 1 # 1 반환
    if check_s(a) == 1: # a의 크기가 1이면,
        return a[0][0] # 그 값 반환
    if len(a) == 2: # a의 길이가 2이면,
        return a[0][0]*a[1][1] - (a[1][0] * a[0][1]) # 값 반환
    # 밑 부분을 간단히 설명하면 a의 1행 1열을 이용해서 행렬식을 구하는 부분입니다.
    # 재귀호출로 들어가는 매개변수의 크기가 2가 될때까지 반복하며 행렬식을 구합니다.
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

# 9-1. cofactor 함수(cofactor_p 함수를 호출하는 함수로 사용자가 쉘 모드에서 직접 호출하는 함수)
def cofactor(a):
    global ans
    if check_s(a) == -1: # 정방 행렬 확인
        return None
    temp = cofactor_p(a) # cofactor_p(a) 호출
    # 이하 동일
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "cofactor")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
# 9-2. cofactor_p 함수(여인수 행렬을 계산하여 반환하는 함수)
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
            temp.append(pow(-1, i + j) * det_p(temp_2)) #간단히 각 소행렬의 행렬식과 적절한 값을 곱해서 여인자를 구해 저장
        res.append(temp)
    return res #반환

# 10-1. adj 함수(adjoint_p를 호출하는 함수로 사용자가 쉘 모드에서 직접 호출하는 함수)
def adjoint(a):
    global ans
    if check_s(a) == -1: # 정방 행렬 확인
        return None
    temp = adjoint_p(a) # adjoint_p(a) 호출
    # 이하 동일
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "adoint")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
# 10-2. adjoint_p 함수(수반 행렬을 반환하는 함수)
def adjoint_p(a):
    temp = transposed_p(cofactor_p(a)) # 수반 행렬은 여인수 행렬의 전치 행렬
    return temp # 호출

# 11-1. inverse 함수(inverse_p를 호출하는 함수로 사용자가 쉘 모드에서 직접 호출하는 함수)
def inverse(a):
    global ans
    if check_s(a) == -1: #a가 정방행렬이 아니라면 
        return None#None 반환
    temp = inverse_p(a) # inverse_p(a) 호출
    # 이하 동일
    save_his(copy.deepcopy(a), None, copy.deepcopy(temp), "inverse")
    ans = copy.deepcopy(temp)
    show(temp)
    return temp
# 11-2. inverse_p 함수(역함수를 반환하는 함수)
def inverse_p(a):
    temp = multiple_p(1 / det_p(a), adjoint_p(a)) # 역행렬은 수반행렬에 행렬식의 역함수를 곱한 것
    return temp # 반환

#ㅡㅡㅡㅡㅡ 부가기능ㅡㅡㅡㅡㅡ

# 1. 변수
ans = None # 가장 최근의 결과값을 저장하는 변수
his = [] # 최대 10개까지 의 계산 기록을 저장하는 리스트

# 2. show 함수(2차원 리스트를 보기 좋게 출력해주는 함수)
def show(a):
    for i in a:
        for j in i:
            print("%.2f" %j , end = "  ")
        print()

# 3. save_his 함수(his 리스트에 결과값을 저장해주는 함수)
def save_his(a, b, r, k):
    global his
    if b == None: 
        dic1 = {"a" : a, "res" : r, "k" : k} 
    else:
        dic1 = {"a" : a, "b" : b, "res" : r, "k" : k} # 피연산자, 결과, 연산의 종류를 딕셔너리의 형태로 리스트에 저장 
    his.insert(0, dic1)
    if(len(his) == 11): # 리스트의 길이가 11이 되면,
        his.pop(10)  # 마지막 인자 제거

# 4. show_his 함수(his 리스트의 값을 보기 좋게 출력한다.)
def show_his():
    global his
    for i in range(len(his)):
        print(i + 1,"번째:")
        print("a : ", end = "") 
        if type(his[i]["a"]) == list: # 값이 행렬이라면,
            print()
            show(his[i]["a"]) # 위의 show 함수를 이용해서 출력
        else: # 아니면
            print(i["a"]) # 그냥 출력.
        #이하 반복
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
