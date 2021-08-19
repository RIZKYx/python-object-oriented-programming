class mangga:
    def __init__(self,nama,jumlah) -> None:
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self) -> str:
        return 'mangga: {} \ndengan jumlah: {}'.format(self.nama,self.jumlah)

    def __str__(self) -> str:
        return 'mangga: {} \ndengan jumlah: {}'.format(self.nama,self.jumlah)

    def __add__(self,object):
        return self.jumlah + object.jumlah

    @property
    def __dict__(self):
        return "object ini mempunyai nama dan jumlah"


belanja = mangga('arummanis',10)
belanja2 = mangga('mana lagi',30)
print(belanja)
print(belanja2)
print(belanja + belanja2)
print(belanja.__dict__)