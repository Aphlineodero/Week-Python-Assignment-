#Activity 1
# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # in percentage

    def call(self, contact):
        print(f"📞 Calling {contact} from {self.brand} {self.model}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"🔋 Battery charged. Current level: {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.battery}% battery)"


# Subclass (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            self.battery -= 10
            print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system.")
        else:
            print("❌ Not enough battery to play games.")

    # Polymorphism (overriding method)
    def charge(self, amount):
        super().charge(amount)
        print("⚡ Fast charging enabled for Gaming Phone!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", 50)
gaming_phone = GamingPhone("Asus", "ROG 6", 70, "Liquid Cooling")

print(phone1)
phone1.call("Alice")
phone1.charge(30)

print("\n--- Gaming Phone ---")
print(gaming_phone)
gaming_phone.play_game("PUBG Mobile")
gaming_phone.charge(20)



#Activity 2
class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
