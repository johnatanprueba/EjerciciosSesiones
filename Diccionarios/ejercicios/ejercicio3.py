def combinar_almacenes(almacen_ap,almacen_bp):
    almacen_apc = almacen_ap.copy()
    almacen_bpc = almacen_bp.copy()

    for k,v in almacen_apc.items():
        if k in almacen_bpc.keys():
            val = almacen_bpc[k]
            valFin = val+v
            almacen_apc[k]=valFin

    almacenAux = {}
    for k,v in almacen_bpc.items():
        if not k in  almacen_apc.keys():
            almacenAux[k] = v

    almacen_apc.update(almacenAux) 

    return   almacen_apc

almacen_a = {}
almacen_b = {"peras": 30, "naranjas": 80, "uvas": 15}

resultado=combinar_almacenes(almacen_a,almacen_b)
print(resultado)
