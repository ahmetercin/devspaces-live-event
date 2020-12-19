import csv

class Person:
    def __init__(self,):
        self.name = -1
        self.x = -1
        self.y = -1
        self.exposed = 0
    def __str__(self):
        return str(self.name) + ' ' + str(self.x) + ' ' + str(self.y) + ' ' + str(self.exposed)

    name = ''
    x = -1
    y = -1
    exposed = False

class PersonInTime:
    def __init__(self,):
        self.person = Person()
        self.time = -1
    def __str__(self):
        return self.person.__str__() + ' ' + str(self.time)
    time = -1
    person = Person() 

def main():
    personsInTime = []
    changeInTime = []
    exposures = []
    lastTime = 1

    file = open("output.csv", "a")


    with open('locations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        tempPerson = PersonInTime
        for row in csv_reader:
            tempPerson = PersonInTime()
            tempPerson.time = row[0]
            tempPerson.person.name = row[1]
            tempPerson.person.x = row[2]
            tempPerson.person.y = row[3]
            tempPerson.person.exposed = 0
            personsInTime.append(tempPerson)
            if int(row[0]) > lastTime:
                lastTime = int(row[0])
            

    with open('exposure.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            tempPerson = PersonInTime()
            tempPerson.time = row[0]
            tempPerson.person.name = row[1]
            tempPerson.person.exposed = 2
            exposures.append(tempPerson)

    for exp in exposures:
        for per in personsInTime:
            if exp.person.name == per.person.name:
                per.person.exposed = 2
    uniqueId = 1
    for time in range(1,lastTime+1):
        print('time:' + str(time))
        currentTimePersons = []
        for person in personsInTime:
            if int(person.time) == time:
                currentTimePersons.append(person)
               
        for exp in currentTimePersons:
            if exp.person.exposed != 2:
                continue
            print('Iterating for exposed: ' + str(exp.person.name))
            for curr in currentTimePersons:
                    if curr.person.name == exp.person.name:
                        continue
                    for xInc in range(-1,2):
                         for yInc in range(-1,2):
                            #print('xinc:' + str(xInc) + ' yinc:' + str(yInc))
                            #print(curr.person.__str__() + ' ------' + exp.person.__str__())
                            if ( (int(curr.person.x) + xInc) == int(exp.person.x) and  ( int(curr.person.y) + yInc) == int(exp.person.y) ):
                                curr.person.exposed = curr.person.exposed + 1
                                print('exposed' + str(curr.person.name))
                                #file.write(str(uniqueId) + "," + str(time)+ ","+ curr.person.name)
                                if curr.person.exposed >= 1:
                                    file.write(str(uniqueId) + "," + str(time)+ ","+ curr.person.name)
                                    uniqueId = uniqueId +1
    file.close()                    
                    
if __name__ == "__main__":
    main()
