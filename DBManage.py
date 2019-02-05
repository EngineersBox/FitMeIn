import pymongo

shopClient = pymongo.MongoClient("mongodb://localhost/")
shopdb = shopClient["shopdb"]
shopcol = shopdb["shop"]

class db_method:

    def findShop(name, typeArg, location):

        query = { "name": str(name), "type": str(typeArg), "location": str(location) }
        if shopcol.find(query).count() == 0:
            return False
        else:
            return True


    def addShop(name, typeArg, location, services, timetable):

        if db_method.findShop(name, typeArg, location) == False:
            dataDict = { "name": str(name), "type": str(typeArg), "location": str(location), "services": list(services), "timetable": list(timetable) }
            x = shopcol.insert_one(dataDict)
            print("Shop Instance Created")
        else:
            print("Shop Instance Already Exists")

    def delShop(name, typeArg, location):

        query = { "name": str(name), "type": str(typeArg), "location": str(location) }
        if db_method.findShop(name, typeArg, location) == True:
            shopcol.delete_one(query)
            print("Shop Instance Deleted")
        else:
            print("Shop Instance Does Not Exist")

    def addService(name, typeArgArg, location, service):

        tempServices = []
        query = { "name": str(name), "type": str(typeArg), "location": str(location) }
        if db_method.findShop(name, typeArg, location) == True:
            retQuery = shopcol.find(query, { "_id": 0, "services": 1 })
            tempList = retQuery[0].get('services')
            tempList.append(service)
            newVal = { "$set": { "services": tempList } }
            shopcol.update_one(query, newVal)
            print("Serivce Added To Shop Instance")

    def delService(name, typeArg, location, service):

        tempServices = []
        query = { "name": str(name), "type": str(typeArg), "location": str(location) }
        if db_method.findShop(name, typeArg, location) == True:
            retQuery = shopcol.find(query, { "_id": 0, "services": 1 })
            tempList = retQuery[0].get('services').remove(str(service))
            tempList.remove(str(service))
            newVal = { "$set": { "services": tempList } }
            shopcol.update_one(query, newVal)
            print("Serivce Removed From Shop Instance")

    def addBooking(name, typeArg, location, time, service, userid):

        tempTimetable = []
        serviceFlag = False
        booking = [str(userid), str(service), str(time)]
        query = { "name": str(name), "type": str(typeArg), "location": str(location) }
        if db_method.findShop(name, typeArg, location) == True:
            retQuery = shopcol.find(query, { "_id": 0, "services": 1, "timetable": 1 })
            for key, value in retQuery[0].items():
                if service in value:
                    serviceFlag = True

            if serviceFlag == True:
                for key, value in retQuery[0].items():
                    if time in value:
                        print("Found Open Time")
                        tempTimetable = value
                        tempTimetable[tempTimetable.index(time)] = booking
                        newVal = { "$set": { "timetable": tempTimetable } }
                        shopcol.update_one(query, newVal)
                        return
                print("No Open Time Found")
            else:
                print("Shop Instance Does Not Have Service")
        else:
            print("Shop Instance Does Not Exist")

    def delBooking(name, typeArg, location, time, service, userid):

        tempTimetable = []
        serviceFlag = False
        booking = [str(userid), str(service), str(time)]
        query = { "name": str(name), "type": str(typeArg), "location": str(location) }
        if db_method.findShop(name, typeArg, location) == True:
            retQuery = shopcol.find(query, { "_id": 0, "serivces": 1, "timetable": 1 })
            for key, value in retQuery[0].items():
                print(value)
                if booking in value:
                    print("Booking Found, Removing")
                    tempTimetable = value
                    tempTimetable[tempTimetable.index(booking)] = int(booking[2])
                    newVal = { "$set": { "timetable": tempTimetable } }
                    shopcol.update_one(query, newVal)
                    return
            print("No Booking Found")
        else:
            print("Shop Instance Does Not Exist")

class db_main:

    def main_init(name, type, location):
        query = { "name": str(name), "type": str(type), "location": str(location) }
        retQuery = shopcol.find(query, { "name": 1, "type": 1, "location": 1, "services": 1, "timetable": 1 })
        return retQuery[0]
