# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
#FIX: how to add print statements to in game dialogue box

    def drop_control(current_drag, dragged_item):
      #this may interfere with other drag properties such as drag_joined
      print(f"current_drag={current_drag.drag_name}, dragged_item={dragged_item[0].drag_name}")
        
    # joined drag is for moving cards together, will likely not use
    # if in use add drag_joined = joined_drag to all drag cards including match_drag
    #def joined_drag(item_dragged):
      #return [(item_dragged, 0.0), (test_drag, 0.0)] 
      #the numbers show how offset the items should be from each other

    def dragFunction(dragged_item, dropped_on):
      if dropped_on is not None:
        # if dragged is the same type or doesn't match print error
        if dragged_item[0].drag_name == dropped_on.drag_name:
            #dragged_item[0].droppable = False
            print("error")
        # if dragged is a different type and a correct match print correct
        if dragged_item[0].drag_name == "sound" and dropped_on.drag_name == "kana":
            dragged_item[0].snap(dropped_on.x, dropped_on.y, 0.5)
            match_drag = Drag(d=Solid("#80e5ff", xysize=(500,500)), drag_name = "match_drag", drag_raise = True, dragged= dragFunction, align=(0.9, 0.5))
            kana_draggroup.add(match_drag)
            kana_draggroup.remove(sound_drag)
            kana_draggroup.remove(kana_drag)
            print("correct")
            #figure out how to add new matches or call a new screen after a certain score

        #else print unknown error
        else:
            print("unknown error")


screen cards:
    image Solid("#ffffff")


    add kana_draggroup

define sound_drag = Drag(d=Solid("#ff9bf4", xysize=(250, 250)), drag_name = "sound",drag_raise = True, dragged = dragFunction, droppable = True, align = (0.3,0.5))
define kana_drag = Drag(d=Solid("#ff9b33", xysize=(250, 250)), drag_name = "kana",drag_raise = True, dragged = dragFunction, droppable = True, align = (0.5,0.5))
define test_drag = Drag(d=Solid("#ff9b33", xysize=(250, 250)), drag_name = "test",drag_raise = True, drop_allowable=drop_control, dragged = dragFunction, droppable = True, align = (0.7,0.5))
define kana_draggroup = DragGroup(sound_drag,kana_drag,test_drag)

define config.longpress_duration = 0.5



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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"


    call screen cards

    #speech bubble test
    define l = Character(None, image="lucy", kind=bubble)
    l "Here's a speech bubble."

    # This ends the game.

    return
