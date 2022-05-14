import math
import time as sleep
import stat_script_1_stat as stat
import ev_script_2_ev as EV

atknat = 1
defnat = 1
satknat = 1
sdefnat = 1
snat = 1 

tes = int(input("[1] EV   [2] Stat : "))
if tes == 1:
    stats = ["SS ", "HP ", "Attack ", "Defense ", "Special Attack ", "Special Defense " , "Speed"]
    bas = [6]
    iv = [6]
    ev1 = [0,0,0,0,0,0,0]
    ev2 = 0
    lvl = int(input("Pokemon Level : "))
    if(lvl < 0 or lvl > 100):
        print("Level Can only reach max 100!")
        sleep(1)
        exit()

    print("Base Stats ")
    for x in range(1,7):
        bas.append(int(input("Input " + stats[x] + " : ")))

    print("\nIVs on each Stats1")
    for y in range(1,7):
        iv.append(int(input("Input " + stats[y] + " IV : ")))
        if (iv[y] < 0 or iv[y] > 31):
                print("Can't Set IVs Out of 0 - 31!")
                sleep(3)
                print("Exiting in 3 seconds")
                sleep(3)                
                exit()

    o = int(input("[1] Single EV Stat     [2] All the Stats\n"))
    if(o == 1):
        s = int(input("Choose Stat you Wish to Input : \n[1] HP   [2] Attack   [3] Defense   [4] Special Attack   [5] Special Defense   [6] Speed\n"))
        tray = int(input("Enter Amount of EV : "))
        if (s < 0 or s > 255):
            print("Can't Set EVs Out of 0 - 255 and More than 510!")
            sleep(3)
            print("Exiting in 3 seconds...")
            sleep(3)                
            exit()
        for p in range(1,7):
            if (p == s):
                ev1.insert(p,tray)
    elif(o == 2):        
        print("Input EV's on each Stats : ")
        for z in range(1,7):
            ev1.append(int(input("Input " + stats[z] + " EV : ")))
            if (ev1[z] < 0 or ev1[z] > 255):
                print("Can't Set EVs Out of 0 - 255 and More than 510!")
                sleep(3)
                print("Exiting in 3 seconds...")
                sleep(3)                
                exit()
        ev2 = ev2 + ev1[z]
        if (ev2 > 510):
                print("Can't Set EV More than 510!")
                sleep(3)
                print("Exiting in 3 seconds...")
                sleep(3)                
                exit()    
    else:
        print("Wrong Input!")
    print("\n[1] Hardy     [2] Lonely    [3] Brave      [4] Adamant    [5] Naughty\n"
          "[6] Bold      [7] Docile    [8] Relaxed    [9] Impish     [10] Lax\n "
          "[11] Timid    [12] Hasty    [13] Serious   [14] Jolly     [15] Naive\n "
          "[16] Modest   [17] Mild     [18] Quiet     [19] Bashful   [20] Rash\n "
          "[21] Calm     [22] Gentle   [23] Sassy     [24] Careful   [25] Quirky")

    natpick = int(input("Pick Pokemon's Nature: "))
    if(natpick == 1 or natpick == 7 or natpick == 13 or natpick == 19 or natpick == 25):
        atknat = 1
        defnat = 1
        satknat = 1
        sdefnat = 1
        snat = 1
    if(natpick == 2 or natpick == 3 or natpick == 4 or natpick == 5): 
        atknat = 1.1
        if(natpick == 2):
            defnat = 0.9
        elif(natpick == 3):
            snat = 0.9
        elif(natpick == 4):
            satknat = 0.9
        else:
            sdefnat = 0.9
    if(natpick == 6 or natpick == 8 or natpick == 9 or natpick == 10):
        defnat = 1.1
        if(natpick == 6):
            atknat = 0.9
        elif(natpick == 8):
            snat = 0.9
        elif(natpick == 9):
            satknat = 0.9
        else:
            sdefnat = 0.9
    if(natpick == 11 or natpick == 12 or natpick == 14 or natpick == 15):
        snat = 1.1
        if(natpick == 11):
            atknat = 0.9
        elif(natpick == 12):
            defnat = 0.9
        elif(natpick == 14):
            snat = 0.9
        else:
            sdefnat = 0.9    
    if(natpick == 16 or natpick == 17 or natpick == 18 or natpick == 20):
        satknat = 1.1
        if(natpick == 16):
            atknat = 0.9
        elif(natpick == 17):
            defnat = 0.9
        elif(natpick == 18):
            snat = 0.9
        else:
            sdefnat = 0.9      
    if(natpick == 21 or natpick == 22 or natpick == 23 or natpick == 24):
        sdefnat = 1.1
        if(natpick == 16):
            atknat = 0.9
        elif(natpick == 17):
            defnat = 0.9
        elif(natpick == 18):
            snat = 0.9
        else:
            satknat = 0.9

    opt = int(input("Check Stat : \n[1] Attack   [2] Defense   [3] Special Attack \n [4] Special Defense   [5] Speed \n"))
    mod = 0
    if opt == 1:
            mod = atknat
    elif opt == 2:
            mod = defnat
    elif opt == 3:
            mod = satknat
    elif opt == 4:
            mod = sdefnat
    elif opt == 5:
            mod = snat

    des = int(input("Desired Increase : "))

    print("Amount of EV Needed for your Pokemon : ", EV.ClassEv.desired(bas, ev1, iv, opt, lvl, des, mod)) 
    exit()
