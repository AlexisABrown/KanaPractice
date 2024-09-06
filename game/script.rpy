# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
  import time
   # timeout variable can be omitted, if you use specific value in the while condition
  timeout = 15 #seconds
  timeout_start = time.time()
  #figure out how to import time into the init block
  #FIX: how to add print statements to in game dialogue box
  #Create arrays and have the numbers match up for value checking


  def drop_control(current_drag, dragged_item): #this may interfere with other drag properties such as drag_joined
      #print(f"current_drag={current_drag.drag_name}, dragged_item={dragged_item[0].drag_name}")
      return

  def dragFunction(dragged_item, dropped_on):

      global card_level
      card_level = 0
      level_array = ["test1","test2"]

      while time.time() < timeout_start + timeout:
       if dropped_on is not None:
        # if dragged is the same type or doesn't match print error
        # if dragged is a different type and a correct match print correct
          if dragged_item[0].drag_name == "sound" and dropped_on.drag_name == "kana":
            dragged_item[0].snap(dropped_on.x, dropped_on.y, 0.5)
            match_drag = Drag(d=Solid("#80e5ff", xysize=(500,500)), drag_name = "match_drag", drag_raise = False, dragged= dragFunction, align=(0.9, 0.5))
            kana_draggroup.add(match_drag)
            kana_draggroup.add(sound_drag)
            kana_draggroup.add(kana_drag)
            print(time)
      
            #make match drags appear at a random spot each time
            #kana_draggroup.remove(sound_drag)
            #kana_draggroup.remove(kana_drag)
      
              #if card_level < 2: #change to end of timer. when timer is done matches have to be a certain height. award extra points for reaching larger heights 
                #renpy.jump(level_array[card_level])
                #card_level += card_level
                #move to next label after this
                #renpy.jump(start)

        #else print unknown error
          else:
            print("unknown error")
       card_level = 1
       renpy.jump(level_array[card_level])



screen cards:
    image Solid("#ffffff")


    add kana_draggroup

define sound_drag = Drag(d=Solid("#ff9bf4", xysize=(250, 250)), drag_name = "sound",drag_raise = True, dragged = dragFunction, droppable = True, align = (0.3,0.5))
define kana_drag = Drag(d=Solid("#ff9b33", xysize=(250, 250)), drag_name = "kana",drag_raise = True, dragged = dragFunction, droppable = True, align = (0.5,0.5))
define test_drag = Drag(d=Solid("#33ff9b", xysize=(250, 250)), drag_name = "test",drag_raise = True, drop_allowable=drop_control, dragged = dragFunction, droppable = True, align = (0.7,0.5))
define kana_draggroup = DragGroup(sound_drag,kana_drag, test_drag)

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

    # This ends the game.

    return
