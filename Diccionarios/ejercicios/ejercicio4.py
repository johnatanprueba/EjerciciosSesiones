agenda = {
"Ana": "Madrid",
"Carlos": "Barcelona",
"Luis": "Madrid",
"Maria": "Sevilla",
"Pedro": "Barcelona"
}

def invertir_agenda(agenda):
    agendaInvertida = {}
    for k,v in agenda.items():
        if v in agendaInvertida.keys():
            lista = agendaInvertida[v]
            lista.append(k)
        else:
            lista = []
            lista.append(k)
            agendaInvertida[v] = lista
    return agendaInvertida

resultado = invertir_agenda(agenda)
print(resultado)
        

