"""" K214061745 Lê Dương Thảo - Bài tập Collection"""""
""""Câu 4 """
"""Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU"""
ds=[]
N=int(input("Bạn muốn nhập vào bao nhiêu số: "))
for i in range(N):
    flag=0
    while flag==0:
        so=input("Nhập số vào: ")
        if so.isdigit():
            so=int(so)
            if len(ds)>0:
                for j in ds:
                    if so!=j:
                        flag=1
                    else:
                        print("Số bạn nhập vào bị trùng, hãy nhập lại !")
                        flag=0
                if flag==1:
                    ds.append(so)
            else:
                ds.append(so)
                flag=1
        else:
            print("Bạn nhập vào không phải là số, hãy nhập lại !")
            flag=0
print(f"list {N} số bạn nhập vào (không trùng nhau) là {ds}")
