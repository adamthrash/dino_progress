import sys
def print_dino_progress(number_of_items, current_position, dinosaur):
    stegasaurus = """
                         .       .
                        / `.   .' \\
                .---.  <    > <    >  .---.
                |    \  \ - ~ ~ - /  /    |
                 ~-..-~             ~-..-~
             \~~~\.'                    `./~~~/
              \__/                        \__/
               /                  .-    .  \\
        _._ _.-    .-~ ~-.       /       }   \/~~~/
    _.-'q  }~     /       }     {        ;    \__/
   {'__,  /      (       /      {       /      `. ,~~|   .     .
    `''''='~~-.__(      /_      |      /- _      `..-'   \\\\   //
                / \   =/  ~~--~~{    ./|    ~-.     `-..__\\\\_//_.-'
               {   \  +\         \  =\ (        ~ - . _ _ _..---~
               |  | {   }         \   \_\\
              '---.o___,'       .o___,'
    """

    dimetredon = """
                                _._
                              _/:|:
                             /||||||.
                             ||||||||.
                            /|||||||||:
                           /|||||||||||
                          .|||||||||||||
                          | ||||||||||||:
                        _/| |||||||||||||:_=---.._
                        | | |||||:'''':||  '~-._  '-.
                      _/| | ||'         '-._   _:    ;
                      | | | '               '~~     _;
                      | '                _.=._    _-~
                   _.~                  {     '-_'
           _.--=.-~       _.._          {_       }
       _.-~   @-,        {    '-._     _. '~==+  |
      ('          }       \_      \_.=~       |  |
      `,,,,,,,'  /_         ~-_    )         <_oo_>
        `-----~~/ /'===...===' +   /
               <_oo_>         /  //
                             /  //
                            <_oo_>
    """

    pleisiosaur = """
                                                            ///\\\\\\\\
                                   --_                    //       \\\\
                                    \\ \\                ///           \\\\
                                    \\  \\             //       ///\\\\    \\
              --___   //////\\\\\\\\    |   \\         ///       //     \\   \\
              \\    ///          \\\\\\\\\\\\\\ |       //        //       \\    \\
               \\///                    \\\\\\\\\\\\\\///        /          \\    \\
              //                                        /            \\   \\
             /                                         /             \\    \\
           //                                        //              \\    \\
         //                                         /                 \\   \\
        /                            /     \\      //                  \\   \\
      //                  \\          \\     /    //                    \\   /
     /                    /           \\    /   /                      /   /
    /     ///\\\\\\\\\\  \\     /           |    |///                       /   /
    //    //        \\\\|    /\\\\\\       ///    /                         /    /
    /    //            /    /   \\\\\\\\/// /    /                          /    /
    /   //              /    /           /   /                          /    /
    /   /              /   _/           /  _/                           /    /
    /   /              /  /            /__/                            /    /
    \\   \\             /__/                                            /    /
    \\  \\                                                           _/    /
    \\  \\                                                       __/     /
    \\  \\                                                  ___/       /
    \\  \\_                                           __---/       ___/
    \\   ---_____                             __---/          __/
     \\______-----                           /        _____---
                                           /     ___/
                                          /     /
                                          |  O  \\
                                          /    /|
                                          /   / /
                                          /  / /
                                          |m/\\_/
            """

    if dinosaur == "dimetredon":
        dino_array = dimetredon.split("\n")
    elif dinosaur == "stegasaurus":
        dino_array = stegasaurus.split("\n")
    elif dinosaur == "pleisiosaur":
        dino_array = pleisiosaur.split("\n")
    else:
        dino_array = stegasaurus.split("\n")

    n_lines = number_of_items/len(dino_array)

    if current_position == 0:
        dino_line = 0
    else:
        dino_line = ((current_position/n_lines)-1)%len(dino_array)
    if current_position%n_lines == 0:
        print(dino_array[dino_line])
        if dino_line != len(dino_array)-1:
            dino_line += 1
        else:
            dino_line = 0

## EXAMPLE USAGE
stuff = [0]*190
for i in range(len(stuff)):
    # process your stuff
    stuff[i] = stuff[i]+i
    print_dino_progress(len(stuff), i, "stegasaurus")
print(stuff)
