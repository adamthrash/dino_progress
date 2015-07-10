def print_steg_progress(number_of_items, current_position):
    stegasaurus = """
                                     .       .
                                    / `.   .' \\
                            .---.  <    > <    >  .---.
                            |    \\\\  \\ - ~ ~ - /  /    |
                             ~-..-~             ~-..-~
                         \\~~~\\.'                    `./~~~/
               .-~~^-.    \\__/                        \\__/
             .'  O    \\     /               /       \\  \\
            (_____,    `._.'               |         }  \\/~~~/
             `----.          /       }     |        /    \\__/
                   `-.      |       /      |       /      `. ,~~|
                       ~-.__|      /_ - ~ ^|      /- _      `..-'   f: f:
                            |     /        |     /     ~-.     `-. _||_||_
                            |_____|        |_____|         ~ - . _ _ _ _ _>
    """

    steg_array = stegasaurus.split("\n")

    n_lines = number_of_items/16

    if current_position == 0:
        dino_line = 0
    else:
        dino_line = ((current_position/n_lines)-1)%16
    if current_position%n_lines == 0:
        print(steg_array[dino_line])
        if dino_line != len(steg_array)-1:
            dino_line += 1
        else:
            dino_line = 0

## EXAMPLE USAGE
# stuff = [0]*100
# for i in range(len(stuff)):
#     # process your stuff
#     stuff[i] = stuff[i]+i
#     print_steg_progress(len(stuff), i)
# print(stuff)
