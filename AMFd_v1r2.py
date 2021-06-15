import random
import asyncio

    
#define variables

userdict = {}

inp_cmd = ""

exit_confirm = ""

#define functions

def restart():
    userdict["Raw_Material"] = 0
    userdict["Standard_product"] = 0
    userdict["Grade1_product"] = 0
    userdict["money"] = 25
    userdict["G1_Raw_Materials"] = 0
    userdict["BigBuyer_RM"] = False
    userdict["debt"] = 0
    userdict["amt_borrowed"] = 0
    userdict["Working"] = False

def CtrlS():
    target = open("savedata.txt", "w")
    target.write(str(userdict))
    target.close()


def interest():
    if userdict["debt"] > (userdict["amt_borrowed"] * 10):
        restart()
        print("you have incurred too much loans. The central bank confiscates all your assets and money.")
        print("The bank left 25 dollars in your account, act wisely next time")
    else:
        if round((userdict["debt"] * 1.03), 3) > -1000:
            userdict["debt"] = round((userdict["debt"] * 1.03), 3)


async def gameplay(command):

    global userdict
    global exit_confirm

#what"s new?

    if command == "what's new?":
        print("""
====================================
Arbeit Macht Frei Desktop VER 1.1
====================================

1.x)
hey, welcome to the desktop version of AMF!
A lot of old commands have been stripped out like online, name? and other online things
i am porting this to desktop to allow for easier coding
the desktop platform will also be the main distribution platform so new updates will come here first
I am also drafting up a TOS for this game so for the meantime: NO UNAUTHORISED DISTRIBUTION
you are free to mod the game however you like though
-Devon Lim

1.2)
savedata.txt detection\
""")

#what"s coming?

    elif command == "what's coming?":
        print("""
============================================
Arbeit Macht Frei Desktop upcoming features
============================================

1) The stonk market\
""")


#help

    elif command == "help":
        print("""\
This game was made by Devon Lim, © 2021
========================================================================================================================
Gameplay:

inventory ---> check your inventory

buyrm {num} ---> buy {num} raw material(s)
(1 raw material = 0.5 money)

buym1 {num} ---> buy {num} grade one raw materials
(1 grade 1 raw material = 10 money)

sw {num} ---> Make your workers produce {num} standard products
(5 raw material = 1 Standard product)

w1 {num} ---> Make your workers produce {num} Grade 1 products
(5 raw material + 5 Grade 1 raw material = 1 Grade 1 product)

sellsp {num} ---> sell {num} of standard products

sellg1p {num} ---> sell {num} of grade 1 products

moneyloan {num} ---> loan out {num} dollars 
(you must have less than 10000 dollars of debt to take out any more loans)
(loan increases by 3%[compound interest] with every production and buy command)
(keep your loan less than 10 times the amount of money you loaned from the bank since you were last debt-free)

loanpay {num} ---> pays back {num} dollars of your loan

========================================================================================================================
Misc:

help ---> brings up this screen

what's new? ---> prints what"s in the current version of the game

what's coming? ---> prints what to expect for future versions of the game

say <num> "<string>" ---> prints "<string>" <num> many times

save ---> does to the dicts what Ctrl + S does to stuff

WIPEMYDATAFORGOOD ---> the big red reset button

========================================================================================================================
type "exit" to save and exit the game\
""")

        
#say

    elif command[:4] == "say ":
        saylist = command.split("\"")
        saystr = saylist[1]
        sayamt = int(saylist[0].split(" ")[1])
        for i in range(sayamt):
            print(saystr)

        
