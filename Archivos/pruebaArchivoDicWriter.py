from csv import DictWriter

def escribirReservaciones(fileName,listReservacionesParam,listTitulosParam):
    with open(fileName,"w",newline="") as f:
        writer = DictWriter(f,fieldnames=listTitulosParam)
        if listTitulosParam:
            writer.writeheader()
            for reservacion in listReservacionesParam:
                writer.writerow({
                    "nombre":reservacion["nombre"],
                    "apellido":reservacion["apellido"],
                    "habitacion":reservacion["habitacion"],
                    "precio":reservacion["precio"],
                    "dias":reservacion["dias"]
                })

listTitulos = ["nombre","apellido","habitacion","precio","dias"]
listReservaciones = [{
    "nombre":"Johnatan",
    "apellido":"Naranjo",
    "habitacion":302,
    "precio":2346,
    "dias":3
},
{
    "nombre":"Diego",
    "apellido":"Herrera",
    "habitacion":567,
    "precio":98877,
    "dias":4
}]

escribirReservaciones("ventas_escribir.csv",listReservaciones,listTitulos)
