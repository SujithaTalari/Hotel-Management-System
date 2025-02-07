class HotelManage:

    def __init__(self):
        print("\t\t*******************************************\n")
        print("\t\t*******************************************\n")
        print("\t\t************WELCOME TO LPU HOTEL***********\n")
        self.room_rate = 0
        self.food_bill = 0
        self.total_bill = 0
        self.additional_charge = 750
        self.customer_name = ''
        self.customer_address = ''
        self.check_in_date = ''
        self.check_out_date = ''
        self.room_no = 1

    def input_data(self):
        self.customer_name = input("\n\t\tEnter your Fullname:")
        self.customer_address = input("\n\t\tEnter your address:")
        self.check_in_date = input("\n\t\tEnter your arrival date:")
        self.check_out_date = input("\n\t\tEnter your leaving date:")
        print("\n\t\tYour room no.:", self.room_no, "\n")

    def room_rent(self):
        print("We have the following rooms for you:-")
        print("1.  LUXURY ROOM---->4000")
        print("2.  DELUX ROOM---->3000")
        print("3.  DOUBLE BED ROOM---->2000")
        print("4.  SINGLE BED ROOM---->1000")

        room_choice = int(input("Enter the number of your choice Please->"))
        nights_stayed = int(input("For how many nights did you stay:"))

        if room_choice == 1:
            self.room_rate = 4000 * nights_stayed
            print("You have chosen Luxury Room")
        elif room_choice == 2:
            self.room_rate = 3000 * nights_stayed
            print("You have chosen Delux Room")
        elif room_choice == 3:
            self.room_rate = 2000 * nights_stayed
            print("You have chosen Double Bed Room")
        elif room_choice == 4:
            self.room_rate = 1000 * nights_stayed
            print("You have chosen Single Bed Room")
        else:
            print("Please choose a valid room.")

        print("Your chosen room rent is =", self.room_rate, "\n")

    def food_purchased(self):
        print("**RESTAURANT MENU**")
        print("1.Dessert----->100", "2.Drinks----->50", "3.Breakfast--->90", "4.Lunch---->110", "5.Dinner--->150",
              "6.Exit")

        while True:
            choice = int(input("Enter the number of your choice:"))

            if choice == 1:
                quantity = int(input("Enter the quantity:"))
                self.food_bill += 100 * quantity
            elif choice == 2:
                quantity = int(input("Enter the quantity:"))
                self.food_bill += 50 * quantity
            elif choice == 3:
                quantity = int(input("Enter the quantity:"))
                self.food_bill += 90 * quantity
            elif choice == 4:
                quantity = int(input("Enter the quantity:"))
                self.food_bill += 110 * quantity
            elif choice == 5:
                quantity = int(input("Enter the quantity:"))
                self.food_bill += 150 * quantity
            elif choice == 6:
                break
            else:
                print("You've entered an invalid key")

        print("Total food Cost = Rs", self.food_bill, "\n")

    def display(self):
        print("***HOTEL BILL***")
        print("Customer details:")
        print("Customer name:", self.customer_name)
        print("Customer address:", self.customer_address)
        print("Check-in date:", self.check_in_date)
        print("Check-out date:", self.check_out_date)
        print("Room no.:", self.room_no)
        print("Your Room rent is:", self.room_rate)
        self.total_bill = self.room_rate + self.food_bill + self.additional_charge
        print("Your Food bill is:", self.food_bill)
        print("Your sub total Purchased is:", self.total_bill - self.additional_charge)
        print("Additional Service Charges is", self.additional_charge)
        print("Your grand total Purchased is:", self.total_bill, "\n")
        self.room_no += 1
def main():
        additional_charge=HotelManage()
        while True:
            print("1.Enter customer data")
            print("2.calculate roomrent")
            print("3.calculate food purchased")
            print("4.show total cost")
            print("5.exit")
            choice  = int(input("\nEnter your choice:"))
            if choice == 1:
                additional_charge.input_data()
            elif choice == 2:
                additional_charge.room_rent()
            elif choice == 3:
                additional_charge.food_purchased()
            elif choice == 4:
                additional_charge.display()
            elif choice == 5:
                quit()
            else:
                print("Invalid")
main()
            
