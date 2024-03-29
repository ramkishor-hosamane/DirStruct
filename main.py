#importing modules
from  test import *  
import sys

def main():
    
    tree = Node('/','Directory','/') #Root Directory
    Node.start = tree                #Reference to Root Directory
    
    while True:

      #make a choice between 1-6 
      try:  
          choice = int(input("Enter your Choice \n 1.Create Directory\n2.Create File\n3.List \n 4.Check Existence \n 5.Search\n6.Exit\n"))
      except:
          print("Invalid choice")
            
      if choice == 1:
            path = input("Please Enter path for Creating directory ")
            print(tree.create_directory(path))
            
      elif choice == 2:
            path = input("Please Enter path for creating File ")
            print(tree.create_file(path))
            
      elif choice == 3:
            path = input("Please Enter path for Listing directories and files ")
            print(list(path))
            
      elif choice == 4:
            item = input("Please Enter Directory/File ")
            print(tree.check_existence(item))
      
      elif choice == 5:
            path = input("Please Enter path for searching File ")
            item = input("Please Enter string to search ")
            tree.search(path,item)
            
      elif choice == 6:
            print("Bye Bye ")
            sys.exit()
            
      else:
          print("Invalid choice")
          
      print()
    


if __name__ == "__main__":
  main()
