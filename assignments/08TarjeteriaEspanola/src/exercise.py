def tarjetas(pliegos,marcadores):
    tarjetaspliegos=pliegos*12
    tarjetasplum=marcadores*35
    if tarjetaspliegos<tarjetasplum:
        return (tarjetaspliegos)
    elif tarjetasplum<tarjetaspliegos:
        return (tarjetasplum)

def main():
    #escribe tu código abajo de esta línea
    pliegospapel=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))
    print ("El número máximo de tarjetas que se pueden hacer es: "+str(tarjetas(pliegospapel,plumones)))
    
if __name__=='__main__':
    main()