#inventory

    elif command == "inventory":
        #achivement detector
        if userdict["BigBuyer_RM"] == True:
            PrintBigbuyerRM = """Bigbuyer(RM) achivement 1/1
(buy 100 or more RM at one go)"""
        elif userdict["BigBuyer_RM"] == False:
            PrintBigbuyerRM = """Bigbuyer(RM) achivement 0/1
(buy 100 or more RM at one go)"""
        else:
            PrintBigbuyerRM = "Error retiving achivement status"
        #rounding function
        userdict["Raw_Material"] = int(userdict["Raw_Material"])
        userdict["G1_Raw_Materials"] = int(userdict["G1_Raw_Materials"])
        userdict["Standard_product"] = int(userdict["Standard_product"])
        userdict["Grade1_product"] = int(userdict["Grade1_product"])
        userdict["money"] = round((userdict["money"]), 3)
        userdict["debt"] = round((userdict["debt"]), 3)
        userdict["amt_borrowed"] = round((userdict["amt_borrowed"]), 3)
        #end of rounding function
        #Inventory compilation
        IC_line1 = "Raw Materials:"
        IC_line2 = "You have " + str(userdict["Raw_Material"]) + " raw material(s)"
        IC_line3 = "You have " + str(userdict["G1_Raw_Materials"]) + " grade one raw materials"
        IC_line4 = "Products:"
        IC_line5 = "You have " + str(userdict["Standard_product"]) + " standard product(s)"
        IC_line6 = "You have " + str(userdict["Grade1_product"]) + " Grade 1 product(s)"
        IC_line7 = "Achievements:"
        IC_line8 = str(PrintBigbuyerRM)
        IC_line9 = "Others:"
        IC_line10 = "You have " + str(userdict["money"]) + " dollars"
        IC_line11 = "You are " + str(userdict["debt"]) + " dollars in debt. You borrowed " + str(userdict["amt_borrowed"]) + " from the bank since the last time you had no debt"
        print(IC_line1 + "\n" +IC_line2 + "\n" +IC_line3 + "\n" +IC_line4 + "\n" +IC_line5 + "\n" +IC_line6 + "\n" +IC_line7 + "\n" +IC_line8 + "\n" +IC_line9 + "\n" +IC_line10 + "\n" + IC_line11)
        #end of IC compilaion

#buyRM

    elif command[:6] == "buyrm ":
        RM_to_buy = int(command[6:])
        if command[6:] == "nan":
            print("nan is not a number!")
            return
        if str(command[6:]) == "inf":
            print("inf is not a valid number!")
            return
        if RM_to_buy <= 0:
            print("invalid {num} in \"buyRM {num}\"")
        elif userdict["money"] < (RM_to_buy / 2):
            print("you need " + str((RM_to_buy / 2) - userdict["money"]) + " more money to buy that much raw materials")
        elif userdict["money"] >= (RM_to_buy / 2):
            userdict["money"] = userdict["money"] - (RM_to_buy / 2)
            interest()
            userdict["Raw_Material"] = userdict["Raw_Material"] + RM_to_buy
            print("you bought " + str(RM_to_buy) + " raw materials for 0.5 dollar apeice")
            print("you now have " + str(userdict["Raw_Material"]) + " raw materials")
            print("you now have " + str(userdict["money"]) + " money left")
            #big buyer
            if RM_to_buy >= 100:
                if userdict["BigBuyer_RM"] == False:
                    userdict["BigBuyer_RM"] = True
                    print("You just got the bigbuyer(RM) achivement!")
                    

#SW
        
    elif command[:3] == "sw ":
        if command[3:] == "nan":
            print("nan is not a number!")
            return
        if str(command[3:]) == "inf":
            print("inf is not a valid number!")
            return
        SW_PGiv = int(command[3:])
        if SW_PGiv <= 0:
            print("input a interger of the standard producs you have to make that is at least 1")
        else:
            if userdict["Raw_Material"] < (SW_PGiv * 5):
                print("you need  " + str((SW_PGiv * 5) - userdict["Raw_Material"]) + " more raw materials to start production")
            elif userdict["Raw_Material"] >= (SW_PGiv * 5):
                userdict["Working"] = True
                SWCd1 = round((SW_PGiv * (random.uniform(1, 1.5))), 2)
                userdict["Raw_Material"] = userdict["Raw_Material"] - (SW_PGiv * 5)
                print("wait " + str(SWCd1) + " seconds for your workers to finish working")
                await asyncio.sleep(SWCd1)
                userdict["Standard_product"] = userdict["Standard_product"] + int(SW_PGiv)
                interest()
                print("You have made " + str(SW_PGiv) + " standard product(s)")
                print("You now have " + str(userdict["Standard_product"]) + " standard product(s)")
                print("you now have " + str(userdict["Raw_Material"]) + " raw material left")
                userdict["Working"] = False
                    

