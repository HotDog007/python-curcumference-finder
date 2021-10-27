
while True:
    print('Welcome to Curcumference Finder  ')

    print('The formula to find Curcumference is  2 * 22/7 * radius')



    def multiply(x, y):
        return x * y
    
    cur = float(input("Enter the radius: "))
    print("2 * 22/7 * " + str(cur) + " =", multiply( 22/7, cur)*2)
    
    nextcal = input("Continue?(yes/no): \n--> ")
    if nextcal == 'yets':
        print('ok, you are the developer!')
    elif nextcal == 'no':
        break
    else:
        print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ")
