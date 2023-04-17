import datetime

def main():
    time = datetime.datetime.now()
    print("""     
                   _______
                  //  ||\ \\
            _____//___||_\ \___
            )  _          _    \\
            |_/ \________/ \___|
           ___\_/________\_/______
       """)
 
    print("\n\tWELCOME TO CAB SERVICE!\n")
    print(f"\tCurrent date and time: {time}")
 
    while True:
        print("""
        ******** Car Rental Shop ********
        1. Login
        2. Rejister
        3. Exit the program
        """)
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            registered_function()
 
        elif choice == 2:
            register()
 
        elif choice == 3:
            break
 
        else:
            print("Please enter a choice between 1-3 only!")
            
def register():
    with open("Data/User_Data.txt", "a") as text:
        while True:
            name = input("Enter name to register: ")
            password = input("Enter password: ")
            record = name + ":" + password
            text.write(record + "\n")
            break
        
 
 
def existing_users():
    nValue = input("Username: ")
    pValue = input("Password: ")
    return login(nValue, pValue, False)
 
 
def login(user, password, elevated):
    with open("Data/User_Data.txt" , "r") as text:
        print("%s Login ********" % ("******** Admin" if elevated else "******** User"))
        for record in text:
            recordList = record.rstrip().split(":")
            if user.lower() in recordList[0].lower() and password in recordList[1]:
                print("Welcome, %s" % user)
                return True
        print("Error! Wrong username or password")
        return False
 
def registered_function():
    if existing_users() is True:
        while True:
            print("""
            ******** Access System ********
            1. Add a new vehicle
            2. Remove a vehicle 
            3. Assign a job (hire)
            4. Release form assigned job (hire)
            5. See available vehicles in each category
            6. Exit to main menu
            """)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number!")
                continue
 
            if choice == 1:
                add_vehicles()
 
            elif choice == 2:
                remove_vehicle()
 
            elif choice == 3:
                book_vehicle()
 
            elif choice == 4:
                release_vehicle()
 
            elif choice == 5:
                available_vehicle()
                
            elif choice == 5:
                break
 
            else:
                print("Please enter a choice between 1-5 only!")
    else:
        print("1. Please re-enter login details")
        print("2. Exit to main menu")
        choice = int(input("Enter choice: "))
        if choice == 1:
            existing_users()
        else:
            return
        
#=============================Add Vehicle detail=======================
        
def add_vehicles():
    
    while True:
        print("""
        ******** Select Vehicle Type ********
        1. Add Cars
        2. Add Vans
        3. Add Three Wheelers
        4. Add Lorries
        5. Add Trucks
        6. Exit the program
        """)
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            print("******** Add Car Details ********")
            add_car()
 
        elif choice == 2:
            print("******** Add Van Details ********")
            add_van()
 
        elif choice == 3:
            print("******** Add Three Wheel Details ********")
            add_three_wheel()
            
        elif choice == 4:
            print("******** Add Lorry Details ********")
            add_lorry()
            
        elif choice == 5:
            print("******** Add Truck Details ********")
            add_truck()
 
        elif choice == 6:
            break
 
        else:
            print("Please enter a choice between 1-6 only!")
            
            
