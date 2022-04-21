import QLSP_DATAA as spd
def hien_thi_sp():
    if len(spd.ds_sp)==0:
        print("Không có sản phẩm nào!")
    else:
        for i in range(len(spd.ds_sp)):
            print(i+1,spd.ds_sp[i])
def them_sp():
    while True:
        ma = input("Nhập mã sản phẩm: ")
        tim= find(ma)
        if tim == False:
            break
        else:
            print("Mã sản phẩm đã tồn tại, vui lòng nhập mã khác!")
    ten=input("Nhập tên sản phẩm: ")
    while True:
        gia = str(input("Nhập giá thành của sản phẩm: "))
        if gia.isdigit():
            gia = int(gia)
            break
        else:
            print("Giá thành cần là một số, mời nhập lại")
    hang=input("Nhập tên hãng sản xuất:")
    thong_tin={'Mã sản phẩm: ': ma,'Tên sản phẩm: ':ten,'Giá thành: ':gia, 'Hãng sản xuất: ':hang}
    spd.ds_sp.append(thong_tin)
def chinh_sua_tt():
    n = input("Nhập mã sản phẩm bạn muốn chỉnh sửa:")
    tim_kiem=find(n)
    if tim_kiem==False:
        print("Không tìm thấy mã sản phẩm trong danh sách sản phẩm")
    else:
        print("Bạn muốn chỉnh sửa: \n 1.Tên sản phẩm \n 2. Giá thành  \n 3.Hãng sảng xuất")
        op=int(input("Nhập vào số thứ tự của chức năng muốn thực hiện: "))
        if op==1:
            tenmoi=input("Nhập tên sản phẩm mới: ")
            spd.ds_sp[tim_kiem['vitri']]["Tên sản phẩm: "]=tenmoi
            print("Đã cập nhật thành công")
        if op==2:
            while True:
                new_prc = str(input("Nhập giá thành mới của sản phẩm: "))
                if new_prc.isdigit():
                    new_prc = int(new_prc)
                    break
                else:
                    print("Giá thành cần là một số, mời nhập lại")
            spd.ds_sp[tim_kiem['vitri']]["Giá thành: "]=new_prc
            print("Đã cập nhật thành công")
        if op==3:
            new_brd=input("Nhập hãng sản xuất mới:")
            spd.ds_sp[tim_kiem['vitri']]["Hãng sản xuất: "]=new_brd
            print("Đã cập nhật thành công")
def xoa_sp():
    if len(spd.ds_sp)==0:
        print("Không có sản phẩm nào để xóa !")
    else:
        n = int(input("Bạn muốn xóa bao nhiêu sản phẩm? "))
        for i in range(n):
            x = input("Bạn muốn xóa sản phẩm nào (theo mã):")
            xoa=find(x)
            if xoa == False:
                print("Không tìm thấy mã sản phẩm trong danh sách sản phẩm, không thể xóa!")
            else:
                spd.ds_sp.remove(xoa['giatri'])
                print("Đã xóa sản phẩm thành công.")
def find(masp):
    for i in range(len(spd.ds_sp)):
        if masp==spd.ds_sp[i]['Mã sản phẩm: ']:
            return {'vitri':i,'giatri':spd.ds_sp[i]}
    return False


