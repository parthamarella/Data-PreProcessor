import pandas as pd


print("This is a Preprocessing tool\n")
#can make this dynamic input from user 
df=pd.read_csv("tested.csv")

print("Enter the corresponding number to perform an action:\n")

#Input loop
flag = True
while flag:    
    print("1.Data Description\n")
    print("2.Handling NULL values\n")
    print("3.Encoding categorical data\n")
    print("4.Download the modified data\n")
    print("5. Exit\n")
    userInput=int(input("Enter your Option:"))
    ####Handling Option 1 (Data Description)
    if userInput==1:
        print("Tasks Data Description:\n")
        print("1.Describe the dataset\n")
        print("2.Show properties of the dataset\n")
        print("3.Show the dataset\n")
        subUserInput=int(input("What do you want to do? (Press -1 to go back)"))
        if subUserInput==1:
            print("1.Describing the dataset\n")
            print(df.describe())
        elif subUserInput==2:
            print("2.Showing properties of the dataset\n")
            print(df.info())
        elif subUserInput==3:
            print("3.Showing the dataset\n")
            print(df.head())
        elif subUserInput==-1:
            print("Going back the menu\n")
            continue
        else:
            print("Enter a valid input\n")
    ######Handing Option 2 (Handling NULL values)
    elif userInput==2:
        print("1.Show number of NULL values\n")
        print("2.Remove columns\n")
        print("3.Fill NULL values with Mean\n")
        print("4.Fill NULL values with Median\n")
        print("5.Fill NULL values with Mode\n")
        print("6.Show the dataset\n")
        subUserInput=int(input("What do you want to do? (Press -1 to go back)"))
        if subUserInput==1:
            print("Showing total NULL values in the dataset:\n")
            print(df.isna().sum())
        elif subUserInput==2:
            print("Removing column:\n")
            columnNumber=int(input("Enter column number you want to delete"))
            print("You have SUCCESSFULLY dropped column:",df.columns[columnNumber])
            newdf=df.drop(df.columns[columnNumber], axis = 1)
            print(newdf)
    elif userInput==3:
        print("Option 3 selected")
    elif userInput==4:
        print("Option 4 selected")
    elif userInput==5:
        print("Program exiting")
        break
    else:
        print("Enter valid input\n")

    
        




