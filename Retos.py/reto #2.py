#Enunciado del reto : Parque de diverciones
# file:///C:/Users/57315/Downloads/Reto%202%20enunciado.pdf
informacion = {
    'id cliente':1,
    'nombre': "johana fernandez",
    'edad2':20,
    'Primer_ingreso1':False,
     }
def cliente (informacion:dict)->dict:
     if informacion ['edad2'] > 18:
        var1 = 'X-Treme'
        var2 = True
        if informacion ['Primer_ingreso1'] == True:  
            total_boleta = 20000 - (20000 * 0.05)
        else :
            total_boleta = 20000
     elif informacion ['edad2'] >=15 and informacion ['edad2'] <=18:
        var1 = "carros chocones"
        var2 = True
        if informacion ['Primer_ingreso1'] == True:
            total_boleta = 5000 - (5000 * 0.07)
        else :
            total_boleta = 5000
     elif informacion ['edad2']>=7 and informacion ['edad2'] <15:
        var1 = "sillas voladoras"
        var2 = True
        if informacion ['Primer_ingreso1'] == True:
            total_boleta = 10000 - (10000 * 0.05)
        else :
            total_boleta = 10000 
     else:
            var1 = "N/A"
            var2 = "N/a"
            total_boleta = "N/a"

     diccionario_de_salida = {
        'nombre': informacion ['nombre'], 
        'edad': informacion ['edad2'], 
        'atraccion' : var1 ,
        'apto': var2,
        'primer_ingreso': informacion ["Primer_ingreso1"],
        'total_boleta' :total_boleta,
    }
     return (diccionario_de_salida)
print(cliente(informacion))