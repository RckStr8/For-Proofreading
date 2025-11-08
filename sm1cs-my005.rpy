label sm1cs_my005:

    scene sm1cs_my005-01 mc-walking-studio-holding-phone_c1 with dissolve
    pause
    scene sm1cs_my005-02 mct-what-hell-say-sorry-wierd-competition_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.8
    mct "What the hell am I even going to say..."
    mct "\"Sorry for the super weird swimsuit competition, and for making you moan, we all good?\""
    scene sm1cs_my005-03 mc-looking-window-silent_c1 with dissolve
    mc "..."
    scene sm1cs_my005-04 mc-staring-ceiling-mct-sometimes-stacy-helps-out-times-makes-things-worse_c1 with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Man, sometimes Stacy really helps me out."
    mct "And sometimes...{w} Well one way or another, it's my choice now."
    scene sm1cs_my005-05 mc-starring-phone-as-walking-mct-cmon-think_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "But what am I going to do. What am I going to say?"
    mc "..."
    scene sm1cs_my005-06 mc-got-idea-mct-wait-know-just-thing_c1 with dissolve
    play voice2 mc_surprised_huh5 noloop
    mct "Wait! I think I know just the thing!"
    scene sm1cs_my005-07 mc-writing-texting_c1 with dissolve
    pause
    scene sm1cs_my005-08 mct-yeah-that-work-mc-smiles-mct-perfect_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Yeah... that'll work! I'll tell her she won the movie date and have her come over..."
    mct "And she's in! Perfect."
    scene sm1cs_my005-09 mc-shouting-stacy-need-take-off-tonight-sy-offcam-why_c1 with dissolve
    play voice2 mc_znames_stacy2 noloop
    mc "Stacy! I need you to take off for the night!"
    play voice4 stacy_surprised_huh3 noloop
    sy "Why!?!"
    scene sm1cs_my005-10 mc-because-part-plan-sy-uuugh_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    if persistent.is_special:
        mc "Because I don't need you cramping my style when Mom gets here."
    else:
        mc "Because I don't need you cramping my style when Melony gets here."
    play voice4 stacy_angry_argh4 noloop
    sy "Uggggggghhhhhhh!"

    jump sm1cs_my005_later

