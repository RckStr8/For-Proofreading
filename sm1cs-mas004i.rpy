label sm1cs_mas004i:

    $ LocationController.draw_current_location("ms")
    show expression cc.get_expression_image("ms", "neutral01") as lst_ms_neutral01
    ms "Hey."
    mc "Hey, Maya."
    hide lst_ms_neutral01
    show expression cc.get_expression_image("ms", "serious01") as lst_ms_serious01
    ms "Nelson wants to talk to us. Something about a doctor's appointment."
    mc "That sounds ominous."
    ms "*shrugs*"

    $ StoryController.end_scene_in_time(MAS_STORY)
    return
