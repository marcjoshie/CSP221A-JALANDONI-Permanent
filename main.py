from robot import CleaningRobot, DroneRobot, run_task_safely


cleaner = CleaningRobot("Roomba")
drone = DroneRobot("Aqua-Drone")


print("Cleaning Robot:")
run_task_safely(cleaner)

print()

print("Drone Robot:")
run_task_safely(drone)