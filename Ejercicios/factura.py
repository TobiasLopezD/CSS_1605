#|/usr/bin/env python2
#|-*-coding:utf-8-*-
''' Crear una factura para ingresar un articulo y generar el iva 12 de la 
misma '''

def factura():
	print "="*30
	precio = float(raw_input("Ingrese el valor neto: "))
	iva = precio * 0.12
	print "="*30
	print precio
	print "+"
	print iva
	print "-"*10
	total = precio + iva
	print total
	print "="*30
	print "El precio total a pagar por la factura es %f"%total

factura()
