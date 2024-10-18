#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0
                    
    min_operations = float('inf')

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            operations = i + (n // i - 1)
            min_operations = min(min_operations, operations)
            
            complement = n // i
            operations = complement + (n // complement - 1)
            min_operations = min(min_operations, operations)
            return min_operations

        # Example usage
        print(minOperations(9))  # Output: 6
