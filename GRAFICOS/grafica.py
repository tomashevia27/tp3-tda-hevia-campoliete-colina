import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit

BT="m_k_bt.txt"
GREEDY1="m_k_greedy.txt"
GREEDY2="m_k_greedy2.txt"
PL="m_k_pl.txt"
TITULO="Cantidad de Maestros"
def leerMediciones(x,y,minimo,nombre_archivo,en_minutos=False):
    with open(nombre_archivo,"r") as file:
        lector=csv.reader(file,delimiter=",")
        file.readline()
        for linea in lector:
            x.append(int(linea[0]))
            if en_minutos:
                y.append((float(linea[1])/1000)/60)
            else:
                y.append(float(linea[1]))

            minimo.append(int(linea[2].rstrip()))

def funcionlogaritmica(x,a,b):
    return (x*np.log(a))+b

def funcionExponencial(x,a,b):
    return a*np.exp(b*x)

def funcionNormal(x,amp,mu,sigma,c):
     return c + amp*np.exp(-np.power(x-mu,2.)/(2*np.power(sigma,2.)))

def graficar():

    x1=[]; y1=[]; z1=[]
    x2=[]; y2=[]; z2=[]
    x3=[]; y3=[]; z3=[]
    x4=[]; y4=[]; z4=[]

    leerMediciones(x1,y1,z1,BT,True)
    leerMediciones(x2,y2,z2,GREEDY1)
    leerMediciones(x3,y3,z3,GREEDY2)
    leerMediciones(x4,y4,z4,PL,True)

    # Apartado para grafico de k fijo y n fijo

    xdata = np.array(x1) 
    ydata = np.array(y1)
    figure,axes = plt.subplots(2,2)

    res_bt , _ = curve_fit(funcionExponencial,xdata,ydata,p0=[1,1],maxfev=1000000)
    res_g1 , _ = curve_fit(funcionlogaritmica,x2,y2)
    res_g2 , _ = curve_fit(funcionlogaritmica,x3,y3)
    res_pl , _ = curve_fit(funcionExponencial,x4,y4,p0=[1,1],maxfev=1000000)

    xfit= np.arange(4,18,0.01)
    yfit=funcionExponencial(xfit,*res_bt)

    xfit_g1=np.arange(4,18,0.01)
    yfit_g1=funcionlogaritmica(xfit_g1,*res_g1)

    xfit_g2=np.arange(4,18,0.01)
    yfit_g2=funcionlogaritmica(xfit_g2,*res_g2)

    xfit_pl=np.arange(4,18,0.01)
    yfit_pl=funcionExponencial(xfit_pl,*res_pl)


    axes[0,0].plot(xdata,ydata,"b",label="Backtracking")
    axes[0,0].scatter(xdata,ydata,c="blue")
    axes[0,0].plot(xfit,yfit,"r",label="Ajuste por funcion Exponencial") 
    axes[0,0].legend(loc='upper left',prop={'size':8})
    axes[0,0].set_xlabel(TITULO)
    axes[0,0].set_ylabel("Tiempo[minutos]")
    axes[0,0].grid(True)

    axes[0,1].plot(x2,y2,"orange",label="Aproximacion")
    axes[0,1].scatter(x2,y2,c="orange")
    axes[0,1].plot(xfit_g1,yfit_g1,"r",label="Ajuste por curva x*log(x)") 
    axes[0,1].legend(loc='upper left',prop={'size':8})
    axes[0,1].set_xlabel(TITULO)
    axes[0,1].set_ylabel("Tiempo[milisegundos]")
    axes[0,1].grid(True)

    axes[1,0].plot(x3,y3,"green",label="Balanceo por cantidad de elemento")
    axes[1,0].scatter(x3,y3,c="green")
    axes[1,0].plot(xfit_g2,yfit_g2,"r",label="Ajuste por curva x*log(x)") 
    axes[1,0].legend(loc='upper left',prop={'size':8})
    axes[1,0].set_xlabel(TITULO)
    axes[1,0].set_ylabel("Tiempo[milisegundos]")
    axes[1,0].grid(True)

    axes[1,1].plot(x4,y4,"purple",label="Programacion Lineal Entera")
    axes[1,1].scatter(x4,y4,c="purple")
    axes[1,1].plot(xfit_pl,yfit_pl,"r",label="Ajuste por funcion exponencial")
    axes[1,1].legend(loc='upper left',prop={'size':8})
    axes[1,1].set_xlabel(TITULO)
    axes[1,1].set_ylabel("Tiempo[minutos]")
    axes[1,1].grid(True)

    figure.tight_layout()
    plt.show()

graficar()
