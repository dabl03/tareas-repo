"""Programa que saca el reporte de venta por cada sucursa"""
sucursales=[];
metas=[];
MAX_SUCURSALES=10;
cant_sucursales=0;

print("Bienvenido al sistema de contabilidad Daniel B.");
print("Calculamos sacamos un reporte de venta de cada sucursales.");

def get_num_input(msg:str, min:int=None, max:int=None):
    """Obtiene un numero de la entrada del usuario verificando
    Si es valido y está en el rango solicitado.

    Args:
        msg (str): Mensaje para mostrar al usuario.
        min (int, optional): El numero minimo aceptable. Defaults to None.
        max (int, optional): El numero maximo aceptable. Defaults to None.

    Returns:
        int or float
    """
    while True:
        num=input(msg+"\n?> ");
        if num.isalnum():
            num=int(num);
            if min!=None and num<min:
                print(f"Error: No se puede ingresar menos de {min}.");
                continue;
            if max!=None and num>max:
                print(f"Error: No se puede ingresar mas de {max}.");
                continue;
            return int(num);
        else:
            try:
                return float(num);
            except ValueError:
                pass
        print("Error: Solo se puede pasar numeros.\nIntentalo de nuevo.");

cant_sucursales=int(get_num_input(
    f"Ingrese las cantidad de sucursales a consultar (maximo {MAX_SUCURSALES}):",
    1,
    10
));
for x in range(cant_sucursales):
    print(f"Sucursar numero {x}:");
    sucursales.append([]);
    metas.append(
        get_num_input(f"  Ingresa la ganacia que se esperada {x}.")
    );
    for y in range(cant_sucursales):
        num=get_num_input(f"  Ingresa la cantidad de dolares ganado el dia {y+1}:");
        sucursales[-1].append(num);

gran_dia=[];
max_ganancia=sucursales[0][0];

max_venta=[];
max_suma=0;
print("Ventas por sucursales:");
for x in range(cant_sucursales):
    suma=0;
    for dia in range(len(sucursales[x])):
        # Maxima ganancia con sus dias.
        ganancia=sucursales[x][dia];
        now={"sucursal":x, "dia":dia+1, "monto":ganancia};
        if ganancia>max_ganancia or x+dia==0:
            gran_dia=[now];
            max_ganancia=ganancia;
        elif ganancia==max_ganancia:# No es el dia base.
            gran_dia.append(now);
        # SubTotal maximo.
        suma+=ganancia;
    
    # SubTotal maximo.
    if suma>max_suma:
        max_venta=[{"sucursal":x, "total":suma}]
        max_suma=suma;
    elif suma==max_suma:
        max_venta.append({"sucursal":x, "total":suma});
    
    # Reporte
    print(f"  - sucursal {x} ha vendido {suma}$ en {cant_sucursales} dias.");
    print("      "+(
            "Ha" if metas[x]<=suma else "No"
        )+f" cumplido la meta de ventas de {metas[x]}$."
    );

if len(max_venta)==1:
    print(f"La sucursal {max_venta[0]['sucursal']} ha tenido un total de venta mas alto. Con un total de {max_venta[0]['total']}$.");
else:
    print(f"Las sucursales que tienen el total de venta mas altos con {max_venta[0]['total']}$ son:");
    for suc in max_venta:
        print(f"  - sucursal {suc['sucursal']}");

if len(gran_dia)==1:
    print("El dia con la venta mas alta es: "+str(gran_dia[0]["dia"]));
    print(f"  Con una venta de: {gran_dia[0]['monto']}$. Por la sucursal {gran_dia[0]['sucursal']}");
else:
    print(f"Los dias con las venta mas alta con una venta de {gran_dia[0]['monto']}$ son:");
    dias={};
    for dia in gran_dia:
        if not dia["dia"] in dias:
            dias[dia["dia"]]=[dia['sucursal']];
        else:
            dias[dia["dia"]].append(dia['sucursal']);
    for dia, sucursal in dias.items():
        print(f"  - Dia: {dia} | Sucursales: {', '.join(str(num) for num in sucursal)}.");