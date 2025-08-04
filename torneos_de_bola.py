#########################################################################
# TORNEOS DE BOLA                                                       #
#########################################################################

#########################################################################
# MÓDULOS                                                               #
#########################################################################
import os # para usar system("cls") /clear screen
import pickle #modulo para archivos
import smtplib # modulo para enviar correo
import ssl #protocolo correo
from email.message import EmailMessage # envia el correo

#########################################################################
# FUNCIONES                                                             #
#########################################################################

#########################################################################
# OPCIÓN REGISTRAR ÁREAS                                                #
#########################################################################

# AGREGAR EQUIPOS
# Entradas: cantidad de equipos
# Salidas: lista de lso equipos del torneo con sus iniciales
def agregar_equipos():

    diccionario={}#en esta variable se guardan todos los equipos existentes
    
    configuracion=open("configuración.dat","r")
    lineas=configuracion.readlines()
    for i in lineas:#busca en la configuracion la cantidad de equipos
        if "Cantidad de equipos participantes: " in i:
            numero=int(i[35:])
    configuracion.close()
            
    
    
    while True:
        try:
            equipos=open("equipos.dat","rb")
            diccionario=pickle.load(equipos)
            if len(diccionario)==numero: #si la cantidad de equipos es la misma que la configuracion regresa al menu anterior
                input("│\n│YA LOS EQUIPOS ESTAN COMPLETOS DE ACUERDO A LA CONFIGURACION")
                equipos.close()
                return
            else:
                equipos.close()
        except EOFError:
            equipos.close()
        os.system("cls")
        print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                              AGREGAR EQUIPOS                                │""")
        #lee el codigo del equipo
        while True:
            try:
                codigo_equipo = input("│Código del equipo: ")
                if codigo_equipo == "C":
                    return
                largo_codigo = len(codigo_equipo)
                if largo_codigo == 3:
                    if codigo_equipo in diccionario:
                        input("ESTE CODIGO DE EQUIPOS YA ESTA EN LA LISTA")
                    else:
                        break
                else:
                    input("│EL CODIGO DEL EQUIPO DEBE SER UNA PALABRA DE 3 LETRAS ")
            except:
                input("│EL CODIGO DEL EQUIPOS DEBE SER UNA PALABRA DE 3 LETRAS")
        # leer nombre del equipo
        while True:
                repetir=0
                nombre_equipo = input("│Nombre del equipo: ")
                largo_nombre=len(nombre_equipo)
                if largo_nombre >= 3 and largo_nombre <= 40:
                    for i in diccionario:
                        codigo=diccionario[i]
                        if nombre_equipo in codigo:
                            repetir=1
                            input("ESTE NOMBRE DE EQUIPO YA ESTA SELECCIONADO")
                    if repetir==0:
                        break
                else:
                    input("│EL NOMBRE DEL EQUIPOS DEBE DE TENER DE 3 A 40 LETRAS ")
        # leer posicion en el escalafon
        while True:
                repetir=0
                posicion_equipo = int(input("│Posición en el escalafón: "))
                if isinstance(posicion_equipo, int) and posicion_equipo >= 1:
                    for i in diccionario:
                        codigo=diccionario[i]
                        if posicion_equipo in codigo:
                            repetir=1
                            input("ESTA POSICION YA ESTA ASIGNADA A UN EQUIPO")
                    if repetir==0:
                        break
                else:
                    input("│LA POSICION DEL EQUIPO TIENE QUE SER UN NUMERO IGUAL O MAYOR A 1 ")
        #OPCIONES DE CONFIRMAR O RECHAZAR LO INGRESADO
        while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    diccionario[codigo_equipo]=(nombre_equipo,posicion_equipo)
                    equipo=open("equipos.dat","wb")
                    pickle.dump(diccionario,equipo)
                    equipo.close()
                    break
                if opcion == "C":
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")


# CONSULTAR EQUIPOS
# Entradas: iniciales equipo
# Salidas: info del equipo

def consultar_equipos():
    while True:
        os.system("cls")
        print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                             CONSULTAR EQUIPOS                               │""")
        #lee el codigo del equipo
        while True:
            try:#revisa si ya se crearon los equipos
                diccionario_equipos=open("equipos.dat","rb")
                diccionario=pickle.load(diccionario_equipos)
            except:
                input("│NO HAY EQUIPOS AGREGADOS")
                return
            try:#busca el codigo en los equipos
                codigo_equipo = input("│Código del equipo: ")
                if codigo_equipo == "C":
                    diccionario_equipos.close()
                    return
                if codigo_equipo in diccionario:
                    info=diccionario[codigo_equipo]
                    print("│Nombre del equipo: ",info[0])
                    print("│Posición en el escalafón: ",info[1])
                    break
                else:
                    input("│EL CODIGO DEL EQUIPO NO EXISTE ")
            except:
                input("│EL CODIGO DEL EQUIPO NO EXISTE")
        #OPCIONES DE CONFIRMAR O RECHAZAR LO INGRESADO
        while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR ")
                if opcion == "A":
                    diccionario_equipos.close()
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")


