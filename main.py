def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Reportes")
    print("5. Acerca del Sistema")
    print("6. Salir")

def menu_gestionar_clientes():
    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1.1 Consulta Clientes")
        print("1.2 Agregar Cliente")
        print("1.3 Modificar Cliente")
        print("1.4 Eliminar Cliente")
        print("1.5 Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1.1":
            print(">> Consulta de Clientes (funcionalidad no implementada)")
        elif opcion == "1.2":
            print(">> Agregar Cliente (funcionalidad no implementada)")
        elif opcion == "1.3":
            print(">> Modificar Cliente (funcionalidad no implementada)")
        elif opcion == "1.4":
            print(">> Eliminar Cliente (funcionalidad no implementada)")
        elif opcion == "1.5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_gestionar_destinos():
    while True:
        print("\n--- GESTIÓN DE DESTINOS ---")
        print("2.1 Consulta Destinos")
        print("2.2 Agregar Destinos")
        print("2.3 Modificar Destinos")
        print("2.4 Eliminar Destinos")
        print("2.5 Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "2.1":
            print(">> Consulta de Destinos (funcionalidad no implementada)")
        elif opcion == "2.2":
            print(">> Agregar Destinos (funcionalidad no implementada)")
        elif opcion == "2.3":
            print(">> Modificar Destinos (funcionalidad no implementada)")
        elif opcion == "2.4":
            print(">> Eliminar Destinos (funcionalidad no implementada)")
        elif opcion == "2.5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_gestionar_ventas():
    while True:
        print("\n--- GESTIÓN DE VENTAS ---")
        print("3.1 Nueva Venta")
        print("3.2 Consultar Ventas")
        print("3.3 Botón de Arrepentimiento")
        print("3.4 Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "3.1":
            print(">> Nueva Venta (funcionalidad no implementada)")
        elif opcion == "3.2":
            print(">> Consultar Ventas (funcionalidad no implementada)")
        elif opcion == "3.3":
            print(">> Botón de Arrepentimiento (funcionalidad no implementada)")
        elif opcion == "3.4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_reportes():
    while True:
        print("\n--- REPORTES ---")
        print("4.1 Reportes Clientes")
        print("4.2 Reportes Destinos")
        print("4.3 Reportes Ventas")
        print("4.4 Reportes Ventas anuladas")
        print("4.5 Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "4.1":
            print(">> Reportes Clientes (funcionalidad no implementada)")
        elif opcion == "4.2":
            print(">> Reportes Destinos (funcionalidad no implementada)")
        elif opcion == "4.3":
            print(">> Reportes Ventas (funcionalidad no implementada)")
        elif opcion == "4.4":
            print(">> Reportes Ventas anuladas (funcionalidad no implementada)")
        elif opcion == "4.5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def acerca_del_sistema():
    print("\n--- ACERCA DEL SISTEMA ---")
    print("Sistema de Gestión de Viajes")
    print("Versión 1.0")
    print("Desarrollado por xAI")
    input("Presione Enter para volver al Menú Principal...")

# Programa principal
while True:
    mostrar_menu_principal()
    seleccion = input("Seleccione una opción: ")

    if seleccion == "1":
        menu_gestionar_clientes()
    elif seleccion == "2":
        menu_gestionar_destinos()
    elif seleccion == "3":
        menu_gestionar_ventas()
    elif seleccion == "4":
        menu_reportes()
    elif seleccion == "5":
        acerca_del_sistema()
    elif seleccion == "6":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")