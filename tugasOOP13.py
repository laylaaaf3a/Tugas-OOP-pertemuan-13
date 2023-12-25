class animal:
    def _init_(self, nama, makanan, hidup, kembang):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.kembang = kembang

    def cetak(self):
        print("Nama hewan\t\t :",self.nama,
            "\nmakannya \t\t\t :",self.makanan,
            "\nhidup di \t\t :",self.hidup, 
            "\nberkembangbiak dengan cara \t :",self.kembang)
        
class badak(animal):
    def _init_(self, nama, makanan, hidup, kembang):
        super()._init_(nama, makanan, hidup, kembang)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.kembang = kembang

    def data (self):
        print("Nama hewan\t\t\t :",self.nama,
            "\nmakannya \t\t\t :",self.makanan,
            "\nhidup di \t\t\t :",self.hidup, 
            "\nberkembangbiak dengan cara \t :",self.kembang,
            "\n---------------------------------------------")
        
class ikan(animal):
    def _init_(self, nama, makanan, hidup, kembang):
        super()._init_(nama, makanan, hidup, kembang)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.kembang = kembang

    def data (self):
        print("Nama hewan\t\t\t :",self.nama,
            "\nmakannya \t\t\t :",self.makanan,
            "\nhidup di \t\t\t :",self.hidup, 
            "\nberkembangbiak dengan cara \t :",self.kembang,
            "\n---------------------------------------------")
        
class ular(animal):
    def _init_(self, nama, makanan, hidup, kembang):
        super()._init_(nama, makanan, hidup, kembang)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.kembang = kembang

    def data (self):
        print("Nama hewan\t\t\t :",self.nama,
            "\nmakannya \t\t\t :",self.makanan,
            "\nhidup di \t\t\t :",self.hidup, 
            "\nberkembangbiak dengan cara \t :",self.kembang,
            "\n---------------------------------------------")
        
hewan1 = badak('badak bercula satu', 'tumbuhan', 'darat', 'melahirkan')
hewan1.data()
hewan2 = ikan('ikan hiu', 'ikan kecil kecil', 'air', 'melahirkan')     
hewan2.data()
hewan3 = ular('ular', 'daging', 'darat', 'bertelur')
hewan3.data()
