#Function definition

def display_menu():
    print("\n"+"="*30)
    print('        LIST OPERATIONS')
    print("  1. Append Element")
    print("  2.Insert Elements")
    print("  3.Extend Elements")
    print("  4.Remove Elements")
    print("  5.Sort List")
    print("  6.Display list summary")
    print("  7.Exit")
    print("="*30)

def main():
    list=[]
    while (True):
        display_menu()
        option=int(input("Enter Option (1-7) : "))
        if option==1:
            element=input("Enter Element : ")
            list.append(element)
            print(f"{element} is appended to the list")
        elif option==2:
            ind=int(input("Enter Index : "))
            element=input("Enter Element : ")
            list.insert(ind,element)
            print(f"{element} is inserted to the list")
        elif option==3:
            elements=input("Enter List : ")
            list.extend(elements.split())
            # method 2
            # elements=eval(input("Enter List : "))
            # list.extend(elements)
            print(f"{elements.split()} is entended to the list")
        elif option==4:
            element=input("Enter Element : ")
            list.remove(element)
            print(f"{element} is removed to the list")
        elif option==5:
            list.sort()
            print("List is sorted in accending order")
        elif option==6:
            print(f"-----Current List-----")
            print(f"List = {list}")
            print(f"Length of the list = {len(list)}")
        elif option==7:
            print("You pressed exit button (7)---bye bye ")
            break
        else :
            print("Please Enter valid options")

if __name__=="__main__":
    main()
