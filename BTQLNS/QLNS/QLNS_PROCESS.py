import QLNS.QLNS_DATA as nvd
def hien_thi():
    for i in range(len(nvd.Dsnv)):
        print(i,nvd.Dsnv[i])
def them_nv():
    ten=input("Nhập tên nhân viên: ")
    ma=input("Nhập mã nhân viên: ")
    sdt=input("Nhập số điện thoại nhân viên: ")
    thong_tin={'Mã nhân viên: ': ma,'Họ và tên nhân viên: ':ten,'Số điện thoại: ':sdt}
    nvd.Dsnv.append(thong_tin)
def chinh_sua_tt():
    pass
def xoa_nv(x):
    nvd.Dsnv.pop(x)
def tim_ma_nv(x,n):
    for i in n:
        if x==i:
            return
