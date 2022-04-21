class NhanVien:
    ds_nv=[]
    def __init__(self,manv,hoten,sdt):
        self.manv=manv
        self.ten=hoten
        self.dt=sdt
        NhanVien.ds_nv.append(self)
    def lay_tt(self):
        return print("Nhân viên:" + str(self.manv)+" - "+self.ten + "- Số điện thoại: "+str(self.dt))
    #them nhan vien
    # @classmethod
    # def add_nv(cls,nv):
    #     cls.ds_nv.append(nv)
    @classmethod
    def hien_thi(cls):
        for nv in cls.ds_nv:
            if len(cls.ds_nv)==0:
                print("Không có nhân viên nào trong danh sách!")
                break
            else:
             print(nv.lay_tt())

  # định dạng hiển thị ds
  #   def __repr__(self):
  #       return f"Nhân viên{self.manv} : {self.ten} - Số diện thoại:{self.dt}"
  #   @classmethod
  #   def hien_thi2(cls):
  #       if len(cls.ds_nv)==0:
  #           return "Danh sách rỗng!"
  #       else:
  #           return("dsnv", cls.ds_nv)
    @staticmethod
    def nhaptt():
        while True:
            ma= input("Nhập mã nv: ")
            tim= NhanVien.kiem_tra(ma)
            if tim != -1:
                print("Mã nhân viên đã tồn tại")
            else:
                break
        ten=input("Nhập tên nv: ")
        while True:
            sdt = str(input("Nhập số điện thoại nhân viên: "))
            if sdt.isdigit():
                sdt = int(sdt)
                break
            else:
                print("Số điện thoại phải là một dãy số, mời nhập lại")
        return NhanVien(ma,ten,sdt)
    #kiểm tra trùng lặp
    @classmethod
    def kiem_tra(cls, ma):
        for i in range(len(cls.ds_nv)):
            if cls.ds_nv[i].manv == ma:
                return {'indx': i, 'val': cls.ds_nv[i]}
        return -1
    @classmethod
    def xoa_nv(cls):
        ma=input("Nhập mã nhân viên cần xoá: ")
        tim=cls.kiem_tra(ma)
        if tim!= -1: # để xoá được cần biết vị trí index và thông tin của phần tử trong ds
            cls.ds_nv.remove(tim['val'])
            print("Xoá thành công")
        else:
            print("Không tìm thấy nhân viên, không thể xoá được")
    @classmethod
    def cap_nhat(self):
        ma=input("Nhập mã cần cập nhật")
        tim=NhanVien.kiem_tra(ma)
        if tim ==-1:
            print("Không tìm thấy nhân viên trong danh sách")

        else:
            if input("Cập nhật họ tên? (y/n?)") =='y':
                ten=input("nhập tên khác")
                NhanVien.ds_nv[tim['indx']].ten=ten
                print("Đã cập nhật thành công")
            if input("Cập nhật số điện thoại? (y/n?)")=='y':
                while True:
                    sdt = str(input("Nhập số điện thoại nhân viên: "))
                    if sdt.isdigit():
                        sdt = int(sdt)
                        NhanVien.ds_nv[tim['indx']].dt=sdt
                        print("Đã cập nhật thành công")
                        break
                    else:
                        print("Số điện thoại phải là một dãy số, mời nhập lại")
# nv1=NhanVien("Nv01","BOZHAN","095959595")
# nv2=NhanVien("Nv02","YIZHAN","018231823")
# print(nv1.__dict__)
# print(nv1.lay_tt())
# print("ds nv:",NhanVien.ds_nv)





