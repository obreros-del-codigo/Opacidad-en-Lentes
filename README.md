# Opacidad-en-Lentes
Estasimulación encuentra la opacidad necesaria en un lente para poder observar el Sol. Hace este cálculo sólo en 441nm.

Para correr la simulación se puede hacer uso del archivo test.py

Ahí se especifica el grosor del lente a calcular, la cantidad de iteraciones que se desea hacer con la ecuación: I1=I0e(-dx*op)

El programa por si solo realizará las iteraciones necesarias para llegar al valor deseado.

Si se quiere modificar más profundamente los parámetros del programa se debe modificar el archivo rte.py:

Ahí se puede modificar la intensidad específica inicial. En esta simulación ese valor corresponde a la intensidad específica para 441nm al mediodía con un ancho de banda de 20nm.
También se puede modificar la intensidad específica resultante deseada. Para nosotros era 0.02. Basta con cambiar ese valor dentro del for loop.


¡Mucha suerte con los experimentos!

