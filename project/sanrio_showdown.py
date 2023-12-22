import random as rnd, csv, time

def main():
    ### Welcome ###
    line_printer("\nWelcome to...")
    ### TITLE CARD - DO NOT TOUCH!!
    # ascii art generated with https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Sanrio%20Showdown
    # double "\" to prevent dash from being read as escape key
    print(
        r"""
     _________                   .__           _________.__                     .___
    /   _____/____    ___________|__| ____    /   _____/|  |__   ______  _  ____| _/______  _  ______
    \_____  \\__  \  /    \_  __ \  |/  _ \   \_____  \ |  |  \ /  _ \ \/ \/ / __ |/  _ \ \/ \/ /    \
    /        \/ __ \|   |  \  | \/  (  <_> )  /        \|   Y  (  <_> )     / /_/ (  <_> )     /   |  \
   /_______  (____  /___|  /__|  |__|\____/  /_______  /|___|  /\____/ \/\_/\____ |\____/ \/\_/|___|  /
           \/     \/     \/                          \/      \/                  \/                 \/
            """
    )
    ### NO TOUCH!
    time.sleep(1.5)  # dramatic pause

    # list of fighters that can be iterated through
    fighters = [
        "Hello Kitty",
        "Kuromi",
        "Cinnamoroll",
        "My Melody",
        "Pompompurin",
        "Pochacco",
    ]
    # lsit of attack files that correspond to each fighter to iterate through
    attack_files = [
        "hk.csv",
        "kuro.csv",
        "cinna.csv",
        "mm.csv",
        "pompom.csv",
        "pocha.csv",
    ]

    ### Character Selection ###
    line_printer("Choose your fighter!")
    viable = [] # list of viable options for users to input
    # print out each available character
    for i in range(len(fighters)):
        viable.append(i + 1)  # +1 prevents 0 from being a viable option
        line_printer(
            f"[{i+1}] {fighters[i]}"
        )  # +1, bc i don't want a choice 0 since it's not conventional

    # asks user to select fighter until they input a valid choice
    while True:
        player_choice = get_input("Select fighter: ")
        player_choice = player_choice
        # if choice insn't an integer
        if not player_choice.isdigit():
            line_printer("Be so for real. That's not even a number (or if it is, not a WHOLE one 😒)")
        # if choice is invalid
        elif int(player_choice) not in viable:
            line_printer("Invalid option. Try again!")
        else: # valid input!
            player_choice = int(
                player_choice
            )  # change string to int so it can be used for indexing
            break
    player_fighter = fighters[
        int(player_choice) - 1
    ]  # -1 to offset the +1 in the for loop in print_menu()
    line_printer(f"You've selected {player_fighter.upper()}!")

    # dict of all fighters and their corresponding attacks and art
    fighter_mapping = {
    "Hello Kitty": (draw_hk, attack_files[0]),
    "Kuromi": (draw_kuro, attack_files[1]),
    "Cinnamoroll": (draw_cinna, attack_files[2]),
    "My Melody": (draw_mm, attack_files[3]),
    "Pompompurin": (draw_pompom, attack_files[4]),
    "Pochacco": (draw_poch, attack_files[5])
    }
    # variables to hold output of fighter[name]
    draw_function, attack_file = fighter_mapping[player_fighter]
    draw_function()
    time.sleep(1) # dramatic pause

    ### Select CPU fighter
    cpu_fighter = rnd.choice(fighters)  # i WANT there to be a possibility for the cpu to be the same as the player. Robot emoji
    if cpu_fighter == player_fighter:
        line_printer(f"\nYour opponent is...ALSO {cpu_fighter.upper()}!")
        line_printer("...So sad to see twins fight :'(")
        cpu_fighter += ".CPU"  # So that cpu character and player character can be distinguished while fighting
    else:
        line_printer(f"Your opponent is...{cpu_fighter.upper()}!")
        draw_function, cpu_attack_file = fighter_mapping[cpu_fighter]
        draw_function()
    time.sleep(1)

    ### Pre-Battle Set Up ###
    # Health
    pl_health = 100  # pl is shorthand for player
    cpu_health = 100

    # Fighter modificatoins
    print("\n _____                   _____")
    print("|__$__|BATTLE PREP SHOP |__$__|")
    line_printer(
        "Before you go out for battle, you need to make sure you're properly equipped!"
    )
    line_printer(
        "Everything is 1 coin each! Buy as many of anything as your heart desires!"
    )
    line_printer("(and by that I mean 5 things, you only have 5 coins)")
    time.sleep(0.05)
    # items + description
    print("---------------------------------------------------------")
    print("🐸 Keroppi's Healing Donuts")
    line_printer(r"    gain 5% of your health!")
    print("🐧 Badtz-Maru's Dodging Classes")
    line_printer("    inrease your liklihood to dodge an attack!")
    print("🍳 Lessons on Constitution from Gudetama")
    line_printer("    increase resistance to getting stunned!")
    print("---------------------------------------------------------")

    # buy
    while True:
        donuts = shop("donuts")
        dodges = shop("dodge classes")
        lessons = shop("constitution lessons")
        total = donuts + lessons + dodges
        # no spending more than 5 coins
        if total > 5 or total < 0:
            line_printer(
                "Hey, you can't spend more than 5 coins. Let's do this again."
            )
        else: # print player stats so they can see them. cpu stats are a secret
            line_printer(f"\n{player_fighter.upper()} starting stats:")
            line_printer(f"Donuts: {donuts} | Dodges: {dodges} | Lessons: {lessons}")
            line_printer(f"HP: {pl_health}")
            time.sleep(1.5)  # so the reader can take it in
            break

    # same thing but with the CPU
    while True:
        cpu_donuts = rnd.randint(0, 5)
        cpu_dodges = rnd.randint(0, 5)
        cpu_lessons = rnd.randint(0, 5)
        cpu_total = cpu_lessons + cpu_dodges + cpu_donuts
        if 0 <= cpu_total <= 5:  # if between 0 and 5, inclusive
            break

    ### FIGHTING, WHOOOO! ###
    # countdown
    line_printer(f"\n{player_fighter.upper()} v. {cpu_fighter.upper()} begins in")
    for i in range(3, 0, -1):  # ?)
        line_printer(f"{i}...")
        time.sleep(0.5)
    time.sleep(0.5)  # I want this wait to be a bit longer
    # ascii art from https://patorjk.com/software/taag/#p=display&c=bash&f=Fire%20Font-k&t=START%0A
    print(
        r"""
   (                     (
   )\ )  *   )    (      )\ )  *   )
  (()/(` )  /(    )\    (()/(` )  /(
   /(_))( )(_))((((_)(   /(_))( )(_))
  (_)) (_(_())  )\_ ) (_)) (_(_())
  / __||_   _|(_/_\(_)| _ \|_   _|
  \__ \  | |   / _ \  |   /  | |
  |___/  |_|  /_/ \_\ |_|_\  |_|
          """
    )
    time.sleep(1)
    # need: tracker for whose turn it is
    pl_turn = True
    line_printer("type 'attack' to attack or 'heal' to eat a health donut")

    # fighting loop until game over
    while True:
        # PLAYER TURN
        if pl_turn == True:
            while True:
                action = get_input(f"\n🌸 {player_fighter.upper()}>")
                action = action.lower()  #!!
                if action != "attack" and action != "heal": # check that input is valid
                    line_printer("Invalid input.")
                else:
                    break

            # if action is 'attack'
            if action == "attack":
                attack, damage = select_attack(attack_file)
                if damage.isdigit():  # attack with HP damage
                    hit = handle_hit(cpu_dodges)
                    cpu_dodges -= 1
                    if hit == True:
                        cpu_health -= int(damage) # subtract damage
                        line_printer(
                            f"{player_fighter} uses {attack.upper()}! {cpu_fighter} loses {damage}HP❤️‍🩹 (Left:{int(cpu_health)}HP)"
                        )
                    else:  # attack dodged
                        line_printer(
                            f"{player_fighter} uses {attack.upper()}! But, {cpu_fighter} DODGES the attack! Badtz-Maru's classes paid off!🐧"
                        )
                    pl_turn = False

                else:  # an attack with a stun effect was made
                    hit = handle_hit(cpu_lessons)
                    cpu_lessons -= 1
                    if hit == True:  # stun works
                        line_printer(
                            f"{player_fighter} uses {attack.upper()}! {cpu_fighter} is {damage}!"
                        )
                        cpu_health -= 5 # same stun damage for everyone
                        line_printer(f"{cpu_fighter} loses 5HP and misses a turn!")
                    else:
                        line_printer(
                            f"{player_fighter} uses {attack.upper()}! But, {cpu_fighter} RESISTS the stunning attack! Gudetama's lessons paid off!🍳"
                        )
                        pl_turn = False
            # if action is 'heal'
            else:
                if donuts > 0:
                    # health donut eaten. increase HP by 10%
                    pl_health *= 1.1
                    line_printer(
                        f"{player_fighter} ate a health donut🍩. {player_fighter} has {int(pl_health)}HP💖"
                    )
                    donuts -= 1
                    pl_turn = False
                else:
                    line_printer(f"{player_fighter} is out of health donuts! Try agin")

        # CPU TURN
        else:
            # handle action
            if (
                cpu_donuts == 0
            ):  # this isn't working for some  reason. CPU still did heal
                action = "attack"
            elif cpu_health > 20:
                # select attack more often than heal
                action = rnd.choice(["attack"] * 3 + ["heal"])
            else:  # i want the cpu to be more likely to heal itself when on low health
                action = rnd.choice(["attack"] + ["heal"] * 2)

            print(f"\n🤖 {cpu_fighter.upper()}>{action}")

            if action == "attack":
                attack, damage = select_attack(cpu_attack_file)
                if damage.isdigit():
                    hit = handle_hit(dodges)  # player dodging
                    dodges -= 1
                    if hit == True:
                        pl_health -= int(damage)
                        line_printer(
                            f"{cpu_fighter} uses {attack.upper()}! {player_fighter} loses {damage}HP❤️‍🩹 (Left:{int(pl_health)}HP)"
                        )
                    else:
                        line_printer(
                            f"{cpu_fighter} uses {attack.upper()}! But {player_fighter} DODGES the attack! Badtz-Maru's classes paid off!🐧"
                        )
                    pl_turn = True

                else:  # stunning attack
                    hit = handle_hit(cpu_lessons)
                    cpu_lessons -= 1
                    if hit == True:
                        line_printer(
                            f"{cpu_fighter} uses {attack.upper()}! {player_fighter} is {damage}!"
                        )
                        pl_health -= 5
                        line_printer(f"{player_fighter} loses 5HP and misses a turn!")
                        # no break because player turn is skipepd over
                    else:
                        line_printer(
                            f"{cpu_fighter} uses {attack.upper()}! But, {player_fighter} RESISTS the stunning attack! Gudetama's lessons paid off!🍳"
                        )
                        pl_turn = True
            else:  # if action is 'heal'
                # health donut eaten. increase HP by 10%
                cpu_health *= 1.1
                line_printer(
                    f"{cpu_fighter.upper()} ate a health donut🍩. {cpu_fighter} has {int(cpu_health)}HP💖"
                )
                pl_turn = True

        # game over conditions
        if pl_health <= 0:
            line_printer(f"🏆🏆🏆 {cpu_fighter.upper()} wins! Flawless victory! 🏆🏆🏆")
            break
        elif cpu_health <= 0:
            line_printer(f"🏆🏆🏆 {player_fighter.upper()} wins! Flawless victory! 🏆🏆🏆")
            break


