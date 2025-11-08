label sm1cs_bg005:

    # Starts with an interaction in the studio with BG
    # Scene starts with KV telling BG and MC she has to run out, and to watch over the photo dojo while she's gone

    # Kanya sees MC and Amore talking. She has a camera in hand.
    scene sm1cs-bg005-01 kv-mc-bg-talking_c1 with dissolve
    pause
    scene sm1cs-bg005-01 kv-mc-bg-talking_c2 with dissolve
    kv "Oh, hey you two. Perfect timing actually."
    scene sm1cs-bg005-02 kv-mc-talking_c1 with dissolve
    mc "Yeah?"
    #kv holds her thumb up behind her
    scene sm1cs-bg005-02 kv-mc-talking_c2 with dissolve
    kv "I've got to run across town to pick up a lens I ordered. Be back in an hour or so."
    # Kanya starts packing her bag.
    scene sm1cs-bg005-03 kv-bg-taking-her-backpack_c1 with dissolve
    kv "You two can hold down the fort, right?"
    #bg looks at mc
    scene sm1cs-bg005-03 kv-bg-taking-her-backpack_c2 with dissolve
    bg "..."
    #bg talking
    scene sm1cs-bg005-04 kv-bg-talking_c1 with dissolve
    bg "We'll be fine."
    # Kanya gives MC a knowing look and grins.
    scene sm1cs-bg005-04 kv-bg-talking_c2 with dissolve
    kv "Try not to break anything. Or each other."
    #mc goofy grin
    scene sm1cs-bg005-05 kv-mc-talking_c1 with dissolve
    mc "We'll do our best."
    scene sm1cs-bg005-05 kv-mc-talking_c2 with dissolve
    kv "That's what I'm afraid of."
    # Kanya leaves. The door clicks shut. Silence.
    scene sm1cs-bg005-06 mc-bg-talking_c1 with dissolve
    "*click*"
    #bg gives mc an awkward look
    bg "So..."
    scene sm1cs-bg005-06 mc-bg-talking_c2 with dissolve
    mc "So."
    #bg smiles trying to change subject
    scene sm1cs-bg005-07 mc-bg-talking_c1 with dissolve
    bg "The shoot was really good, right? I mean, I think we got some incredible—"
    scene sm1cs-bg005-07 mc-bg-talking_c2 with dissolve
    mc "Amore."
    bg "—shots, and Kanya's editing is always—"
    #mc holds up a hand
    scene sm1cs-bg005-08 mc-bg-talking_c1 with dissolve
    mc "Stop."
    # Amore fidgets with her costume.
    scene sm1cs-bg005-08 mc-bg-talking_c2 with dissolve
    bg "Stop what?"
    #mc is not angry - but he wants to talk about something and she keeps avoiding it
    scene sm1cs-bg005-09 mc-grinning_c1 with dissolve
    mc "Deflecting. We both know that's not what we're talking about."
    scene sm1cs-bg005-10 mc-bg-talking_c1 with dissolve
    bg "Mmm. I don't know what you mean."
    #mc grinning - self confident
    scene sm1cs-bg005-10 mc-bg-talking_c2 with dissolve
    mc "How about we start with me making you cum so hard you couldn't form sentences."
    mc "Or we can go into how you bolted right after. Acting like the studio was on fire."
    # Amore's shoulders tense - she looks to the side
    scene sm1cs-bg005-11 bg-nervous_c1 with dissolve
    bg "I just... I had somewhere to be."
    scene sm1cs-bg005-12 mc-worried_c1 with dissolve
    mc "Twice now, we hook up, have great sex. And then you run off."
    #bg looks nervous
    scene sm1cs-bg005-13 mc-bg-talking_c1 with dissolve
    bg "I don't—"
    scene sm1cs-bg005-13 mc-bg-talking_c2 with dissolve
    mc "Yes, you do."
    menu:
        "I'm worried about you" (hint="sm1cs_bg005_m01_h01"):
            $ player.set_choice("sm1cs_bg005_worried_about_bg")
            $ CharacterController.get_character("bg").add_point(2)
            scene sm1cs-bg005-14 mc-talking_c1 with dissolve
            mc "Hey. I'm not mad, Amore. I'm worried."
            #mc is worried about her
            mc "You seemed overwhelmed. Did I push too far? Did I do something wrong?"
            # Amore's defensive posture softens slightly.
            scene sm1cs-bg005-15 mc-bg-looking-down_c1 with dissolve
            bg "No! God, no. You did nothing wrong."
            bg "The sex was great."
            #mc is confused
            scene sm1cs-bg005-15 mc-bg-looking-down_c2 with dissolve
            mc "Then talk to me. What's going on?"
            scene sm1cs-bg005-15 mc-bg-looking-down_c1 with dissolve

        "We need to communicate" (hint="sm1cs_bg005_m01_h02"):
            $ player.set_choice("sm1cs_bg005_need_communicate")
            $ CharacterController.get_character("bg").add_point(1)
            #mc talking to Amore
            scene sm1cs-bg005-15 mc-bg-looking-down_c2 with dissolve
            mc "If we're going to keep hooking up, shouldn't we be able to have a normal conversation about it?"
            mc "No more disappearing acts. That's not how this works."
            # Amore looks down, guilt written across her body language.
            scene sm1cs-bg005-15 mc-bg-looking-down_c1 with dissolve
            bg "You're right. I'm sorry."
            scene sm1cs-bg005-14 mc-talking_c1 with dissolve
            mc "I don't need you to apologize."
            #mc looking caring
            mc "I just want to know what's going on."
            scene sm1cs-bg005-15 mc-bg-looking-down_c1 with dissolve

        "Can't handle me?" (hint="sm1cs_bg005_m01_h03"):
            $ player.set_choice("sm1cs_bg005_tease_bg")
            #mc expression - dumb himbo
            scene sm1cs-bg005-14 mc-talking_c1 with dissolve
            mc "What, one night with me and you're already scared?"
            mc "Too much for you to handle?"
            # Amore bristles.
            scene sm1cs-bg005-13 mc-bg-talking_c1 with dissolve
            bg "*scoff* I don't scare easily."
            #mc isn't sold on that
            scene sm1cs-bg005-16 mc-dumb_c1 with dissolve
            mc "Really? Because it sure looks like it from here."
            scene sm1cs-bg005-15 mc-bg-looking-down_c1 with dissolve
            bg "I'm not—"
            # She stops, deflating.
            bg "...Okay, maybe I am. A little."

    bg "It's just..."
    mc "Just what?"
    scene sm1cs-bg005-17 mc-bg-talking-cold_c2 with dissolve
    bg "This is...{w} God, this is embarrassing."
    mc "Try me."
    # Amore takes a shaky breath.
    scene sm1cs-bg005-18 bg-deflating_c1 with dissolve
    bg "This is my first time."
    #mc doesn't understand
    scene sm1cs-bg005-19 mc-bg-talking_c2 with dissolve
    mc "Your... your first time doing anal? I kind of figured—"
    scene sm1cs-bg005-19 mc-bg-talking_c1 with dissolve
    bg "No.{w} I mean, yes.{w} But that's not—"
    # She gestures helplessly.
    bg "Hooking up with you is my first time like... trying out this kink."
    #mc not understanding - bg talking
    scene sm1cs-bg005-20 mc-bg-admitting_c2 with dissolve
    mc "...What?"
    scene sm1cs-bg005-21 mc-bg-pointing-out_c1 with dissolve
    bg "All of this. The Dom-Sub play. The BDSM. The... {w}everything."
    #mc didn't expect that
    scene sm1cs-bg005-21 mc-bg-pointing-out_c2 with dissolve
    mc "Huh?"
    mc "But you're so confident, Amore. The way you talk, the way you—"
    #bg kind of smiles
    scene sm1cs-bg005-22 mc-bg-smiling_c1 with dissolve
    bg "I guess that means I'm a good actress. Or it's just your fantasy helping me sell it."
    # Amore starts pacing.
    bg "I've spent years imagining this. Reading about it, watching it, buying the parts of my outfit."
    bg "I've done solo shoots where I could pretend, where I could let this side of me show."
    #amore stroking her thighs with her hands
    scene sm1cs-bg005-24 bg-talking_c1 with dissolve
    bg "And play out the scenarios I imagined back in college."
    bg "But it was always just me."
    #bg running her hands up her body
    scene sm1cs-bg005-25 bg-talking_c1 with dissolve
    bg "*moans* Alone. Just touching myself."
    bg "It was exciting, and the photoshoots helped pay some bills."
    #mc thinks he understands
    scene sm1cs-bg005-25 bg-talking_c2 with dissolve
    mc "But it was only part of the fantasy..."
    #bg faces him
    scene sm1cs-bg005-26 bg-talking_c1 with dissolve
    bg "*low breathing* And now it's so much more."
    #bg's hand raises to her mask
    scene sm1cs-bg005-27 bg-talking_c1 with dissolve
    bg "I wasn't just putting a mask on anymore."
    bg "It was like... I was finally fully stepping into a new body. Being a different person than I normally am."
    #bc thinking of how good it makes her feel - light breathing - horny
    bg "..."
    #mc thinking she is about to kiss him
    #bc is uncertain again
    scene sm1cs-bg005-28 mc-bg-talking_c1 with dissolve
    bg "And that's... {w}terrifying to me."
    #mc is curious
    scene sm1cs-bg005-29 mc-bg-talking_c2 with dissolve
    mc "Why?"
    bg "Because of... how you make me feel when we're together."
    mc "I'm not sure that's a reason to be terrified."
    #bg holding her hands together - down below her belly - head down a bit
    scene sm1cs-bg005-30 bg-looking-down_c1 with dissolve
    bg "You fell into the role so easily."
    bg "But you also made it feel..."
    bg "Like it was the most normal thing in the world. For us to have sex together."
    #bg's eyes go up to look at him
    scene sm1cs-bg005-31 bg-looking-at-him_c1 with dissolve
    bg "For us to play these roles."
    # Amore wraps her arms around herself.
    scene sm1cs-bg005-32 mc-bg-talking_c1 with dissolve
    bg "Doing this... it's one of the few {b}good{/b} things I have in life."
    bg "And I'm scared I'm going to ruin it."
    #mc doesn't understand
    scene sm1cs-bg005-32 mc-bg-talking_c2 with dissolve
    mc "How would you ruin it?"
    scene sm1cs-bg005-33 bg-upset_c1 with dissolve
    bg "By not being good enough. By doing something {b}wrong{/b}."
    #bg fears rejection
    bg "By being too much, or not enough, or—"
    scene sm1cs-bg005-34 mc-bg-talking-closer_c1 with dissolve
    mc "Amore."
    #bg looking at him
    bg "I could ask something. And it might scare you away, [mcname]."
    mc "Stop."
    # MC steps closer to her.
    scene sm1cs-bg005-34 mc-bg-talking-closer_c2 with dissolve
    mc "You've been incredible.{w} There's no \"perfect\" way to do this."
    mc "If things feel like too much, we slow down. Or stop. No judgment."
    #bg making sure he is being serious
    scene sm1cs-bg005-34 mc-bg-talking-closer_c3 with dissolve
    bg "Really?"
    mc "Really."
    # Amore relaxes slightly.
    scene sm1cs-bg005-35 bg-talking_c1 with dissolve
    bg "That's... {w}thank you, [mcname]."
    mc "Can I ask you something?"
    bg "Yeah?"
    mc "Is there a reason we did anal, last time?"
    # Amore's whole body tenses with embarrassment and she closes her eyes.
    # Amore's whole body tenses with embarrassment and she closes her eyes.
    scene sm1cs-bg005-36 mc-bg-talking_c1 with dissolve
    bg "Oh God."
    scene sm1cs-bg005-36 mc-bg-talking_c2 with dissolve
    mc "You don't have to answer if—"
    scene sm1cs-bg005-37 bg-talking_c1 with dissolve
    bg "No, it's...{w} it's a fair question."
    # She takes a breath.
    bg "It felt safer. Less real, somehow."
    bg "Like it was still part of the fantasy. Still just...play."
    menu:
        "I could play with your pussy" (hint="sm1cs_bg005_m02_h01"):
            $ player.set_choice("sm1cs_bg005_play_with_pussy")
            scene sm1cs-bg005-38 mc-bg-we-could-play-puss_c1 with dissolve
            mc "I could play with your pussy."
            mc "Make it feel as good as your ass did."
            #bg gives him a knowing look
            scene sm1cs-bg005-38 mc-bg-we-could-play-puss_c2 with dissolve
            bg "I know you could."

        "I don't understand" (hint="sm1cs_bg005_m02_h02"):
            $ player.set_choice("sm1cs_bg005_dont_understand")

    #bg sighing a bit - she is holding off on vaginal sex
    scene sm1cs-bg005-39 mc-bg-sighing_c1 with dissolve
    bg "I guess you'd call it an issue of degrees of intimacy."
    bg "If you were to be technical."
    #mc asking for the non-technical answer
    scene sm1cs-bg005-39 mc-bg-sighing_c2 with dissolve
    mc "I didn't study relationships in college."
    #bg speaking
    scene sm1cs-bg005-40 bg-talking_c1 with dissolve
    bg "Vaginal sex with someone..."
    bg "It means something special to me."
    #bg touching his chest - sexy - but not like super sexy - little teasing of the player
    scene sm1cs-bg005-41 mc-bg-chesty_c1 with dissolve
    bg "When I let you inside of me... we'd be connected in a way I can't take back."
    # MC nods slowly.
    scene sm1cs-bg005-41 mc-bg-chesty_c2 with dissolve
    mc "I get it. We don't do anything until you're ready."
    #bg giving him a hard truth
    scene sm1cs-bg005-42 mc-bg-talking_c1 with dissolve
    bg "And if I'm never ready to do that? If I just want to keep some things..."
    bg "For me."
    #mc accepts it
    #mc speaking
    scene sm1cs-bg005-42 mc-bg-talking_c2 with dissolve
    mc "And now my watch begins."
    #bg grins
    scene sm1cs-bg005-43 mc-bg-talking_c1 with dissolve
    bg "Hahaha."
    #bg talking
    bg "There is no way in the Seven Hells you'd go celibate, [mcname]."
    #mc holding up a finger
    scene sm1cs-bg005-43 mc-bg-talking_c2 with dissolve
    mc "Hey, the Night's Watch's oath says no lands or children."
    mc "Not no 'sex'."
    #bg smiling
    scene sm1cs-bg005-44 mc-bg-smiling_c1 with dissolve
    bg "Touché."
    #bg looks glad that he is not disappointed
    bg "You're not...disappointed?"
    scene sm1cs-bg005-44 mc-bg-smiling_c2 with dissolve
    mc "Not even a little."
    bg "You are something special."
    #mc gestures toward her
    mc "All credit to the people around me. They lift me up."
    # Amore laughs, some of the tension breaking.
    scene sm1cs-bg005-45 bg-surprised_c1 with dissolve
    bg "Hahah."
    #mc thinking
    scene sm1cs-bg005-46 mc-gesturing_c1 with dissolve
    mc "I do think that if we're going to keep hooking up, here or..."
    mc "Wherever...{w} we need some ground rules."
    #bg asking a question
    scene sm1cs-bg005-47 mc-bg-thinking_c1 with dissolve
    bg "Of course. What do you suggest, [bg_mcname!t]?"
    scene sm1cs-bg005-48 mc-bg-talking_c1 with dissolve
    mc "First, words to help control the flow."
    mc "Like safewords, but more technical."
    scene sm1cs-bg005-48 mc-bg-talking_c2 with dissolve
    bg "Go on."
    # MC counts on his fingers.
    scene sm1cs-bg005-49 mc-bg-counting_c1 with dissolve
    mc "Green means everything's good, keep going."
    mc "Yellow means slow down, check in, something's off."
    mc "Red means full stop. Scene over. No questions, no hesitation."
    bg "I like that. It's clear."
    mc "Exactly."
    # Amore fidgets with her hands.
    scene sm1cs-bg005-48 mc-bg-talking_c2 with dissolve
    bg "Can I...{w} can I ask for something else?"
    mc "Of course."
    bg "What about aftercare?"
    #bg nervously touches the side of her mask
    scene sm1cs-bg005-43 mc-bg-talking_c2 with dissolve
    mc "Aftercare?"
    scene sm1cs-bg005-43 mc-bg-talking_c1 with dissolve
    bg "After we're together...{w} I think I'll need...{w} I'll need to come back down."
    bg "To be held, or...{w} I don't know. To remember I'm still me."
    scene sm1cs-bg005-39 mc-bg-sighing_c2 with dissolve
    menu:
        "What do you need from me?" (hint="sm1cs_bg005_m03_h01"):
            $ player.set_choice("sm1cs_bg005_aftercare_humor")
            $ CharacterController.get_character("bg").add_point(2)
            mc "Okay. Walk me through it."
            mc "Cuddling? A glass of water? Me telling you how perfect you are?"
            scene sm1cs-bg005-38 mc-bg-we-could-play-puss_c2 with dissolve
            # Amore's laugh is breathy.
            bg "Probably nothing. But maybe... sometimes..."
            bg "All of the above?"
            #mc smiling
            scene sm1cs-bg005-38 mc-bg-we-could-play-puss_c1 with dissolve
            mc "I can manage that."
            mc "Though fair warning, the praise might get excessive."
            scene sm1cs-bg005-37 bg-talking_c1 with dissolve
            bg "I think I can handle it."
            #mc talking to her and she blushes
            scene sm1cs-bg005-36 mc-bg-talking_c2 with dissolve
            mc "Can you though? Because I've got a lot of material."
            mc "Your dedication. Your trust. That thing you do with your tongue—"
            scene sm1cs-bg005-36 mc-bg-talking_c1 with vpunch
            bg "[mcname]!"
            #big grin on mc
            scene sm1cs-bg005-25 bg-talking_c2 with dissolve
            mc "Already blushing and we haven't even started."
            # Amore covers her face with her hands.
            scene sm1cs-bg005-36 mc-bg-talking_c1 with dissolve
            bg "You're terrible."
            mc "You love it."
            bg "Shut up.{w} Hehehe."

        "I'll take care of you" (hint="sm1cs_bg005_m03_h02"):
            $ player.set_choice("sm1cs_bg005_aftercare_firm")
            $ CharacterController.get_character("bg").add_point(1)
            mc "Don't worry. After any hookup, I'll make sure you're okay."
            mc "That's my job as your [bg_mcname!t]."
            # Amore's breath catches.
            scene sm1cs-bg005-40 bg-talking_c1 with dissolve
            bg "Your job?"
            scene sm1cs-bg005-36 mc-bg-talking_c2 with dissolve
            mc "Part of being a Dom is taking care of my Sub. Especially after intense scenes."
            mc "You give yourself to me. If I can't make you feel safe and comfortable after, I'd be a pretty terrible Dom."
            # Her voice comes out small.
            scene sm1cs-bg005-37 bg-talking_c1 with dissolve
            bg "I...{w} thank you."
            mc "No need to thank me. It's not optional."

    scene sm1cs-bg005-34 mc-bg-talking-closer_c2 with dissolve
    mc "One more rule. This one's mine."
    #bg is cautious
    scene sm1cs-bg005-34 mc-bg-talking-closer_c3 with dissolve
    bg "..."
    #bg talking
    bg "Okay. What is it?"
    scene sm1cs-bg005-43 mc-bg-talking_c2 with dissolve
    mc "No more running away."
    #mc saying if they have sex, they should hang out after
    mc "If we smash booties... if we hook up, we'll stay together and check in on each other."
    mc "No running away. Unless the building is literally on fire."
    #mc is like - then move your ass
    mc "Then run like crazy."
    mc "Even if it's just sitting in silence...{w} I think I'd like that better than you fleeing."
    # Amore's eyes look suspiciously bright behind her mask.
    scene sm1cs-bg005-44 mc-bg-smiling_c1 with dissolve
    bg "I can do that."
    scene sm1cs-bg005-44 mc-bg-smiling_c2 with dissolve
    mc "Good."
    # MC takes a step closer.
    scene sm1cs-bg005-42 mc-bg-talking_c2 with dissolve
    mc "So. We're really doing this."
    mc "For us to be in a real Dom/Sub relationship?"
    mc "Not just for photos. Not just fantasy. For real."
    # Amore's entire demeanor transforms. Her anxiety melts into pure joy.
    scene sm1cs-bg005-42 mc-bg-talking_c1 with dissolve
    bg "Well... it's still got a bit of fantasy involved. It's not like we can do this in broad daylight."
    #mc is like who says
    mc "Huh? Who says that?"
    #bg smiling
    bg "But there are laws. Conventions.{w} Common decency."
    #mc being a goofball
    scene sm1cs-bg005-39 mc-bg-sighing_c2 with dissolve
    mc "Those words are all foreign to me.{w} Especially the last one."
    #bg smiles
    bg "Haha."
    #mc being calm and serious
    mc "So... is that it? And you're not backing out?"
    #bg telling him she wants to do the dom/sub relationship
    scene sm1cs-bg005-38 mc-bg-we-could-play-puss_c2 with dissolve
    bg "Yes. {w} Absolutely yes. I want this. I want to do it with you [bg_mcname!t]."
    # MC pulls her into an embrace. She melts against him.
    bg "Thank you for not running away from me."
    scene sm1cs-bg005-12 mc-worried_c1 with dissolve
    mc "I was about to say the same thing, Amore."
    # They stay like that for a moment. Then Amore pulls back slightly.
    scene sm1cs-bg005-13 mc-bg-talking_c1 with dissolve
    bg "I have so many ideas. Things I've always wanted to try."
    bg "And now I can actually do them. With you."
    # She's practically bouncing.
    bg "This is going to be great, [bg_mcname!t].{w} The best submissive you've ever had."
    #mc looking abit horny - so is bg
    scene sm1cs-bg005-14 mc-talking_c1 with dissolve
    mc "I can't wait for our first session."
    #bg smiling
    scene sm1cs-bg005-01 kv-mc-bg-talking_c1 with dissolve
    bg "Me too."
    # The door opens. Kanya walks in carrying a camera bag.
    scene sm1cs-bg005-01 kv-mc-bg-talking_c2 with dissolve
    kv "Still in one piece, I see."
    scene sm1cs-bg005-02 kv-mc-talking_c1 with dissolve
    mc "Yup. All good. Better than good."
    #bg smirks
    #kv talks
    scene sm1cs-bg005-02 kv-mc-talking_c2 with dissolve
    kv "Ahhh..."
    #kv looks at mc
    #kv looks at bg
    #kv raises an eyebrow
    kv "Mmmm. I miss something?"
    #mc smiling
    #bg being a bit shy
    scene sm1cs-bg005-03 kv-bg-taking-her-backpack_c2 with dissolve
    pause
    scene sm1cs-bg005-04 kv-bg-talking_c1 with dissolve
    bg "No biggie."
    #kv doesn't believe her one bit
    scene sm1cs-bg005-03 kv-bg-taking-her-backpack_c1 with dissolve
    kv "Uh huh..."
    #kv puts down her bag
    kv "Well, I'll be around if you need me, lovebirds."
    #bg blushes and is acting surprised
    scene sm1cs-bg005-04 kv-bg-talking_c1 with dissolve
    bg "What?"
    #mc reating similar
    mc "Say whaaaaah?"
    #kv is grinning - not believing them
    scene sm1cs-bg005-02 kv-mc-talking_c2 with dissolve
    kv "Yeah, save it for the camera, hahaha."
    #kv checks her phone
    kv "Speaking of which, I think another client is coming."
    #kv playfully telling them to scram
    kv "So run along you two."
    #bg and mc moving - bg talking
    scene sm1cs-bg005-11 bg-nervous_c1 with dissolve
    bg "We will, but not because you told us, Kanya."
    kv "Haha."
    #bg looks at mc
    bg "I should probably get going, [mcname]."
    scene sm1cs-bg005-06 mc-bg-talking_c2 with dissolve
    mc "Yeah. Me too."
    scene sm1cs-bg005-06 mc-bg-talking_c1 with dissolve
    bg "But...{w} same time next week?"
    #mc likes the sound of that
    mc "Wouldn't miss it."
    bg "Good."
    # She stands on her toes and kisses his cheek.
    scene sm1cs-bg005-01 kv-mc-bg-talking_c1 with dissolve
    $ SMGallery.unlock_gallery_slot("achievement", "13_I_AM_THE_KINK")
    bg "See you soon, [bg_mcname!t]."
    mc "See you soon, Amore."
    #sexy shot of bg walking away

    $ StoryController.end_scene(BG_STORY)
    return
