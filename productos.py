nombre = input("Ingrese el producto: ")
cantidad = float(input("Ingrese la cantidad: "))
precio = float (input("Ingrese el precio: "))

subtotal = cantidad * precio
descuento = 0.25
iva = 0.19
total_con_descuento = subtotal - (subtotal * descuento)
total_con_iva = str (total_con_descuento + (total_con_descuento * iva))

