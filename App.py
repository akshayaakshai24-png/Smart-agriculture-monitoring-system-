

from datetime import datetime
import random

print("=" * 45)
print(" SMART AGRICULTURE MONITORING SYSTEM")
print("=" * 45)

farm_name = input("Enter farm name: ")

print("\nChoose data input:")
print("1. Enter readings manually")
print("2. Generate sample readings")

choice = input("Enter choice (1 or 2): ")

if choice == "1":
    soil = float(input("Enter soil moisture (0-100%): "))
    temperature = float(input("Enter temperature (0-50 C): "))
    humidity = float(input("Enter humidity (0-100%): "))
elif choice == "2":
    soil = random.randint(10, 90)
    temperature = random.randint(20, 45)
    humidity = random.randint(30, 90)
else:
    print("Invalid choice. Please run again.")
    raise SystemExit

# Validate readings
if not (0 <= soil <= 100 and
        0 <= temperature <= 50 and
        0 <= humidity <= 100):
    print("Invalid readings. Please check the values.")
    raise SystemExit

# Analyze soil moisture
if soil < 30:
    status = "DRY - Check irrigation requirement"
elif soil < 60:
    status = "MODERATE MOISTURE"
else:
    status = "HIGH SOIL MOISTURE"

# Display results
print("\n" + "=" * 45)
print(" FARM MONITORING REPORT")
print("=" * 45)

print("Farm Name:", farm_name)
print("Date and Time:", datetime.now().strftime(
    "%d-%m-%Y %H:%M:%S"
))
print(f"Soil Moisture: {soil}%")
print(f"Temperature: {temperature} C")
print(f"Humidity: {humidity}%")
print("Soil Condition:", status)

if temperature > 40:
    print("Warning: High temperature!")

if humidity > 80:
    print("Notice: High humidity!")

print("\nMonitoring completed successfully.")
print("=" * 45)
