

distance = 5.1
speed = input("Speed (km/hr) : ")
speed_convert = int(speed)
km_per_minute = (speed_convert / 60)
total_time = distance / km_per_minute

print("Distance from Uion Mall to Post Office : %.2f km " % (distance))
print("Speed: %.2f km/hr" % (km_per_minute))
print("Total Time: %.2f minute" % (total_time))
