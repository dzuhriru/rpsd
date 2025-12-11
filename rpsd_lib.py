import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def rpsd_plt(A,Sesi,Nama,NIU,NIF):
    # Membaca Titik-Titik Data dari File Text
    Npts = 361
    f = open('RPSD_PLT_'+ Sesi +'_' + str(NIU) + '.txt', "r")
    V = np.zeros((3,Npts))
    W = np.zeros((3,Npts))
    for i in range(0,Npts):
      V[0,i] = float(f.readline())
      V[1,i] = float(f.readline())
      V[2,i] = 1
    for i in range(0,Npts):
      W[0,i] = float(f.readline())
      W[1,i] = float(f.readline())
      W[2,i] = 1
    f.close()

    # Menghitung Titik-Titik Data Hasil Transformasi
    Z = A@V

    # Menampilkan Grafik
    subplots = []
    fig = make_subplots(
        rows=1, cols=1)
    fig.add_trace(go.Scatter(x=V[0,:],y=V[1,:], mode="lines", name='Original Shape'),
                row=1, col=1)
    fig.add_trace(go.Scatter(x=W[0,:],y=W[1,:], mode="lines", name='Target Shape'),
                row=1, col=1)
    fig.add_trace(go.Scatter(x=Z[0,:],y=Z[1,:], mode="lines", name='Current Shape'),
                row=1, col=1)
    fig.update_yaxes(scaleanchor="x",
                    scaleratio=1)
    fig.update_layout(height=600, width=700,
                    title_text="Linear Transformation")
    fig.show()

    # Proses Penyimpanan Data
    f = open("RPSD_Hasil_"+Sesi+"_"+str(NIU)+"_"+str(NIF)+"_"+Nama+".txt", "w")
    f.write(Nama + "\n")
    f.write(str(NIU) + "\n")
    f.write(str(NIF) + "\n")
    f.write(Sesi + "\n")
    for row in range (0,3):
      for col in range (0,3):
        f.write(str(A[row,col]) + "\n")
    for col in range (0,Npts):
      for row in range (0,2):
        f.write(str(V[row,col]) + "\n")
    for col in range (0,Npts):
      for row in range (0,2):
        f.write(str(W[row,col]) + "\n")
    for col in range (0,Npts):
      for row in range (0,2):
        f.write(str(Z[row,col]) + "\n")
    f.close()