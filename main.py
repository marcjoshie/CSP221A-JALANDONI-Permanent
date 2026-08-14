from robot import (
    CleaningRobot,
    DroneRobot,
    run_task_safely,
    fleet_report
)


cleaner = CleaningRobot("Roomba")
drone = DroneRobot("Aqua-Drone", battery=80)

robots = [cleaner, drone]


fleet_report(robots)

print()

for robot in robots:
    run_task_safely(robot)
    print(CleaningRobot.perform_task.__name__)