#!/usr/bin/env python3

#
#  Radiative Transfer Equation
#  Copyright (C) 2019 Victor De la Luz
#                     Obreros del Código
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import math
import matplotlib
import matplotlib.pyplot as plt
def run(grosor,N):
	c=3e10 #cm/
	N=10000 #number of points in the raypath
	I0= 0.2 #Wcm^-2
	dx = grosor/N   #[cm]
	layers = range(1,int(N+1))
	up=0
	lentesx=[]
	lentesy=[]

	while True:
		up+=1
		I = I0
		X = []
		Y = []
		op=up/100
		for i in layers:#tqdm(layers):
			x = float(i)*dx
			I = I*math.exp(-op*dx)
			X.append(x)
			Y.append(I)
		lentesx.append(op)
		lentesy.append(I)
		if I<0.02:
			print(I,op)
			break
		print(I,up/100)

	fig, ax = plt.subplots()
	ax.plot(X, Y)
	fig.suptitle('Intensidad específica al pasar por el lente', fontsize=20)
	plt.xlabel('Grosor recorrido en Cm', fontsize=10)
	plt.ylabel('Intensidad específica en Wcm^-2', fontsize=10)
	fig.savefig('Figure.jpg')
	plt.show()

	fig2, ax2 = plt.subplots()
	ax2.plot(lentesx,lentesy)
	fig2.suptitle('Intensidad específica después de pasar por cada lente', fontsize=15)
	plt.xlabel('Opacidad del lente', fontsize=10)
	plt.ylabel('Intensidad específica rendida en Wcm^-2', fontsize=10)
	fig2.savefig('Figure2.jpg')
	plt.show()
