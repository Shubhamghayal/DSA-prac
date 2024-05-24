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

def pattern(num):
   for i in range(num):
        for j in range(num,0,-1):
           print("5",end="")
        for j in range(0,i+1):
               print("*",end="")
        print()
        
       
pattern(9)




        
    