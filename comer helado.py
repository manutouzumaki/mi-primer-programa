apetece_helado_input = input("quieres helado? si/no").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("no se que quisiste decir pero supongo que no")
    apetece_helado = False

tienes_dinero_input = input("tienes dinero? si/no").upper()

if tienes_dinero_input == "SI":
    puedo_permitirmelo = True
elif tienes_dinero_input == "NO":
    puedo_permitirmelo = False
else:
    print("no se que quisiste decir pero supongo que no")
    apetece_helado = False

esta_senor_input = input("esta el senor de los helados si / no").upper()

if esta_senor_input == "SI":
    esta_seor = True
elif esta_senor_input == "NO":
    esta_seor = False
else:
    print("no se que quisiste decir pero supongo que no")
    esta_seor = False

esta_tia_iput = input("esta tu tia? si/no").upper()

if esta_tia_iput == "SI":
    puedo_permitirmelo = True
elif esta_tia_iput == "NO":
    puedo_permitirmelo = False
else:
    print("no se que quisiste decir pero supongo que no")
    puedo_permitirmelo = False


apetece_helado = apetece_helado_input == "SI"
puedo_permitirmelo = tienes_dinero_input == "SI" or esta_tia_iput == "SI"
esta_seor = esta_senor_input == "SI"


if apetece_helado and puedo_permitirmelo and esta_seor:
    print("comete un helado")
else:
    print("pues nada")