# ELIMINAR EQUIPOS
# Entradas: iniciales equipo
# Salidas: info del equipo

def eliminar_equipos():
    while True:
        os.system("cls")
        print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                             CONSULTAR EQUIPOS                               │""")
        #lee el codigo del equipo
        while True:
            try:#revisa si ya se crearon los equipos
                diccionario_equipos=open("equipos.dat","rb")
                diccionario=pickle.load(diccionario_equipos)
                diccionario_equipos.close()
            except:
                print("NO HAY EQUIPOS AGREGADOS")
            try:#imprime la info
                codigo_equipo = input("│Código del equipo: ")
                if codigo_equipo == "C":
                    return
                if codigo_equipo in diccionario:
                    break
                else:
                    input("│EL CODIGO DEL EQUIPO NO EXISTE ")
            except:
                input("│EL CODIGO DEL EQUIPO NO EXISTE")
        #OPCIONES DE CONFIRMAR O RECHAZAR LO INGRESADO
        while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    del diccionario[codigo_equipo]#borra de la lista el codigo
                    diccionario_equipos=open("equipos.dat","wb")
                    pickle.dump(diccionario,diccionario_equipos)
                    diccionario_equipos.close()
                    break
                if opcion == "C":
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# AGREGAR Resultados
# Entradas: Calendario
# Salidas: Equipos con lso resultados del juego
def agregar_resultado():
    while True:
        esta=0# es una variable curiosa que la llame asi porque literalmente me ayuda a saber si una variable esta en listas, NO BORRAR que se jode toda una parte 
        partido=[]
        try:#verifica que haya un calendario de juego
            equipos=open("juegos.dat","rb")
            diccionario=pickle.load(equipos)
        except EOFError:
            equipos.close()
            input("│\n│Primero cree el calendario de juegos")
            return
        try:#si ya esta la lista de juegos la carga, si no la crea
            equipos=open("juegos.dat","rb")
            diccionario=pickle.load(equipos)
            resultados=pickle.load(equipos)
            equipos.close()
        except EOFError:
            resultados=[]
            equipos.close()
        #lee el codigo del equipo
        while True:
            os.system("cls")
            print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                            AGREGAR RESULTADOS                               │""")
            try:# lee codigo de equipo que juega de casa y visita
                codigo_equipo_casa = input("│Código del equipo casa: ")
                if codigo_equipo_casa == "C":
                    return
                codigo_equipo_visita = input("│Código del equipo visita: ")
                if len(codigo_equipo_casa) == 3 and len(codigo_equipo_visita) == 3:
                    partido=(codigo_equipo_casa,codigo_equipo_visita)
                    for i in diccionario:
                        for j in i:
                            if partido==j:
                                esta=1
                    if esta ==0:
                        input("│ESTE JUEGO NO ESTÁ EN EL CALENDARIO, NO SE PUEDE REGISTRAR RESULTADO")
                    else:#verifica si ya existe en la lista resultados
                        esta=0
                        if len(resultados)>0:
                            for i in resultados:
                                rivales=[]
                                for j in i:
                                    rivales.append(j)
                                if (codigo_equipo_casa,codigo_equipo_visita) == tuple(rivales):
                                    esta=1
                        if esta ==1:
                            input("│\n│ESTE JUEGO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")
                        else:
                            partido={codigo_equipo_casa:1,codigo_equipo_visita:1}
                            break
                else:
                    input("│LOS CODIGOS DEL EQUIPO DEBE SER UNA PALABRA DE 3 LETRAS ")
            except:
                input("│EL CODIGO DEL EQUIPOS DEBE SER UNA PALABRA DE 3 LETRAS")
        #leer goles o goleadores de el equipo de casa
        while True:
            juego=[]
            indice=0
            try:
                goles_casa=int(input("│Goles del equipo casa: "))
                goles=goles_casa
                while goles>indice:
                    indice+=1
                    minuto=1
                    try:#lee nombre del goleador y el minuto del gol
                        goleador=input("│Nombre del goleador: ")
                        minuto=int(input("│Minuto del gol: "))
                        if minuto>0:
                            if len(juego)==0:
                                juego=[(goleador,minuto)]
                            else:
                                juego.append((goleador,minuto))
                        else:
                            indice-=1
                            print("ERROR EL MINUTO DEBE SER NUMERO ENTERO MAYOR A 0")
                    except:
                        indice-=1
                        print("ERROR EL MINUTO DEBE SER NUMERO ENTERO")
                momentaneo=juego
                juego=(goles_casa,tuple(momentaneo))
                momentaneo=juego
                juego=(codigo_equipo_casa,momentaneo)
                partido[codigo_equipo_casa]=tuple(juego)
                break
            except ValueError:
                input("\n ERROR LOS GOLES DEL EQUIPO DE CASA DEBE SER UN NUMERO ENTERO")
                    
        #leer goles o goleadores de el equipo de visita
        while True:
            juego=[]
            indice=0
            try:
                goles_visita=int(input("│Goles del equipo visita: "))
                goles=goles_visita
                while goles>indice:
                    indice+=1
                    minuto=1
                    try:#lee nombre del goleador y el minuto del gol
                        goleador=input("│Nombre del goleador: ")
                        minuto=int(input("│Minuto del gol: "))
                        if minuto>0:
                            if len(juego)==0:
                                juego=[(goleador,minuto)]
                            else:
                                juego.append((goleador,minuto))
                        else:
                            indice-=1
                            print("ERROR EL MINUTO DEBE SER NUMERO ENTERO MAYOR A 0")
                    except:
                        indice-=1
                        print("ERROR EL MINUTO DEBE SER NUMERO ENTERO")
                momentaneo=juego
                juego=(goles_visita,tuple(momentaneo))
                momentaneo=juego
                juego=(codigo_equipo_visita,momentaneo)
                partido[codigo_equipo_visita]=tuple(juego)
                break
            except ValueError:
                input("\n ERROR LOS GOLES DEL EQUIPO DE CASA DEBE SER UN NUMERO ENTERO")
        #OPCIONES DE CONFIRMAR O RECHAZAR LO INGRESADO
        while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    resultados.append(partido)
                    diccionario_partidos=open("juegos.dat","wb")
                    pickle.dump(diccionario,diccionario_partidos)
                    pickle.dump(resultados,diccionario_partidos)
                    diccionario_partidos.close()
                    break
                if opcion == "C":
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")