elif tes == 2:
    stats = ["SS ", "HP ", "Attack ", "Defense ", "Special Attack ", "Special Defense " , "Speed"]
    bas = [6]
    iv = [6]
    ev1 = [0,0,0,0,0,0,0]
    ev2 = 0
    pokemon = str(input("Enter Pokemon : "))
    lvl = int(input("Enter level : "))
    if(lvl < 0 or lvl > 100) :
        print("Maximum Level is ONLY 100!")
        sleep(1)
        exit() 

    print("[1] Hardy     [2] Lonely    [3] Brave      [4] Adamant     [5] Naughty\n"
          "[6] Bold      [7] Docile    [8] Relaxed    [9] Impish      [10] Lax\n "
          "[11] Timid    [12] Hasty    [13] Serious   [14] Jolly      [15] Naive\n "
          "[16] Modest   [17] Mild     [18] Quiet     [19] Bashful    [20] Rash\n "
          "[21] Calm     [22] Gentle   [23] Sassy     [24] Careful    [25] Quirky")

    natpick = int(input("Choose Pokemon's Nature : "))
    if(natpick == 1 or natpick == 7 or natpick == 13 or natpick == 19 or natpick == 25):
        atknat = 1
        defnat = 1
        satknat = 1
        sdefnat = 1
        snat = 1
    if(natpick == 2 or natpick == 3 or natpick == 4 or natpick == 5): 
        atknat = 1.1
    if(natpick == 2):
        defnat = 0.9
    elif(natpick == 3):
        snat = 0.9
    elif(natpick == 4):
        satknat = 0.9
    else:
        sdefnat = 0.9
    if(natpick == 6 or natpick == 8 or natpick == 9 or natpick == 10):
        defnat = 1.1
    if(natpick == 6):
        atknat = 0.9
    elif(natpick == 8):
        snat = 0.9
    elif(natpick == 9):
        satknat = 0.9
    else:
        sdefnat = 0.9
    if(natpick == 11 or natpick == 12 or natpick == 14 or natpick == 15):
        snat = 1.1
    if(natpick == 11):
        atkat = 0.9
    elif(natpick == 12):
        defnat = 0.9
    elif(natpick == 14):
        snat = 0.9
    else:
        sdefnat = 0.9    
    if(natpick == 16 or natpick == 17 or natpick == 18 or natpick == 20):
        satknat = 1.1
    if(natpick == 16):
        atknat = 0.9
    elif(natpick == 17):
        defnat = 0.9
    elif(natpick == 18):
        snat = 0.9
    else:
        sdefnat = 0.9      
    if(natpick == 21 or natpick == 22 or natpick == 23 or natpick == 24):
        sdefnat = 1.1
    if(natpick == 16):
        atknat = 0.9
    elif(natpick == 17):
        defnat = 0.9
    elif(natpick == 18):
        snat = 0.9
    else:
        satknat = 0.9

print("Enter Base Stats : ")
for x in range(1,7):
        bas.append(int(input("Input " + stats[x] + " : ")))

print("Enter IV for each Stats : ")
for y in range(1,7):
        iv.append(int(input("Input " + stats[y] + " IV : ")))
        if (iv[y] < 0 or iv[y] > 31):
                print("Can't Set IVs Out of 0 - 31!")
                sleep(3)
                print("Exiting in 3 seconds...")
                sleep(3)                
                exit()

o = int(input("[1] Single EV Stat [2] All the Stats \n"))
if(o == 1):
        s = int(input("Choose Stat you Wish to Input : \n[1] HP   [2] Attack   [3] Defense   [4] Special Attack   [5] Special Defense   [6] Speed\n"))
        tray = int(input("Number of EV : "))
        if (s < 0 or s > 255):
            print("Can't Set Evs Out of 0 - 255 and More than 510!")
            sleep(3)
            print("Exiting in 3 seconds...")
            sleep(3)                
            exit()
        for p in range(1,7):
            if (p == s):
                ev1.insert(p, tray)
elif(o == 2):        
        print("Enter EV for each Stats : ")
        for z in range(1, 7):
            ev1.append(int(input("Input "+ stats[z] + " EV : ")))
            if (ev1[z] < 0 or ev1[z] > 255):
                print("Can't Set EVs Out of 0 - 255 and More than 510!")
                sleep(3)
                print("Exiting in 3 seconds...")
                sleep(3)                
                exit()
        ev2 = ev2 + ev1[z]
        if (ev2 > 510):
                print("Can't Set More than 510 EV!")
                sleep(3)
                print("Exiting in 3 seconds...")
                sleep(3)                
                exit()  
else:
    print("Invalid Input!")
    exit()
print("Pokemon Stats : ")
print("HP : ", stat.ClassStat.hpReturn(bas, iv, ev1, lvl))
print("Attack : ", stat.ClassStat.attackReturn(bas, iv, ev1, lvl, atknat))
print("Defense : ", stat.ClassStat.defenseReturn(bas, iv, ev1, lvl, defnat))
print("Speed : ", stat.ClassStat.speedReturn(bas, iv, ev1, lvl, snat))
print("Special Attack : ", stat.ClassStat.spattackReturn(bas, iv, ev1, lvl, satknat))
print("Special Defense : ", stat.ClassStat.spdefenseReturn(bas, iv, ev1, lvl, sdefnat))