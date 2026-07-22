import random

while True:
    print("====================================")
    print("        OPERATION BOMB DEFUSE")
    print("====================================")
    print("1. Start Mission")
    print("2. Exit")

    choice = int(input("Enter your choice : "))
    match choice:
        case 1:

            agent = input("Enter Agent Name : ")
            print("Welcome Agent", agent)

            bombId=random.randint(100, 999)
            correctWire=random.randint(1, 4)
            lives=3
            score=0
            scan=False
            while True:
                print("\nLives :", lives)
                print("Score :", score)
                print("1. Scan Bomb")
                print("2. View Hint")
                print("3. Cut Wire")
                print("4. Abort Mission")

                mission=int(input("Enter your choice : "))

                if mission==1:
                    print("\nBomb ID :", bombId)
                    print("Status : ACTIVE")
                    print("Scan Completed")
                    scan = True

                elif mission==2:
                    if scan==False:
                        print("Please Scan Bomb First")

                    elif correctWire==1:
                        print("Correct Wire is RED")

                    elif correctWire==2:
                        print("Correct Wire is BLUE")

                    elif correctWire==3:
                        print("Correct Wire is GREEN")

                    else:
                        print("Correct Wire is YELLOW")

                elif mission==3:
                    if scan==False:
                        print("Please Scan Bomb First")

                    else:
                        print("1. RED  2. BLUE  3. GREEN  4. YELLOW")
                        wire=int(input("Choose Wire : "))

                        if wire==correctWire:
                            score=score + 100
                            print("Bomb Defused Successfully")
                            print("Final Score :", score)
                            break

                        else:
                            lives=lives - 1
                            print("Wrong Wire, Lives Left :", lives)
                            if lives==0:
                                print("BOOM !!! Mission Failed")
                                break

                elif mission==4:
                    print("Mission Aborted")
                    break

                else:
                    print("Invalid Choice")

        case 2:
            print("Thank You Agent")
            break

        case _:
            print("Invalid Choice")