dayNo = int (input ("Enter the number of the day you want to show: "))

def dayName (dayNo):
    d = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return d[dayNo]

print (dayName(dayNo))