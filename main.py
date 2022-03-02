from alarm import AlarmClock
# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# 1. Print the clock’s time to the terminal

# 2. Call the alarm clock’s change time method to change the time

# 3. Toggle the alarm clock’s on off switch

current_time = AlarmClock(False)
print(current_time.current_time)

current_time.add_to_current_time(20)

turn_on_alarm = AlarmClock(False)
print(turn_on_alarm.alarm_is_active)
