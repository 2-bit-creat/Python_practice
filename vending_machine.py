class VendingMachine:
    item_name = {}
    item_price = {}
    money = 0
    revenue = 0
    count = 0


    def __init__(self, name, price):
        self.item_name = name
        self.item_price = price
        print(self.item_name)

    def run(self):
        while True:
            choice = input("Another VM(y/n) ? ")
            if choice.lower() == 'y':
                break
            elif choice.lower() != 'n':
                print("Invalid input")
                continue
            try:
                self.money = int(input("how much ? "))

            except ValueError:
                print("Invalid input")

            else:
                if self.money % 100 != 0:
                    print("it is not 100 unit")
                    self.run()
                else:
                    self.select_product()

    def select_product(self):
        product_num = input("select(1 or 2 or 3) ? ")
        self.payment(product_num)

    def payment(self, num):
        if self.money < self.item_price[num]:
            print("not enough money")
            self.return_change()
        else:
            print("Payment is done")
            self.money -= self.item_price[num]
            self.revenue += self.item_price[num]
            self.count += 1
            print("revenue:", self.revenue, "count:", self.count)
            self.return_change()

    def return_change(self):
        print("Your change is", self.money)
        self.money = 0


if __name__ == '__main__':
    VM1_revenue = (0,0)
    VM2_revenue = (0,0)
    VM3_revenue = (0,0)

    while True:
        ch = input("print revenue(y/n) ? ")
        if ch.lower() == 'y':
            print("VM1: revenue =", VM1_revenue[0], ", count =", VM1_revenue[1])
            print("VM2: revenue =", VM2_revenue[0], ", count =", VM2_revenue[1])
            print("VM2: revenue =", VM3_revenue[0], ", count =", VM3_revenue[1])
        elif ch.lower() != 'n':
            print("Invalid input")
            continue

        print("1:drinks, 2:snacks, 3:necessaries")
        select_VM = input("Choose(1 or 2 or 3) ? ")

        if select_VM == '1':
            name = {"1": "drink1(800 won)", "2": "drink2(1000 won)", "3": "drink3(500 won)"}
            price = {"1": 800, "2": 1000, "3": 500}
            a = VendingMachine(name, price)
            a.run()
            VM1_revenue = a.revenue, a.count

        elif select_VM == '2':
            name = {"1": "snack1(800 won)", "2": "snack2(1000 won)", "3": "snack3(500 won)"}
            price = {"1": 800, "2": 1000, "3": 500}
            a = VendingMachine(name, price)
            a.run()
            VM2_revenue = a.revenue, a.count

        elif select_VM == '3':
            name = {"1": "nec1(800 won)", "2": "nec2(1000 won)", "3": "nec3(500 won)"}
            price = {"1": 800, "2": 1000, "3": 500}
            a = VendingMachine(name, price)
            a.run()
            VM3_revenue = a.revenue, a.count

        else:
            print("Invalid input")


