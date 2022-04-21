""""K214061745 Lê Dương Thảo - Bài tập Collection"""""
"""Câu 5 + Câu 6"""

"""Nhập vào dãy số theo thứ tự tăng dần (Câu 5)"""

print("Nhập vào dãy số tăng dần")
cac_so = int(input("Bạn muốn nhập vào bao nhiêu số: "))
ds =[]
flag=0
i=0
while i+1 <=cac_so:
    so=input("Nhập số vào: ")
    if len(ds) == 0:
     if so.isdigit():
         ds.append(int(so))
         i+=1
     elif so.startswith('-') and so[1:].isdigit():
        ds.append(int(so))
        i +=1
    elif ds[i - 1] < int(so):
        ds.append(int(so))
        flag = 1
        i += 1
    elif not(so.isdigit()):
     print("Bạn nhập vào không phải số, hãy nhập lại")
    else:
        print("Số bạn vừa nhập nhỏ hơn hoặc bằng số trước đó, hãy nhập lại!")
if flag==1:
    print("Dãy số tăng dần bạn nhập vào là: ", ds)

"""Câu 6"""
"""Chương trình nhập vào n số thực và xuất ra dãy số theo thứ tự giảm dần"""

print("Nhập vào n số thực, sắp xếp, xuất dãy số theo thứ tự giảm dần")
ds_n_so=[]
n_so=int(input("Bạn muốn nhập bao nhiêu số:"))
while len(ds_n_so)+1<= n_so:
 so=input("Nhập số vào: ")
 if so.isdigit():
    so=int(so)
    ds_n_so.append(so)
 else:
    print("Bạn nhập không phải là số, hãy nhập lại")
for i in range (0,len(ds_n_so)):
    for k in range(i+1,len(ds_n_so)):
        if ds_n_so[i]<ds_n_so[k]:
            thu_tu=ds_n_so[k]
            ds_n_so[k]=ds_n_so[i]
            ds_n_so[i]=thu_tu
print("Dãy số bạn nhập được xếp theo thứ tự giảm dần là: ", ds_n_so)