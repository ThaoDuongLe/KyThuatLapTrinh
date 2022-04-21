import process as p
print("-"*18)
print("1.Thêm nhân viên")
print("2.Xoá nhân viên")
print("3.Cập nhật thông tin nhân viên")
print("4.Hiển thị danh sách nhân viên")
print("5.Thoát chương trình")
chon=0
while chon!=5:
    print("-"*23)
    chon=int(input("Chọn chức năng số: "))
    if chon==1:
        p.NhanVien.nhaptt()
    if chon==2:
        p.NhanVien.xoa_nv()
    if chon==3:
        p.NhanVien.cap_nhat()
    if chon==4:
        p.NhanVien.hien_thi()
    if chon==5:
        print("Kết thúc chương trình")
        break