#buyM1

    elif command[0:6] == "buym1 ":
        if command[6:] == "nan":
            print("nan is not a number!")
            return
        if str(command[6:]) == "inf":
            print("inf is not a valid number!")
            return
        M1_to_buy = int(command[6:])
        if M1_to_buy <= 0:
            print("invalid {num} in \"buyM1 {num}\"")
        elif userdict["money"] < M1_to_buy * 10:
            print("you need " + str((M1_to_buy * 10) - userdict["money"]) + " more money to buy that much grade one raw materials")
        elif userdict["money"] >= M1_to_buy * 10:
            userdict["money"] = userdict["money"] - M1_to_buy * 10
            userdict["G1_Raw_Materials"] = userdict["G1_Raw_Materials"] + M1_to_buy
            interest()
            print("you bought " + str(M1_to_buy) + " grade one raw materials for 10 dollars apeice")
            print("you now have " + str(userdict["G1_Raw_Materials"]) + " grade one raw materials")
            print("you now have " + str(userdict["money"]) + " money left")
            


#W1

    elif command[0:3] == "w1 ":
        if command[3:] == "nan":
            print("nan is not a number!")
            return
        if str(command[3:]) == "inf":
            print("inf is not a valid number!")
            return
        W1_AmtMake = int(command[3:])
        if W1_AmtMake <= 0:
            print("input a interger of the grade 1 producs you have to make that is at least 1")
        else:
            if userdict["Raw_Material"] < (W1_AmtMake * 5):
                print("you need  " + str((W1_AmtMake * 5) - userdict["Raw_Material"]) + " more raw materials to start production")
            elif userdict["Raw_Material"] >= (W1_AmtMake * 5):
                if userdict["G1_Raw_Materials"] < (W1_AmtMake * 5):
                    print("you need  " + str((W1_AmtMake * 5) - userdict["G1_Raw_Materials"]) + " more Standard products to start production")
                elif userdict["G1_Raw_Materials"] >= (W1_AmtMake * 5):
                    userdict["Working"] = True
                    W1Cd1 = round((W1_AmtMake * (random.uniform(1.5, 2.5))), 2)
                    userdict["Raw_Material"] = userdict["Raw_Material"] - (W1_AmtMake * 5)
                    userdict["G1_Raw_Materials"] = userdict["G1_Raw_Materials"] - (W1_AmtMake * 5)
                    print("wait " + str(W1Cd1) + " seconds for your workers to finish working")
                    await asyncio.sleep(W1Cd1)
                    userdict["Grade1_product"] = userdict["Grade1_product"] + W1_AmtMake
                    interest()
                    print("You have made " + str(W1_AmtMake) + " Grade 1product(s)")
                    print("You now have " + str(userdict["Grade1_product"]) + " Grade 1product(s)")
                    print("You now have " + str(userdict["Raw_Material"]) + " Raw Materials left")
                    print("You now have " + str(userdict["G1_Raw_Materials"]) + " Grade 1 Raw Materials left")
                    userdict["Working"] = False

#sellSP

    elif command[0:7] == "sellsp ":
        if command[7:] == "nan":
            print("nan is not a number!")
            return
        else:
            SWsell = int(command[7:])
            if userdict["Standard_product"] < SWsell:
                print("you need  " + str(SWsell - userdict["Standard_product"]) + " more standard products to sell that much stuff")
            elif userdict["Standard_product"] >= SWsell and SWsell >= 0:
                Morket_SW_value = round(random.uniform(1,5), 2)
                Morket_SW_get_money = round((SWsell * Morket_SW_value), 3)
                userdict["Standard_product"] -= SWsell
                userdict["money"] += Morket_SW_get_money
                print("Market value for standard products was " + str(Morket_SW_value) +" apeice")
                print("You sold " + str(SWsell) + " standard products")
                print("You gained " + str(Morket_SW_get_money) + " dollars from the market")
                print("You now have " + str(userdict["money"]) + " dollars")
                print("You have " + str(userdict["Standard_product"]) + " standard product(s)")
            else:
                print("invalid {num} in \"sellSP {num}\"")

#sellG1P

    elif command[0:8] == "sellg1p ":
        if command[8:] == "nan":
            print("nan is not a number!")
            return
        if str(command[8:]) == "inf":
            print("inf is not a valid number!")
            return
        else:
            G1Psell = int(command[8:])
            if userdict["Grade1_product"] < G1Psell:
                print("you need  " + str(G1Psell - userdict["Grade1_product"]) + " more grade 1 products to sell that much stuff")
            elif userdict["Grade1_product"] >= G1Psell and G1Psell >= 0:
                Morket_G1P_value = round(random.uniform(20,90), 2)
                Morket_G1P_get_money = round((G1Psell * Morket_G1P_value), 3)
                userdict["Grade1_product"] -= G1Psell
                userdict["money"] += Morket_G1P_get_money
                print("Market value for grade 1 products was " + str(Morket_G1P_value) +" apeice")
                print("You sold " + str(G1Psell) + " grade 1 products")
                print("You gained " + str(Morket_G1P_get_money) + " dollars from the market")
                print("You now have " + str(userdict["money"]) + " dollars")
                print("You have " + str(userdict["Grade1_product"]) + " grade 1 product(s)")
            else:
                print("invalid {num} in \"sellG1P {num}\"")

