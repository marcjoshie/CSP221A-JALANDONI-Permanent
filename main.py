from robot import CleaningRobot, DroneRobot


cleaner = CleaningRobot("Roomba")
drone = DroneRobot("Aqua-Drone")


print(cleaner)
print(cleaner.perform_task())
print(cleaner)

print()

print(drone)
print(drone.perform_task())
print(drone)