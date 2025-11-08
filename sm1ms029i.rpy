label sm1mc029i:

    #FRIDAY OR SATURDAY AFTERNOON< INTERACTION WITH SY IN STUDIO

    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as sy_excited
    sy "Is it time!?"
    mc "Yeah, I think it's time for the launch party."
    sy "Eeeeee!"
    hide sy_excited
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    sy "Let me go get changed!"
    sy "And grab my mask!"
    sy "Make sure you grab your mask, [mcname]!"

    $ StoryController.end_scene(MS)
    return
