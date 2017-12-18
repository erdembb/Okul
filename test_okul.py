import pytest
import okul
from okul import Okul
class TestOkul():
    def test_arg_gir(x):
        test1 = Okul.arg_gir("9")
        assert test1 == "1-4 aralığında değer giriniz"
        test2 = Okul.arg_gir("x")
        assert test2 == "Geçersiz argüman girişi"
        test3 = Okul.arg_gir("E 2")
        assert test3 == "HATA : sadece bir argüman girebilirsiniz"
        test4 = Okul.arg_gir("")
        assert test4 == True
        test5 = Okul.arg_gir("E")
        assert test5 == True
        test6 = Okul.arg_gir("e")
        assert test6 == True
        test7 = Okul.arg_gir("k")
        assert test7 == True
        test8 = Okul.arg_gir("3")
        assert test8 == True
    def test_tekil_kont(self):
        assert Okul.tekil_kont() == "Liste başarılı"
        Okul.oku("no_unique_okul.csv")
        assert Okul.tekil_kont() == "Liste Unique değil"
    def test_oku(self):
        assert Okul.oku("okul.csv") == "Liste yüklendi"
