Make sure the images match the dialogue (check image name for reference)

Make sure that the order of the images are maintained properly

Do not edit or remove any dialogues except adding the images

Images without a dilogaue needs a `pause` after it

This is an example of previous part of a scene. Use this as the template for how the images go with the dialogues -

```
    scene sm1ms029-21 mc-aight-sure-got-invitation-mc-sy-they-start-ariving-soon_c1 with Fade(0.5, 0.5, 0.5)
    mc "All right, and you sure everyone got the invite?"
    scene sm1ms029-21 mc-aight-sure-got-invitation-mc-sy-they-start-ariving-soon_c1 with dissolve
    sy "Uh huh! They'll start arriving any second."
    # mc smiles at sy
    scene sm1ms029-22 mc-wow-sy-what_c1 with dissolve
    mc "Wow..."
    sy "Wow what?"
    scene sm1ms029-23 mc-never-thought-hosting-own-fl-party_c1 with dissolve
    mc "I just... never thought I'd be hosting my own Fetish Locator party."
    # sy hands on hips
    scene sm1ms029-24 sy-well-you-no-mc-but_c1 with dissolve
    sy "Well, you're not now, [mcname]."
    mc "But-"
    scene sm1ms029-25 sy-but-nothing-this-sm-party_c1 with dissolve
    sy "But nothing! This is a S&M Studio party. Not an FL party."
    # mc rolling his eyes
    scene sm1ms029-26 mc-semantics-what-trying-say-is_c1 with dissolve
    mc "Semantics. What I'm trying to say is..."
    # mc grabs sy's hands
    scene sm1ms029-27 mc-grabs-hands-things-really-changed-standing-beautiful-studio_c1 with dissolve
    mc "Things have really changed, and I think for the better."
    mc "Here I am, standing in our beautifully remodeled studio apartment."
    scene sm1ms029-28 mc-with-beautiful-stacy_c1 with dissolve
    if persistent.is_special:
        mc "With my amazing sister."
    else:
        mc "With my incredible girlfriend."
    scene sm1ms029-29 mc-have-kink-party-launch-porn-studio-how-things-get-better_c1 with dissolve
    mc "About to have a kink party to celebrate launching our porn studio."
    mc "How could things be any better?"
    # sy smirks
    scene sm1ms029-30 sy-smirks-better-careful-get-sentimental-mc-nah-romantic_c1 with dissolve
    sy "Better be careful, [mcname]. Talking like that, I'll think you're getting sentimental on me."
    mc "Nah, I'm just a romantic."
    scene sm1ms029-31 sy-maybe-classic-setup-to-push-new-heights_c1 with dissolve
    sy "Or maybe, this is the classic setup for the next chapter? Some epic villain or downfall before us?"
    sy "Something to push us to new heights, through more difficult challenges?"
    # mc smirks
    scene sm1ms029-32 mc-nah-overthinking-just-kiss-me-sy-whatever-say_c1 with dissolve
    mc "Nah, you're overthinking it. Just, kiss me, Stacy."
    sy "Whatever you say, [mcname]."
    scene sm1ms029-33 mc-sy-kiss_c1 with dissolve
    pause
    # sy and mc kiss
    scene sm1ms029-34 mc-sy-start-kissing-passionately_c1 with dissolve
    pause
    # sy and mc start to kiss more passionately
    scene sm1ms029-35 sy-notices-kv-offcam-ahem_c1 with dissolve
    "*door opens*"
    kv "Ahem."
    # sy and mc turn, and kv is standing in the door
    kv "Didn't realize the party was starting early."
    scene sm1ms029-36 kv-not-realize-party-start-sooner-sy-ofc-it-is_c1 with dissolve
    sy "Of course it is!"
    # sy picks up a mask
    scene sm1ms029-37 you-just-time-join-us_c1 with dissolve
    sy "And you're just in time to join us!"
    # sy passes the mask to kv
    scene sm1ms029-38 kv-thank-god-itching-fun_c1 with dissolve
    kv "Thank God. I've been itching for a little bit of fun."
    # kv starts walking in
    if _sm1mc029_kv_available:
        scene sm1ms029-41 kv-kisses-mc_c1 with dissolve
        # kv kisses mc
        # kv leans back, smirking
        scene sm1ms029-42 kv-back-mm-deff-itching-fun_c1 with dissolve
        kv "Mmmmm. Definitely been itching for some fun."
        menu:
            "Tell Kanya to offer Stacy a kiss" (hint = "sm1ms029_m01_h01"):
                scene sm1ms029-44 choice-offer-kiss-stacy-mc-know-who-else-looking-kiss_c1 with dissolve
                mc "You know who else is looking for some fun?"
                # kv and mc both look over at sy
                scene sm1ms029-45 kv-kv-look-sy-what-kv-think-right-mc_c1 with dissolve
                sy "What?"
                scene sm1ms029-46 kv-goes-sy-what-going-on-kv_c1 with dissolve
                kv "Mmmm, I think you're right, [mcname]."
                # kv walks over to sy
                sy "What's going on, Kanya?"
                # kv kisses sy
                # kv steps back, smiling
                scene sm1ms029-48 kv-tonight-be-lot-fun-sy-oh-yes-it-is_c1 with dissolve
                kv "Tonight is going to be a lot of fun!"
                sy "Oh yes, yes it is."

            "Thank her for the kiss" (hint = "sm1ms029_m01_h02"):
                scene sm1ms029-49 choice-thank-her-mc-mm-be-fun-kv-yes-yes-it-is_c1 with dissolve
                mc "Mmmm, tonight is definitely going to be a lot of fun."
                kv "Yes, yes it is."
                scene sm1ms029-50 kv-walk-inside-studio_c1 with dissolve
                # kv walks into the studio

    # sy smiling at mc
    scene sm1ms029-51 sy-see-told-ya-mc-yes-yes_c1 with dissolve
    sy "See? Told ya'!"
    mc "Yes, yes."
    scene sm1ms029-52 sy-smug-when-going-listen-hm_c1 with dissolve
    # sy hands on her hips, looking smug
    if persistent.is_special:
        sy "When are you going to learn to listen to your sister? Hmmm?"
    else:
        sy "When are you going to learn to listen to me? Hmmm?"
    scene sm1ms029-53 mc-know-know-eventually-learn-lesson_c1 with dissolve
    # mc puts his hands up
    mc "I know, I know."
    mc "I will eventually learn my lesson."
    scene sm1ms029-54 sy-excited-arj-ofcamm-surprise-two-arguing_c1 with dissolve
    pause
    scene sm1ms029-55 arj-reveal_c1 with dissolve
    arj "Surprise, surprise, Stacy and [mcname] bickering."
    # sy and mc turning, sy looking excited
    scene sm1ms029-56 sy-excited-amrose-you-made-arj-how-could-resist_c1 with dissolve
    sy "AmRose! You made it!"
    arj "How could I resist the inagural S&M Studio party?"
    scene sm1ms029-57 sy-turns-mc-sy-see-amrose-gets-it-mc-hey-arj-happy-made-it_c1 with dissolve
    # sy looking at mc
    sy "See! AmRose gets it!"
    mc "Hey, AmRose. Happy you made it."
    scene sm1ms029-58 arj-smiling-hey-mcname_c1 with dissolve
    # arj smiling
    arj "Thanks, [mcname]."
    # sy holds up a mask for arj
    scene sm1ms029-59 sy-hands-mask-your-mask-cant-forget-mask-arj-aah-yes-mask_c1 with dissolve
    sy "And your mask! Can't forget your mask!"
    arj "Ahh, yes. How could I forget about the masks."
    # sy and mc looking at arj, arj back to camera, "putting on mask"
    scene sm1ms029-60 sy-loved-masks-old-parties-thought-bring-back-mc-they-add-whimsy_c1 with dissolve
    sy "I loved the masks from the old parties, so I thought I'd bring them back!"
    mc "They did add a level of whimsy and mystery to the parties that was a lot of fun."
    scene sm1ms029-61 arj-whimsy-hell-way-describe-parties_c1 with dissolve
    arj "\"Whimsy and fun\" is a hell of a way to describe those parties."
    # arj standing there, mask on, looking at mc and sy
    scene sm1ms029-62 arj-how-do-look-sy-banging_c1 with dissolve
    arj "How do I look?"
    scene sm1ms029-63 mc-look-great-arj-thanks-mc-walks-up-to-him_c1 with dissolve
    sy "Banging!"
    mc "You look great, AmRose."
    # arj smiling
    arj "Thanks, [mcname]."
    scene sm1ms029-64 arj-kisses-mc_c1 with dissolve
    pause
```
