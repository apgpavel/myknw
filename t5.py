class Car:
    def __init__(self, vin, seller, contact, phone):
        self.vin = vin
        self.seller = seller
        self.contact = contact
        self.phone = phone

    def addcontact(self):
        self.contact = "Test"

    def displaycarinfo(self):
        print("Car VIN:", self.vin, "\nSeller:", self.seller, "\nContact:", self.contact, "\nPhone:", self.phone, "\n")

class Truck(Car):
    def displaycarinfo(self):
        print("Truck VIN:", self.vin, "\nSeller:", self.seller, "\nContact:", self.contact, "\nPhone:", self.phone, "\n")

class Scar(Car):
    def displaycarinfo(self):
        super().displaycarinfo()
        print("You can find addintitionat info in www.rogaikopita.com the best car seller site\n")

test1 = Car("VF1LM1B0H36666155", "Roga i Kopita", "Ukraine, Kyiv, ul. Test2", "+48792656627")
test2 = Truck("VF1LM1B0H36666155", "filial Roga i Kopita", "France, Paris, str. Test3", "+48792656627")
test3 = Scar("VF1LM1B0H36666155", "Roga i Kopita Incorporate", "France, Paris, str. Test4", "+48792656627")
test4 = Scar("VF1LM1B0H36666155", "Roga i Kopita Incorporate", "France, Paris, str. Test5", "+48792656627")

test1.displaycarinfo()
test2.displaycarinfo()
test3.displaycarinfo()
test4.addcontact()
test4.displaycarinfo()
