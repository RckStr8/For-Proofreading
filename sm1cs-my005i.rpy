label sm1cs_my005i:

    # Talk to sy in afternoon in studio

    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "ask01") as lst_sy_ask01
    if persistent.is_special:
        sy "Have you talked to Mom since the swimsuit competition?"
    else:
        sy "Have you talked to Melony since the swimsuit competition?"
    mc "Uhm, no?"
    sy "I think you should."
    mc "Why?"
    hide lst_sy_ask01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    sy "Because she kind of sprinted out of here the other night and it was super weird?"
    mc "..."
    mc "You've got a good point there."

    $ StoryController.end_scene(MY_STORY)
    return
