rooms = []
def add_room():
    room_number = 1
    while True:
        length = float(input("Geben Sie die Raumlänge ein: "))
        width = float(input("Geben Sie die Raumbreite in Metern an: "))
        area = length * width
        room_name = input("Geben Sie dem Raum einen Namen: ")
        room = {"name": room_name, "length": length, "width": width, "area": area}
        rooms.append(room)
        print("Raum " + room_name + " mit einer Fläche von " + str(area) + " Quadratmetern wurde hinzugefügt.")
        room_number += 1
        add_more = input("Möchten sie noch einen weiteren Raum hinzufügen? (ja/nein) ")
        if add_more.lower() != "ja":
            break
def calculate_room_area():
    total_area = 0
    sorted_rooms = sorted(rooms, key=lambda room: room["area"])
    for room in sorted_rooms:
        print("Raum " + room["name"] + " hat eine Fläche von " + str(room["area"]) + " Quadratmetern.")
        total_area += room["area"]
    print("Gesamtfläche aller Räume ist " + str(total_area) + " Quadratmeter.")

# Beispielaufruf
add_room()
calculate_room_area()
