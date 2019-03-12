sec = int(input("I will convert seconds into minutes and hours and days. How many seconds you want to convert?"))
day = sec // (24 * 60 * 60)
hours = sec % (24 * 60 * 60) // (24 * 60)
minutes = (sec % (24 * 60 * 60)) % (24 * 60) // 60
sec_ = (sec % (24 * 60 * 60)) % (24 * 60) % 60
print(sec, "seconds are:", day, "days", hours, "hours", minutes, "minutes and", sec_, "seconds")
