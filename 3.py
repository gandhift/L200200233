class pohon(object):
    def __init__(self,data):
        self.data = data 
        self.kanan = None
        self.kiri = None

A = pohon('1')
B = pohon('2')
C = pohon('3')
D = pohon('4')
E = pohon('5')
F = pohon('6')
G = pohon('7')

A.kiri = B ; A.kanan = C
B.kiri = D ; B.kanan = E
C.kiri = F ; C.kanan = G

def tampilLuarKanan(data):
    if data.kanan is not None:
        tampilLuarKanan(data.kanan)
    print(data.data)
def tampilLuarKiri(data):
    if data.kiri is not None:
        tampilLuarKiri(data.kiri)
    print(data.data)

tampilLuarKiri(A)