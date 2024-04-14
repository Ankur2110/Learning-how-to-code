def timeConversion(s):
    min_sec_string = s[2:8]
    hour_value_string = s[0:2]
    hour_value_int = int(s[0:2])
    if s[-2] =="A":
        if hour_value_int == 12:
            hour_value_string = '00'
        else:
            pass
    else:
        if hour_value_int ==12:
            pass
        else:
            hour_value_string = str(hour_value_int + 12)
    military_time = hour_value_string + min_sec_string
    return military_time

print(timeConversion('06:40:03AM'))