import pandas as pd
import numpy as np
import sqlalchemy
import matplotlib.pyplot as plt
import pymysql
df=pd.DataFrame()
csv_file="C:\\Users\\Ketan Thombare\\OneDrive\\Documents\\Projects\\my-frontend\\Project.csv"
csv_export ="C:\\Users\\Ketan Thombare\\OneDrive\\Documents\\Projects\\my-frontend\\export.csv"
def read_csv_file():
    df =pd.read_csv(csv_file)
    print(df)
def clear():
    for x in range(10):
        print()
def data_analysis_menu():
    df=pd.read_csv(csv_file)
    while True:
        clear()
        print('Data Analysis MENU')
        print('_'*150)
        print('1. Show Whole DataFrame\n')
        print('2. Show Columns\n')
        print('3. Show Top Rows\n')
        print('4. Show Bottom Rows\n')
        print('5. Show Specific Column\n')
        print("6. Show Specific Row\n")
        print('7. Add a New Record\n')
        print('8. Add a New Column\n')
        print('9. Delete a Column\n')
        print('10. Delete a Record\n')
        print('11. Product Id Wise Stock\n')
        print('12. Data Summary\n')
        print('13. Exit(Back to Main Menu)\n')
        ch = int(input('Enter your choice:'))
        if ch==1:
            print(df)
            wait = input()
        elif ch==2:
            print(df.columns)
            wait = input()
        elif ch==3:
            n=int(input('Enter Total Rows You Want To Show :'))
            print(df.head(n))
            wait = input()
        elif ch==4 :
            n=int(input('Enter Total Rows You Want To Show :'))
            print(df.tail(n))
            wait = input()
        elif ch==5:
            print(df.columns)
            col_name=input('Enter Column Name That You Want To Print :')
            print(df[col_name])
            wait = input()
        elif ch==6:
            print("Enter index no. of row that you what to see from 0-",len(df)-1)
            k= int(input(":"))
            print (df.iloc[k])
            wait =input()
        elif ch==7:
            Product_Number=input('Inventory Control ID:')
            Product_Detail=input('Product Detail:')
            Product_Quantity=(int(input('Quantity Purchased : ')))
            Product_Price=(int(input('Price: ')))
            Quantity_in_Stock=(int(input("Quantity in Stock :")))
            Reorder_Level=(int(input("Reorder Level :")))
            Reorder_Quantity=(int(input("Reorder Quantity :")))
            Quantity_Sold=(int(input("Quantity Sold :")))
            Total_Reorder=(int(input("Total Reorder :")))
            df.loc[len(df)]=[Product_Number,Product_Detail,Product_Quantity,Product_Price,Quantity_in_Stock,Reorder_Level,Reorder_Quantity,Quantity_Sold,Total_Reorder]
            print(df)
            wait = input()
            
        elif ch==8:
            col_name=input('Enter new column name :')
            col_value=eval(input('Enter default column value :'))
            df[col_name]=col_value
            print(df)
            print('Press any key to continue......')
            wait=input()
        elif ch==9:
         print(df.columns)
         col_name=input('Enter column Name to delete :')
         del df[col_name]
         print(df)
         wait=input()
        elif ch==10:
            print('Choose Row Index From 0 to',len(df)-1)
            index_no =int(input('Enter The Index Number That You Want To Delete: '))
            df=df.drop(index_no)
            print(df)
            print('\n\n press any key to continue....')
            wait= input()
        elif ch ==11:
        
           print("enter 1 to see all the  Currently avalable stock ")
           print("enter 2  to see all the Currently  unavalible stocks")
           r =int (input("enter   your choice : "))
           if r==1:
               df1=df.loc[(df["Quantity_in_Stock"]!=0),:]
               print(df1)
           elif r==2:
               df1=df.loc[(df["Quantity_in_Stock"]==0),:]
               print(df1)
           else :
               print(' wrong choice ')
               print('\n\n press enter key to continue....')
               wait = input ()
        elif ch==12:
            
                   print(df.info())
                   print('\n\n press any key  to continue....')
                   wait=input()
        elif ch==13:
            break
def graph():
    df=pd.read_csv(csv_file)
    while True:
        clear()
        print ('\nGraph Menu')
        print ('_'*100)
        print ("1. Line chart\n")
        print ("2. Bar chart\n")
        print ("3. Histogram\n")
        print ('4. exit (back to manin menu)\n')
        ch =int(input("Enter your choice :"))
        if ch == 1:
            print("\n1. Price Graph")
            print("\n2. Currently_available and Currently_unavailable ")
            print("\n3. Custom Graphs ")
            t=int(input("Enter you choice: "))
            if t==1:
                plt.plot(df['Inventory_Control_ID'],df['Price'],marker ='o',color = 'red')
                plt.xticks(rotation="vertical")
                plt.xlabel("Inventry Control ID")
                plt.ylabel("Price")
                plt.show()
                wait=input()
            elif t==2:
                plt.plot(df["Inventory_Control_ID"],df["Price"],marker ="X",linewidth=1.75)
                plt.plot(df["Inventory_Control_ID"],df["Total_Reorder"],marker ="D",linewidth=1.75)
                plt.xlabel("Inventory Control ID")
                plt.ylabel("Price")
                plt.legend(["Price","Total_Reorder"])
                plt.xticks(rotation="vertical")
                plt.grid(True)
                plt.show()
                wait=input()
            elif t==3:
                print("1. Single Line Chart\n")
                c=int(input("Enter you choice: "))
                if c==1:
                    print(df.columns)
                    x=input("Enter the column name you want on x axis : ")
                    y=input("Enter the column name you want on y axis : ")
                    plt.plot(df[x],df[y],marker='o')
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.show()
                    wait=input()

        elif ch == 2:
                plt.barh(df["Inventory_Control_ID"],df["Price"])
                plt.xlabel("Inventory Control ID")
                plt.ylabel("Price")
                plt.show()
                wait=input()
        elif ch == 3:
            plt.hist(df["Total_Reorder"],bins=4,color="b", edgecolor="red")
            plt.show()
        elif ch == 4:
            break
        
def export_menu():
    df=pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\n Export Menu:')
        print('_'*100)
        print()
        print('1. csv file\n')
        print('2. Mysql table\n')
        print('3. Exit(Back  to Main Menu) ')
        ch=int(input('Enter your choice: '))
        if ch==1:
            df.to_csv(csv_export)
            print('\n\n Check your new file at : ', csv_export)
            wait= input()
        elif ch==2:
            engine=sqlalchemy.create_engine('mysql+pymysql://root:142005@localhost:3306/inventory')
            df.to_sql(name='inventory',con=engine,index=False,if_exists='replace')
            print('\n\nPlease Check Project Database For Inventory Control System.......')
            wait=input()
        elif ch== 3:
            break
        
def Main_Menu():
    while True:
        print ('Main Menu')
        print ('_'*100)
        print ()
        print ('1. Read CSV File\n')
        print ('2. Data Analysis Menu\n')
        print ('3. Graph Menu\n')
        print ('4. Export Data\n')
        print ('5. Exit\n')
        choice=(int(input('enter your choice: ')))
        if choice == 1:
           read_csv_file()
           wait=input()
        elif choice == 2:
             data_analysis_menu()
             wait=input()
        elif choice == 3:
             graph()
             wait=input()
        elif choice == 4:
             export_menu()
             wait=input()
        else :
              break

#call your main menu
Main_Menu()
                      



           
            
        
        
       

