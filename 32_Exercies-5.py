# write a program to wish a morning or night on tiem

import time
time1 = int(time.strftime("%H"))
print(time1)

if (time1>=5 and time1<12):
    print("Good morning yarr !")
elif(time1>=12 and time1<17):
    print("Good afternoon yarr !")
elif(time1>=17 and time1<21):
    print("Good evening yarr !")
elif(time1>=22 and time1<5):
    print("Good night yarr !")