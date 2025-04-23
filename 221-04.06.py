for hour in range(24):
    if hour == 0:
        suffix = "Midnight"
    elif hour == 12:
        suffix = "Noon"
    elif hour < 12:
        suffix = "AM"
    else:
        suffix = "PM"
    print(f"{hour}:00 - {suffix}")
