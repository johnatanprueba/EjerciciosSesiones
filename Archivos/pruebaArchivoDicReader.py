import csv


with open('ventas_semana_pasada.csv') as f:
    DictReader_obj = csv.DictReader(f)
    for item in DictReader_obj:
        print(item["JORNADA1"])
			