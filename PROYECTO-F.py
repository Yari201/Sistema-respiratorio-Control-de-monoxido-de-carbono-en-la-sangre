"""
Proyeto Final: Control de de Monóxido de  en sangre.

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: 
 Escobedo Tellez Yadhira Lisset 21210779   
 Gonzalez Morales Fabian 18211551 
 Hernandez Peraza Paola Giselle 19210608
 Zavala Silva Rosa Helena 18211599
 
Correo institucional: 
    yadhira.escobedo201@tectijuana.edu.mx
    fabian.gonzalez193@tectijuana.edu.mx
    paola.hernandez19@tectijuana.edu.mx
    rosa.zavala201@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

import numpy 
import matplotlib.pyplot as plt
import control

x0,t0,tF,dt = 0,0,10,1E-3
N=round((tF-t0)/dt)+1 #Numero total de iteraciones
t=numpy.linspace(t0,tF,N) #Arreglo del tiempo de 0:dt:10 segundos
u1=numpy.sin((3.1416*t)/2) #Funcion sinosoidal, 1.5708 rad/s = 250 mHz

#Elementos del circuito CONTROL
L1=0.01
R1=1
R2=0.5
C1=0.5
C2=10

#Elementos del circuito INTOXICACIÓN
L2=0.01
R3=1
R4=0.5
C3=1
C4=0.5

#Funcion de transferencia 
a1=L1*C1*C2*R2
b1=C1*C2*R1*R2+L1*C1+L1*C2
c1=C1*R1+C2*R1+C2*R2
d1=1
num1=[1]
den1=[a1,b1,c1,d1]
sys1=control.tf(num1,den1)
print(sys1)

#Funcion de transferencia INTOXICACIÓN
a2=L2*C3*C4*R4
b2=C3*C4*R3*R4+L2*C3+L2*C4
c2=C3*R3+C4*R3+C4*R4
d2=1
num2=[1]
den2=[a2,b2,c2,d2]
sys2=control.tf(num2,den2)
print(sys2)

#Respuesta en 10 segundos
fig4=plt.figure()
#plt.plot(t,u1, '-', color='cyan', label='$Pao(t)$') #Entrada

ts,Pp1=control.forced_response(sys1,t,u1,x0)
plt.plot(t,Pp1, '-', color='magenta', label='$P_p(t)$: Control') #Salida 

ts,Pp2=control.forced_response(sys1,t,u1,x0)
plt.plot(t,Pp2, ':',color="#7E2F8E", label='$P_p(t)$: Tratamiento') #Salida 

ts,Pp3=control.forced_response(sys2,t,u1,x0)
plt.plot(t,Pp3, '-', color='red' , label='$P_p(t)$: Caso') #Salida 

#Imprimir imagen

#plt.grid(True)
plt.xlim(0,10)
plt.xticks(numpy.arange(0, 11, 1))
plt.ylim(-1.2, 1.2)
plt.xlabel('$t$ $[segundos]$')
plt.ylabel('$V(t)$ $[volts]$')
plt.title('Control de CO en la sangre')
plt.legend(bbox_to_anchor=(0.5,-0.28),loc='center',ncol=4)
plt.show()
fig4.set_size_inches(7,5)
fig4.savefig('python_ProyectoFinal.png', dpi=600, bbox_inches='tight')
fig4.savefig('python_ProyectoFinal.pdf')
