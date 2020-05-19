from colorama import*

def calcular_precio(marca,puerta,color,total_ventas):
    
    marcas = {'FORD':100000,'CHEVROLET':120000,'FIAT':80000}
    puertas = {2:50000,4:65000,5:78000}
    colores = {'Blanco':10000,'Azul':20000,'Negro':30000}
    
    precio = marcas[marca]+colores[color]+puertas[puerta]
    
    if total_ventas > 5 and total_ventas < 11:
        precio = precio*0.9
    elif total_ventas >10 and total_ventas<51:
        precio = precio*0.85
    elif total_ventas>50:
        precio = precio*0.82
    return precio
     
print("Vendemos Ford, Chevrolet y Fiat")
print("Los Mejores Autos del Mercado")
print("Hola")  

ventas = []
   
hay_clientes = "si"

marcas_vehiculos = ['FORD','CHEVROLET','FIAT']
puertas_vehiculos = [2,4,5]
colores_vehiculos = ['Blanco','Azul','Negro']
       
while hay_clientes == "si":
            
    nombre_comprador = input("Nombre del comprador: ")
    apellido_comprador = input("Apellido del comprador: ")
    
    marca = ''
    puerta = 0
    color = ''
    
    while marca not in marcas_vehiculos:
        m = input("marca: ")
        marca = m.upper()
    
    while puerta not in puertas_vehiculos:
        puerta = int(input("puerta: "))
        
    while color not in colores_vehiculos:
        c = input("Color: ")
        color = c.capitalize()
    
    total_ventas = len(ventas)
    total_ventas = total_ventas + 1
    precio = calcular_precio(marca,puerta,color,total_ventas)
           
    ventas.append({'nombre':nombre_comprador,'apellido':apellido_comprador,'marca':marca,'puertas':puerta,'color':color,'precio':precio})
    hay_clientes = input("hay mas Clientes: ")
    
    
  
for i in ventas:
    
    precio_carro = i['precio']
    
    print("Nombre del comprador es: ", i['nombre'], " ", i['apellido'], "Marca: ", Fore.BLUE + i['marca'], Style.RESET_ALL, "Color: ",  i['color'], "de ", i['puertas'], "puertas",  "El Precio del Vehiculo es: ", Fore.RED, format(precio_carro, '.0f'), Style.RESET_ALL)
        
print("Las ventas de hoy fueron: ", total_ventas)   
        
    
    
        
