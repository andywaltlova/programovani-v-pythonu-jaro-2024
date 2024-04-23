from datetime import datetime, timedelta, timezone

program_start = datetime.now()

print(datetime.now())

course = datetime(2024, 4, 23-7, 18)
print(course)

yesterday = datetime(2024, 4, 22)
print(yesterday)

apollo_start = datetime(1969, 7, 16, 14, 32)

print(yesterday.weekday())
print(yesterday.isoweekday())

print(apollo_start.isoformat())
# 16. 7. 1969, 14:32
print(apollo_start.strftime("%d. %m. %Y, %H:%M"))

apollo_land = datetime(1969,7,21,18,54)

dlzka_misie = apollo_land - apollo_start
print(dlzka_misie)

planned_departure = datetime(2024, 4, 23, 19)
delay = timedelta(minutes=10, weeks=1)
real_departure = planned_departure + delay
print(real_departure)

program_end = datetime.now()

program_duration = program_end - program_start
print(program_duration)

# Balicky
