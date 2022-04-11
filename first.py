#simple operators
print(8//2)
print(2**3)
print(8%2)
print("*************")

#math metods
print(abs(-5)) #modul
print(round(6.5)) #cut edede teref yuvarlaq edir x.5 olanda, eks halda hara yaxinn olsa
print(round(12.76925,3)) #2 arg alanda 3 eded deqiqliyi ile yuvarlaq edir
print(divmod(17,3)) #17/3 ededini ve qaliqini qaytarir
print(pow(4,2))
print(max(4,10,7))
print(min("refiqe","ehmed","sekine",key=len))
a=[10,3,7,2,6,8]
print(sum(a))
print("**************")

#castle
print(int(3.5))
print(float(5))
print("******************")

#say sistemleri arasinda kecid
n=12
print(bin(n)[2:])
print(0b1100)
print(oct(n)[2:])
print(0o14)
print(hex(n)[2:])
print(0xc)
print("*********************")

#integer methodlari
b=13
print(b.bit_length())  #tam ededin yaddasda tutdugu bit sayisi
print((12).bit_length())
c=3.5
print(c.as_integer_ratio()) #c hansi 2 ededin bir birine bolunmesinden alinir?
print((12.0).is_integer())
print("****************")

#komplex ededler
k=24-5j
print(k.real," ",k.imag)
print(k.conjugate())  #qosma