label sm1cs_my005_later:

    scene black
    show screen scene_transition(_("A Few Hours Later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1cs_my005-11 hours-later-door-knocking_c1
    with Fade(0.5, 0.5, 0.5)
    "*KNOCK, KNOCK, KNOCK*"
label sm1cs_my005_replay hide:
    scene sm1cs_my005-12 mc-goes-open-door_c1 with dissolve
    pause
    scene sm1cs_my005-13 mc-opens-door-hey-melony-or-mom_c1 with dissolve
    pause
    scene sm1cs_my005-14 my-evening-mc_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    if persistent.is_special:
        mc "Hey, Mom!"
    else:
        mc "Hey, Melony!"
    scene sm1cs_my005-15 my-cozy-outfit-reveal_c1 with dissolve
    play voice3 girl34_arrogant_ha3 noloop
    my "Evening, [mcname]!"
    scene sm1cs_my005-16 my-enters-not-paid-bills-mc-what-no_c1 with dissolve
    play voice3 girl34_thinking_emm2 noloop
    my "Mmm. Mood lighting. Did you forget to pay your power bill this month?"
    play voice2 mc_surprised_what1 noloop
    mc "What! No!"
    scene sm1cs_my005-17 my-just-kidding-figured-movie-night_c1 with dissolve
    play voice3 girl34_happy_laugh2 noloop
    my "Hehehehehe, I'm just kidding, [mcname]."
    my "I figured this is all mise-en-scène for this \"movie night\" you're throwing."
    scene sm1cs_my005-18 mc-why-say-like-that-my-like-what_c1 with dissolve
    play voice2 mc_surprised_why1 noloop
    mc "Why do you say it like that?"
    play voice3 girl34_arrogant_huh1 noloop
    my "Like what?"
    scene sm1cs_my005-19 mc-like-quotes-around-movie-night_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "Like you have quotes around movie night?"
    scene sm1cs_my005-20 my-shrugs-wants-see-what-movie-night-is_c1 with dissolve
    play voice3 girl34_disappointed_oh2 noloop
    my "Because I want to see what this \"movie night\" is."
    scene sm1cs_my005-21 mc-hey-doing-lot-over-here-see_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, I'm doing a lot over here!"
    scene sm1cs_my005-22 mc-holding-popcorn-look-my-made-bowl-popcorn_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Look."
    play voice3 girl34_thinking_emm1 noloop
    my "You... made a bowl of popcorn."
    scene sm1cs_my005-23 mc-yeah-my-knwo-takes-twomins-make-right_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah."
    play voice3 girl34_arrogant_laugh2 noloop
    my "You know... that takes about two minutes to make, right?"
    scene sm1cs_my005-24 mc-smirking-maybe_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "...{w} Maybe."
    scene sm1cs_my005-25 my-giggles-hehe-mc-what_c1 with dissolve
    play voice3 girl34_happy_laugh6 noloop
    my "Hehehehehehe."
    play voice2 mc_surprised_what3 noloop
    mc "What!"
    scene sm1cs_my005-26 my-oh-nothing-mcname-what-movie-picked-tonight_c1 with dissolve
    play voice3 girl34_hey_happy noloop
    my "Oh, nothing, [mcname]. You're just incorrigible sometimes."
    my "So, what movie have you picked for us tonight?"
    scene sm1cs_my005-27 mc-sits-couch-new-epic-adventure-movie-my-calls-mcname_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, well, there's this new epic adventure movie that just came out-"
    play voice3 girl34_thinking_hmm7 noloop
    my "[mcname]."
    if player.get_choice("sm1cs_my004_choose_my"):
        scene sm1cs_my005-28 mc-yes-mom-melony_c1 with dissolve
        play voice2 mc_yes_yes2 noloop
        if persistent.is_special:
            mc "Yes, Mom?"
        else:
            mc "Yes, Melony?"
        scene sm1cs_my005-29 my-this-movie-you-or-winner-mc-you-remembered_c1 with dissolve
        play voice3 girl34_arrogant_ha3 noloop
        my "Is this movie night for you? Or for the winner of the swimsuit competition?"
        play voice2 mc_surprised_oh3 noloop
        mc "Oh, you remembered!"
        scene sm1cs_my005-30 my-smiles-ofc-remembered-think-want-watch-adventure-movie_c1 with dissolve
        play voice3 girl34_yes_questioning2 noloop
        my "Of course I remembered, [mcname]."
        my "Which goes to my point. Do you really think that I want to watch an epic adventure movie?"
    else:
        play voice3 girl34_yes_questioning2 noloop
        my "Do you really think that I want to watch an epic adventure movie?"
    scene sm1cs_my005-31 mc-didnt-let-finish-my-then-go-finish_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, you didn't let me finish!"
    play voice3 girl34_yes_aga3 noloop
    my "Then go on, finish your thought!"
    scene sm1cs_my005-32 mc-thanks-you-there-romance-movie-my-romance-movie-obvs_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Thank you.{w} I was also going to say, that there is also a romance movie-"
    play voice3 girl34_yes_yeap4 noloop
    my "The romance movie, obviously."
    scene sm1cs_my005-33 mc-ugh-my-no-way-talk-swimsuit-winner_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Ughhh-"
    play voice3 girl34_hey_angry7 noloop
    my "Hey, that's no way to talk to your swimsuit champion!"
    scene sm1cs_my005-34 mc-admits-you-right-you-right_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "You're right, you're right."
    scene sm1cs_my005-35 mc-holding-rmeote-my-offcam-mm-ask-mc_c1 with dissolve
    my "..."
    play voice3 girl34_thinking_hmm3 noloop
    my "[mcname]?"
    scene sm1cs_my005-36 mc-yes-mom-melony_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    if persistent.is_special:
        mc "Yeah, Mom?"
    else:
        mc "Yeah, Melony?"
    scene sm1cs_my005-37 my-nervous-wanted-apologize-other-day-mc-nothing-apologize-for_c1 with dissolve
    play voice3 girl34_disappointed_eeh4 noloop
    my "I...{w} wanted to apologize for running out the other day... I-"
    play voice2 mc_no_nono1 noloop
    mc "There's nothing to apologize for."
    scene sm1cs_my005-38 mc-you-came-we-tossed-lot-mc-unfair-least-warn_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "You came over, and we kind of tossed a lot on you."
    mc "I could have warned you about what we had in mind."
    scene sm1cs_my005-39 mc-lot-wasnt-prepared-now-my-look-smiles-wow-telling-stacy-mischievous_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Probably would have made things go smoother."
    play voice3 girl34_surprised_wow4 noloop
    if persistent.is_special:
        my "Well, we know how mischevious your sister can be."
    else:
        my "Well, we know how mischevious Stacy can be."
    scene sm1cs_my005-40 my-never-would-guessed-mc-haah-you-right_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "Hahahahahaha! Yeah, you're right."
    scene sm1cs_my005-41 my-looks-around-speaking-where-she-mc-had-out-something_c1 with dissolve
    play voice3 girl34_thinking_eeh1 noloop
    my "Speaking of, where is she tonight?"
    play voice2 mc_surprised_oh1 noloop
    mc "She had to go out and do... something."
    scene sm1cs_my005-42 my-uh-huh-something-doing-quotes-again_c1 with dissolve
    play voice3 girl34_yes_aga2 noloop
    my "Uh huh. \"Something\"."
    play voice2 mc_arrogant_huh2 noloop
    mc "You're doing the quotes thing again!"
    scene sm1cs_my005-43 my-giggling-hehe_c1 with dissolve
    play voice3 girl34_happy_laugh9 noloop
    my "Hehehehehe!"
    scene sm1cs_my005-44 my-looks-tv-got-movie-qued-mc-i-do_c1 with dissolve
    play voice3 girl34_thinking_hmm6 noloop
    my "Have you got the movie queued up?"
    play voice2 mc_yes_ugu1 noloop
    mc "I do!"
    scene sm1cs_my005-45 my-smiling-what-waiting-for-mc-nothing-all_c1 with dissolve
    play voice3 girl34_arrogant_huh2 noloop
    my "Then what are we waiting for?"
    play voice2 mc_no_nah2 noloop
    mc "Nothing, nothing at all."
    scene sm1cs_my005-46 mc-starts-movie_c1 with dissolve
    "*CLICK*"

    jump sm1cs_my005_half_movie

label sm1cs_my005_half_movie:

    scene black
    show screen scene_transition(_("About halfway through the movie"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1cs_my005-47 mc-my-watching-movie-halfway-through_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs_my005-48 my-looks-mc-calls-mc-hmm_c1 with dissolve
    play voice3 girl34_hey_simple3 noloop
    my "[mcname]?"
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Hmm?"
    scene sm1cs_my005-49 my-do-me-favour-mc-sure_c1 with dissolve
    play voice3 girl34_disappointed_eem1 noloop
    if persistent.is_special:
        my "Can you do your dear old mother a favor?"
    else:
        my "Can you do me a favor?"
    play voice2 mc_yes_sure1 noloop
    mc "Sure!"
    scene sm1cs_my005-50 my-can-give-massage-mc-really_c1 with dissolve
    play voice3 girl34_disappointed_mmf4 noloop
    my "Can you give me a little foot massage?"
    play voice2 mc_surprised_huh7 noloop
    mc "Really?"
    scene sm1cs_my005-51 my-pouty-face-please-mc-fine_c1 with dissolve
    play voice3 girl34_happy_relief3 noloop
    my "Please, [mcname]."
    play voice2 mc_disappointed_ehh1 noloop
    mc "Fiiiiine."
    scene sm1cs_my005-52 my-cheering-yay_c1 with dissolve
    play voice3 girl34_happy_yay2 noloop
    my "Yay!"
    scene sm1cs_my005-53 mc-starts-massaging-my-feet_c1 with dissolve
    pause
    scene sm1cs_my005-54 mct-least-could-do-prolly-score-points_c1 with dissolve
    my "Mmmmm."
    play voice2 d1s5_mcthinks noloop volume 1.7
    mct "Honestly, this is the least I could do after the whole swimsuit debacle."
    mct "Besides, it'll probably score me some brownie points."
    scene sm1cs_my005-55 mct-oh-yeah-deff-score-points-she-melt-puddle_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "Oh yeah. This is definitely going to score me some brownie points."
    mct "She's going to melt into a puddle! Time to ramp up my massage game."
    scene sm1cs_my005-56 my-mmm-feels-wonderful-mc-only-best_c1 with dissolve
    play voisex3 girl13_sex_closedmoan6 noloop
    my "Mmmmm... that feels wonderful, [mcname]."
    play voice2 mc_thinking_hmm3 noloop
    if persistent.is_special:
        mc "Only the best for my Mom."
    else:
        mc "Only the best for you, Melony."
    scene sm1cs_my005-57 my-enjoying-much-mmm-good_c1 with dissolve
    play voisex3 girl13_sex_closedmoans1
    my "Mmmm... good..."
    scene sm1cs_my005-58 mct-aight-this-good-who-knew-loved-foot-massge_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "All right, this is good! I've got a new secret weapon."
    if persistent.is_special:
        mct "Who knew Mom loved foot massages?"
    else:
        mct "Who knew Melony liked foot massages?"
    scene sm1cs_my005-59 my-mmm_c1 with dissolve
    my "Mmmmmm..."
    scene sm1cs_my005-60 mct-man-she-really-into-it-my-mmm-again_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Man, she really likes a good foot massage."
    my "Mmmmm..."
    scene sm1cs_my005-61 tv-loved-second-saw-mc-sounds-getting-interesting_c1 with dissolve
    "TV" "I've loved you from the second I met you!"
    play voice2 mc_thinking_hmm6 noloop
    mct "Oh, sounds like things are getting interesting in the movie."
    scene sm1cs_my005-62 tv-render-holding-hands_c1 with dissolve
    mct "I feel like I've missed most of this movie. But this has to be the part where the couple gets together."
    "TV" "Kiss me like you've never kissed me before."
    scene sm1cs_my005-63 tv-render-couple-kissing_c1 with dissolve
    my "Mmmmm... Ooooo..."
    play voice2 mc_thinking_hmm5 noloop
    mct "And now, they'll fade to black, and-"
    scene sm1cs_my005-65 tv-need-feel-in-me-mct-wait-why-say-that-tv-be-pleasure_c1 with dissolve
    "TV" "I need to feel you in me."
    play voice2 mc_surprised_huh6 noloop
    mct "Wait, what did she just say?"
    "TV" "It would be my pleasure."
    scene sm1cs_my005-66 tv-render-naked-couple-making-out_c1 with dissolve
    pause
    scene sm1cs_my005-67 mc-wait-how-fuck-they-naked-tv-take-me-lover_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "Wait, how the fuck did they get undressed so fast?"
    "TV" "Take me! Take me as your lover, forever!"
    scene sm1cs_my005-68 mct-no-way-they-fuck-holly-shit_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "There's no way they're going to actually fuck-"
    mct "Holy shit!"
    scene sm1cs_my005-69 tv-render-couple-fucking-mct-they-actually-fuck-mct-kinda-hot_c1 with dissolve
    mct "They're actually fucking. That's real, live sex in a porno."
    mct "And it's kind of hot..."
    scene sm1cs_my005-70 my-muaah-mct-wow-not-expecting-spicy_c1 with dissolve
    my "Mmmmmuuuuaaaaaahhhhhh..."
    play voice2 mc_surprised_wow4 noloop
    mct "Wow... I wasn't expecting this movie to be so... spicy."
    scene sm1cs_my005-71 mct-this-chick-really-into-get-great-tits-mct-big-bouncing-tits_c1 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mct "And this chick is really into it. And she's got great tits."
    mct "Great, big, bouncy tits... kind of like-"
    play voice2 mc_scared_huuuh3 noloop
    scene sm1cs_my005-72 mc-shock-face-mct-shit-getting-boner-melony-feet-on-my-dick_c1 with vpunch
    mct "Oh no! Shit, I'm getting a boner!"
    stop voisex3 fadeout 1.5
    if persistent.is_special:
        mct "And Mom's feet are right on my dick! Fuck! Fuck, fuck, fuck!"
    else:
        mct "And Melony's feet are right on my dick! Shit! Shit, shit, shit!"
    scene sm1cs_my005-73 my-silent-moaning-mmm_c1 with dissolve
    play voisex3 girl34_disappointed_mmf2 noloop volume 1.5
    my "Mmmmmmm..."
    scene sm1cs_my005-74 mc-getting-boner-under-pants-mct-oh-hell-what-do-now-think-cows_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Oh God, what the hell do I do know?"
    mct "Think, damnit think! Uhhhh, cows! Baseball. Anything other than-"
    scene sm1cs_my005-75 mc-my-watching-couple-fucking-hard_c1 with dissolve
    my "Huh."
    scene sm1cs_my005-76 tv-render-cock-fills-up-perfectly-my-ouaaa_c1 with dissolve
    "TV" "Oh, your cock fills me up perfectly! I love how it slams into my pussy so snugly!"
    play voisex3 girl13_sex_openmoans_short1 noloop volume 1.5
    my "Ooooooooouuuaaaaaaa..."
    play voice2 mc_disappointed_ah2 noloop
    mct "This movie is doing me no favors."
    scene sm1cs_my005-77 mc-worried-my-mmmrpg-mct-maybe-not-noticed_c1 with dissolve
    play voisex3 girl13_sex_closedmoans1
    my "Mmmmrrrrmmmmmgggg..."
    mct "Maybe she hasn't noticed?"
    mct "Maybe the foot massage is keeping her distracted enough."
    my "Mmmmmmmmmmmmpppph..."
    scene sm1cs_my005-78 mc-looking-my-mct-really-enjoying-massage-not-sure-even-noticed_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "In fact, she seems to really be enjoying this foot massage."
    mct "I'm not sure she's even noticed anything."
    scene sm1cs_my005-79 my-oo-mmrm-mct-wait-sounds-like_c1 with dissolve
    play voisex3 girl13_sex_openmoans1
    my "Ooooo... mmmmrmmmmm..."
    play voice2 d1s5_orgasm noloop
    mct "Wait, it kind of sounds like..."
    scene sm1cs_my005-80 my-moaning-ouuah-mct-wait-she-moaning_c1 with dissolve
    my "Oooouuuuaaaahhhhh..."
    play voice2 mc_pain_mff5 noloop
    mct "No way. Is she {u}moaning?{/u}"
    scene sm1cs_my005-81 mct-holly-shit-she-moaning-melony-has-foot-thing_c1 with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mct "Holy shit, she is!"
    if persistent.is_special:
        mct "Mom has a foot thing."
    else:
        mct "Melony has a foot thing!"
    scene sm1cs_my005-82 mct-what-hell-do-now-not-want-make-this-akward_c1 with dissolve
    play voice2 mc_pain_mff4 noloop
    mct "Oh shit, what... what the hell do I do now?"
    mct "This could blow up in my face."
    if persistent.is_special:
        mct "Mom totally has foot thing!"
    else:
        mct "Melony totally has a foot thing!"
    scene sm1cs_my005-83 my-moaning-mc-holy-shit-this-hot_c1 with dissolve
    my "Mmmmmmmmmm!"
    mct "Holy shit this is kind of hot."
    scene sm1cs_my005-84 my-feet-directing-mc-bulge-mct-feet-directly-boner-tv-oh-yes-cock-feels-incredible_c1 with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "Oh my God, her feet are directly on my dick. There's no way she can't feel my boner."
    "TV" "Oh yes, fuck me! Your cock feels incredible, oh yessss!"
    scene sm1cs_my005-85 mc-shit-could-channel-something-she-wait-she-rubbing-dick_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "Shit, I wish I could change the channel or something."
    scene sm1cs_my005-86 my-starts-rubbing-mc-feet_c1 with dissolve
    play voice2 mc_pain_rrrr noloop
    if persistent.is_special:
        mct "What is... is Mom ubbing my dick with her foot?"
    else:
        mct "What is... is Melony rubbing my dick with her foot?"
    scene sm1cs_my005-87 mc-rubbing-my-feet-rubbing-mc-crotch_c1 with dissolve
    play voisex2 mc_sex_closedmoans1
    mct "She totally is. Okay, shit, remain calm, keep calm."
    scene sm1cs_my005-88 rubbing-alt-angle-mct-shit-feels-good-though_c2 with dissolve
    mct "Shit, that feels kind of good though..."
    my "Mmmmmooouuuaaaahhhh..."
    mct "Focus, just focus on rubbing her feet."
    scene sm1cs_my005-89 rubbing-alt-angle-shit-ride-this-out-my-mmm_c3 with dissolve
    mct "Just going to ride this out until... whatever happens, happens."
    my "Mmmmmmmmm..."
    scene sm1cs_my005-90 rubbing-alt-angle-mct-feet-soft-my-ooo-oo_c4 with dissolve
    mct "God, her feet are so soft..."
    if persistent.is_special:
        mct "How are Mom's feet so soft?"
    else:
        mct "How are Melony's feet so soft?"
    my "Oooo... ooooooooooo..."
    scene sm1cs_my005-91 rubbing-alt-angle-remember-pedicure-oo_c5 with dissolve
    my "Oooooo... oooooooooooooooo... oooooooooooo..."
    mct "Oh, her breathing is picking up-"
    scene sm1cs_my005-92 rubbing-alt-angle-mc-shit-is-she-my-mmmmmrgg_c6 with dissolve
    play voisex3 girl13_sex_openmoans2
    my "Mmpphhh, mmmmmmpppppph!"
    mct "Shit... is she..."
    my "Mmmmmrrrrggggggg..."
    my "Mrrg!"
    mct "Oh my God, it sounds like-"
    my "Ngghhhhh!"
    scene sm1cs_my005-93 rubbing-alt-angle-my-moans-mc-melony-about-cum_c7 with dissolve
    if persistent.is_special:
        mct "It sounds like Mom is about to cum!"
    else:
        mct "It sounds like Melony is about to cum!"
    my "Oooo-ooooooo-ooooooooooo!"
    if persistent.is_special:
        mct "I'm about to make my Mom cum, holy shit."
    else:
        mct "I'm about to make Melony cum, holy shit."
    my "Oooooooo!"
    play voisex3 girl13_sex_orgasm2 noloop
    scene sm1cs_my005-94 my-bites-lip-orgasm-face-mct-did-just-oh-god_c1 with vpunch
    queue voisex3 girl34_angry_breath2 noloop
    stop voisex2 fadeout 1.0
    my "Nnnngggghhhhhhh! Oooo-oooooo-oooooo! Mmmmmmmmm..."
    play voisex2 d1s5_orgasm2 noloop
    mct "Did she just...{w} oh my God."
    scene sm1cs_my005-95 my-relax-face-mmm-mc-she-just-came-omg_c1 with dissolve
    play voice3 girl13_sex_closedmoan3 noloop
    my "Mmmmmmmmm..."
    mct "She just came. Oh my God..."
    scene sm1cs_my005-96 mct-what-she-do-now_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 2.0
    mct "What's she going to do?"
    scene sm1cs_my005-97 my-asleep-mct-does-know-has-to-right_c1 with dissolve
    play voice3 girl34_happy_relief4 noloop
    if persistent.is_special:
        my "That was a wonderful foot massage, son. Thank you..."
    else:
        my "That was a wonderful foot massage, [mcname]. Thank you..."
    play voice2 d2s9_confused noloop volume 1.7
    mc "Uhm, not a problem."
    scene sm1cs_my005-98 mc-my-watch-rest-movie-my-falling-asleep_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mct "Does she know, that I know what just happened?"
    mct "She has to, right?..."
    scene sm1cs_my005-99 after-movie-mc-my-watching-my-sleeping_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "But she has not sprinted off yet... so maybe everything's fine?"
    mct "Let's maybe not question a good thing, and I'll just let her sleep..."

    jump sm1cs_my005_after_movie

label sm1cs_my005_after_movie:

    scene black
    show screen scene_transition(_("After the Movie"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1cs_my005-100 my-opens-eyes-goodness-fall-asleep-mc-yep_c1
    with Fade(0.5, 0.5, 0.5)
    play voice3 girl34_surprised_oh3 noloop
    my "Oh, goodness... did I fall asleep?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yep."
    scene sm1cs_my005-101 my-oh-sorry-not-realise-how-tired_c1 with dissolve
    play voice3 girl34_disappointed_oh2 noloop
    my "Oh, I'm sorry. I didn't realize how tired I was."
    scene sm1cs_my005-102 my-foot-massage-knocked-out-mc-happy-help_c1 with dissolve
    play voice3 girl34_happy_relief2 noloop
    my "And that foot massage really took my breath away."
    play voice2 mc_thinking_hmm4 noloop
    mc "Oh yeah. You must have been really stressed."
    scene sm1cs_my005-103 my-appreciate-mc_c1 with dissolve
    play voice3 girl34_happy_relief6 noloop
    my "{b}I was...{/b}{w} I appreciate it, [mcname]."
    scene sm1cs_my005-104 my-sits-up-mc-anything-winner-my-hehe_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "*nervously* Anything for the winner of our swimsuit competition."
    play voice3 girl34_happy_laugh8 noloop
    my "Hehehehehehe. You're so sweet."
    my "But I am still exhausted. I should get back before I fall asleep on your couch again."
    scene sm1cs_my005-105 mc-welcome-pass-out-couch-any-time_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    if persistent.is_special:
        mc "Hey, our couch is always open to you, Mom."
    else:
        mc "Hey, you're welcome to pass out on our couch any time, Melony."
    scene sm1cs_my005-106 my-stretches-old-woman-need-bed-comforter_c1 with dissolve
    play voice3 girl34_yes_aga6 noloop
    my "I appreciate that, but when oyu get to be my age, oyu want a nice, big soft bed, with a down comforter."
    my "My days of couch crashing our far behind me."
    scene sm1cs_my005-107 mc-not-old-still-got-it_c1 with dissolve
    play voice2 mc_no_uhuh1 noloop
    if persistent.is_special:
        mc "You're not that old, Mom. You still got it."
    else:
        mc "You're not that old, Melony. You still got it."
    scene sm1cs_my005-108 my-too-sweet-silver-tongue-devil-should-head-out_c1 with dissolve
    play voice3 girl34_disappointed_eeh3 noloop
    my "Haha. You silver tongued charmer."
    my "But I should head out... I'm very, {i}very{/i} happy we got to do this."
    my "We should do another movie night soon."
    scene sm1cs_my005-109 my-walk-towards-exit_c1 with dissolve
    pause
    scene sm1cs_my005-110 my-maybe-next-time-able-stay-awake-can-pick-movie-next-time_c1 with dissolve
    play voice3 girl34_hey_simple4 noloop
    my "And maybe next time I'll be able to stay awake for the whole thing."
    play voice2 mc_arrogant_heh3 noloop
    mc "Can I pick the movie next time?"
    scene sm1cs_my005-111 my-absoleutly-not-goodnight-mc-good-night_c1 with dissolve
    play voice3 girl34_no_angry6 noloop
    my "Absolutely not. Good night, [mcname]."
    play voice2 mc_hey_bye2 noloop
    if persistent.is_special:
        mc "Good night, Mom."
    else:
        mc "Good night, Melony."
    scene sm1cs_my005-112 mc-watch-my-leaving_c1 with dissolve
    $ SMGallery.unlock_gallery_slot("replay", "sm1cs_my005")
    pause
    scene sm1cs_my005-113 my-exit-scene-mc-stares-door_c1 with dissolve
    pause
    scene sm1cs_my005-114 mc-confused-holy-shit-what-happened-just-made-melony-cum_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Holy shit... did that just happen?"
    if persistent.is_special:
        mct "I just made my mom cum from a foot massage, and then flrted with her like it was no big deal..."
    else:
        mct "I just made Melony cum from a foot massage, and then flrted with her like it was no big deal..."
    scene sm1cs_my005-115 mct-walked-away-nothing-happened-means-things-go-well_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mct "She just walked out the door like nothing happened..."
    mct "That must mean things are going well..."
    mct "I need to make our next date a fucking doozy."
    scene sm1cs_my005-116 mct-think-close-something-happens-who-knows-what-exactly-end-scene_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "It feels like we're getting a lot closer than ever before. But... what's going to happen next between us?"
    $ renpy.end_replay()

    jump sm1cs_my005_exit_to_studio

label sm1cs_my005_exit_to_studio:
    $ StoryController.end_scene(MY_STORY, 4, 0, 3)
    return
