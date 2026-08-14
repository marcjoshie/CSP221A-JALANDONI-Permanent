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
config = {
    "name": "Config-Drone",
    "battery": 65
}

config_drone = DroneRobot.from_config(config)

print(config_drone)
print(repr(config_drone))

for robot in robots:
    run_task_safely(robot)
print(CleaningRobot.perform_task.__name__)