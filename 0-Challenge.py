#Instrucciones:

# Write a Python script to:

# Display all the prime numbers between 1 to 250.
# Store the results in a results.txt file.
# Test the script. Verify that it produced the expected results in the results.txt file.

# Save the script and make a note of its location (absolute path) for future reference.

def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
def main():
    with open('results.txt', 'w') as f:
        for i in range(1, 251):
            if isPrime(i):
                f.write(str(i) + ' es primo \r')

if __name__ == '__main__':
    main()

