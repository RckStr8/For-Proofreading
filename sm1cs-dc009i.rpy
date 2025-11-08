label sm1cs_dc009i:

    #interaction with dc in park
    #ONE DAY HAS PASSED SINCE dc008

    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "excited01") as lpa_dc_excited01
    dc "[mcname]! Hi!"
    mc "Hey, Debbie!"
    dc "What brings you to the park?"
    mc "I'll give you three guesses."
    dc "Hahahaha!"
    hide lpa_dc_excited01
    show expression cc.get_expression_image("dc", "smile01") as lpa_dc_smile01
    dc "But, what's gonig on?"
    hide lpa_dc_smile01
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious
    dc "Is there something you need to tell a police officer about?"
    mc "Nope, just something I need to tell Debbie."
    hide lpa_dc_serious
    show expression cc.get_expression_image("dc", "smile01") as lpa_dc_smile01
    dc "Oh yeah? And what's that?"
    mc "Well, I've been thinking about this next date of ours-"
    hide lpa_dc_smile01
    show expression cc.get_expression_image("dc", "excited01") as lpa_dc_excited01
    dc "Yeah!?"
    mc "And I think I have something figured-"
    dc "I get off in an hour!"
    dc "Want to meet here!?"
    mc "Sure, Debbie, that sounds great."
    dc "Awesome!! Yay, I'm looking forward to it!"
    hide lpa_dc_excited01
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious
    dc "But now I need to go and see if I can apprehend a bike thief."
    dc "I'll see you in a bit, [mcname]."
    mc "See you in a bit!"

    $ StoryController.end_scene(DC_STORY)
    return
