# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

screen cards:
    image Solid("#ffffff")

    draggroup:
        drag:
            drag_name: "sound"
            align(0.5,0.3)
            drag_raise True
            image Solid("#ff9bf4") xysize(250, 250)
            
        drag:
            drag_name: "kana"
            align(0.5,0.7)
            drag_raise True
            image Solid("#ff9b33") xysize(250, 250)



define e = Character("Eileen")

#speech bubble test
define l = Character(None, image="lucy", kind=bubble)


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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    l "Here's a speech bubble."

    call screen cards

    # This ends the game.

    return
