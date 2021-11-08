# Inv.Mult.

En en el archivo "Inversa.py" se encontrará la implementación del algoritmo de la inversa multiplicativa. En dicho programa se hace uso de las funciones:
- mod(a,b): El cual retorna el valor del entero a en módulo b
- euclides(a,b): El cual retorna el GCD de a y b
- ext(a,b): El cual retorna los valores de a, x, b, y, d (GCD de a y b) en la expresión lineal ax + by = d
- inMul(a,n): El cual retorna la inversa multiplicativa del entero a en módulo n. Siendo a y n coprimos entre sí. Se crearán 3 variables:
-     d = GCD(a,n) --> Para verificar que a y n son coprimos
-     xP= Valor de x en la expresión ax + by = d
-     yP= Valor de y en la expresión ax + by = d
- En caso d sea diferente de 1, significa que los números a y n no son coprimos, por lo que no se puede calcular la inversa multiplicativa
- En caso d sí sea igual a 1, significa que a y n son coprimos y se procede a retornar el valor de xP mod n. Dicho resultado es la inversa multiplicativa de a mod n
