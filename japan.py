def cook():
    print("we are making sushi")

def is_prime(number):
    """
    Checks if number is prime
    :param number: the number to test
    :return: true if prime, false if not
    """
    for i in range(2, number//2+1):
        if number % i ==0:
            return False # not a prime number
    return True


if __name__=="__main__":
    print("testing my function:")
   assert is_prime(5) is True, "Error in function,5 is prime"


