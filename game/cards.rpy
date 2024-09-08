init python:
  import time
  import datetime
  
  #figure out how to import time into the init block
  #FIX: how to add print statements to in game dialogue box
  #Create arrays and have the numbers match up for value checking

  # Create class that acts as a countdown
  def countdown(seconds):
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")

  def drop_control(current_drag, dragged_item): #this may interfere with other drag properties such as drag_joined
      print(f"current_drag={current_drag.drag_name}, dragged_item={dragged_item[0].drag_name}")

  def scoring(card_level):
      level_array = ["test1","test2"]
      card_level = card_level + 1
      renpy.jump(level_array[card_level])

  def check_for_match(dragged_item, dropped_on):
     # timeout variable can be omitted, if you use specific value in the while condition
     #timeout = 15 #seconds
     #timeout_start = time.time()
     #print(timeout)
     #while time.time() < timeout_start + timeout:
       if dropped_on is not None:
        # if dragged is the same type or doesn't match print error
        # if dragged is a different type and a correct match print correct
          if dragged_item[0].drag_name == "sound" and dropped_on.drag_name == "kana":
            dragged_item[0].snap(dropped_on.x, dropped_on.y, 0.5)
            kana_draggroup.remove(dragged_item[0])
            kana_draggroup.remove(dropped_on)
            match_drag = Drag(d=Solid("#80e5ff", xysize=(500,500)), drag_name = "match_drag", drag_raise = False, dragged= dragFunction, align=(0.9, 0.5))
            kana_draggroup.add(match_drag)
            kana_draggroup.add(sound_drag)
            kana_draggroup.add(kana_drag)
      
              #if card_level < 2: #change to end of timer. when timer is done matches have to be a certain height. award extra points for reaching larger heights 
                #renpy.jump(level_array[card_level])
                #card_level += card_level
                #move to next label after this
                #renpy.jump(start)

        #else print unknown error
          else:
            print("unknown error")
       countdown(10)

  def dragFunction(dragged_item, dropped_on):
      global card_level
      card_level = 0
      check_for_match(dragged_item, dropped_on)



screen cards:
    image Solid("#ffffff")


    add kana_draggroup

define sound_drag = Drag(d=Solid("#ff9bf4", xysize=(250, 250)), drag_name = "sound",drag_raise = True, dragged = dragFunction, droppable = True, align = (0.3,0.5))
define kana_drag = Drag(d=Solid("#ff9b33", xysize=(250, 250)), drag_name = "kana",drag_raise = True, dragged = dragFunction, droppable = True, align = (0.5,0.5))
define test_drag = Drag(d=Solid("#33ff9b", xysize=(250, 250)), drag_name = "test",drag_raise = True, drop_allowable=drop_control, dragged = dragFunction, droppable = True, align = (0.7,0.5))
define kana_draggroup = DragGroup(sound_drag,kana_drag, test_drag)

define config.longpress_duration = 0.5

#Card Sets refrence: https://www.tofugu.com/japanese/learn-hiragana/
#vowels
#k sounds
#s sounds
#t sounds
#n sounds
#h sounds
#m sounds
#y sounds
#r sounds
#w sounds
#Dakuten 
#Han-Dakuten
#combination hirigana 