# given by ddb
def line_printer(string, **kwargs): # **kwargs (key word arguments) allows for function to take in a non-fixed bumber of inputs
    end = kwargs.get("end", "\n")  # gets value of 'end' if it exists, otherwise, it uses '\n'
    print(string, end=end)
    if len(string) < 30:
        time.sleep(0.25)
    elif 30 < len(string) < 50:
        time.sleep(0.5)
    else:
        time.sleep(1.5)


# GOT ROM STACK OVERFLOW ABSOLUTELY IN LOVE https://stackoverflow.com/questions/2520893/how-to-flush-the-input-stream
def flush_input(): # it clears all of the input that the user could have typed in while the prompt was still being asked
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios  # for linux/unix

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


# so that I don't have to keep calling flush_input then input(). Made with assitance from ddb
def get_input(
    prompt="",
):  # prompt="" allows for get_input() to work like input(), which can take an optional argument
    flush_input()
    time.sleep(0.05)
    return (
        input(prompt).lower().strip()
    )  # inputs need to be lower case and i want to ignore leading and trailing spaces (strip does this part)


def handle_hit(case):
    # handles dodges and lessons (the cases) bought at the pre-battle shop
    miss_chance = 0  # 0% chance that an attack misses
    # Each class gives attack a 10% chance of missing. Goes down to 5% if case > 3
    for i in range(case):
        if i <= 3: # number of dodges and lessons
            miss_chance += 10  # 10% increase
        elif i > 3: # i don't want to make fighters too powerful
            miss_chance += 5  # 5% increase
    hit = rnd.choice([False] * miss_chance + [True] * (100 - miss_chance)) # chance of attack hitting or missing
    return hit # boolean


