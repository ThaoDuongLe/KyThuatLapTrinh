"""K214061745_Lê Dương Thảo Bài tập Functions"""""

"""Hàm kiếm tra năm nhuận"""
def nam_nhuan(y):
    if y % 400==0 or (y % 4 ==0 and y % 100!=0):
        return f"Năm {y} là năm nhuận!"
    else:
        return f"Năm {y} không phải năm nhuận!"

"""Hàm chuyển đổi năm dương lịch sang âm lịch"""
def can_chi(nam):
    can=['Canh','Tân','Nhâm','Qúy','Giáp','Ất','Bính','Đinh','Mậu','Kỷ']
    chi=['Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi']
    for i in range(len(can)):
     if nam % 10 == i:
        for j in range(len(chi)):
            if nam % 12 ==j:
                return  can[i] + " " + chi[j]

"""Hàm kiểm tra số nguyên tố"""
import math
def so_ngto(n):
    x=0
    for i in range(1, n + 1):
        if n % i == 0:
            x+=1
    if x==2:
        return f"{n} là số nguyên tố"
    return f"{n} không là số nguyên tố"

"""Hàm kiểm tra số chính phương"""
def chinh_phuong(x):
    flag =0
    for i in range(x):
     if (x==i*i):
         flag=1
    if (flag==1):
        return f"{x} là số chính phương"
    else:
        return f"{x} không là số chính phương"

"""Hàm tính tổng số hạng """
def tinh_tong(n):
    s=0
    for i in range(n+1):
        s=s+i
    return s

def tong_dequy(n):
    if n==0:
        return 0
    else:
        return n+tong_dequy(n-1)

"""Hàm tìm ước số chung lớn nhất của hai số """
def uscln(a,b):
    while a * b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
def uscln_dequy(a, b):
    if (b == 0):
        return a
    return uscln_dequy(b, a % b)

"""Hàm tính biểu thức S(x,n)=x^2+x^4+....+x^2n"""
def bieu_thuc(x,n):
    S=0
    for i in range(1,n+1):
        S+=x**(2*i)
    return S
def bt_dequy(x,n):
    if n==0:
        return 1
    elif x==0:
        return 0
    else: return x**(2*n)+bt_dequy(x,n-1)

"""Hàm tính biểu thức S(n)=1 +1/(1+2)+1/(1+2+3)+...+1/(1+2+3+...+n)"""
def tong_n_so(so):
    s=0
    for i in range(1,so+1):
        s+=i
    return s

def tinh_bt(n):
    s=1
    for i in range(2,n+1):
     s+=1/(tong_n_so(i))
    return s
def tinh_bt_dequy(n):
    if n == 1:
        return 1
    else: return (1 / tong_n_so(n) + tinh_bt_dequy( n - 1))

"""Hàm tính chỉnh hợp, tổ hợp chập k của n phần tử"""
def giai_thua(n):
    if n==1:
      return 1
    else: return n*giai_thua(n-1)

"""Hàm tính tổ hợp"""
def to_hop(n,k):
   if k==0:
        return 1
   else:
        C=(giai_thua(n))/((giai_thua(k)*giai_thua(n-k)))
   return C

""" Hàm tính chỉnh hợp"""
def chinh_hop(n,k):
    if k==0:
        return 1
    else:
        A=giai_thua(n)/(giai_thua(n-k))
    return A

""""Hàm giải phương trình bậc 2 ax^x + b +c=0"""""
def tinh_delta(a,b,c):
    delta= b**2-(4*a*c)
    return delta
def pt_bac2(a,b,c):
    
    if a==0:
        if b==0:
            print("Phương trình vô nghiệm")
        else:
            return "Phương trình có một nghiệm x =  ",-c/b
    else:
        if tinh_delta(a,b,c)>0:
            x1=(-b+math.sqrt(tinh_delta(a,b,c)))/(2*a)
            x2=(-b-math.sqrt(tinh_delta(a,b,c)))/(2*a)
            return f"Phương trình có hai nghiệm phân biệt: x1= {x1} và x2= {x2}"
        elif tinh_delta(a,b,c)==0:
            return 'Phương trình có nghiệm kép x1=x2= ',-b/(2*a)
        else:
            return "Phương trình vô nghiệm"

"""Hàm tính chỉ số BMI"""
def BMI(h,w):
    BMI=w/(h*h)*10000
    if BMI < 18.5:
        return "Tình trạng cân nặng của bạn là gầy"
    elif BMI>=18.5 and BMI <25:
        return "Tình trạng cân nặng của bạn là bình thường"
    elif BMI>=25 and BMI <30:
        return "Tình trạng cân nặng của bạn là mập"
    elif BMI>= 30:
        return "Tình trạng cân nặng của bạn là béo phì "

"""Hàm tổng ước số"""
def tong_uoc_so(n):
    s=0
    for i in range(1,n):
        if n % i==0:
         s+=i
    return s
def kt_so_hoan_thien(num):
    if tong_uoc_so(num) == num:
        return num,'là số hoàn thiện'
    else: return num,' không phải số hoàn thiện'
def kt_so_thinh_vuong(num):
    if tong_uoc_so(num) > num:
        return num,'là số thịnh vượng'
    else: return num,'không phải số thịnh vượng'