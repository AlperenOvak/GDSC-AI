# girdi ve cikti listelerinii oluşturdum
girdi=[]
cikti=[]
for i in range(10):
    girdi.append(float(input(f"x için {i+1}. değeri giriniz:    ")))
    cikti.append(float(input(f"y için {i+1}. değeri giriniz:    ")))
# a ve b ve c tanımladım
# aynidogrulamax değişkenini ise tüm girdilerin aynı olup olmadığını kontrol etmek için kullanacağım
# hatalidenklem değişkenini x,y ikililerinin bir ax+b=y denklemini sağlayıp sağlamadığını kontrol etmek için kullanacağım
# aynidogrulamay değişkenini ise tüm çıktıların aynı olup olmadığını kontrol etmek için kullanacağım
a, b, c, aynidogrulamax, hatalidenklem, aynidogrulamay = None, None, None, False, False, False
# ax+b=y denkleminde a'nın değerini buldum
for i in range(10):
    if girdi[0]!=girdi[i]:
        a=(cikti[0]-cikti[i])/(girdi[0]-girdi[i])
        c=a
        break
# farklı x ve y değerleri bir ax+b=y denklemi sağlamıyorsa hatalıdenklem True olacaktır
for i in range(10):
    if girdi[0]!=girdi[i]:
        a=(cikti[0]-cikti[i])/(girdi[0]-girdi[i])
        if a!=c:
            hatalidenklem=True
# tüm girdiler aynı ise aynidogrulamax False olacaktır.
for i in range(10):
    if girdi[0]!=girdi[i]:
        aynidogrulamax=True
# tüm çıktılar aynı ise aynidogrulamay False olacaktır.
for i in range(10):
    if cikti[0]!=cikti[i]:
        aynidogrulamay=True
# bir x için farklı y'ler varsa hatalıdenklem True olacaktır.
for i in range(10):
    for z in range(10):
        if girdi[i]==girdi[z]:
            if cikti[i]!=cikti[z]:
                hatalidenklem=True
# son çıktıyı yazdırıyorum
print("a,b,x,y birer reel sayı olmak üzere:")
if aynidogrulamax==False:
    if aynidogrulamay==False:
        print("Girilen veriler için sonsuz ax+b=y denklemi vardır.")
    else:
        print("Girilen veriler için bir ax+b=y denlemi bulunmamaktadır.")
else:
    if hatalidenklem==True:
        print("Girilen veriler için bir ax+b=y denklemi bulunmamaktadır.")
    else:
        b=cikti[0]-girdi[0]*a
        print(f"Girilen değerler için {a}x+{b}=y denklemi sağlanmaktadır.")
        sondeger=float(input("x için 11. değeri giriniz:    "))
        sonuc=(sondeger*a)+b
        print(f"y={sonuc}")
# kapanmasın diye
bekle=input("")