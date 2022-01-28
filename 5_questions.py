# Question 1
print("Question 1 result:\t")
def hello_name(user_name):
    """Prints hello to the user based on user name."""
    print("Hello " + user_name.title() + "!")
    

hello_name("billy jean")

# Question 2
print("\nQuestion 2 result:\t")

def first_odds(num):
    """Prints odd numbers up to 100."""
    while num < 100:
        num +=1
        if num % 2 == 1:
            print(num)
            continue
        
first_odds(0)

# Question 3
print("\nQuestion 3 result:\t")

a_list = [1, 5, 8, 45, 59]

def max_num_in_list(a_list):
    """Returns the maximum number in a list
    """
    a_max = max(a_list)
    return a_max

max_num = max_num_in_list(a_list)
print(max_num)


# Question 4
print("\nQuestion 4 result:\t")

def is_leap_year(a_year):
    year = int(a_year)
    if year % 100 == 0 and year % 400 == 0:
        print("True")
    elif year % 4 == 0 and year % 100 != 0:
        print("True")    
    else:
        print("False")

is_leap_year(1980)

# Question 5
print("\nQuestion 5 result:\t")

num_list = [1, 2, 3, 4, 5, 6, 7, 8]

def is_consecutive(nums):
    
    for num in nums:
        if num + 1 > num and num < num + 2:
            print("True")
        else:
            print("False")

is_consecutive(num_list)
