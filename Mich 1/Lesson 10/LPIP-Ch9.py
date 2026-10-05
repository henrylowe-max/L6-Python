"""
Learn to program in Python (LPIP)
CH3
"""

"""
City,Temperature,Local time
London,7,1200
Accra,30,1200
Baghdad,20,1500
Winnipeg,-12,0600
New York,14,0700
Nairobi,27,1500
Sydney,22,2300
"""
""""
001, Ghostbusters, 2016, PG, 116, Comedy
002, The Legend of Tarzan, 2016, PG, 109, Action
003, Jason Bourne, 2016, PG, 123, Action
004, The Nice Guys, 2016, R, 116, Crime
005, The Secret Life of Pets, 2016, G, 91, Animation
006, Star Trek Beyond, 2016, PG, 120, Action
"""


def eg1():
    #Program name: Ch 9 Example 1 read film file.py
    # Description: Open the file named films.txt, read all the records and print them out.

    filmFile = open("films.txt", "r")
    films = filmFile.read()
    print(films)
    filmFile.close()

def eg2():
    #Program name: Ch 9 Example 2 films rated G.py
    filmFile = open("films.txt","r")
    filmRec = filmFile.readline()
    while filmRec != "":
        field = filmRec.split(",")
        ID = field[0]
        title = field[1]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
        if rating == "G":
            print (ID, title, rating, duration)
        filmRec = filmFile.readline()
    filmFile.close()

def eg3():
    #Program name: Ch 9 Example 3 comedy films v1.py
    filmFile = open("films.txt","r")
    filmRec = filmFile.readline()
    while filmRec != "":
        field = filmRec.split(",")
        ID = field[0]
        title = field[1]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
        if genre == "Comedy\n":
            print (ID, title, rating, genre, duration)
        filmRec = filmFile.readline()
    filmFile.close()

def eg4():
    #Program name: Ch 9 Example 4 read and print each film record.py
    filmFile = open("films.txt","r")
    for row in filmFile:
        field = row.split(",")
        print (field[0], field[1], field[2], field[3], field[4], field[5], end ="")
    filmFile.close()

def eg5():
    #Program name: Ch 9 Example 5 comedy films.py
    filmFile = open("films.txt","r")

    for row in filmFile:
        field = row.split(",")
        ID = field[0]
        title = field[1]
        yearReleased = field[2]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]

        #slice off the last character of genre, which is "\n"
        lastchar = len(genre) - 1
        genre = genre[0:lastchar]
        if genre == "Comedy":
            print (ID, title, yearReleased, rating, genre, duration)

    filmFile.close()

def eg6():
    #Program name: Ch 9 Example 6 append to temperatures file.py
    tempsFile = open("temperatures.txt", "a")
    print("This program writes temperature data to \ntemperatures.txt")
    print("If the file does not exist, it will be created")
    city = input ("Enter city name, xxx to end: ")
    while city != "xxx":
        temperature = input("Enter temperature: ")
        localTime = input ("Enter local time: ")
        tempsFile.write(city + "," + temperature + "," + localTime + "," + "\n")
        city = input ("Enter city name, xxx to end: ")
    #endwhile
    tempsFile.close()

def eg7():
    #Program name: Ch 9 Example 7 process temperatures file.py
    tempsFile = open("temperatures.txt", "r")
    cityTable = []
    newCityRec = []

    for row in tempsFile:
        cityRec = row.split(",")
        city = cityRec [0]
        temperatureC = float (cityRec[1])
        tempF = (temperatureC * 9/5) + 32
        localTime = cityRec [2]
        
        newCityRec.append(city)
        newCityRec.append(temperatureC)
        newCityRec.append(tempF)
        newCityRec.append(localTime)
    
        #Append record to table, and clear newCityRec for next record
        cityTable.append(newCityRec)
        newCityRec = []


    #All the records are now held in a 2-D list called cityTable
    #Sort the list in descending sequence on temperatureC
    #Refer to Chapter 7 for how to do this using the lambda function
    sortedTable = sorted (cityTable, key=lambda x:x, reverse=True)

    print("\nList of cities in descending order of temperature \n")
    for n in range (len (sortedTable)):
        print (sortedTable [n], sortedTable [n], sortedTable [n], sortedTable [n])
    
    tempsFile.close()


def with_eg5():
    # Equivalanet of eg5() using the with statement
    # More modern python version
    with open("films.txt", "r", encoding="utf-8") as filmFile:
        for row in filmFile:
            # Each line comes with its raw comma-separated string
            field = row.split(",")
            ID = field[0]
            title = field[1]
            
            
            # Clean up the trailing newline '\n' on the final field if necessary
            genre = field[5].rstrip('\n') 
            
            print(f"ID: {ID} | Title: {title} | Genre: {genre}")

def readFilms(fn):
    inF = open(fn, "r")
    data = []
    with open("films.txt", "r", encoding="utf-8") as inF:
        aLine = aLine.rstrip()
        for aLine in inF:
            record = aLine.split(",")
            record[2] = int(record[2]) #year
            record[4] = int(record[4]) #duration
            #record[5] = record[5].rstrip()
        
        data.append(record)
        
    inF.close()
    return data
        
data = readFilms("films.txt")
print(data)