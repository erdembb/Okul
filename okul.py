import csv
aList = []
bList = []
class Okul:
    def oku(ogrenci):
        with open(ogrenci, newline='') as CSV:
            spamreader = csv.reader(CSV)
            for row in spamreader:
                aList.append(','.join(row));
                bList.append(row[0])
            return "Liste yüklendi"
    def tekil_kont():
        if len(bList) > len(set(bList)):
            print("Liste Unique değil")
            return "Liste Unique değil"
            exit()
        else:
            return "Liste başarılı"
    def arg_gir(x):
        cList = []
        harf_list = ["E", "K", "e", "k"]
        if len(x) > 1:
            print("HATA : sadece bir argüman girebilirsiniz")
            return "HATA : sadece bir argüman girebilirsiniz"
        elif len(x) == 0:
            for elem in aList:
                print(elem)
            return aList[::] == aList
        else:
            if x.isdigit() == 1 and "0" < x < "5":
                for i in range(0, len(aList)):
                    dlist = aList[i]
                    if x == dlist[-1]:
                        cList.append(dlist)
                    else:
                        continue
                for elem in cList:
                    print(elem)
                return x in cList[::][-1]

            elif x.isdigit() == 1 and (x > "4" or x < "1"):
                print("1-4 aralığında değer giriniz")
                return "1-4 aralığında değer giriniz"
            elif x.isdigit() == 0 and x in harf_list:
                for i in range(0, len(aList)):
                    dlist = aList[i]
                    if x.upper() == dlist[-3]:
                        cList.append(aList[i])
                    else:
                        continue
                for elem in cList:
                    print(elem)
                return x.upper() in cList[::][-2]
            else:
                print("Geçersiz argüman girişi")
                return "Geçersiz argüman girişi"


    oku("okul.csv")
    tekil_kont()
    #arg_gir(str(input()))