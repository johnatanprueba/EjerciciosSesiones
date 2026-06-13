python = {(101, "Ana"), (102, "Carlos"), (103, "Sofía"), (104, "David")}
bases_datos = {(102, "Carlos"), (104, "David"), (105, "Elena"), (106, "Mario")}
diseno_ux = {(103, "Sofía"), (106, "Mario"), (107, "Laura")}

setPython = set(python)
setBD = set(bases_datos)
setDux = set(diseno_ux)

setIntePythonBD = setPython & setBD
print(setIntePythonBD) #1

setPyNoDi = setPython - setDux
print(setPyNoDi)#2

setUnionAll = setPython|setBD|setDux
print(setUnionAll)#3