class Fecha():
    def __init__(self):
        self._dia=0
        self._mes=0
        self._año=0

    def modificar_dia(self, dia):
        Fecha._comprobar_dia(dia)
        self._dia = dia

    def modificar_mes(self, mes):
        Fecha._comprobar_mes()
        self._mes = mes

    def modificar_año(self, año):
        self._año = año

    def modificar_fecha(self, año, mes, dia):
        self._comprobar_fecha(dia, mes)
        self._dia = dia
        self._mes = mes
        self._año = año
    
    def _comprobar_fecha(self, dia, mes):
        Fecha._comprobar_dia(dia)
        Fecha._comprobar_mes(mes)
    
    def _comprobar_dia(dia):
        if dia > 1 and dia < 31:
            return True
        else:
            raise ValueError("El numero debe estar entre 1 y 31")
    
    def _comprobar_mes(mes):
        if mes > 1 and mes < 12:
            return True
        else:
            raise ValueError("El numero debe estar entre 1 y 12")
    
    def devolver_dia(self):
        return self._dia
    
    def devolver_mes(self):
        return self._mes

    def devolver_año(self):
        return self._año
    
    def __str__(self) -> str:
        return str(self._dia) + "-" + str(self._mes) + "-" + str(self._año)
    
f1 = Fecha()
f1.modificar_fecha(2024, 2, 13)
print (f1)
