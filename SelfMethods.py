from uuid import uuid4

class methods:

    def search(typeArg, location, maxdist, service, time):
        foundflag = False
        shopinst = []
        for cshop in shoplist:
            if cshop.typeArg == typeArg and cshop.location == location and service in cshop.services and time in cshop.timetable:
                foundflag = True
                shopinst = [cshop, service, time]
                print(shopinst)

        if foundflag == True and str(input("Would you like to book your selection? (y/n): ").lower()) == 'y':
            methods.book(currentuser, shopinst)
        else:
            pass

    def book(user, shopitem):
        booking = [user, shopitem[1], shopitem[2]]
        for i in shopitem[0].timetable:
            if i == shopitem[2]:
                shopitem[0].timetable[shopitem[0].timetable.index(i)] = booking
                print("Booked: " + shopitem[1] + " " + str(shopitem[2]))

    def rembooking(user, shopitem, time):
        for cur in shopitem.timetable:
            if not isinstance(cur, int) and user in cur and time in cur:
                shopitem.timetable[shopitem.timetable.index(cur)] = cur[2]

class user:

    def __init__(self):
        self.uid = uuid4()