def add_car():   
    with open("Data/Available_Vehicle/Available_Car_Data.txt", "a") as text:
        
        carNumber = input("Car Number: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        passengers = input("Maximum number of passengers: ")
        AC = input("AC / Non-AC: ")
        text.write("\n%s:%s:%s:%s:%s:%s" % (carNumber, brand, color, year,passengers,AC))
        
def add_van():
    with open("Data/Available_Vehicle/Available_Van_Data.txt", "a") as text:
        
        vanNumber = input("Van Number: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        passengers = input("Maximum number of passengers: ")
        AC = input("AC / Non-AC: ")
        text.write("\n%s:%s:%s:%s:%s:%s" % (vanNumber, brand, color, year,passengers,AC))
        
        if AC==AC:
            with open("Data/Available_Vehicle/Available_VanAC_Data.txt", "a") as text: 
               text.write("\n%s:%s:%s:%s:%s:%s" % (vanNumber, brand, color, year,passengers,AC))
               
        else:
            with open("Data/Available_Vehicle/Available_VanNonAC_Data.txt", "a") as text: 
               text.write("\n%s:%s:%s:%s:%s:%s" % (vanNumber, brand, color, year,passengers,AC))
        
def add_three_wheel():
    with open("Data/Available_Vehicle/Available_ThreeWheel_Data.txt", "a") as text:
        
        three_wheelNumber = input("Three Wheel Number: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        passengers = input("Maximum number of passengers: ")
        text.write("\n%s:%s:%s:%s:%s" % (three_wheelNumber, brand, color, year,passengers))
        
def add_lorry():
    with open("Data/Available_Vehicle/Available_Lorry_Data.txt", "a") as text:
        
        lorryNumber = input("Lorry Number: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        size = input("7Ft or 12Ft: ")
        load = input("Max Load(2500Kg or 3500Kg): ")
        text.write("\n%s:%s:%s:%s:%s:%s" % (lorryNumber, brand, color, year,size,load))
        
def add_truck():
    with open("Data/Available_Vehicle/Available_Truck_Data.txt", "a") as text:
        
        truckNumber = input("Truck Number: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        size = input("7Ft or 12Ft:")
        text.write("\n%s:%s:%s:%s:%s" % (truckNumber, brand, color, year,size)) 
        

#=================================Remove Vehicle==============================

def remove_vehicle():
    while True:
        print("""
        ******** Select Vehicle Type ********
        1. Remove Cars
        2. Remove Vans
        3. Remove Three Wheelers
        4. Remove Lorries
        5. Remove Trucks
        6. Exit the program
        """)
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            print("******** Remove Cars ********")
            remove_car()
 
        elif choice == 2:
            print("******** Remove Vans ********")
            remove_van()
 
        elif choice == 3:
            print("******** Remove Three Wheeles ********")
            remove_three_wheel()
            
        elif choice == 4:
            print("******** Remove lorry ********")
            remove_lorry()
            
        elif choice == 5:
            print("******** Remove Trucks ********")
            remove_truck()
 
        elif choice == 6:
            break
 
        else:
            print("Please enter a choice between 1-6 only!")
            
            
def remove_car():
    available_car()
    with open("Data/Available_Vehicle/Available_Car_Data.txt", "r") as f:
        index_to_remove= int(input("Select record to remove: "))  
        lines = f.readlines()
        lines.pop(index_to_remove)
        with open("Data/Available_Vehicle/Available_Car_Data.txt", "w") as new_f:
            for line in lines:        
                new_f.write(line)

    
def remove_van():
    available_van()
    with open("Data/Available_Vehicle/Available_Van_Data.txt", "r") as f:
        index_to_remove= int(input("Select record to remove: "))  
        lines = f.readlines()
        lines.pop(index_to_remove)
        with open("Data/Available_Vehicle/Available_Van_Data.txt", "w") as new_f:
            for line in lines:        
                new_f.write(line)
    
def remove_three_wheel():
    available_three_wheel()
    with open("Data/Available_Vehicle/Available_ThreeWheel_Data.txt", "r") as f:
        index_to_remove= int(input("Select record to remove: "))  
        lines = f.readlines()
        lines.pop(index_to_remove)
        with open("Data/Available_Vehicle/Available_ThreeWheel_Data.txt", "w") as new_f:
            for line in lines:        
                new_f.write(line)
    
def remove_lorry():
    available_lorry()
    with open("Data/Available_Vehicle/Available_Lorry_Data.txt", "r") as f:
        index_to_remove= int(input("Select record to remove: "))  
        lines = f.readlines()
        lines.pop(index_to_remove)
        with open("Data/Available_Vehicle/Available_Lorry_Data.txt", "w") as new_f:
            for line in lines:        
                new_f.write(line)
    
def remove_truck():
    available_truck()
    with open("Data/Available_Vehicle/Available_Truck_Data.txt", "r") as f:
        index_to_remove= int(input("Select record to remove: "))  
        lines = f.readlines()
        lines.pop(index_to_remove)
        with open("Data/Available_Vehicle/Available_Truck_Data.txt", "w") as new_f:
            for line in lines:        
                new_f.write(line)
    
    
    
#==============================Book Vehicle===================================

def book_vehicle():
    while True:
        print("""
        ******** Select Vehicle Type ********
        1. Book Cars
        2. Book Vans
        3. Book Three Wheelers
        4. Book Lorries
        5. Book Trucks
        6. Exit the program
        """)
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            print("******** Book Cars ********")
            Book_car()
 
        elif choice == 2:
            print("******** Book Vans ********")
            Book_van()
 
        elif choice == 3:
            print("******** Book Three Wheeles ********")
            Book_three_wheel()
            
        elif choice == 4:
            print("******** Book lorry ********")
            Book_lorry()
            
        elif choice == 5:
            print("******** Book Trucks ********")
            Book_truck()
 
        elif choice == 6:
            break
 
        else:
            print("Please enter a choice between 1-6 only!")
            
def Book_car():   
    available_car()
    with open("Data/Available_Vehicle/Available_Car_Data.txt", "r") as f:
        index_to_book= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Book_Vehicle/Book_Car_Data.txt", "a") as f:
            f.writelines(lines[index_to_book])
            lines.pop(index_to_book)
            with open("Data/Available_Vehicle/Available_Car_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)
                    
                    
def Book_van():   
    available_van()
    with open("Data/Available_Vehicle/Available_Van_Data.txt", "r") as f:
        index_to_book= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Book_Vehicle/Book_Van_Data.txt", "a") as f:
            f.writelines(lines[index_to_book])
            lines.pop(index_to_book)
            with open("Data/Available_Vehicle/Available_Van_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)

def Book_three_wheel():   
    available_three_wheel()
    with open("Data/Available_Vehicle/Available_ThreeWheel_Data.txt", "r") as f:
        index_to_book= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Book_Vehicle/Book_ThreeWheel_Data.txt", "a") as f:
            f.writelines(lines[index_to_book])
            lines.pop(index_to_book)
            with open("Data/Available_Vehicle/Available_ThreeWheel_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)
def Book_lorry():   
    available_lorry()
    with open("Data/Available_Vehicle/Available_Lorry_Data.txt", "r") as f:
        index_to_book= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Book_Vehicle/Book_Lorry_Data.txt", "a") as f:
            f.writelines(lines[index_to_book])
            lines.pop(index_to_book)
            with open("Data/Available_Vehicle/Available_Lorry_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)

def Book_truck():   
    available_truck()
    with open("Data/Available_Vehicle/Available_Truck_Data.txt", "r") as f:
        index_to_book= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Book_Vehicle/Book_Truck_Data.txt", "a") as f:
            f.writelines(lines[index_to_book])
            lines.pop(index_to_book)
            with open("Data/Available_Vehicle/Available_Truck_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)                                                                               
                    
#=========================Release form assigned job=========================

def release_vehicle():
    while True:
        print("""
        ******** Select Vehicle Type ********
        1. Release Cars
        2. Release Vans
        3. Release Three Wheelers
        4. Release Lorries
        5. Release Trucks
        6. Exit the program
        """)
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            print("******** Release Cars ********")
            release_car()
 
        elif choice == 2:
            print("******** Release Vans ********")
            release_van()
 
        elif choice == 3:
            print("******** Release Three Wheeles ********")
            release_three_wheel()
            
        elif choice == 4:
            print("******** Release lorry ********")
            release_lorry()
            
        elif choice == 5:
            print("******** Release Trucks ********")
            release_truck()
 
        elif choice == 6:
            break
 
        else:
            print("Please enter a choice between 1-6 only!")
            

def release_car():   
    DisplayBook_car()
    with open("Data/Book_Vehicle/Book_Car_Data.txt", "r") as f:
        index_to_release= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Available_Vehicle/Available_Car_Data.txt", "a") as f:
            f.writelines(lines[index_to_release])
            lines.pop(index_to_release)
            with open("Data/Book_Vehicle/Book_Car_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)
            
def release_van():   
    DisplayBook_van()
    with open("Data/Book_Vehicle/Book_Van_Data.txt", "r") as f:
        index_to_release= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Available_Vehicle/Available_Van_Data.txt", "a") as f:
            f.writelines(lines[index_to_release])
            lines.pop(index_to_release)
            with open("Data/Book_Vehicle/Book_Van_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)
                    
def release_three_wheel():   
    DisplayBook_three_wheel()
    with open("Data/Book_Vehicle/Book_ThreeWheel_Data.txt", "r") as f:
        index_to_release= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Available_Vehicle/Available_ThreeWheel_Data.txt", "a") as f:
            f.writelines(lines[index_to_release])
            lines.pop(index_to_release)
            with open("Data/Book_Vehicle/Book_ThreeWheel_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)
                    
def release_lorry():   
    DisplayBook_lorry()
    with open("Data/Book_Vehicle/Book_Lorry_Data.txt", "r") as f:
        index_to_release= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Available_Vehicle/Available_Lorry_Data.txt", "a") as f:
            f.writelines(lines[index_to_release])
            lines.pop(index_to_release)
            with open("Data/Book_Vehicle/Book_Lorry_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)
                    
def release_truck():   
    DisplayBook_truck()
    with open("Data/Book_Vehicle/Book_Truck_Data.txt", "r") as f:
        index_to_release= int(input("Select record to book: "))  
        lines = f.readlines()
        with open("Data/Available_Vehicle/Available_Truck_Data.txt", "a") as f:
            f.writelines(lines[index_to_release])
            lines.pop(index_to_release)
            with open("Data/Book_Vehicle/Book_Truck_Data.txt", "w") as new_f:
                for line in lines:        
                    new_f.write(line)                                                                       
            
#==============================Display Book Vehicle===========================

def DisplayBook_car():
    with open("Data/Book_Vehicle/Book_Car_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            car_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            passengers = splitted[4]
            AC = splitted[5]
            print("%d. Car number: %s Brand: %s Color: %s Year: %s Passengers: %s AC / Non-AC: %s" % (index, car_number, brand, color, year, passengers, AC))
            index += 1
            
def DisplayBook_van():
    with open("Data/Book_Vehicle/Book_Van_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            car_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            passengers = splitted[4]
            AC = splitted[5]
            print("%d. Van number: %s Brand: %s Color: %s Year: %s Passengers: %s AC / Non-AC: %s" % (index, car_number, brand, color, year, passengers, AC))
            index += 1
            
def DisplayBook_three_wheel():
    with open("Data/Book_Vehicle/Book_ThreeWheel_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            car_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            passengers = splitted[4]
            print("%d. Threewheel number: %s Brand: %s Color: %s Year: %s Passengers: %s " % (index, car_number, brand, color, year, passengers))
            index += 1
            
def DisplayBook_lorry():
    with open("Data/Book_Vehicle/Book_Lorry_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            car_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            size = splitted[4]
            load = splitted[5]
            print("%d. Lorry number: %s Brand: %s Color: %s Year: %s Size: %s Max_Load: %s" % (index, car_number, brand, color, year, size, load))
            index += 1
            
def DisplayBook_truck():
    with open("Data/Book_Vehicle/Book_Truck_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            car_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            size = splitted[4]
            print("%d. Truck number: %s Brand: %s Color: %s Year: %s Size: %s" % (index, car_number, brand, color, year, size))
            index += 1                                                
         
        
        
#========================Check Available Vehicle=====================

def available_vehicle():
    while True:
        print("""
        ******** Select Vehicle Type ********
        1. Available Cars
        2. Available Vans
        3. Available Three Wheelers
        4. Available Lorries
        5. Available Trucks
        6. Exit the program
        """)
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            print("******** Available Cars ********")
            available_car()
 
        elif choice == 2:
            print("******** Available Vans ********")
            available_van()
 
        elif choice == 3:
            print("******** Available Three Wheeles ********")
            available_three_wheel()
            
        elif choice == 4:
            print("******** Available lorry ********")
            available_lorry()
            
        elif choice == 5:
            print("******** Available Trucks ********")
            available_truck()
 
        elif choice == 6:
            break
 
        else:
            print("Please enter a choice between 1-6 only!")
            
            
def available_car(): 

    with open("Data/Available_Vehicle/Available_Car_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            Vehicle_type = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            passengers = splitted[4]
            AC = splitted[5]
            print("%d. Car Number: %s Brand: %s Color: %s Year: %s Passengers: %s AC / Non-AC: %s" % (index, Vehicle_type, brand, color, year, passengers, AC))
            index += 1
            
            
def available_van():
    with open("Data/Available_Vehicle/Available_Van_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            car_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            passengers = splitted[4]
            AC = splitted[5]
            print("%d. Van number: %s Brand: %s Color: %s Year: %s Passengers: %s AC / Non-AC: %s" % (index, car_number, brand, color, year, passengers, AC))
            index += 1
            
def available_three_wheel():
    with open("Data/Available_Vehicle/Available_ThreeWheel_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            three_wheel_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            passengers = splitted[4]
            print("%d. Three Wheel Number: %s Brand: %s Color: %s Year: %s Passengers: %s" % (index, three_wheel_number, brand, color, year, passengers))
            index += 1
            
def available_lorry():
    with open("Data/Available_Vehicle/Available_Lorry_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            lorry_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            size = splitted[4]
            load = splitted[5]
            print("%d. Lorry Number: %s Brand: %s Color: %s Year: %s Size: %s Max_Load: %s" % (index, lorry_number, brand, color, year, size, load))
            index += 1
            
def available_truck():
    with open("Data/Available_Vehicle/Available_Truck_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            truck_number = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            size = splitted[4]
            print("%d. Truck Number: %s Brand: %s Color: %s Year: %s Size: %s" % (index, truck_number, brand, color, year, size))
            index += 1



if __name__ == "__main__":
    main()