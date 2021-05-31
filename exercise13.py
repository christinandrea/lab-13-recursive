#Christina Andrea Putri - Universitas Kristen Duta Wacana

#Ami ingin mengetahui rangkaian fibonacci berdasarkan nilai yang ia beri. 
#Bagaimana rangkaian fibonacci yang terbentuk jika nilainya adalah 10?

#Input : nilai 
#Proses : fungsi akan menghitung sampai n yang dimaksud
#Output : rangkaian angka fibonacci

def fib(val):

    if val<0 :
        print("Error")
    elif val == 0 :
        return 0
    elif val == 1 :
        return 1 
    else :
        return fib(val-1)+fib(val-2)

try :
    inp = int(input("Nilai: "))
    print("Rangkaian Angka Fibonacci :")
    for i in range(inp):
        print(fib(i))

except:
    print("Terjadi kesalahan dalam proses rekursif. Silahkan coba lagi. ")



