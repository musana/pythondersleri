from matplotlib import pyplot as plt #Grafikleri çizeceğimiz alan(plot)
from sys import argv #Dışarıdan argüman alacağımız için import ediyoruz.

logfile = argv[1]
n = int(argv[2])

with open(logfile, "r") as f:
	log = f.readlines()

ip = [i.split()[0] for i in log]

uniq_ip = list()
[uniq_ip.append(i) for i in ip if i not in uniq_ip]


freq = list()
[freq.append(ip.count(i)) for i in uniq_ip if i not in freq]

eq = sorted(zip(freq, uniq_ip), reverse=True)

y_axis  = [i[0] for i in eq] # y ekseni

# x ekseni. Her bir x noktasına bir y noktası denk geleceği için x ve y liste uzunluklarının eşit olmasına dikkat ediniz.
x_axis  = range(len(y_axis))

x_label = [i[1] for i in eq] # x eksenindeki etiket isimleri (ip adresleri)

#y_axis değişkenimizde frekans sayıları, x_label değişkenimizde ise ip adresleri yer almaktadır.


# Grafiğimizi çizdik. marker ile x ve y ekseninin kesiştiği yere .(nokta) koyduk.
plt.plot(x_axis[:n], y_axis[:n], marker='.')

# x ve eksenindeki bilgi etiketlerini yazdırıyoruz.
plt.title(argv[1]+" Dosyası Analizi")
plt.ylabel("Total Request")
plt.xlabel("Ip Address")

# Grid ile x ve y ekseninde yatay ve dikey referans çizgilerini aktif ediyoruz.
plt.grid(True)

# X eksenimizdeki etiket alanında sayi görünmesi yerine ip adreslerini gösteriyoruz. 90 derece göndererek overlop olmasının önüne geçiyoruz.
plt.xticks(x_axis[:n], x_label[:n], rotation=90)

# y eksenimizi 50 birimlik referans çizgileri ile belirliyoruz. Daha fazla detay için küçük değer verilebilir.
plt.yticks(range(0,max(y_axis),50))

#Grafiğimizi gösteriyoruz.
plt.show()