# AGREGAR Resultados
# Entradas: Calendario
# Salidas: Equipos con los resultados del juego
def consultar_resultado():
    esta=0# es una variable curiosa que la llame asi porque literalmente me ayuda a saber si una variable esta en listas, NO BORRAR que se jode toda una parte
    while True:
        try:#carga la lista de los resultados
            equipos=open("juegos.dat","rb")
            diccionario=pickle.load(equipos)
            resultados=pickle.load(equipos)
            equipos.close()
        except EOFError:
            equipos.close()
            input("PRIMERO DEBE HABER RESULTADOS DE ALGUN PARTIDO")
            return
        #lee el codigo del equipo
        while True:
            os.system("cls")
            print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                            CONSULTAR RESULTADOS                             │""")
            try:# lee codigo de equipo que juega de casa y visita
                codigo_equipo_casa = input("│Código del equipo casa: ")
                if codigo_equipo_casa == "C":
                    return
                codigo_equipo_visita = input("│Código del equipo visita: ")
                if len(codigo_equipo_casa) == 3 and len(codigo_equipo_visita) == 3:
                    partido=(codigo_equipo_casa,codigo_equipo_visita)
                    for i in resultados:
                        rivales=[]
                        for j in i:
                            rivales.append(j)
                        if partido == tuple(rivales):
                            consulta=i
                            esta=1
                    if esta ==0:
                        input("│\n│ESTE RESULTADO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")
                    else:
                        break
                else:
                    input("│LOS CODIGOS DEL EQUIPO DEBE SER UNA PALABRA DE 3 LETRAS ")
            except:
                input("│EL CODIGO DEL EQUIPOS DEBE SER UNA PALABRA DE 3 LETRAS")
        while True:#carga los goles con el goleador
            print("│\n│Goles del equipo casa:",consulta[codigo_equipo_casa][1][0])
            jugadores=consulta[codigo_equipo_casa][1][1]
            for i in jugadores:
                print("│Nombre goleador:",i[0])
                print("│Minuto del gol:",i[1])
            print("│\n│Goles del equipo casa:",consulta[codigo_equipo_visita][1][0])
            jugadores=consulta[codigo_equipo_visita][1][1]
            for i in jugadores:
                print("│Nombre goleador:",i[0])
                print("│Minuto del gol:",i[1])
            break
        #OPCION DE ACEPTAR PARA CONTINUAR
        while True:
            opcion = input("│                     OPCIÓN     <A>ACEPTAR ")
            if opcion == "A":
                break
            input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
            

# ELIMINAR Resultados
# Entradas: Calendario
# Salidas: Equipos con lso resultados del juego actualizada
def eliminar_resultado():
    esta=0# es una variable curiosa que la llame asi porque literalmente me ayuda a saber si una variable esta en listas, NO BORRAR que se jode toda una parte
    while True:
        try:#carga la lista de los resultados
            equipos=open("juegos.dat","rb")
            diccionario=pickle.load(equipos)
            resultados=pickle.load(equipos)
            equipos.close()
        except EOFError:
            equipos.close()
            input("PRIMERO DEBE HABER RESULTADOS DE ALGUN PARTIDO")
            return
        #lee el codigo del equipo
        while True:
            os.system("cls")
            print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                            ELIMINAR RESULTADOS                              │""")
            try:# lee codigo de equipo que juega de casa y visita
                codigo_equipo_casa = input("│Código del equipo casa: ")
                if codigo_equipo_casa == "C":
                    return
                codigo_equipo_visita = input("│Código del equipo visita: ")
                if len(codigo_equipo_casa) == 3 and len(codigo_equipo_visita) == 3:
                    partido=(codigo_equipo_casa,codigo_equipo_visita)
                    for indice,i in enumerate(resultados):
                        rivales=[]
                        for j in i:
                            rivales.append(j)
                        if partido == tuple(rivales):
                            eliminar=indice
                            consulta=i
                            esta=1
                    if esta ==0:
                        input("│\n│ESTE RESULTADO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")
                    else:
                        break
                else:
                    input("│LOS CODIGOS DEL EQUIPO DEBE SER UNA PALABRA DE 3 LETRAS ")
            except:
                input("│EL CODIGO DEL EQUIPOS DEBE SER UNA PALABRA DE 3 LETRAS")
        #OPCIONES DE CONFIRMAR O RECHAZAR LO INGRESADO
        while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    resultados.pop(eliminar)#elimina el resultado
                    diccionario_partidos=open("juegos.dat","wb")
                    pickle.dump(diccionario,diccionario_partidos)
                    pickle.dump(resultados,diccionario_partidos)
                    diccionario_partidos.close()
                    break
                if opcion == "C":
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Enviar correo
# Entradas: lista resultados
# Salidas: envio de correo
def envio_correo(torneo,nombre):
    try:
        # correo del programa para enviar los resultados
        email_sender = 'correobotprograma@gmail.com'
        email_password = 'osetwcyhzowysnbc'
        #pregunta el correo al que va a enviar la informacion
        while True:
            email_receiver = input("│Correo al que quiere mandar los resultados:")
            if "@" in email_receiver:
                break
            elif "C" == email_receiver:
                return
            else:
                input("Correo invalido, revise el @")
        #carga y acomoda los resultados
        subject = "Torneo: "+nombre
        print("│"+nombre)
        imprimir="Tabla posiciones\nEquipo JJ JG JE JP GF GC GD PUNTOS"
        for equipo, letras in torneo:
            imprimir+=f"\n{equipo} {letras['JJ']} {letras['JG']} {letras['JE']} {letras['JP']} {letras['GF']} {letras['GC']} {letras['GD']} {letras['PUNTOS']}"
        print(imprimir)
        body=imprimir

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # CAPA DE SEGURIDAD PARA EL CORREO
        context = ssl.create_default_context()

        # el codigo se loguea en el gmail para enviar el correo
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        input("\nCorreo enviado\nprecione ENTER para continuar")
    except:
        input("Hubo un error en el sistema intente mas tarde")
        return

                    
