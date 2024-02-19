class Bombilla():
    def  __init__(self):
        self._encendida = False
        self._fundida = False
        self._contador = int(0)
    def encender(self):
        if self._contador >= 1000:
                print ("La bombilla se ha fundido")
        else:
            if self._encendida == True:
                print("La bombilla estaba encendida")
            else:
                print("La bombilla se ha encendido")
                self._encendida = True
                self._contador += 1
                
                return

    def apagar(self):
        if self._contador >= 1000:
                print ("La bombilla se ha fundido")
        else:
            if self._encendida == False:
                print ("La bombilla ya estaba apagada")
            else:
                print ("La bombilla se ha apagado")
                self._encendida = False


                  
            return

bombilla=Bombilla()
for i in range(1005):
    bombilla.encender()
    bombilla.apagar()
