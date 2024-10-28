class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
            return f"PersegiPanjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main():
        try:
            panjang = input("Masukan panjang persegi panjang: ")
            lebar = input("Masukan lebar persegi panjang: ")
            PP = PersegiPanjang(panjang, lebar)

            if (panjang <= 0 or lebar >= 0):
                print("nilai tidak boleh nol atau minus, nilai tidak valid")
                return
            print(PP)
            print(f"keliling: {PP.keliling()} cm")
            print(f"luas persegi panjang:{PP.luas()} cm2")
        except ValueError:
            print("Nilai tidak valid")

main()

# Menjalankan fungsi main
if __name__ == "main":
    main()