#########################################################################                    
# Menu configuración del torneo                                         #                          
def menu_config_torneo():
        while True:
            os.system("cls")
            print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                          CONFIGURACION DEL TORNEO                           │""")
            # leer config nombre torneo
            while True:
                try:
                    nombre_torneo = input("│Nombre del torneo: ")
                    if nombre_torneo == "C":
                        return
                    largo_nombre = len(nombre_torneo)
                    if largo_nombre >= 5 and largo_nombre <= 40:
                        break
                    else:
                        input("│NOMBRE DEL TORNEO DEBE SER UNA PALABRA ENTRE 5 Y 40 ")
                except:
                    input("│NOMBRE DEL TORNEO DEBE SER UNA PALABRA ENTRE 5 Y 40 ")
            # leer config numero participantes torneo
            while True:
                cantidad_equipos = int(input("│Cantidad de equipos participantes: ")) 
                if isinstance(cantidad_equipos, int) or int(cantidad_equipos) >= 2:
                    break
                else:
                    input("│LA CANTIDAD DE EQUIPOS DEBEN SER UN NUMERO ENTERO Y MINIMO DOS EQUIPOS ")
            # leer config cantidad de equipos que clasifican
            while True:
                cantidad_clasificados = int(input("│Cantidad de equipos que clasifican: ")) 
                if isinstance(cantidad_clasificados, int) or int(cantidad_clasificados) >= 1 and int(cantidad_clasificados) < cantidad_equipos:
                    break
                else:
                    input("│LA CANTIDAD DE EQUIPOS CLASIFICADOS DEBE SER UN NUMERO MAYOR A 1 Y MENOR A LA CANTIDAD DE EQUIPOS PARTICIPANTES ")
            # leer puntos que dan por victoria
            while True:
                puntos_partido_ganado = int(input("│Puntos ganados por cada partido ganado: "))
                if isinstance(puntos_partido_ganado, int) or puntos_partido_ganado >= 1:
                    break
                else:
                    input("│LA CANTIDAD DE PUNTOS DADOS AL GANAR TIENE QUE SER UN NUMERO ENTERO MAYOR A 1 ")
            # leer puntos que dan por empate
            while True:
                puntos_partido_empatado = int(input("│Puntos ganados por cada partido empatado: "))
                if isinstance(puntos_partido_empatado, int):
                    if puntos_partido_empatado >= 1 and puntos_partido_empatado < puntos_partido_ganado:
                        break
                    else:
                        input("│LA CANTIDAD DE PUNTOS DADOS AL EMPATAR TIENE QUE SER UN NUMERO ENTERO MAYOR A 1 Y MENOR A LOS PUNTOS QUE DAN AL GANAR")
                else:
                    input("│LA CANTIDAD DE PUNTOS DADOS AL EMPATAR TIENE QUE SER UN NUMERO ENTERO MAYOR A 1 Y MENOR A LOS PUNTOS QUE DAN AL GANAR")
            # leer opción y guardar datos !!!!
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    configuracion=open("configuración.dat","w")
                    configuracion.write("Nombre del torneo: ")
                    configuracion.write(str(nombre_torneo))
                    configuracion.write("\nCantidad de equipos participantes: ")
                    configuracion.write(str(cantidad_equipos))
                    configuracion.write("\nCantidad de equipos que clasifican: ")
                    configuracion.write(str(cantidad_clasificados))
                    configuracion.write("\nPuntos ganados por cada partido ganado: ")
                    configuracion.write(str(puntos_partido_ganado))
                    configuracion.write("\nPuntos ganados por cada partido empatado: ")
                    configuracion.write(str(puntos_partido_empatado))
                    configuracion.close()
                    return
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

                               
#########################################################################                    
# Registrar equipos                                                     #                          
def menu_registrar_equipos():
    while True:
        os.system("cls")
        print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                             REGISTRAR EQUIPOS                               │
│                                                                             │
│ 1. Agregar equipos                                                          │
│ 2. Consultar equipos                                                        │
│ 3. Modificar equipos                                                        │
│ 4. Eliminar equipos                                                         │
│ 0. Fin                                                                      │""")
        opcion = input("│    OPCIÓN ")
        # leer menu registro de equipos
        match opcion:
            case "1":
                agregar_equipos()
            case "2":
                consultar_equipos()
            case "3":
                input("│Para modificar un equipo eliminelo y lo crea de nuevo con la info actualizada")
            case "4":
                eliminar_equipos()
            case "0":
                return


