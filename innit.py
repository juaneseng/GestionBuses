class Empresa:
    def __init__(self):
        self.vehiculos = []

    def total_descuentos_femenino(self):
        total = 0
        for v in self.vehiculos:
            if 'trayectos' in v:
                for t in v['trayectos']:
                    precio = t['ruta']['precio']
                    total += t['menores_femenino'] * precio * 0.2
        return total

    def agregar_vehiculo(self):
        placa = input("Ingrese la placa del vehiculo: ")
        while len(placa) != 6:
            print("Placa no valida, debe tener 6 caracteres")
            placa = input("Ingrese la placa del vehiculo: ")

        opciones = {"1": "Mototaxi", "2": "Intermunicipal", "3": "Interveredal"}
        tipo = input("Ingrese el tipo del vehiculo \n1.Mototaxi \n2.Intermunicipal \n3.Interveredal: ").strip()
        while tipo not in opciones:
            print("Tipo de vehiculo no valido")
            tipo = input("Ingrese el tipo del vehiculo \n1.Mototaxi \n2.Intermunicipal \n3.Interveredal: ").strip()

        self.vehiculos.append({"placa": placa, "tipo": opciones[tipo]})

    def otro_vehiculo(self):
        respuesta = input("¿Desea agregar otro vehiculo? (Y/N): ").lower().strip()
        while respuesta not in ["y", "n"]:
            print("Respuesta no valida")
            respuesta = input("¿Desea agregar otro vehiculo? (Y/N): ").lower().strip()
        if respuesta == "y":
            self.agregar_vehiculo()
            self.otro_vehiculo()

    def mostrar_vehiculos(self):
        print("Vehiculos registrados:")
        for v in self.vehiculos:
            print(f"Placa: {v['placa']} Tipo: {v['tipo']}")

    def asignar_ruta(self):
        while True:
            respuesta2 = input("¿Desea asignar una ruta a un vehiculo? (Y/N): ").lower().strip()
            while respuesta2 not in ["y", "n"]:
                print("Respuesta no valida")
                respuesta2 = input("¿Desea asignar una ruta a un vehiculo? (Y/N): ").lower().strip()
            if respuesta2 == "n":
                break
            self.mostrar_vehiculos()
            placas_registradas = [v['placa'] for v in self.vehiculos]
            placa = input("Ingrese la placa del vehiculo al que desea asignar una ruta: ")
            while placa not in placas_registradas:
                print("Placa no encontrada")
                placa = input("Ingrese la placa del vehiculo al que desea asignar una ruta: ")

            salida = input("Ingrese el lugar de salida: ")
            llegada = input("Ingrese el lugar de llegada: ")
            precio = input("Ingrese el precio del pasaje: ")
            pasajeros = input("Ingrese el numero total de pasajeros: ")
            menores = input("Ingrese el número de pasajeros menores de edad: ")
            menores_femenino = input("Ingrese el numero de menores de edad de género femenino: ")

            self.agregar_trayecto(placa, salida, llegada, precio, pasajeros, menores, menores_femenino)
            print(f"Trayecto registrado para el vehículo {placa}: {salida} a {llegada}, Precio: {precio}, Pasajeros: {pasajeros}, Menores: {menores}, Menores femeninos: {menores_femenino}")

            otra_ruta = input("¿Desea asignar otra ruta (puede ser a otro vehiculo)? (Y/N): ").lower().strip()
            while otra_ruta not in ["y", "n"]:
                print("Respuesta no valida")
                otra_ruta = input("¿Desea asignar otra ruta (puede ser a otro vehiculo)? (Y/N): ").lower().strip()
            if otra_ruta == "n":
                break

    def agregar_trayecto(self, placa, salida, llegada, precio, pasajeros, menores, menores_femenino):
        for v in self.vehiculos:
            if v['placa'] == placa:
                if 'trayectos' not in v:
                    v['trayectos'] = []
                v['trayectos'].append({
                    'ruta': {'salida': salida, 'llegada': llegada, 'precio': float(precio)},
                    'pasajeros': int(pasajeros),
                    'menores': int(menores),
                    'menores_femenino': int(menores_femenino)
                })
                return
    def total_recaudado(self):
        total = 0
        for v in self.vehiculos:
            if 'trayectos' in v:
                for t in v['trayectos']:
                    precio = t['ruta']['precio']
                    adultos = t['pasajeros'] - t['menores']
                    total += adultos * precio + t['menores'] * precio * 0.8
        return total


    def buseta_intermunicipal_mas_recaudo(self):
        max_recaudo = 0
        mejor_placa = None
        for v in self.vehiculos:
            if v['tipo'] == 'Intermunicipal' and 'trayectos' in v:
                recaudo = 0
                for t in v['trayectos']:
                    precio = t['ruta']['precio']
                    adultos = t['pasajeros'] - t['menores']
                    recaudo += adultos * precio + t['menores'] * precio * 0.8
                if recaudo > max_recaudo:
                    max_recaudo = recaudo
                    mejor_placa = v['placa']
        return mejor_placa, max_recaudo

    def ruta_menos_recaudo(self):
        min_recaudo = None
        peor_ruta = None
        for v in self.vehiculos:
            if 'trayectos' in v:
                for t in v['trayectos']:
                    precio = t['ruta']['precio']
                    adultos = t['pasajeros'] - t['menores']
                    recaudo = adultos * precio + t['menores'] * precio * 0.8
                    if min_recaudo is None or recaudo < min_recaudo:
                        min_recaudo = recaudo
                        peor_ruta = t['ruta']
        return peor_ruta, min_recaudo

    def comparar_recaudo(self):
        interveredal = 0
        intermunicipal = 0
        for v in self.vehiculos:
            if 'trayectos' in v:
                for t in v['trayectos']:
                    precio = t['ruta']['precio']
                    adultos = t['pasajeros'] - t['menores']
                    recaudo = adultos * precio + t['menores'] * precio * 0.8
                    if v['tipo'] == 'Interveredal':
                        interveredal += recaudo
                    elif v['tipo'] == 'Intermunicipal':
                        intermunicipal += recaudo
        if interveredal > intermunicipal:
            return 'Interveredales'
        elif intermunicipal > interveredal:
            return 'Intermunicipales'
        else:
            return 'Igual'

    def total_descuentos(self):
        total = 0
        for v in self.vehiculos:
            if 'trayectos' in v:
                for t in v['trayectos']:
                    precio = t['ruta']['precio']
                    total += t['menores'] * precio * 0.2
        return total

empresa = Empresa()
empresa.agregar_vehiculo()
empresa.otro_vehiculo()
empresa.mostrar_vehiculos()
empresa.asignar_ruta()
print("\nESTADISTICAS DE LA EMPRESA")
print(f"1. Valor total recaudado: {empresa.total_recaudado()}")
placa_max, rec_max = empresa.buseta_intermunicipal_mas_recaudo()
if placa_max:
    print(f"2. Buseta intermunicipal que más recaudo: {placa_max} (${rec_max})")
else:
    print("2. No hay busetas intermunicipales registradas.")
ruta_min, rec_min = empresa.ruta_menos_recaudo()
if ruta_min:
    print(f"3. Ruta que menos recauda: {ruta_min['salida']} -> {ruta_min['llegada']} (${rec_min})")
else:
    print("3. No hay rutas registradas.")
print(f"4. Deja más dinero: {empresa.comparar_recaudo()}")
print(f"5. Total descuentos otorgados: {empresa.total_descuentos()}")
print(f"   Total descuentos otorgados a menores femeninos: {empresa.total_descuentos_femenino()}")


