# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def dragFunction(dragged_item, dropped_on):
      if dropped_on is not None:
        # if dragged is the same type or doesn't match print error
        if dragged_item[0].drag_name == dropped_on.drag_name:
            #dragged_item[0].droppable = False
            print("error")
        # if dragged is a different type and a correct match print correct
        if dragged_item[0].drag_name != dropped_on.drag_name:
            dragged_item[0].snapped(dropped_on.x, dropped_on.y)
            print("correct")
        #else print unknown error
        else:
            print("unknown error")


screen cards:
    image Solid("#ffffff")

    draggroup:
        drag:
            drag_name "sound"
            alternate Help()
            align(0.5,0.3)
            dragged dragFunction
            drag_raise True
            droppable True
            image Solid("#ff9bf4") xysize(250, 250)
            
        drag:
            drag_name "kana"
            alternate Help()
            align(0.5,0.7)
            dragged dragFunction
            drag_raise True
            droppable True
            image Solid("#ff9b33") xysize(250, 250)

    #add kana_draggroup

default sound_drag = Drag(d=Solid("#ff9bf4"), xysize=(250, 250), drag_name ="sound",drag_raise =True,align= (0.5,0.3))
#default kana_drag = Drag(d=Solid("#ff9b33"), xysize=(250, 250), drag_name ="kana",drag_raise =True,align= (0.5,0.5))
default kana_drag = Drag(d=Solid("#ff9b33"), xysize=(250, 250), drag_name ="kana",drag_raise =True,align= (0.5,0.7))
default kana_draggroup = DragGroup(sound_drag,kana_drag)

define config.longpress_duration = 0.5



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