#########################################################################                    
# Crea calendario de juegos                                             #                          
def crear_calendario_juegos():
        os.system("cls")
        vuelta=[]
        def generar_calendario(equipos):#funcion encargada de generar el calendario de equipo
            total_equipos = len(equipos)
            if total_equipos % 2 != 0:
                equipos.append("Fecha Libre")
                total_equipos += 1

            num_jornadas = total_equipos - 1
            num_partidos_por_jornada = total_equipos // 2

            for i in range(num_jornadas):
                fecha=[]
                for j in range(num_partidos_por_jornada):
                    equipo_local = equipos[j]
                    equipo_visitante = equipos[total_equipos - 1 - j]

                    if equipo_local != "Fecha Libre" and equipo_visitante != "Fecha Libre": # si el numero de equipos es impar se usa fecha libre para el que quede sin jugar en la fecha
                        fecha.append((equipo_local,equipo_visitante))
                vuelta.append(tuple(fecha))
            

                # Rotar los equipos
                ultimo_equipo = equipos.pop()
                equipos.insert(1, ultimo_equipo)

            vuelta_original=()
            vuelta_original=vuelta.copy()
            for i in vuelta_original:
                fecha_reversa=[]
                for j in i:
                    reversa_partido=list(j)
                    reversa_partido.reverse()
                    fecha_reversa.append(tuple(reversa_partido))
                vuelta.append(tuple(fecha_reversa))
                
                
            archivo=open("juegos.dat", "wb")
            pickle.dump(vuelta,archivo)
            archivo.close()

        # Carga la lista de equipos desde el archivo equipos.dat
        with open("equipos.dat", "rb") as equipos_file:
            diccionario = pickle.load(equipos_file)
        equipos_torneo = list(diccionario.keys())
        generar_calendario(equipos_torneo)


