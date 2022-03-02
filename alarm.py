
class AlarmClock:
    
    def __init__(self, alarm_on_or_off):
        self.current_time = 1200
        self.alarm_is_active = alarm_on_or_off
        self.alarm_time = 1240

    def add_to_current_time(self, time_add):
        self.current_time += time_add
        print(self.current_time)
    def sub_from_current_time(self, time_sub):
        self.current_time -= time_sub
        print(self.current_time)
    def add_to_new_alarm_time(self, time_add):
        self.alarm_time += time_add
    def sub_from_new_alarm_time(self, time_sub):
        self.alarm_time -= time_sub

# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.

# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.

# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# 1. Print the clock’s time to the terminal

# 2. Call the alarm clock’s change time method to change the time

# 3. Toggle the alarm clock’s on off switch
    
