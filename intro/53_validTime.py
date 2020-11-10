def validTime(time):
    hours, minutes = time.split(':')
    return 0 <= int(hours) < 24 and 0 <= int(minutes) < 60
