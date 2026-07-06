def cm_to_meter(a):
    meters = a / 100
    return f"{a} cm = {meters:.2f} m"

def meter_to_cm(a):
    return f"{a}m = {a*100}cm"

def celsius_to_fahrenheit(a):
    m = (a*1.8) + 32
    return f"{a}celsius is {m}F"

def fahrenheit_to_celsius(a):
    m = (a-32)/1.8
    return f"{a}F is {m:.2f}C"