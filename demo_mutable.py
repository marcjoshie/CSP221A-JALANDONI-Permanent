class BadRobotGroup:
    names = []

    def __init__(self, name):
        self.name = name
        self.names.append(name)


first_group = BadRobotGroup("Alpha")
second_group = BadRobotGroup("Beta")

print("Bad example:")
print(first_group.names)
print(second_group.names)


class GoodRobotGroup:

    def __init__(self, name):
        self.names = []
        self.names.append(name)


first_good_group = GoodRobotGroup("Alpha")
second_good_group = GoodRobotGroup("Beta")

print()
print("Correct example:")
print(first_good_group.names)
print(second_good_group.names)