#moneyloan

    elif command[0:10] == "moneyloan ":
        if command[10:] == "nan":
            print("nan is not a number!")
            return
        if str(command[10:]) == "inf":
            print("inf is not a valid number!")
            return
        else:
            want_loan = float(command[10:])
            if want_loan < 0:
                print("invalid {num} in \"moneyloan {num}\"")
            elif userdict["debt"] > 10000:
                print("you have more than 10000 dollars of debt, pay back your debts first before moving on")
            elif userdict["amt_borrowed"] > 20000:
                print("you have borrowed more than 20000 dollars sice you were debt free, pay back all your debts first before moving on")
            elif want_loan > 10000:
                print("you cannot loan out more than 10000 dollars!")
            else:
                userdict["debt"] += want_loan
                userdict["amt_borrowed"] += want_loan
                interest()
                userdict["money"] += want_loan
                print("you borrowed " + str(want_loan) +" dollars")
                print("You now have " + str(userdict["money"]) + " dollars")
                print("You are " + str(userdict["debt"]) + " dollars in debt")

#loanpay

    elif command[0:8] == "loanpay ":
        if command[8:] == "nan":
            print("nan is not a number!")
            return
        if str(command[8:]) == "inf":
            print("inf is not a valid number!")
            return
        else:
            want_loanpay = float(command[8:])
            if want_loanpay <= 0:
                print("invalid {num} in \"loanpay {num}\"")
            elif (want_loanpay - userdict["debt"]) > 1000:
                print("you cannot have less than -1000 dollars of debt")
            elif want_loanpay > userdict["money"]:
                print("you need " + str(want_loanpay - userdict["money"]) + " more money to repay that much debt")
            else:
                userdict["debt"] -= want_loanpay
                userdict["money"] -= want_loanpay
                print("You paid " + str(want_loanpay) + " off your debt")
                print("You are " + str(userdict["debt"]) + " dollars in debt")
                print("You now have " + str(userdict["money"]) + " dollars")
                if userdict["debt"] <= 0:
                    userdict["amt_borrowed"] = 0
                            

#stats for nerds

    elif command == "stats for nerds":
        print("USERDICT")
        print(userdict)


#save

    elif command == "save":
        CtrlS()
        print("progress saved.")

#datarecovery

    elif command == "datarecovery":
        userdict = eval(open("savedata.txt","r").read())
        print("savedata recovered from last save.")

#wipemydata

    elif command == "WIPEMYDATAFORGOOD":
        reset_confirm = input("enter \"YES\" to continue with the reset")
        if reset_confirm == "YES":
            restart()
            print("""\
All data successfully wiped
To clear any ongoing works, close & reopen the game\
""")
        else:
            print("reset cancelled")

    elif command == "exit":
        if userdict["Working"] == True:
            print("WARNING: You still have ongoing works!")
        exit_confirm = input("""\
to confirm exit, type \"YES\"
note: all ongoing works will be lost if you exit the game! \
""")

    else:
        print("""\
Invalid Command
Type \"help\" to see commands\
""")


#game run

print("""\
Greetings fellow comrade!
As you know, ever since the recession, our economy has been left in shambles.
Thus, from today onwards you will be the designated manager of the Factory der freien völker.
We now depend on men like you to rebuild this country.
The journey ahead will be difficult, but we hope you soon get the hang of things.
""")

try:
    userdict = eval(open("savedata.txt", "r").read())
except:
    udict_notfound = input("savedata.txt is not found!")
    exit()
print("""\
savedata recovered from last save.
""")
if bool(userdict) == False:
    restart()
userdict["Working"] = False

while True:
    inp_cmd = input("so, what would you like to do next? ")
    print("")
    asyncio.run(gameplay(inp_cmd))
    print("""
""")
    if exit_confirm == "YES":
        break

exiter = input("""\
would you like to save before exiting?
(type \"y\" to save) \
""")
if exiter == "y":
    CtrlS()
