label sm1fs_t008i:

    # questlog - "You helped make a great show at the theater. You should talk to Denise on Thursday in the late afternoon and see how the reviews are."
    # interaction - Talk to Denise

    $ LocationController.draw_current_location("dvh")
    show expression cc.get_expression_image("dvh", "serious01") as lth_dvh_serious01
    mc "Hey, Denise."
    dvh "Hello, [mcname]."
    mc "So... any reviews yet for the show?"
    dvh "Nothing from the newspapers."
    dvh "A few online blogs and personal tidbits."
    hide lth_dvh_serious01
    show expression cc.get_expression_image("dvh", "smile01") as lth_dvh_smile01
    dvh "I would say that the audience enjoyed our take."
    dvh "As a matter of fact, I have something besides reviews I want to talk to you about."
    mc "Okay."
    hide lth_dvh_smile01
    show expression cc.get_expression_image("dvh", "ask01") as lth_dvh_ask01
    if curr_position == LTH_DIRECTORS_OFFICE:
        dvh "We should talk about your future with the theater group."
    else:
        dvh "Please. Come with me to my office."
        dvh "It's time we talked about your future with the theater group."
        mc "Sure."

    $ StoryController.end_scene(THEATER_STORY_LINE)
    return
