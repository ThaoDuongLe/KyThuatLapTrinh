""" K214061745 Lê Dương Thảo - Bài tập Collection"""""
""" Câu 1 """

"""Khới tạo List"""
list = []

"""Thêm phần tử vào list"""
so_phan_tu=0
while True:
    k= input("Nhập phần tử vào ( nếu muốn dừng nhập hãy nhập 'kt') :")
    if k=='kt':
        break
    list.append(k)

"""Nhập k, kiểm tra số lần k xuất hiện trong list"""
kiem_tra=input("Nhập phần tử muốn kiểm tra số lần xuất hiện: ")
for i in range(len(list)-1):

    if kiem_tra==list[i]:
        so_phan_tu+=1
print(f"Số lần xuất hiện của {kiem_tra} trong list là {so_phan_tu}")

"""Tính tổng số nguyên tố trong list"""
so_ng_to=[]
tong_snt=0
def so_ngto(n):
    j = 0

    for i in range(1, n + 1):
        if n % i == 0:
            j += 1
    if j == 2:
        return True
    return False
for i in range (len(list)):

    if list[i].isdigit() and not (list[i].startswith('-') ):
       list[i]=int(list[i])

       if so_ngto(list[i])==True :
           so_ng_to.append(list[i])

if len(so_ng_to)==0:
    print("Không có số nguyên tố trong list đã nhập")
else:

    for i in range (len(so_ng_to)):
        tong_snt+=so_ng_to[i]
    print(f"Tổng {len(so_ng_to)} số nguyên tố :{so_ng_to} bạn đã nhập là {tong_snt}")

"""sắp xếp list"""
print("Sắp xếp các phần tử là số/ chữ(chữ cái) ( vd: (1,2,3) hoặc (d,s, một, hai))")
so=[]
chu=[]
so_chu=[]
flag=0
for i in range (len(list)):
   if i<(len(list))and (list[i].startswith('-') and list[i].isalnum()):
        flag=1

        if list[i].isdigit() :
            so.append(int(list[i]))
        if list[i].startswith('-') and list[i].isdigit():
            so.append(int(list[i]))
        elif list[i].isalpha():
            chu.append(list[i])
if flag==1:
    print(f"Sắp xếp các số giảm dần: {sorted(so,reverse=True)}")
    print(f"Sắp xếp các số tăng dần: {sorted(so,reverse=False)}")
    print(f"(Theo chữ cái đầu của phần tử)\nSắp xếp các chữ giảm dần: {sorted(chu,reverse=True)}")
    print(f"Sắp xếp các chữ tăng dần : {sorted(chu,reverse=False)}")
else:
 print("Hãy chắc chắn tất cả phần tử bạn nhập vào là số/chữ hoặc số và chữ")

"""Xóa list """
del(list)
print(list)
