#see if python functions from script file can be reused here
init python:
    print("vowel file")

define e = Character("Eileen") 

label vowel_intro:
    e "We'll start with learning vowel sounds."
    #play sound at each pronunciation example 
    e "Say ah for a. And oh for o."
    e "E is pronounced "

    call screen cards

    return 