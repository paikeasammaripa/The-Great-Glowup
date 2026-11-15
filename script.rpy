define h = Character("Haylie", color="#d875b9")
define j = Character("Justin", color="#76cc67")
define m = Character("Marley", color="#784581ff")
define e = Character("emilie", color="#515bc46d")
define d = Character("Darel", color="#e4d534")

image bg_trashy_apartment = "images/trashy_apartment.jpg"
image bg_clean_apartment = "images/clean_apartment.jpg"
image bg_baking_kitchen = "image/baking_kitchen.avif"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg baking kitchen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
