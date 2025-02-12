class Palin():
    def __init__(self,message,number):
        self.message = message
        self.number = number

    def is_message(self):
        if message==message[::-1]:
            print(f"The String {message} is Palindrome")

        else:
            print(f"The String {message} is  Not an Palindrome")

    def is_factorial(self):
        factorial = 1

        if number<0:
            print("The Number Can't be Taken As factorial")

        elif number==0:
            print("The factorial is 1")

        else:
            for i in range(1,number+1):
              factorial = factorial*i
        print(f"The factorial is {factorial}")



message=input("Enter Your Word:")
number=int(input("Enter a Number:"))

palin=Palin(message,number)
# palin1 = Palin(number)
palin.is_message()
palin.is_factorial()







