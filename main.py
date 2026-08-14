from robot import CleaningRobot

cleaner = CleaningRobot("Roomba")

print(cleaner)
print(repr(cleaner))
print(cleaner.perform_task())