"""k214061745 - Lê Dương Thảo - BÀI TẬP CHUÕI"""
from funcs import *
print("1. Kiểm tra tính đối xứng của chuỗi")
print("2. Chuẩn hóa chuỗi được nhập vào (các từ cách nhau bởi một khoảng trắng)")
print("3. Xuất ra các số nguyên âm trong chuỗi")
print("4. Trả về tên và phần mở rộng của tập tin")
print("5. Kiểm tra địa chỉ email hợp lệ, nếu hợp lệ trả về user_name và domain_name")
print("6. Tách họ, tên đệm và tên: ")
print("7. Đảo ngược các từ trong chuỗi")
print("Chọn 0 để thoát chương trình ")
print("-"*19)
while True:
 chon=int(input("Chọn lệnh để thực hiện :"))
 if chon==1:
  print("Kiểm tra tính đối xứng")
  doi_xung(nhap_vao())
 elif chon==2:
  print("Chuẩn hóa chuỗi")
  print("Chuỗi sau khi được chuẩn hóa:", chuan_hoa(nhap_vao()))
 elif chon==3:
  print("In ra số nguyên âm")
  print( NegativeNumberInStrings(nhap_vao()))
 elif chon==4:
  print("Trả về tên và phần mở rộng của tập tin")
  print(xuli_taptin(nhap_vao()))
 elif chon==5:
  print("Kiểm tra tính hợp lệ của Email và trả về username, domain_name nếu hợp lệ ")
  print(kiemtra_email(nhap_vao()))
 elif chon==6:
  print("Tách họ, tên đêm và tên ")
  tach_ten(nhap_vao())
 elif chon==7:
  print("Đảo ngược các từ: ")
  print("Chuỗi đảo ngược: ",dao_chuoi(nhap_vao()))
 else:
  break