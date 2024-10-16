## 1

nilaiavg = float (input ("berapa nilai mtk kamu?"))

if nilaiavg >= 90:
    print ("Excellent")
elif nilaiavg>= 80:
    print ("Very Good")
elif nilaiavg>= 70:
    print ("Good")
elif nilaiavg >= 60:
    print ("Skip2")
else:
    print ("ga naik kelas kamu")



## 2


def scterbesar (a,b,c):
    if a >= b and a>= c:
        return  a
    elif b >= c and b>= a:
        return b
    else:
        return c

a = int (input ("nilai 1 = "))
b = int (input ("nilai 2 = "))
c = int (input  ("nilai 3 = "))

terbesar = scterbesar (a,b,c)

print(f"bilangan terbesar adalah:{terbesar}")



## 3



def fibonaci(n):
    a, b = 0, 1
    while a <= n:
        print (a, end="")
        a,b = b, a + b
    print()
               
n = int (input("masukkan beberapa angka :"))
print(f"deret fibbonaci {n}:")
fibonaci(n)






## 4



def ganjil(n):
    for i in range (1, n + 1, 2):
        print (i, end=" ")
    print()
    
n = int(input("masukan angka:"))
print (f"angka ganjil {n}:")
ganjil(n)






## 5


def Nomor2(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)
        
n = int(input("Masukkan nilai n: "))
Nomor2(n)

