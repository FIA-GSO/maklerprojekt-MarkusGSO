rooms = []
def add_room():
    room_number = 1
    while True:
        aarea = 0
        anbau = str(input("Gibt es einen Raumeinrückung (Anbau)? (ja/nein)"))
        if anbau == "ja":
            alenght = float(input("Geben Sie die Länge des Anbaus in Meter ein: ").replace(',', '.'))
            awidth = float(input("Geben Sie die Breite des Anbaus in Meter ein: ").replace(',', '.'))
            aarea = alenght * awidth
        length = float(input("Geben Sie die Länge des Raumes in Meter ein: ").replace(',', '.'))
        width = float(input("Geben Sie die Breite des Raumes in Meter ein: ").replace(',', '.'))
        area = length * width
        area += aarea
        room_name = input("Geben Sie den Namen des Raumes ein: ")
        room = {"name": room_name, "length": length, "width": width, "area": area}
        rooms.append(room)
        print("Raum " + room_name + " mit einer Fläche von " + str(area) + " Quadratmetern wurde hinzugefügt.")
        room_number += 1
        add_more = input("Möchten Sie mehr Räume hinzufügen? (ja/nein) ")
        if add_more.lower() != "ja":
            break
    # Sortiere die Liste der Räume nach der Fläche in absteigender Reihenfolge
    rooms.sort(key=lambda room: room["area"], reverse=True)
def calculate_room_area():
    total_area = 0
    for room in rooms:
        print("Raum " + room["name"] + " hat eine Fläche von " + str(room["area"]) + " Quadratmeter.")
        total_area += room["area"]
    print("Die Fläche aller Räume beträgt " + str(total_area) + " Quadratmeter.")
    av = total_area / len(rooms)
    print(f"Durchschnitt: {av}")
# Beispielaufruf
add_room()
calculate_room_area()