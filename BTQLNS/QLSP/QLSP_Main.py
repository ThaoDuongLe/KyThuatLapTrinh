import QLSP_Process as ssp
chon=1
while chon!= 5:
    print("_"*18)
    print("1.Thêm sản phẩm")
    print("2.Hiện thị danh sách sản phẩm")
    print("3.Cập nhật thông tin")
    print("4.Xóa sản phẩm")
    print("5.Thoát chương trình")
    print("_"*23)
    chon=int(input("Mời bạn chọn tính năng: "))
    if chon==1:
        ssp.them_sp()
    elif chon==2:
        ssp.hien_thi_sp()
    elif chon==3:
        ssp.chinh_sua_tt()
    elif chon==4:
        ssp.xoa_sp()
    else:
        break