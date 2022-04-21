""" K214061745 Lê Dương Thảo - Bài tập Collection"""""
""" Câu 2 """

"""Khởi tạo ngẫu nhiên """
sl_pt=int(input("Bạn muốn nhập vào bao nhiêu phần tử : "))
ds = []
while len(ds)+1<=sl_pt:
     so=input("Nhập vào : ")
     ds.append(so)


"""Nhập số k, xóa tất cả các phần tử có giá trị k tồn tại trong list """

ds=[]
while True :
    k = input("Nhập số k vào: ")
    if k.isdigit():
        ds.append(int(k))
        break
    elif k.startswith('-') and k[1:].isdigit():
        ds.append(int(k))
        break
    else:
     print("Bạn nhập vào không phải số, hãy nhập lại")
new_ds=[]
for i in ds:
    print(i)
    if k==i :
        ds.pop(ds.index(i))
print(f"list sau khi xóa phần tử k={k} là: {ds}")

""" Kiểm tra list có đối xứng hay không """
if ds == ds[::-1]:
    print(ds, " là chuỗi đối xứng!")
else:
    print("Chuỗi", ds, "không đối xứng")
