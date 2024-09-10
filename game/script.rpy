# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "What do you want to practice?"


    call screen cards

label test1:
    #speech bubble test
    define l = Character(None, image="lucy", kind=bubble)
    l "Here's a speech bubble."
    call screen cards

label test2:
    #speech bubble test
    define l = Character(None, image="lucy", kind=bubble)
    l "End."
    jump vowel_intro

    return
