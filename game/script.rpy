

define e = Character("Eileen")


# The game starts here.

label start:

    scene bg room

    show eileen happy

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
