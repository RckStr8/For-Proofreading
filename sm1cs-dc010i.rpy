label sm1cs_dc010i:

    # TWO DAYS HAVE PASSED SINCE dc009
    # RENOVATION COMPLETE
    #interaction with debbie

    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "smile01") as lpa_dc_smile01
    dc "Hey, [mcname]!"
    mc "Hey, Debbie! I have a question for you."
    hide lpa_dc_smile01
    show expression cc.get_expression_image("dc", "nervous01") as lpa_dc_nervous01
    dc "Uhm, what's up?"
    mc "Do you want to go on another date tonight?"
    hide lpa_dc_nervous01
    show expression cc.get_expression_image("dc", "smile01") as lpa_dc_smile01
    dc "Oh my God, you had me worried there!"
    mc "What?"
    dc "You can't just tell a woman you have a question for her! I thought it was something serious!"
    mc "Hahahaha! But it is serious!"
    dc "Of course I would love to go on a date with you!"
    dc "What are you thinking?"
    mc "Well, there's this new action move-"
    hide lpa_dc_smile01
    show expression cc.get_expression_image("dc", "excited01") as lpa_dc_excited01
    dc "Yes! Sounds awesome! Yay!"
    dc "Meet you there at 7?"
    mc "Sounds great!"
    dc "Okay! I'll see you there! Yay!"

    $ StoryController.end_scene(DC_STORY)
    return
