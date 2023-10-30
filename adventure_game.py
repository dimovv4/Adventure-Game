while True:
    answer = input("Would you like to play? (yes/no): ").lower()

    if answer == "yes":
        while True:
            answer = input("You reach a crossroad, would you like to go left or right? (left/right): ").lower()

            if answer == "left":
                answer = input("You encounter a monster, are you going to fight it, or run for your life? (fight/run): ").lower()

                if answer == "fight":
                    print("That was not a great idea. You lost!")
                    break

                elif answer == "run":
                    print("Good job! You made it away safely!")
                    break

                else:
                    print("Invalid choice. Please choose 'fight' or 'run'.")
                    continue

            elif answer == "right":
                print("You walk aimlessly for hours. You get very hungry and you start going crazy. There is nothing to the right. You lose.")
                break

            else:
                print("Invalid choice. Please choose 'left' or 'right'.")
                continue

        answer = input("You see a plane and a car. Which one are you taking? (plane/car): ").lower()
        if answer == "plane":
            print("Unfortunately, you do not know how to fly... Game over!")
        elif answer == "car":
            print("Good job! Fortunately, the car started and had enough fuel for you to go home! You win!")
        else:
            print("Invalid choice. Please choose 'plane' or 'car'.")
            continue

    elif answer == "no":
        print("See you later.")
        break

    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
