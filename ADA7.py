import networkx as nx
import folium
import webbrowser
import os

class GrafoMexico:
    def __init__(self):
        self.G = nx.Graph()
        # Coordenadas de varios estados de México
        self.coordenadas = {
            "Baja California": (32.5, -115.0),
            "Sonora": (29.0, -110.0),
            "Chihuahua": (28.6, -106.0),
            "Coahuila": (27.0, -101.0),
            "Nuevo León": (25.7, -100.3),
            "Tamaulipas": (24.2, -98.7),
            "Sinaloa": (25.0, -107.5),
            "Durango": (24.0, -104.7),
            "Zacatecas": (23.6, -102.5),
            "San Luis Potosí": (22.2, -100.9),
            "Nayarit": (21.8, -104.9),
            "Jalisco": (20.7, -103.3),
            "Guanajuato": (20.9, -101.2),
            "Querétaro": (20.6, -100.4),
            "Hidalgo": (20.5, -98.9),
            "Veracruz": (19.2, -96.1),
            "Puebla": (19.0, -98.2),
            "Michoacán": (19.7, -101.2),
            "Guerrero": (17.5, -99.5),
            "Oaxaca": (17.0, -96.7),
            "Chiapas": (16.7, -93.1),
            "Tabasco": (17.8, -92.6),
            "Campeche": (19.8, -90.5),
            "Yucatán": (20.9, -89.6),
            "Quintana Roo": (19.6, -88.0),
            "CDMX": (19.4, -99.1),
            "Estado de México": (19.3, -99.6),
            "Morelos": (18.8, -99.2),
            "Tlaxcala": (19.3, -98.2)
        }

    def agregar_estado(self, nombre):
        """Agrega un estado solo por nombre"""
        if nombre not in self.coordenadas:
            print("⚠️ Ese estado no está registrado en la base. Intenta con otro nombre.")
            return
        self.G.add_node(nombre)
        print(f"✅ Estado agregado: {nombre}")

    def agregar_conexion(self, estado1, estado2, costo):
        """Agrega conexión entre dos estados"""
        if estado1 in self.G.nodes and estado2 in self.G.nodes:
            self.G.add_edge(estado1, estado2, weight=costo)
            print(f"🔗 Conexión agregada: {estado1} ↔ {estado2} | Costo: {costo}")
        else:
            print("⚠️ Ambos estados deben existir primero.")

    def mostrar_estados(self):
        print("\n📍 Estados registrados:")
        for e in self.G.nodes:
            print(f" - {e}")
        print("\nConexiones:")
        for e1, e2, data in self.G.edges(data=True):
            print(f" - {e1} ↔ {e2} | Costo: {data['weight']}")

    def recorrer_sin_repetir(self):
        if len(self.G.nodes) == 0:
            print("⚠️ No hay estados registrados.")
            return
        recorrido = list(nx.dfs_preorder_nodes(self.G))
        costo_total = 0
        for i in range(len(recorrido)-1):
            costo_total += self.G[recorrido[i]][recorrido[i+1]]['weight']
        print(f"\n🚗 Recorrido sin repetir: {' → '.join(recorrido)}")
        print(f"Costo total: {costo_total}")

    def recorrer_con_repetir(self):
        if len(self.G.nodes) == 0:
            print("⚠️ No hay estados registrados.")
            return
        recorrido = list(nx.bfs_edges(self.G))
        recorrido_estados = [recorrido[0][0]] + [e[1] for e in recorrido] + [recorrido[0][0]]
        costo_total = 0
        for i in range(len(recorrido_estados)-1):
            try:
                costo_total += self.G[recorrido_estados[i]][recorrido_estados[i+1]]['weight']
            except KeyError:
                continue
        print(f"\n🔁 Recorrido repitiendo al menos un estado: {' → '.join(recorrido_estados)}")
        print(f"Costo total: {costo_total}")

    def dibujar_mapa(self):
        if len(self.G.nodes) == 0:
            print("⚠️ No hay estados registrados.")
            return

        mapa = folium.Map(location=[23.6345, -102.5528], zoom_start=5)
        for estado in self.G.nodes:
            lat, lon = self.coordenadas[estado]
            folium.Marker(location=[lat, lon],
                          popup=estado,
                          icon=folium.Icon(color="blue")).add_to(mapa)

        for e1, e2, data in self.G.edges(data=True):
            coord1 = self.coordenadas[e1]
            coord2 = self.coordenadas[e2]
            folium.PolyLine([coord1, coord2],
                            color="green",
                            weight=3,
                            tooltip=f"{e1} ↔ {e2} (Costo: {data['weight']})").add_to(mapa)

        nombre_archivo = "mapa_estados.html"
        mapa.save(nombre_archivo)
        print(f"\n🗺️ Mapa generado: {nombre_archivo}")
        ruta_absoluta = os.path.abspath(nombre_archivo)
        webbrowser.open_new_tab('file://' + ruta_absoluta)

    def menu(self):
        while True:
            print("\n=== MENÚ DE GRAFOS DE ESTADOS ===")
            print("1. Agregar estado")
            print("2. Agregar conexión")
            print("3. Mostrar estados y conexiones")
            print("4. Recorrer sin repetir")
            print("5. Recorrer repitiendo alguno")
            print("6. Mostrar mapa")
            print("7. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                nombre = input("Nombre del estado (ej. Jalisco): ")
                self.agregar_estado(nombre)

            elif opcion == '2':
                e1 = input("Estado origen: ")
                e2 = input("Estado destino: ")
                costo = float(input("Costo de traslado: "))
                self.agregar_conexion(e1, e2, costo)

            elif opcion == '3':
                self.mostrar_estados()

            elif opcion == '4':
                self.recorrer_sin_repetir()

            elif opcion == '5':
                self.recorrer_con_repetir()

            elif opcion == '6':
                self.dibujar_mapa()

            elif opcion == '7':
                print("👋 Saliendo del programa...")
                break
            else:
                print("⚠️ Opción no válida.")


if __name__ == "__main__":
    app = GrafoMexico()
    app.menu()
