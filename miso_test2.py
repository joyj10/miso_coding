# n1 = input("enter Number(Korean) 1 =>  ")
# n2 = input("enter Number(Korean) 2 =>  ")

n1_kor = "십삼억오천칠백육십사만삼천이백팔십구"
n2_kor = "천삼백육"


def kor_number_sum(num_kor):
    numKor_List = ['일','이','삼','사','오','육','칠','팔','구']
    num_List = list(range(1,10))

    numIndexKor_List = ['십','백','천','만','억']
    numIndex_List = [10,100,1000,10000,100000000]

    if num_kor[0] in numIndexKor_List:
        num_kor = "일" + num_kor

    n1_int = 0
    n_index= 1
    index=1
    cnt = 0
    for i in range(len(num_kor)-1,-1,-1):

        if cnt==0 and num_kor[i] not in numIndexKor_List:
            r = numKor_List.index(num_kor[i])
            n1_int = num_List[r]

        if num_kor[i] in numIndexKor_List:
            num = 1
            if num_kor[i] == '만':
                n_index=10000
                index = n_index
            elif num_kor[i] == '억':
                n_index = 100000000
                index = n_index
            else:
                r = numIndexKor_List.index(num_kor[i])
                index = n_index * numIndex_List[r]

            if num_kor[i-1] not in numIndexKor_List:
                r = numKor_List.index(num_kor[i-1])
                num = num_List[r]
            n1_int += num * index
        cnt += 1
    return n1_int


n1_int = kor_number_sum(n1_kor)
n2_int = kor_number_sum(n2_kor)
re = n1_int+n2_int

print("Number 1 : ",n1_kor)
print("Number 2 : ",n2_kor)
print("*result : ",re)
