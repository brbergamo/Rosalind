def get_number_rabbits_pair(n, k):
    # Initialize a dictionary to store the number of rabbit pairs for each month
    data = {month:None for month in range(1, n + 1)}
    # Set initial values
    data[1] = 1
    data[2] = 1
    # Calculate the number of rabbit pairs for each subsequent month
    for month in range(3, n + 1):
        data[month] = data[month - 1] + (k * data[month - 2])
    # Return the number of rabbit pairs in the nth month
    return data[n]
print(get_number_rabbits_pair(32,5))
