class Atm:

    __counter = 1           

    def __init__(self): 
        self.__pin = ""          
        self.__balance = 0       
        self.sno = Atm.__counter   
        Atm.__counter = Atm.__counter + 1    
        self.__menu()

# get or set for update counter

    @staticmethod     
    def get_counter():    
        return Atm.__counter  

    @staticmethod
    def set_counter(new):   
        if type(new) == int:
            Atm.__counter = new
        else:
            print("not allowed counter")    

# get or set method for access privet methods

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str and len(new_pin) == 4:
            self.__pin = new_pin
            return ("done")
        else:
            print("not allowed")  
    
    def __menu(self):
        user_input = input(""""
        hello, what u like
        1. enter 1 to create pin
        2. enter 2 to deposit
        3. enter 3 to withdraw
        4. enter 4 to check balance
        5. enter 5 to exit
        """)

        if user_input =="1":
            self.create_pin()
        elif user_input =="2":
            self.deposit()
        elif user_input =="3":
            self.withdraw()
        elif user_input =="4":
            self.check_balance()
        else:
            print("Exit successful")
            
    def create_pin(self):
        temp = input("enter pin")
        if len(temp) != 4:
            print("pin must be 4 digit")
        else:
            self.__pin = temp
            print("pin created")

    def deposit(self):
        temp = input("enter pin")
        if temp == self.__pin:
            ammount = int(input("input"))
            self.__balance = self.__balance + ammount
            print("deposit done", self.__balance)
        else:
            print("invalid pin")

    def withdraw(self):
        temp = input("enter pin")
        if temp == self.__pin:
            ammount = int(input("input"))
            if ammount < self.__balance:
                self.__balance = self.__balance - ammount
                print("withdraw done", self.__balance)
            else:
                print("insufficient balance")
        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("enter pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")

