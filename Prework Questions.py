#Question 1

def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")
hello_name(' user_name')


#Question 2
def odd_numbers():
    for i in range(1,101,2):
        print(i)
        


#Question 3

def max_num_in_list(a_list):

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20]

list.sort()

print(list[-1])



#Question 4

def is_leap_year(a_year):
    if (a_year % 4) == 0:
        if (a_year % 100) == 0:
            if (a_year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
randrange([1000,] stop[,10000])
a_year= 
if(is_leap_year(a_year)):
    print("True")
else:
    print("False")
#change the "a_year" to check!


#Question 5

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)


