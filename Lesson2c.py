# Lists vs Tuples
# They store multiple values in a single variable
cars = ['Toyota', 'Nissan','Honda', 'Mazda', 'BMW', 500, 78.9]
print(cars)
print(type(cars))

# Slicing
print(cars[0]) # Toyota
print(cars[1:4]) # Nissan, Honda, Mazda, Theres is -1

# List is mutable/can be updated/Dynamic
cars.append("Volkwagon")
cars.append("Subaru")
cars.remove("Nissan")
cars.insert(1, "Jaguar") # insert at specified position
print(cars)

