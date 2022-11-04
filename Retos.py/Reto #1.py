'''
Una entidad Bancaria o entidad financiera, requiere calcular
el valor de los intereses ganados y el total final de dinero para diferentes clientes, de
acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un
producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo
determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece
rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo
determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira
antes de este periodo se aplica una penalidad del 2%.'''
def CDT (usuario:str,capital:int,tiempo:int):
    porcentaje_a_ganar = 0.03
    porcentaje_a_perder = 0.02
    if tiempo >2:
        porcentaje_de_ganancia = (capital * porcentaje_a_ganar * tiempo)/12
        valor_total = int(capital + porcentaje_de_ganancia)
    else:
        porcentaje_de_perdida = (capital * porcentaje_a_perder *tiempo)  /12
        valor_total = int(capital - porcentaje_de_perdida) 
    resultado =(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es:{valor_total}")
    return resultado
print(CDT("ABJKL", 1000000, 3))