def play_again(): # asks if they want to play again
    options = ["y", "n", "yes", "no"] # valid options
    while True:
        line_printer("\nPlay again? (y/n/yes/no): ", end="")
        choice = get_input()
        choice = choice
        if choice not in options:
            line_printer("Please put something that makes sense")
        else:
            break
    if choice == "yes" or choice == "y":
        return True
    else:
        line_printer(r"""
  _______ _                 _                           __                   _             _             _
 |__   __| |               | |                         / _|                 | |           (_)           | |
    | |  | |__   __ _ _ __ | | __  _   _  ___  _   _  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _| |
    | |  | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | |
    | |  | | | | (_| | | | |   <  | |_| | (_) | |_| | | || (_) | |    | |_) | | (_| | |_| | | | | | (_| |_|
    |_|  |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, (_)
                                    __/ |                             | |             __/ |         __/ |
                                   |___/                              |_|            |___/         |___/
                     """)
        # art from https://patorjk.com/software/taag/#p=display&f=Big&t=Thank%20you%20for%20playing!
        return False


def select_attack(file): # grabs the attacks that are associated with each fighter
    attacks = {}
    weights = (
        []
    )  # the probabilty of an attack being chosen, mostly to prevent stun attacks from happening a lot
    with open("attacks/" + file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip first row
        for row in reader:
            key = row[0]
            value = row[1]
            weight = int(row[2])
            attacks[key] = value
            weights.append(weight)
    # attacks is not a dictionary where the key is the attack name and the value is the attack effect/damage

    # randomly select an attack
    attack_names = list(
        attacks.keys()
    )  # list of key values, which are the attack names
    rnd_attack = rnd.choices(attack_names, weights, k=1)[
        0
    ]  # randomly select an attack. given by ddb
    # This will return a list with one element, which is why we use [0] to get the actual element. The k=1 argument means that we want to select one element.
    damage = attacks[
        rnd_attack
    ]  # print value associated with the randomly selected attack
    return rnd_attack, damage


def shop(item): # asks user for how much of each thing that they want. Given with the hlep (not fully!) of chatgpt
    while True:
        line_printer(f"Number of {item}: ", end="")
        user_input = get_input()
        if user_input.isdigit() and int(user_input) >= 0:
            return int(user_input)
        else:
            line_printer(
                "Input must be a positive digit. No negative numbers, fractions, or words"
            )


# these functions are in the order of the fighters list, not alpha order
def draw_hk():
    print(
        """
    ⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆⠀⠀⠀
⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽⠀⠀⠀
⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇⠀⠀⠀
⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀⠀⠀
⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒
⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤⠀
⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀
⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀
              """
    )


# art from https://emojicombos.com/hello-kitty-ascii-art


def draw_kuro():
    print(
        """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠈⣷
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠛⡗⠊⠁
⠀⠀⠀⠀⠀⠀⠀⢸⡁⠀⣸⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠚⠁⠀⠀⢠⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⠀⠉⠑⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⠉⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠉⠒⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡤⠒⠚⠉⠉⠉⠉⠉⠉⠉⠙⠒⠦⣄⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀
⠀⠀⢀⣠⣤⣄⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠙⢦⡀⢀⣰⠇⠀⠀⠀
⣴⣾⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣟⠁⣿⣿⣿⣀⣿⠃⠀⠀⠀⠀⠀⠀⠹⡉⠁⠀⠀⠀⠀
⢿⣿⣿⣿⣿⡿⠇⠀⢀⣤⣄⣀⠉⠉⠑⡶⠦⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠉⠛⢿⢿⠿⠏⢁⡴⠛⠦⣀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠿⣷⣶⣧⡀⠀⠀⠀⠀⢀⠔⠉⠀⠀⠀⠉⠓⠢⠤⠤⠚⠁⠀⠀⠀⣰⠓⢆⠀⠀⢸⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠻⢷⣄⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⡇⠈⢣⠀⢸⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠉⠁⡇⠀⠀⣷⠶⠶⣤⡀⠀⠀⠀⢀⡤⢄⠀⠻⣿⣿⠏⠀⢸⠀⡼⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⢣⠀⠀⠀⣀⣀⡀⠁⠀⢀⡀⠀⠓⣉⠀⠀⠠⣾⣿⣇⡜⡴⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠢⣀⠀⠈⢇⠀⢺⣿⣿⡟⠀⠀⠸⣍⢩⠟⠁⠀⠀⠀⠀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⣦⣌⣳⣄⡀⠀⠀⠀⠀⠀⠈⠁⠀⠀⢀⣀⡴⡞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠛⢲⣋⣀⣀⣀⡀⠈⠉⠉⠑⠒⣒⠚⠉⠉⠉⡤⢄⣀⠈⢳⠤⢤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠋⠀⠀⠀⠀⠹⣄⣀⢀⡤⠚⠉⠓⠦⣄⣀⣇⡀⠀⠉⠙⠦⠴⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡅⢈⡏⠀⠀⠀⠀⠀⠸⣅⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """
    )


# art from https://emojicombos.com/kuromi-ascii-art


def draw_cinna():
    print(
        """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠤⠤⠤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⢦⣤⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⢋⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠙⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠀⠉⠓⠦⣤⣤⣤⣤⣤⣤⣄⣀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣷⡄⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀
⠀⠀⣠⠞⠁⠀⠀⣀⣠⣏⡀⠀⢠⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⡃⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆
⢀⡞⠁⠀⣠⠶⠛⠉⠉⠉⠙⢦⡸⣿⡿⠀⠀⠀⡄⢀⣀⣀⡶⠀⠀⠀⢀⡄⣀⠀⣢⠟⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃
⡞⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⢳⢀⣠⠀⠀⠀⠉⠉⠀⠀⣀⠀⠀⠀⢀⣠⡴⠞⠁⠀⠀⠈⠓⠦⣄⣀⠀⠀⠀⠀⣀⣤⠞⠁⠀
⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠁⠀⢀⣀⣀⡴⠋⢻⡉⠙⠾⡟⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠉⠉⠀⠀⠀⠀
⠘⣦⡀⠀⠀⠀⠀⠀⠀⣀⣤⠞⢉⣹⣯⣍⣿⠉⠟⠀⠀⣸⠳⣄⡀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠒⠒⠒⠒⠚⠋⠁⠀⡴⠋⢀⡀⢠⡇⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⢀⡾⠋⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠉⠋⠻⣄⠀⠀⠀⠀⠀⣀⣠⣴⠞⠋⠳⠶⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠦⢤⠤⠶⠋⠙⠳⣆⣀⣈⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              """
    )


# art from https://emojicombos.com/cinnamoroll-text-art


def draw_mm():
    print(
        """
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⠟⠛⠛⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠛⢷⣄⢀⣠⣤⡶⠾⠟⠛⠛⠛⠛⠛⠛⠻⢷⡄
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢘⣿
⠀⠀⠀⢰⣿⠀⠀⢰⣆⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏
⠀⢀⣤⣼⣿⠶⣦⡄⠛⢷⣤⣤⣀⣀⣴⡿⢶⣦⣤⣤⣤⣤⣶⣶⡶⠾⠟⠛⠁⠀
⢰⣟⠁⠉⣁⠀⢼⣇⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠙⠻⢶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⢹⡶⠈⠛⣀⠀⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀
⠀⠘⢿⣶⡾⠛⠛⠋⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣀⡀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀
⠀⠀⣿⠃⠀⠀⠀⠀⣀⣤⡶⠟⠛⠋⠉⠉⠉⠉⠉⠛⠿⣦⡀⢸⡇⠀⠀⠀⠀⠀
⠀⠸⣿⠀⠀⠀⣠⡾⠛⡁⠀⠀⠀⠀⠀⠀⠀⠀⣾⣷⠀⢹⣧⣿⠁⠀⠀⠀⠀⠀
⠀⠀⢻⣆⠀⢰⡟⠁⢸⣿⠀⠀⠀⠀⣴⡄⠀⠀⠉⠁⠀⣸⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⣦⣿⣇⠀⠈⠉⠀⠀⠀⢰⣶⡾⠇⠀⢀⣤⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣷⣤⣄⣀⣀⣀⣀⣠⣤⣴⡾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              """
    )


# art from https://emojicombos.com/my-melody-text-art


def draw_pompom():
    print(
        """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣾⣿⣷⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣤⣴⣶⠿⠛⠋⠁⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠈⠙⠻⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⣾⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⣤⣀⠀⠀⠀
⢠⣿⠏⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⣰⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠉⠻⣷⣄⠀
⣿⠇⠀⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠉⠁⠀⠀⣀⠀⠸⣶⠖⠀⠀⠀⠀⠘⠿⠁⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆
⣿⡆⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠿⣦⡾⠿⣦⣤⡿⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿
⠹⣿⣦⣀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣀⠀⠀⠀⣀⣴⣿⠃
⠀⠈⠙⠛⠛⣛⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⡟⠛⠛⠋⠀⠀
⠀          """
    )


# art from https://emojicombos.com/pompompurin


def draw_poch():
    print(
        """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⡿⠟⢀⣀⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡼⠟⠛⠛⠓⠙⠚⢡⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⢫⣍⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡶⠛⣶⡼⠃⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⠀⣀⣿⠀⠀⠘⠋⠀⣀⠀⠀⠀⠀⠀⠀⣠⡿⠙⣽⣷⣦⡀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣧⡀⠀⠀⠈⠛⠃⠀⢾⠇⠀⠰⠾⠁⠀⠈⠻⢿⣿⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡳⡤⢀⡀⠀⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣶⣬⣽⣿⣶⣶⣶⣟⠙⠳⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡏⠉⠉⠉⠉⠉⠛⠛⠻⠿⣽⣿⣿⣿⡛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡟⠉⠀⠀⠀⢰⡶⣤⣄⣀⣀⣀⣀⣀⠀⠀⠈⠉⠳⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠛⠛⠒⠒⠒⠒⠛⠛⠀⠈⠉⠉⠉⠙⠓⠒⠲⠶⠖⠒⠓⠀⠀⠀⠀⠀⠀⠀⠀

          """
    )


# art from https://emojicombos.com/pochacco-ascii-art


main()
# play again prompt
while True:
    play_again_choice = play_again()
    if play_again_choice == True:
        main()
    else:
        break
