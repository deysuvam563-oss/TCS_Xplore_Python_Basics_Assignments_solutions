numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))

while True:
    print("\nMENU")
    print("a. Add all numbers")
    print("b. Find the highest number")
    print("c. Find the average of all the numbers")
    print("d. Find the number with highest frequency")
    print("e. Exit")

    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        print("Sum of all numbers =", sum(numbers))

    elif choice == 'b':
        print("Highest number =", max(numbers))

    elif choice == 'c':
        average = sum(numbers) / len(numbers)
        print("Average of all numbers =", average)

    elif choice == 'd':
        highest_frequency = 0
        most_frequent = numbers[0]

        for num in numbers:
            frequency = numbers.count(num)
            if frequency > highest_frequency:
                highest_frequency = frequency
                most_frequent = num

        print("Number with highest frequency =", most_frequent)
        print("Frequency =", highest_frequency)

    elif choice == 'e':
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
