# Dibuat oleh: Cahya Amalinadhi Putra
# 2 Mei 2019, 03:23
# Code ini dapat disebarluaskan untuk tujuan pendidikan


"""
============================================================================== 
                                Visualisasi Data
============================================================================== 
Visualisasi data adalah satu bagian penting dalam membantu proses analisis dan
penyajian data yang telah didapat.

Visualisasi ini biasa ditampilkan dalam bentuk grafik.

Pada code kali ini, engcode.id akan membahas cara memvisualkan data dalam
bentuk grafik menggunakan bantuan matplotlib
==============================================================================

"""

# ----- Langkah 01: Buat Fungsi -----
# Buat fungsi yang akan divisualkan

# import library numpy untuk mempermudah perhitungan 
import numpy as np 	

def f(x, y):
	"""
	Fungsi yang ingin dibuat adalah
	f(x, y) = x^2 + y^2
	
	"""

	hasil = np.sin(np.sqrt(x ** 2 + y ** 2))
	return hasil


# ----- Langkah 02: Persiapkan domain -----
# Persiapkan domain fungsi (x dan y) yang akan digunakan

# Buat elemen domain dengan bantuan fungsi linspace.
# 	linspace(lb, up, n)
#	lb 		: lower bound (batas bawah)
#	ub		: upper bound (batas atas)
#	n 		: jumlah titik pembagi
#
#	contoh:
#		p = np.linspace(0, 2.0, 5)
#	maka
#		p = [0, 0.5, 1.0, 1.5, 2.0]
delX = np.linspace(-6, 6, 30)
delY = np.linspace(-6, 6, 30)

# Buat grid pasangan x dan y dengan bantuan meshgrid
X, Y = np.meshgrid(delX, delY)

# Silahkan hilangkan simbol pagar (#) untuk melihat mesh grid yang dimaksud
#print(X)
#print(Y)


# ----- Langkah 03: Cari hasil fungsi -----
Z = f(X, Y)


# ----- Langkah 04: Plot grafis -----
# Visualisasikan fungsi dengan bantuan matplotlib

# import library matplotlib
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Definisikan template plot
#
# Cek website berikut:
# 	https://matplotlib.org/examples/mplot3d/index.html
# untuk mengeksplor metode plotting yang lebih banyak
ax = plt.axes(projection='3d')
#ax.plot_wireframe(X, Y, Z, color='black')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')

# Atur penamaan label
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Tampilkan hasil visualisasi
plt.show()
