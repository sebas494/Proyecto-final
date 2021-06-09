print("Parqueadero pontificia universidad javeriana cali\n" )
def opcion_1 (opciones1):
    import json                      
    archivo = open("usuarios.json", "r+", encoding = "utf-8")
    usuariosJson = json.load(archivo)
    #archivo2=open("Pisos.json", "r+", encoding = "utf-8")
    #PisosJson = json.load(archivo2)
    archivo3=open("Pisos_ocupados.json", "r+", encoding = "utf-8")
    PisosJson_ocupados = json.load(archivo3)
    while opciones1!=-1:
        opciones=eval(input("¿Que desea hacer?\n1)Permitir el ingreso de vehiculos\n2)Registrar un vehiculo\n3)Retirar un vehiculo del estacionamiento\n4)Generear un conjunto de estadisticas para la Oficina de Servicios Generales de la Universidad\n\n Escriba aqui el numero dependiendo de la opcion= "))
        #Si el usuario marca la opcion 1 del menu.
        if opciones==1: 
            #Ingresa el numero de la placa
            placa=input("Ingrese el numero de la placa: ")
            numero_comprobante=0

            for piso in PisosJson_ocupados:
                w=PisosJson_ocupados[piso]
                for parqueaderos in w:
                    for parqueadero in parqueaderos:
                        if parqueadero[1]!=0:
                            if parqueadero[1][0]==placa:
                                numero_comprobante+=1          
            
            if numero_comprobante==1:
                return opcion_1(eval(input("Ya tienes un vehiculo en el parqueadero, no puedes ingresar mas\nIngresa 1 para volver al menu principal: ")))
            else:
                def buscar_placa (usuariosJson, placa):
                    for buscar_placa in usuariosJson["usuarios"]:
                        for buscar_listas in usuariosJson:
                            if buscar_placa[3]==placa:               
                                return True

                buscar_placa(usuariosJson,placa)


                fila=0
                columna=0
                nombre=""
                tipo_usuario_parquear=""
                if buscar_placa(usuariosJson,placa)==True:
                    print("¡Bienvenido Javeriano, ya estas registrado en nuestra base de datos!")
                    
                    for buscar in range (len(usuariosJson["usuarios"])):
                        for encontrar_elemento in range (6):
                            if usuariosJson["usuarios"][buscar][encontrar_elemento]==placa:
                                fila=buscar
                                columna=encontrar_elemento
                                break            
                        
                    if(usuariosJson["usuarios"][fila][4])=="Discapacitado":
                        tipo_vehiculo=4
                    elif(usuariosJson["usuarios"][fila][4])=="Motocicleta":
                        tipo_vehiculo=3
                    elif(usuariosJson["usuarios"][fila][4])=="Automóvil Eléctrico":
                        tipo_vehiculo=2
                    elif(usuariosJson["usuarios"][fila][4])=="Automóvil":
                        tipo_vehiculo=1
            
                    elif(usuariosJson["usuarios"][fila][2])=="Personal Administrativo":
                        tipo_usuario_parquear="Personal Administrativo"
                    elif(usuariosJson["usuarios"][fila][2])=="Profesor":
                        tipo_usuario_parquear="Profesor"
                    elif(usuariosJson["usuarios"][fila][2])=="Estudiante":
                        tipo_usuario_parquear="Estudiante"

                else:
                    print("\nSeras catalogado como visitante y tendras un pago diario, ya que esta placa no esta registrada en la base de datos.\n")
                
                identificacion=eval(input("Ingrese su numero de identificacion: "))
                tipo_vehiculo=eval(input("¿Que tipo de vehiculo es?\n1)Automovil\n2)Automovil electrico\n3)Motocicleta\n4)Discapacitado\nEscriba de acuerdo a la letra asignada en las opciones: "))
                nombre_vehiculo=""
                if tipo_vehiculo==1:                  
                    nombre_vehiculo="Automovil"
                elif tipo_vehiculo==2:                  
                    nombre_vehiculo="Automovil electrico"
                elif tipo_vehiculo==3:
                    nombre_vehiculo="Motocicleta"
                elif tipo_vehiculo==4:
                    nombre_vehiculo="Discapacitado"
                variable_nombre=nombre_vehiculo
                tipo_usuario_parquear="Visitante"

                
                
            #Se evalua piso por piso el numero total de estacionamientos disponibles de acuerdo al tipo de vehiculo ingresado  
            res=0
            for cada_piso in PisosJson_ocupados:
                llave_piso=PisosJson_ocupados[cada_piso]
                for lista_parqueadero in llave_piso:
                    for espacios in lista_parqueadero:
                        if tipo_vehiculo==1:
                            if espacios[0]==1:
                                res+=1              
                        elif tipo_vehiculo==2:
                            if espacios[0]==1 or 2:               
                                res+=1
                        elif tipo_vehiculo==3:
                            if espacios[0]==3:
                                res+=1            
                        elif tipo_vehiculo==4:
                            if espacios[0]==1 or 4:
                                res+=1               

            #Se valida que hayan parqueaderos disponibles para el tipo de vehiculo ademas que el usuario selecciona el piso que desea visualizar.

            if res>0:
                print("\nEl numero total para de parqueaderos disponibles para el tipo vehiculo que se quiere ingresar es de :"+str(res))     
                
                seleccione_piso=eval(input("\nIngrese el numero de piso que quiere visualizar.\n Piso #1:(1)\nPiso #2:(2)\nPiso #3:(3)\nPiso #4:(4)\nPiso #5:(5)\nPiso #6:(6)\nIngrese aqui el numero del piso: "))
                
                print("\nLas posiciones llenas o no disponibles estan marcadas con (X) y las vacias y disponibles con (0).\n")
                
                seleccionado=""
                if seleccione_piso==1:
                    seleccionado="Piso1"
                elif seleccione_piso==2:
                    seleccionado="Piso2"
                elif seleccione_piso==3:
                    seleccionado="Piso3"
                elif seleccione_piso==4:
                    seleccionado="Piso4"   
                elif seleccione_piso==5:
                    seleccionado="Piso5"
                elif seleccione_piso==6:
                    seleccionado="Piso6"       

                if seleccione_piso<=5:
                    if tipo_vehiculo==1:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(10):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==1:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""
                    if tipo_vehiculo==2:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(10):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==1 or 2:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""
                    if tipo_vehiculo==3:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(10):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==3:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""
                    if tipo_vehiculo==4:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(10):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==1 or 4:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""
                else:
                    if tipo_vehiculo==1:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(5):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==1:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""
                    if tipo_vehiculo==2:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(5):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==1 or 2:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""
                    if tipo_vehiculo==3:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(5):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==3:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""
                    if tipo_vehiculo==4:
                        a=""
                        print("Piso #"+str(seleccione_piso)+"\n")
                        for ver in range(5):
                            for mejor in range(10):                        
                                if PisosJson_ocupados[seleccionado][ver][mejor][0]==1 or 4:               
                                    a+=str(0) +"\t"
                                else:
                                    a+="x" +"\t"
                            print(a)
                            a=""

                def posicion_parqueo(b):
                    while b!=0:                
                        print("\n¿En que posicion desea parquear su vehiculo?\n")
                        ingrese_fila=eval(input("Ingrese el numero de la fila: "))
                        ingres_columna=eval(input("Ingrese columna: "))
                        if PisosJson_ocupados[seleccionado][ingrese_fila][ingres_columna][0]==tipo_vehiculo:
                            print("¡Efectivamente esta desocupado para este tipo de vehiculo!")
                            parquear_usuario=[placa,variable_nombre,tipo_usuario_parquear,"Diario"]
                            PisosJson_ocupados[seleccionado][ingrese_fila][ingres_columna][1]=parquear_usuario
                            with open("Pisos_ocupados.json", "w",encoding = "utf-8") as archivo_introducir:
                                json.dump(PisosJson_ocupados,archivo_introducir, indent=4, ensure_ascii=False)  
                                archivo_introducir.close
                                break
                        else:
                            return posicion_parqueo (eval(input("\nEste puesto no le sirve para su tipo de vehiculo\n\nIngrese el numero (2) para volver a escoger un puesto en el mimsmo piso:\nIngrese (0) para volver al menu principal:\n\nDigite su opcion:")))
                
                b=1
                posicion_parqueo(b)
            else:
                print("No hay parqueaderos disponibles para este tipo de vehiculo.")
            
            
            #Se ingresa el tipo de pago 
            print("\n¡Su vehiculo se ha registrado con exito!.\n")
            opciones1=eval(input("Ingrese el numero 1 para volver al menu principal: "))
        
        if opciones==2:
            nombres_registro=str(input("Ingrese su nombre y apellido: "))
            identificacion_registro=eval(input("Ingrese su numero de identificacion: "))
            for buscar in usuariosJson["usuarios"]:
                if buscar[1]==identificacion_registro:
                    print("Este usuario ya esta registrado")                        
                    return opcion_1 (eval(input("Escriba el numero 2 para volver al menu principal= ")))

            Tipo_usuario=eval(input("¿Que tipo de usuario eres?\n1)Estudiante(1)\n2)Profesor(2)\n3)Personal administrativo(3)\nIngrese el numero segun corresponda: "))
            placa_registro=input("Ingrese el numero de placa del vehiculo: ")
            tipo_vehiculo_registro=eval(input("¿Que tipo de vehiculo es?\n1)Automovil\n2)Automovil electrico\n3)Motocicleta\n4)Discapacitado\nEscriba de acuerdo a la letra asignada en las opciones: "))
            nombre_vehiculo=""
            if tipo_vehiculo_registro==1:                  
                nombre_vehiculo="Automovil"
            elif tipo_vehiculo_registro==2:                  
                nombre_vehiculo="Automovil electrico"
            elif tipo_vehiculo_registro==3:
                nombre_vehiculo="Motocicleta"
            elif tipo_vehiculo_registro==4:
                nombre_vehiculo="Discapacitado"
            variable_nombre=nombre_vehiculo
            plan_pago=eval( input("Ingrese el tipo de pago\n1)Diario\n2)Mensualidad\nIngrese el numero segun corresponda: "))
            usuario_nuevo_registro=[nombres_registro,identificacion_registro,Tipo_usuario,placa_registro,nombre_vehiculo,plan_pago]
            with open("usuarios.json", "w",encoding = "utf-8") as archivo:
                json.dump(usuario_nuevo_registro, archivo, indent=4, ensure_ascii=False)  
                archivo.close
            print("\n¡Se te registro exitosamente!\n")


        #Si el usuario marca la opcion 2 del menu.
        def opcion_2(num):
            archivo3=open("Pisos_ocupados.json", "r+", encoding = "utf-8")
            PisosJson_ocupados = json.load(archivo3)
            archivo1=open("Pisos.json", "r+", encoding = "utf-8")
            PisosJson = json.load(archivo1)           
            if opciones==3:
                opcion_2_0=0
                while opcion_2_0 !=1:    
                    fila_hallar=0
                    columna_hallar=0
                    piso=0
                    pasar=False
                    placa_retirar=input("Ingrese el numero de la placa del vehiculo que desea retirar: ")             
                    for buscar_pisos in range (6):
                        for buscar_listas in range(10):
                            for buscar_elementos in range(10):
                                if buscar_pisos==1:
                                    if PisosJson_ocupados["Piso1"][buscar_listas][buscar_elementos][1]!=0:
                                        if PisosJson_ocupados["Piso1"][buscar_listas][buscar_elementos][1][0]==placa_retirar:
                                            piso=buscar_pisos
                                            fila_hallar=buscar_listas
                                            columna_hallar=buscar_elementos
                                            pasar=True                        
                                            break
                                elif buscar_pisos==2:
                                    if PisosJson_ocupados["Piso2"][buscar_listas][buscar_elementos][1]!=0:
                                        if PisosJson_ocupados["Piso2"][buscar_listas][buscar_elementos][1][0]==placa_retirar:
                                            piso=buscar_pisos
                                            fila_hallar=buscar_listas
                                            columna_hallar=buscar_elementos
                                            pasar=True                        
                                            break
                                elif buscar_pisos==3:
                                    if PisosJson_ocupados["Piso3"][buscar_listas][buscar_elementos][1]!=0:
                                        if PisosJson_ocupados["Piso3"][buscar_listas][buscar_elementos][1][0]==placa_retirar:
                                            piso=buscar_pisos
                                            fila_hallar=buscar_listas
                                            columna_hallar=buscar_elementos
                                            pasar=True                        
                                            break
                                elif buscar_pisos==4:
                                    if PisosJson_ocupados["Piso4"][buscar_listas][buscar_elementos][1]!=0:
                                        if PisosJson_ocupados["Piso4"][buscar_listas][buscar_elementos][1][1]==placa_retirar:
                                            piso=buscar_pisos
                                            fila_hallar=buscar_listas
                                            columna_hallar=buscar_elementos
                                            pasar=True                        
                                            break
                                elif buscar_pisos==5:
                                    if PisosJson_ocupados["Piso5"][buscar_listas][buscar_elementos][1]!=0:
                                        if PisosJson_ocupados["Piso5"][buscar_listas][buscar_elementos][1][0]==placa_retirar:
                                            piso=buscar_pisos
                                            fila_hallar=buscar_listas
                                            columna_hallar=buscar_elementos
                                            pasar=True                        
                                            break
                                elif buscar_pisos==6:
                                    for buscar_listas in range(5):
                                        for buscar_elementos in range(10):
                                            if PisosJson_ocupados["Piso6"][buscar_listas][buscar_elementos][1]!=0:
                                                if PisosJson_ocupados["Piso6"][buscar_listas][buscar_elementos][1][0]==placa_retirar:
                                                    piso=buscar_pisos
                                                    fila_hallar=buscar_listas
                                                    columna_hallar=buscar_elementos
                                                    pasar=True
                                                    break       
                    
                    if pasar==True:                            
                        print("El vehiculo con esta placa se encuentra en el parqueadero.")
                        tiempo=eval(input("Ingrese el numero de horas que permanecio el vehiculo en el parqueadero: "))
                        pago_total=0
    
                        fila_hallar_usuarios=0
                        for buscar in range (len(usuariosJson["usuarios"])):
                            for encontrar_elemento in range (6):
                                if usuariosJson["usuarios"][buscar][encontrar_elemento]==placa_retirar:
                                    fila_hallar_usuarios=buscar
                                    break            
                                                
                            def retirar(usuariosJson,tiempo,fila_hallar_usuarios):
                                nombre=""
                                if usuariosJson["usuarios"][fila_hallar_usuarios][5]=="Diario" and usuariosJson["usuarios"][fila_hallar_usuarios][2]=="Personal Administrativo":
                                    return(tiempo*1500)                                
                                elif usuariosJson["usuarios"][fila_hallar_usuarios][5]=="Diario" and usuariosJson["usuarios"][fila_hallar_usuarios][2]=="Profesor":
                                    return(tiempo*2000)      
                                elif usuariosJson["usuarios"][fila_hallar_usuarios][5]=="Diario" and usuariosJson["usuarios"][fila_hallar_usuarios][2]=="Estudiante":
                                    return(tiempo*1000)                                                                     
                                else:  
                                    if usuariosJson["usuarios"][fila_hallar_usuarios][5]=="Mensualidad":
                                        return 0
                                

                            retirar(usuariosJson,tiempo,fila_hallar_usuarios)
                            pago_total=(retirar(usuariosJson,tiempo,fila_hallar_usuarios))
                    

                            seleccionado=""
                            if piso==1:
                                seleccionado="Piso1"
                            elif piso==2:
                                seleccionado="Piso2"
                            elif piso==3:
                                seleccionado="Piso3"
                            elif piso==4:
                                seleccionado="Piso4"   
                            elif piso==5:
                                seleccionado="Piso5"
                            elif piso==6:
                                seleccionado="Piso6" 

                            if PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]!=0:
                                PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]=0
                            if PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]!=0:
                                PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]=0
                            if PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]!=0:
                                PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]=0
                            if PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]!=0:
                                PisosJson_ocupados[seleccionado][fila_hallar][columna_hallar][1]=0

                            with open("Pisos_ocupados.json", "w",encoding = "utf-8") as volver_numero:
                                json.dump(PisosJson_ocupados,volver_numero, indent=4, ensure_ascii=False)  
                                volver_numero.close                       
                    else:
                        print("El vehiculo con esta placa NO se encuentra en el parqueadero.")
                        return opcion_2 (eval(input("Ingrese 2 para ingresar otro placa de vehiculo: ")))

                    if pago_total>0:
                        print("El valor total a pagar es de $"+str(pago_total))
                        print("\n¡Muchas gracias por usar nuestros servicios!\n")
                        return opcion_1 (eval(input("Escriba el numero 2 para volver al menu principal= ")))
                    else:
                        print("No debes realizar ningun pago ya que tienes paga la mensualidad.")
                        print("\n¡Muchas gracias por usar nuestros servicios!\n")
                        return opcion_1 (eval(input("Escriba el numero 2 para volver al menu principal= ")))
        num=0
        opcion_2(num)
        
        if opciones==4:
            Opciones4_1=eval(input("¿Que reporte desea generar?\n1)Reporte con la cantidad de vehículos estacionados según el tipo de usuario\n2)Reporte de cantidad de vehículos estacionados según el tipo de vehículo.\n3)Reporte que indique el porcentaje de ocupación del parqueadero\nDigite el numero segun la opcion"))
            personal_administrativo=0
            profesor=0
            estudiante=0
            visitante=0

            motocicleta=0
            automovil=0
            Automovil_electrico=0
            discapacitado=0

            piso1=0
            piso2=0
            piso3=0
            piso4=0
            piso5=0
            piso6=0
            ocuapcion_total=0
            for pisos in PisosJson_ocupados: 
                variable=PisosJson_ocupados[pisos]
                for parqueaderos in variable:
                    for parqueadero in parqueaderos:
                        if parqueadero[1]!=0:
                            ocuapcion_total+=1
                            if pisos=="Piso1": 
                                piso1+=1
                            elif pisos=="Piso2":
                                piso2+=1
                            elif pisos=="Piso3":
                                piso3+=1                
                            elif pisos=="Piso4":
                                piso4+=1
                            elif pisos=="Piso5":
                                piso5+=1
                            elif pisos=="Piso6":
                                piso6+=1

                            if parqueadero[0]==1:
                                automovil+=1
                            elif parqueadero[0]==2:
                                Automovil_electrico+=1
                            elif parqueadero[0]==3: 
                                motocicleta+=1                   
                            elif parqueadero[0]==4:
                                discapacitado+=1
                            
                            if parqueadero[1][1]=="Estudiante":
                                estudiante+=1
                            elif parqueadero[1][1]=="Profesor":
                                profesor+=1
                            elif parqueadero[1][1]=="Personal Administrativo":
                                personal_administrativo+=1
                            elif parqueadero[1][1]=="Visitante":
                                visitante+=1
                PisosJson_ocupados.close()

                PocupacionGlobal=(ocuapcion_total/550)*100#calculo del porcentaje de ocupación global
                PocupacionP1=(piso1/100)*100#calculo del porcentaje de ocupación del piso 1
                PocupacionP2=(piso2/100)*100#calculo del porcentaje de ocupación del piso 2
                PocupacionP3=(piso3/100)*100#calculo del porcentaje de ocupación del piso 3
                PocupacionP4=(piso4/100)*100#calculo del porcentaje de ocupación del piso 4
                PocupacionP5=(piso5/100)*100#calculo del porcentaje de ocupación del piso 5
                PocupacionP6=(piso6/50)*100#calculo del porcentaje de ocupación del piso 6

                if Opciones4_1==1:
                    with open ("Estadisticas_del_parqueadero.txt","w") as archivo:#se crea el archivo de texto del reporte 1
                        archivo.write("La cantidad de vehiculos de usuarios profesores es: "+str(profesor)+"\n")        
                        archivo.write("La cantidad de vehiculos de usuarios estudiantes es: "+str(estudiante)+"\n")
                        archivo.write("La cantidad de vehiculos de usuarios personal administrativo es: "+str(personal_administrativo)+"\n")
                        archivo.write("La cantidad de vehiculos de usuarios visitantes es: "+str(visitante)+"\n") 
                        archivo.close() 
                        print("\n¡Estadisticas generadas!\n\n")    
                elif Opciones4_1==2:
                    with open ("Estadisticas_del_parqueadero.txt","w") as archivo:#se crea el archivo de texto del reporte 2
                        archivo.write("La cantidad de vehiculos del tipo automovil es: "+str(automovil)+"\n")
                        archivo.write("La cantidad de vehiculos del tipo automovil eléctrico es: "+str(Automovil_electrico)+"\n")        
                        archivo.write("La cantidad de vehiculos del tipo motocicleta es: "+str(motocicleta)+"\n")
                        archivo.write("La cantidad de vehiculos del tipo discapacitado es: "+str(discapacitado)+"\n")   
                        archivo.close() 
                        print("\n¡Estadisticas generadas!\n\n")  
                elif Opciones4_1==3:
                    with open ("Estadisticas_del_parqueadero.txt","w") as archivo:#se crea el archivo de texto del reporte 3
                        archivo.write("El porcentaje de ocupación del parqueadero es del: "+str(PocupacionGlobal)+"%.\n")
                        archivo.write("El porcentaje de ocupación del piso 1 es de: "+str(PocupacionP1)+"%.\n")
                        archivo.write("El porcentaje de ocupación del piso 2 es de: "+str(PocupacionP2)+"%.\n")
                        archivo.write("El porcentaje de ocupación del piso 3 es de: "+str(PocupacionP3)+"%.\n")
                        archivo.write("El porcentaje de ocupación del piso 4 es de: "+str(PocupacionP4)+"%.\n")
                        archivo.write("El porcentaje de ocupación del piso 5 es de: "+str(PocupacionP5)+"%.\n")
                        archivo.write("El porcentaje de ocupación del piso 6 es de: "+str(PocupacionP6)+"%.\n")
                        archivo.close()
                        print("\n¡Estadisticas generadas!\n\n")
opciones1=0
opcion_1(opciones1)