#########################################################################                    
# Menu Consultar calendario de juegos                                   #                          
def consultar_calendario_juegos():#busca la info existente
    os.system("cls")
    archivo=open("juegos.dat", "rb")
    campeonato=pickle.load(archivo)
    archivo.close()
    configuracion=open("configuración.dat","r")
    lineas=configuracion.readlines()
    for i in lineas:
        if "Nombre del torneo: " in i:
            nombre=i[19:]
    configuracion.close()
    
    print("""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│  """,nombre)
    for fecha,i in enumerate(campeonato, start=1):#imprime todos los partidos en las fechas
        print("│Fecha",fecha)
        for j in i:
            print("│",j[0],"-",j[1])
            
    while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR ")
                if opcion == "A":
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

        
#########################################################################                    
# Menu registrar resultados                                             #                          
def menu_registrar_resultados():
    while True:
        os.system("cls")
        print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                            REGISTRAR RESULTADOS                             │
│                                                                             │
│ 1. Agregar resultados                                                       │
│ 2. Consultar resultados                                                     │
│ 3. Modificar resultados                                                     │
│ 4. Eliminar resultados                                                      │
│ 0. Fin                                                                      │""")
        opcion = input("│    OPCIÓN ")
        # leer menu registro de equipos
        match opcion:
            case "1":
                agregar_resultado()
            case "2":
                consultar_resultado()
            case "3":
                input("│Para modificar un resultado eliminelo y lo crea de nuevo con la info actualizada")
            case "4":
                eliminar_resultado()
            case "0":
                return


#########################################################################                    
# Menu Tabla posiciones                                                 #                          
def menu_tabla_posiciones():
    while True:
        torneo=[]
        try:#busca info existente sobre los puntos por ganar y empatar
            diccionario=open("configuración.dat","r")
            configuracion=diccionario.readlines()
            for i in configuracion:
                if "Puntos ganados por cada partido ganado: " in i:
                    puntos_por_ganar=i[40:]
                elif "Puntos ganados por cada partido empatado: " in i:
                    puntos_por_empatar=i[42:]
                elif "Nombre del torneo: " in i:
                    nombre=i[19:]
            diccionario.close()
        except:
            #restriccion para poder funcionar
            print("Configure los goles por ganas y por empatar antes de continuar")
            return
        try:#carga los resultados de los partidos y informacion
            diccionario=open("equipos.dat","rb")
            participantes=pickle.load(diccionario)
            diccionario=open("juegos.dat","rb")
            todos_los_juegos=pickle.load(diccionario)
            juegos=pickle.load(diccionario)
            diccionario.close()
        except:
            diccionario.close()
            input("PRIMERO DEBE HABER RESULTADOS DE ALGUN PARTIDO")
            return
            
        os.system("cls")
        print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                              TABLA POSICIONES                               │
│                                                                             │""")
        
        for equipo in participantes:#por cada pais se establecen las variables correspondientes en 0
                jj=0#juegos jugados
                jg=0#juegos ganados
                je=0#juegos empatados
                jp=0#juegos perdidos
                gf=0#goles a favor
                gc=0#goles en contra
                gd=0#goles de diferencia
                puntos=0#puntos totales
                resultado={}
                for i in juegos:
                    equipos=[]
                    if equipo in i:
                        for j in i:#revisa toda la lista de juegos y de resultados a ver si ya esta el resultados del partido y si esta anota el aprtido jugado
                            if equipo in j:
                                datos_equipo=i[j]
                            else:
                                datos_equipos_2=i[j]
                        jj+=1
                        if datos_equipo[1][0] > datos_equipos_2[1][0]:#resultado del partido
                            jg+=1 
                        elif datos_equipo[1][0] == datos_equipos_2[1][0]:
                            je+=1
                        else:
                            jp+=1
                        gf+=datos_equipo[1][0]#goles a favor en el partido
                        gc+=datos_equipos_2[1][0]#goles en contra en el partido
                        gd=gf-gc
                        if gd > 0:
                            gd="+"+str(gd)
                        puntos=jg*puntos_por_ganar+je*puntos_por_empatar#saca los puntos
                    if len(resultado)==0:#asigna las variables al diccionario
                        resultado["JJ"]=jj
                        resultado["JG"]=jg
                        resultado["JE"]=je
                        resultado["JP"]=jp
                        resultado["GF"]=gf
                        resultado["GC"]=gc
                        resultado["GD"]=gd
                        resultado["PUNTOS"]=puntos
                    else:#actualiza los contrenidos del diccionario
                        resultado["JJ"]+=jj
                        resultado["JG"]+=jg
                        resultado["JE"]+=je
                        resultado["JP"]+=jp
                        resultado["GF"]+=gf
                        resultado["GC"]+=gc
                        resultado["GD"]+=gd
                        resultado["PUNTOS"]+=puntos
                torneo.append((equipo,resultado))
        envio_correo(torneo,nombre)#pide la info para enviar el correo
        return


