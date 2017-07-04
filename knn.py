#!python3
#50859 (Sınıf sınırımız)

# Grafik için gerekli kütüphaneler. Axes3D 3 boyutlu bir grafik için.
from matplotlib import pyplot as  plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt

class knn():
    # başlangıç fonksiyonumuz ve değişkenlerimiz. inp değişkenimiz sınıf niteliği
    # belli olmayan örneğimizdir. Siz isterseniz bu değeri dışardan da alabilirsiniz.
    # __init__ metodundaki dataset veri setimizi, k en yakın k komşuyu, nfrom veri
    # setini okumaya başlanacağı satır ve nto ise kaçıncı satıra kadar okuyacağını
    # belirtir. Son iki parametre çok büyük veri setlerini çözümlerken pc'ler yeter
    # siz kaldığından isteğe bağlı olarak sadece veri setinin belli bir kısmını
    # seçmek için ekledim. Ki bu örneğimizde öyle bir örnek.
    def __init__(self, dataset, k, nfrom, nto):
        self.b, self.g, self.r, self.class_attr = [], [], [], []
        self.inp = [150,140,230]
        self.k = k

    # Veri setimizi nfrom satırından nto satırına kadar okuyoruz.
    # Ayrıca veri setindeki her sutunu bir listeye atıyoruz. (r,g,b,class_attr)
        with open(dataset, "r") as f:
            for i in f.readlines()[nfrom:nto]:
                self.r.append(int(i.split()[0]))
                self.g.append(int(i.split()[1]))
                self.b.append(int(i.split()[2]))
                self.class_attr.append(i.split()[3])

    # Uzaklık hesaplamamızı yaptığımız metodumuz. dist parametresine göre
    # ilgili hesaplanma yapılmaktadır. Default oklid uzaklığı kullanılmaktadır.
    # Burda dikkat edilmesi gerekilen en önemli nokta; uzaklık değeri hesaplandıktan
    # sonra hangi uzaklığın başta hangi index numarasına sahip olduğunu bilmeyiz.
    # Çünkü bu indis numarasını kullanarak ilgili uzaklığın sınıf değerine ulaşacağız.
    # Bu sebeple uzaklığı ve uzaklığın indis değerini demet şeklinde
    # dist listemize ekliyoruz.Çünkü uzaklığı küçükten büyüğe sıraladığımızda
    # uzaklığa ait gerçek sınıf değerine ulaşamamaktayız.
    #
    # öklid = 1, manhattan=2
    def distance(self, dist=1):
        self.dist = []
        # for döngüsündeki karışık gibi gelen üs alma, mutlak değer gibi işlemler
        # minkowski formulunun karşılığından ibarettir.
        for i in range(len(self.class_attr)):
            self.dist.append((pow((pow((
            abs(int(self.b[i]) - int(self.inp[0])) +
            abs(int(self.g[i]) - int(self.inp[1])) +
            abs(int(self.r[i]) - int(self.inp[2]))), 2)), 1/dist), i))

        return self.dist

    # uzaklık hesaplanması yapıldıktan sonra örneğimize en yakın olan k tane
    # elemanı buluyoruz ve bu elemanların sınıf değerlerini class_values
    # listemizde tutuyoruz. Ve döngünün sununda class_values listesindeki 1(cilt)
    # 2(cilt değil) sayılarını hesaplayıp, örneğin hangi sınıfa ait olduğunu
    # buluyoruz.
    def findClass(self):
        self.class_values = []
        self.result = ""

        for i in sorted(self.dist)[:self.k]:
            self.class_values.append(self.class_attr[i[1]])

        self.first = self.class_values.count("1")
        self.secnd = self.class_values.count("2")

        print("Birinci Sınıf:", self.first)
        print("İkinci Sınıf:", self.secnd)

        if self.first > self.secnd:
            self.result = "1. Sınıf(Kırmızı)"
        else:
            self.result = "2. Sınıf(Yeşil)"

        print("SONUÇ: "+self.result)

#GORSELLEŞTİRME
    # Algoritmanın daha somut bir şekilde anlaşılması adına 3 boyutlu uzayda
    # grafiğini oluşturdur. Kırmızı noktalar cilt, yeşil noktalar cilt olmayan
    # ve mavi nokta ise sınıf değerin belli olmayan örneğimiz.
    def grafik(self):
        fig = plt.figure()
        ax  = fig.add_subplot(111, projection='3d')

        for bi, gj, rk, class_attr in zip(self.b, self.g, self.r, self.class_attr):
        	if class_attr == "1":
        		ax.scatter(bi,gj,rk, c='r', marker='.')
        	else:
        		ax.scatter(bi,gj,rk, c='g', marker='.')

        ax.scatter(int(self.inp[0]), int(self.inp[1]), int(self.inp[2]), c='b')
        ax.set_xlabel('X Ekseni')
        ax.set_ylabel('Y Ekseni')
        ax.set_zlabel('Z Ekseni')

        fig.text(0, 0, "Kırmızı(1)[Cilt] : "+str(self.first)+
                " -- Yeşil(2)[Cilt Değil] : "+str(self.secnd)+
                " -- {{SONUÇ : "+self.result+"}}")

        plt.legend()
        plt.show()

# Sınıfımızdan nesne türetip gerekli metodlarımızı çağırıyoruz. Ve sonuç.
ins = knn("ten_dataset.txt", 17, 50000, 51800)
ins.distance(1)
ins.findClass()
ins.grafik()
