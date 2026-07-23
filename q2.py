# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 2 - Question 2
# /* Student Name: Angeline Victoriano
# /* SID: 20528831
## /***************************************************/

def run():
    def isPrime(n):

        if n <= 1 :
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    #create a list of 2 to n

    n = int(input("enter an integer: "))
    create_list = lambda n: list(range(2, n + 1))
    list1 = create_list(n)

    prime_list = []
    #loop to step through the created list
    for num in list1:
        if isPrime(num):
            prime_list.append(num)
    print(f"list of prime numbers less than or egual to {n}:")
    print(prime_list)

if __name__ == "__main__":
    # This allows students to run this specific file
    # individually for testing (e.g., `python q1.py`)
    run()