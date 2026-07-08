cart=[]
def shoppingCart():
    print("1.Add Product")
    print("2.Remove Product")
    print("3.View Cart")
    choice=int(input("Enter choice : "))
    if choice==1:
        cart.append(input("Enter Product want to add : "))
    elif choice == 2:
        cart.remove(input("Enter Product want to remove : "))
    elif choice == 3:
        for i in cart:
            print(f"{i}", end = ",")
        print()
    else :
        print("Please Enter correct choice ")
        shoppingCart()

while True:
    check=input("Enter X for Exit or Enter anything for continue : ")
    if check=="X" or check=="x":
        break
    shoppingCart()
