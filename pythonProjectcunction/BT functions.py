"""K214061745_Lê Dương Thảo Bài tập FUnctions"""""

from cac_ham import *
print("1. Kiểm tra kiểm tra năm nhuận")
print("2. Chuyển đổi năm dương lịch sang âm lịch")
print("3. Kiểm tra một số có phải là số nguyên tố, số chính phương")
print("4. Tính tổng của n số hạng (đệ quy và khử để quy)")
print("5. Tìm ước số chung lớn nhất của 2 số ( đệ quy và khử đệ quy)")
print("6. Tính biểu thức tổng x^(2*n) khử đệ quy và đệ quy")
print("7. Tính biểu thức tổng 1/(n!) khử đệ quy và đệ quy")
print("8. Tính chỉnh hợp, tổ hợp chập k của n phần tử")
print("9. Giải phương trình bậc 2 ( (a^2)*x + b*x +c )")
print("10. Tính chỉ số BMI của một người")
print("11. Tính tổng ước số để kiểm tra số hoàn thiện và số thịnh vượng")
print("Chọn 0 để thoát chương trình ")
print("-"*19)
while True:
 chon=int(input("Chọn lệnh để thực hiện :"))
 if chon==1:
     print("Kiểm tra năm nhuận")
     print(nam_nhuan(int(input("Nhập năm muốn kiểm tra:"))))
 if chon==2:
     print("Chuyển đổi năm dương lịch sang âm lịch")
     year=int(input("Nhập năm muốn chuyển đổi"))
     print(f"Năm {year} là năm {can_chi(year)}")
 if chon==3:
     print("Kiểm tra số nguyên tố")
     print(so_ngto(int(input("Nhập số muốn kiểm tra: "))))
     print("kiểm tra số chính phương")
     print(chinh_phuong(int(input("Nhập số muốn kiểm tra: "))))
 if chon==4:
     print("Tính tổng của n số hạng (khử để quy)")
     print("Kết quả là:", tinh_tong(int(input("Nhập n: "))))
     print("Tính tổng của n số hạng (đệ quy):")
     print("Kết quả là",tong_dequy(int(input("Nhập n: "))))
 if chon==5:
     print("Tìm ước số chung lớn nhất của 2 ")
     a=int(input("Nhập số a:"))
     b=int(input("Nhập số b:"))
     print(f"USCLN của hai số{a,b} là:",uscln(a,b))
     print(f"USCLN (đệ quy)của hai số{a, b} là:", uscln_dequy(a, b))
 if chon==6:
     print("Tính biểu thức tổng x^(2*n)")
     x=int(input("Nhập số x:"))
     n=int(input("Nhập số n:"))
     print("Tổng =",bieu_thuc(x,n))
     print("Tổng (đệ quy)=", bt_dequy(x, n))
 if chon==7:
     print("Tính biểu thức tổng 1/(n!) ")
     n=int(input("Nhập số n:"))
     print("Tổng là ",tinh_bt(n))
     print("Tổng (đệ quy) là ", tinh_bt_dequy(n))
 if chon==8:
     print("Tính chỉnh hợp và tổ hợp chập k của n phần tử")
     n = int(input("Nhập số n:"))
     k = int(input("Nhập số k:"))
     print(f"Chỉnh hợp chập{k} của {n} phần tử là ", chinh_hop(n,k))
     print(f"Tổ hợp chập{k} của {n} phần tử là ", to_hop(n,k))

 if chon==9:
     print("Giải phương trình bậc 2 ")
     a=int(input("Nhập hệ số bậc 2 a:"))
     b=int(input("Nhập số bậc 1 b:"))
     c=int(input("Nhập số tự do c:"))
     print(pt_bac2(a,b,c))
 if chon==10:
     print("Tính chỉ số BMI của một người")
     cao=int(input("Nhập chiều cao (cm): "))
     nang=int(input("Nhập cân nặng (kg): "))
     print(BMI(cao,nang))
 if chon==11:
     print("Kiểm tra số hoàn thiện và số thịnh vượng  ")
     so_kt = int(input("Nhập số muốn kiểm tra:"))
     print(kt_so_hoan_thien(so_kt))
     print(kt_so_thinh_vuong(so_kt))
 if chon == 0:
     break