def nhap_vao():
 chuoi=input("Nhập vào: ")
 return chuoi

"""Hàm kiểm tra đối xứng (câu 1) """
def doi_xung(a):
 if a == a[::-1]:
   print(a, " là chuỗi đối xứng!")
 else : print("Chuỗi",a, "không đối xứng")

"""Hàm chuẩn hoá chuỗi (câu 2)"""
def chuan_hoa(n):
  a=n.split()
  b=" "
  return b.join(a)

"""Hàm xuất ra các số nguyên âm trong chuỗi ( câu 3 )"""
def NegativeNumberInStrings(str):
    so_am=[]
    i = 0
    flag=0
    while i + 1 < len(str):
        if str[i] == '-' and str[i + 1].isdigit():
            so = ''
            while i + 1 < len(str) and str[i + 1].isdigit():
                so += str[i + 1]
                i += 1
                flag=1
            else:
                so_am += [-int(so)]
                flag=1
        i += 1
    if flag!=1:
         print("Không có số nguyên âm trong chuỗi!")
    return so_am

"""Hàm xử lý trả về tên và phần mở rộng của tập tin (Câu 4)"""
def xuli_taptin(duong_dan):
    Mo_rong=''
    Ten = ''
    Ten+=duong_dan[duong_dan.rfind("\\")+1:duong_dan.rfind(".")]
    Mo_rong+=duong_dan[duong_dan.rfind(".")+1:]
    return f"Tên tập tin là: {Ten}", f"Phần mở rộng: {Mo_rong}"

"""Hàm kiểm tra địa chỉ email hợp lệ (Câu 5)"""
def kiemtra_email(email):
    if email.isascii():
        tach_ky_tu= []
        for i in email:
            tach_ky_tu.append(i)
        if tach_ky_tu[0].isalnum() and tach_ky_tu[-1].isalpha():
            email=''.join(tach_ky_tu)
            if email.count('@')==1:
                if email.rfind('.') and email.find(" ")<=0 :
                    print("Email hợp lệ!") #Em chưa tìm ra cách loại bỏ các ký tự đặc biệt trong username
                    domain_name = ''
                    username= ''
                    username+= email[0:email.rfind('@')]
                    domain_name += email[email.rfind("@") + 1:]
                    return f"Tên người dùng: {username}", f"Tên miền : {domain_name}"
    else:
        print("Email không hợp lệ!!!")

""" Hàm tách họ, tên đệm và tên (Câu 6)"""
def tach_ten(ten):
    ho_va_ten=ten.split()
    print("Họ:",ho_va_ten[0])
    print("Tên đệm:"," ".join(ho_va_ten[1:-1]))
    print("Tên:" , ho_va_ten[-1])

"""Hàm đảo ngược các từ trong chuỗi (Câu 7)"""
def dao_chuoi(chuoi):
 a=chuoi.split()
 b=""
 for i in range(len(a)-1,-1,-1):
     b+=a[i]+" "
 return b
