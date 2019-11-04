import Inventory as I
from Cashier import Cashier as c
import os


def main():
    try:
        db = 'vend.db'
        inv = I.Inventory(db)
        vend(inv)
    except IOError:
        print("DB Not Found!!")


def vend(inv):
    load = inv.loadinventory()
    breaker = 0
    change = 0
    while breaker == 0:
        if change > 0:
            print("Remaining cash: ${}".format(change))

        for i in range(0, len(load)):
            message = "{}: {} -- $ {}".format(i+1, load[i].getName(), load[i].getPrice())
            if load[i].getQty() > 0:
                print(message)
            else:
                print(message, " --OUT OF STOCK")

        selection = input("Choose a candy: ")
        if selection.isalpha():
            if change > 0:
                os.system('clear')
                print("Goodbye! Here is your change {}".format(change))
                break
            else:
                os.system('clear')
                print("Goodbye!")
                break
        os.system('clear')
        selection = int(selection) - 1

        if load[selection].getQty() > 0:
            if change == 0:
                print("{} selected! Please insert $ {}".format(load[selection].getName(),
                                                               load[selection].getPrice()))
                cash = float(input("Insert money: "))

            elif change >= float(load[selection].getPrice()):
                cash = change

            else:
                print("{} selected! Please insert $ {}".format(load[selection].getName(),
                                                               load[selection].getPrice() - change))
                cash = float(input("Insert money: ")) + change

            os.system('clear')
            if cash >= load[selection].getPrice():
                change = c(cash, load[selection].getPrice())
                change = float(change.makechange())

                for i in range(1, 5):
                    print("Dispensing {} ".format(load[selection].getName()), "."*i)
                    os.system('sleep .1')
                    os.system('clear')

                load[selection].sale()

            else:

                while cash < load[selection].getPrice():
                    print("Insert more money ${} needed".format(abs(round((cash - load[selection].getPrice()),2))))
                    insuf = float(input('Insert Money: '))
                    insufchange = c((load[selection].getPrice() - cash), insuf)
                    insufchange = float(insufchange.makechange())
                    if insufchange <= (load[selection].getPrice() - change):
                        load[selection].sale()
                        os.system('clear')
                        change = abs(insufchange)
                        break
                    else:
                        change = (insufchange - load[selection].getPrice())
        else:
            print("Out of stock.\nPlease select new item.")
            os.system('sleep 2')
            os.system('clear')


if __name__ == '__main__':
    os.system('clear')
    main()