#########################################################################                    
# Menu Tabla posiciones                                                 #                          
def menu_tabla_goleadores():
        jugadores=[]
        try:#carga info existente
            diccionario=open("equipos.dat","rb")
            participantes=pickle.load(diccionario)
            diccionario=open("juegos.dat","rb")
            juegos_totales=pickle.load(diccionario)
            juegos=pickle.load(diccionario)
            diccionario.close()
        except:
            diccionario.close()
            input("PRIMERO DEBE HABER RESULTADOS DE ALGUN PARTIDO")
            return
            
        os.system("cls")
        print(""""
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TORNEOS DE BOLA                                │
│                              TABLA GOLEADORES                               │
│                                                                             │""")
        
        for partido in juegos:
            for sigla in partido:
                equipo=partido[sigla]
                pais=participantes[equipo[0]][0]#verifica el pais del goleador con el nombre que esta revisando
                for goleadores in equipo[1][1]:
                    if len(jugadores)==0:
                        jugadores.append([goleadores[0],pais,1])
                    else:
                        for indice,i in enumerate(jugadores):
                            esta=0
                            pais_jugador=i[1]
                            if goleadores[0] == i[0] and i[1]==pais: # si el pais del jugador y el nombre es el mismo se le agrega un gol
                                jugadores[indice][2]+=1
                                esta=1
                                break
                        if esta==0:#si no es el mismo se agrega a la lista el jugador con diferente pais
                            jugadores.append([goleadores[0],pais,1])
        print("│Jugador    Equipo    Goles")   
        for i in jugadores:
            print("│",i[0],"  ",i[1],"  ",i[2])#imprime los resultados (NOMBRE-PAIS-GOLES)
        input("│\n│Preciones ENTER para continuar")
        
        diccionario=open("juegos.dat","wb")
        pickle.dump(juegos_totales,diccionario)
        pickle.dump(juegos,diccionario)
        pickle.dump(jugadores,diccionario)
        diccionario.close()


