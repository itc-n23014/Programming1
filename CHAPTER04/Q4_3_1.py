def f(*args, separator="_"):
    return separator.join(args)


print(f("Hantagawa", "Naha", "Okinawa", "Japan"))
