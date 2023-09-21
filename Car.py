class Car:
    def __init__(self, fuel_consumption, possible_destinations):
        self.fuel_consumption = fuel_consumption
        self.possible_destinations = possible_destinations
        self.total_distance = 0
        self.distance_left = 0

    def ride(self, distance):
        try:
            self.check_distance(distance)
        except ValueError as e:
            print(e)
        else:
            self.total_distance += distance
            self.distance_left -= distance
            print(f"The ride was successful! Distance traveled: {distance}")

    def check_distance(self, distance):
        if self.distance_left < distance:
            raise ValueError("Not enough fuel, recharge the car!")

    def calculate_average_speed(self, distance, duration):
        if duration == 0:
            return 0
        try:
            average_speed = distance / duration
            return average_speed
        except ZeroDivisionError:
            return distance

    def ride_to_destination(self, destination):
        try:
            distance = self.possible_destinations[destination]
            self.ride(distance)
            print(f"Reached {destination}!")
        except KeyError:
            print(f"Destination not in possible destinations!")

    def recharge(self, fuel):
        self.distance_left += fuel * self.fuel_consumption
        print(f"Car charged successfully! Distance left to ride: {self.distance_left}.")

possible_destinations = {
    "Eriador": 100,
    "Gondor": 50
}

ford_mustang = Car(14, possible_destinations)
ford_mustang.ride(10)
ford_mustang.recharge(10)
ford_mustang.ride(50)

average_speed = ford_mustang.calculate_average_speed(150, 2)
print(f"Average speed: {average_speed}")

average_speed = ford_mustang.calculate_average_speed(150, 0)
print(f"Average speed: {average_speed}")

ford_mustang.ride_to_destination("Gondor")
ford_mustang.ride_to_destination("Wonderland")

# PL-------------------------------------------------------------------------------

class Samochod:
    def __init__(self, spalanie_paliwa, dostepne_destynacje):
        self.spalanie_paliwa = spalanie_paliwa
        self.dostepne_destynacje = dostepne_destynacje
        self.calokrajowy_dystans = 0
        self.pozostaly_dystans = 0

    def podroz(self, dystans):
        try:
            self.sprawdz_dystans(dystans)
        except ValueError as e:
            print(e)
        else:
            self.calokrajowy_dystans += dystans
            self.pozostaly_dystans -= dystans
            print(f"Podróż zakończona sukcesem! Przejechany dystans: {dystans} km")

    def sprawdz_dystans(self, dystans):
        if self.pozostaly_dystans < dystans:
            raise ValueError("Za mało paliwa, naładuj samochód!")

    def oblicz_srednia_predkosc(self, dystans, czas):
        if czas == 0:
            return 0
        try:
            srednia_predkosc = dystans / czas
            return srednia_predkosc
        except ZeroDivisionError:
            return dystans

    def podroz_do_celu(self, cel):
        try:
            dystans = self.dostepne_destynacje[cel]
            self.podroz(dystans)
            print(f"Dotarto do celu: {cel}!")
        except KeyError:
            print(f"Cel nie znajduje się w dostępnych destynacjach!")

    def naladuj(self, paliwo):
        self.pozostaly_dystans += paliwo * self.spalanie_paliwa
        print(f"Samochód naładowany pomyślnie! Pozostały dystans do przejechania: {self.pozostaly_dystans} km.")

dostepne_destynacje = {
    "Eriador": 100,
    "Gondor": 50
}

ford_mustang = Samochod(14, dostepne_destynacje)
ford_mustang.podroz(10)
ford_mustang.naladuj(10)
ford_mustang.podroz(50)

srednia_predkosc = ford_mustang.oblicz_srednia_predkosc(150, 2)
print(f"Średnia prędkość: {srednia_predkosc}")

srednia_predkosc = ford_mustang.oblicz_srednia_predkosc(150, 0)
print(f"Średnia prędkość: {srednia_predkosc}")

ford_mustang.podroz_do_celu("Gondor")
ford_mustang.podroz_do_celu("Kraina Czarów")