#########################################################################
# FUNCIÓN PRINCIPAL                                                     #
#########################################################################

# Menú principal
while True:
    os.system("cls")
    print("""



┌─────────────────────────────────────────────────────────────────────────────┐
│                               TORNEO DE BOLA                                │
│                                                                             │
│ 1. Configuración del torneo                                                 │
│ 2. Registrar equipos                                                        │
│ 3. Crear calendario de juegos                                               │
│ 4. Consultar calendario de juegos                                           │
│ 5. Registrar los resultados                                                 │
│ 6. Tabla de posiciones                                                      │
│ 7. Tabla de goleadores                                                      │
│ 8. Ayuda                                                                    │
│ 9. Acerca de                                                                │
│ 0. Fin                                                                      │""")
    opcion = input("│    OPCIÓN ")
    match opcion: 
        case "1":
            menu_config_torneo()
        case "2":
            configuracion=open("configuración.dat","r")
            if len(configuracion.read())>0:
                menu_registrar_equipos()
            else:
                input("PRIMERO TIENES QUE CONFIGURAR EL TORNEO")
            configuracion.close()
        case "3":
            crear_calendario_juegos()
        case "4":
            consultar_calendario_juegos()
        case "5":
            menu_registrar_resultados()
        case "6":
            menu_tabla_posiciones()
        case "7":
            menu_tabla_goleadores()
        case "8":
            input("│En el .zip del programa puedes encontrar el manual de usuario del programa")
        case "9":
            input("""
│PROGRAMA: TORNEO DE BOLA
│VERSION: 1.0
│FECHA CREACION: 13/05/2024
│AUTOR: JOSHUA VALVARDE ARGUEDAS
│
│Precione Enter para continuar""")
        case "0":
            print("FIN DEL PROGRAMA")
            break
            


