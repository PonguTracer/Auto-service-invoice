# Define service prices
services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0  # Change 'No service' to 0
}

# Display menu
print("Davy's auto shop services")
for service, price in services.items():
    if service != '-':
        print(f"{service} -- ${price}")
print()

# Input services
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")

# Calculate prices based on user input
price1 = services.get(first_service, 0)
price2 = services.get(second_service, 0)

# Display invoice
print("\nDavy's auto shop invoice\n")

if first_service != '-':
    if first_service == '':
        print("Service 1: No service")
    else:
        print(f"Service 1: {first_service}, ${price1}")
else:
    print(f"Service 1: No service")
if second_service != '-':
    if second_service == '':
        print("Service 2: No service")
    else:
        print(f"Service 2: {second_service}, ${price2}")
else:
    print(f"Service 2: No service\n")

# Calculate total
total_invoice = price1 + price2
print(f"Total: ${total_invoice}")
