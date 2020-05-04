hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

endh = (hour + (mins+dura)//60)%24
endm = (mins+dura)%60

print(endh,endm)