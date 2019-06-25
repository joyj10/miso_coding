n1 = input("enter Number 1 =>  ")
n2 = input("enter Number 2 =>  ")


strNumList = list(range(0,10))

# str을 int로 변환하기 위한 함수
def convert_int(str_num):
    int_num = 0
    length_num = len(str_num)
    for i in range(length_num):
        for strN in strNumList :
            if str_num[i]== str(strN):
                int_num += strN*(10**(length_num-1))
        length_num -= 1
    return int_num

n1_int = convert_int(n1)
n2_int = convert_int(n2)

re = n1_int+n2_int
print("*result : ",re)