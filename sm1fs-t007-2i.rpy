label sm1fs_t007_2i:

    #questlog - "Talk to Bruce to start the show on Saturday Evening"
    # Interaction with Bruce to start the show.

    $ LocationController.draw_current_location("sb")
    show expression cc.get_expression_image("sb", "neutral01") as lth_sb_neutral01
    sb "There you are. Big night. Opening night."
    sb "You ready for this?"
    menu:
        "I'm ready":
            mc "Ready as I'll ever be. Let's do this."
            hide lth_sb_neutral01
            show expression cc.get_expression_image("sb", "smile01") as lth_sb_smile01
            sb "That's what I like to hear."

        "A little nervous":
            mc "Honestly? I'm a little nervous. This is my first opening night."
            hide lth_sb_neutral01
            show expression cc.get_expression_image("sb", "smile01") as lth_sb_smile01
            sb "Good. Means you care. Just put those nerves to good use."

        "I was born ready":
            mc "Born ready, Bruce. I could run this show in my sleep."
            hide lth_sb_neutral01
            show expression cc.get_expression_image("sb", "smile01") as lth_sb_smile01
            sb "*chuckles* Let's hope it doesn't come to that."

    sb "Denise is counting on you tonight, and I need someone I can rely on."
    hide lth_sb_smile01
    show expression cc.get_expression_image("sb", "neutral01") as lth_sb_neutral01
    sb "The better you perform, the more responsibility—and pay—you'll get in the future."
    mc "Understood."
    sb "Alright. Get into your blacks and meet me backstage in five. We've got a show to run."

    $ StoryController.end_scene(THEATER_STORY_LINE)
    return
