# def pattern(num):
#     for i in range(num):
#         print(num*"*")
        




# def pattern(num):
#     for i in range(num):
#         print(i*"*")


# def pattern(num):
#     for i in range(num):
#         for j in range(i+1):
#             print(j+1, end=" ")
#         print()

# def pattern(num):
#     for i in range(num):
#         for j in range(i+1):
#             print(i+1, end=" ")
#         print()


# def pattern(num):
#     for i in range(num,0,-1):
#         for j in range(i):
    
#             print("*", end=" ")
#         print()


# def pattern1(num):
#    for i in range(num):
#          for j in range(num-i):
#                 print(end=" ")
#          for j in range(2*i+1):
#                 print("*",end="")
#          print()
         
# pattern1(5)
          
          
   

# def pattern(num):
#    for i in range(num,0,-1):
#          for j in range(num-i):
#                print(end=" ")
#          for j in range(2*i-1):
#              print("*",end="")
         
#          print()
        
       
# pattern(6)


# def pattern1(num):
#       for i in range(num):
#          for j in range(num-i):
#                 print(end=" ")
#          for j in range(2*i+1):
#                 print("*",end="")
#          print()
#       for i in range(num,0,-1):
#          for j in range(num+1-i):
#                print(end=" ")
#          for j in range(2*i-1):
#              print("*",end="")
         
#          print()
         
# pattern1(5)


# def pattern10(num):
#       for i in range(num):
#             for j in range(i):
#                    print("*",end="")
#             print()
#       for i in range(num,0,-1):
#             for j in range(i):
#                    print("*",end="")
#             print()
# pattern10(5)

def pattern11(num):
       for i in range(1,num):
            for j in range(i,i+i):
                   print(j%2,end="")
            print()
            
pattern11(6)



        
    