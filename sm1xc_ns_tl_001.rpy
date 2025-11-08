label sm1xc_ns_tl_001:

    # MC can begin the scene by either interacting with Taisia or Nari during the early morning period on any day.

    if player.get_choice("sm1xc_ns_tl_001_interaction_character") == "tl":
        # Taisia and MC meet Nari while walking to the kitchen.
        scene sm1cs_ns_tl001-01 mc-ns-tl-entry1_c1 with dissolve
        play voice3 girl24_surprised_oh1 noloop
        tl "Oh. Morning, Nari."
        scene sm1cs_ns_tl001-01 mc-ns-tl-entry1_c2 with dissolve
        play voice4 nari_happy_relief noloop
        ns "Good morning, Taisia. I apologize if I'm intruding on your breakfast preparation."
        scene sm1cs_ns_tl001-02 mc-ns-tl-egg_c1 with dissolve
        pause
        scene sm1cs_ns_tl001-03 mc-ns-tl-talk_c1 with dissolve
        play voice3 girl24_arrogant_kgh2 noloop
        tl "*snorts* Intruding? Girl, it's a kitchen, not an operating theater."
        # Taisia walks over to the fridge and pulls out a carton of eggs.
        # She cracks them into a bowl with practiced efficiency.
    else:
        # Taisia notices them coming over while she's cracking some eggs.
        scene sm1cs_ns_tl001-01 mc-ns-tl-entry1_c1 with dissolve
        play voice3 girl24_hey_greeting noloop
        tl "Morning. There's coffee in the pot if you want it."
        scene sm1cs_ns_tl001-01 mc-ns-tl-entry1_c2 with dissolve
        play voice4 nari_happy_mmm noloop
        ns "Thank you. I've already had my morning allotment of caffeine."
        scene sm1cs_ns_tl001-02 mc-ns-tl-egg_c1 with dissolve
        pause
        scene sm1cs_ns_tl001-03 mc-ns-tl-talk_c1 with dissolve
        play voice2 d1s2_hmm noloop volume 1.7
        mc "What are you making?"
        play voice3 girl24_disappointed_eeh1 noloop
        tl "Pancakes. Got a craving."
    scene sm1cs_ns_tl001-04 mc-ns-tl-mixing_c1 with dissolve
    pause
    scene sm1cs_ns_tl001-05 mc-ns-tl-talk_c1 with dissolve
    pause
    scene sm1cs_ns_tl001-03 mc-ns-tl-talk_c2 with dissolve
    # Taisia continues working as Nari stands around awkwardly. MC breaks the tension.
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "You two haven't really had a chance to get to know each other since Nari moved in, right?"
    scene sm1cs_ns_tl001-06 mc-ns-tl-talk2_c1 with dissolve
    play voice3 girl24_no_nope noloop
    tl "Not really. Different schedules."
    scene sm1cs_ns_tl001-05 mc-ns-tl-talk_c2 with dissolve
    play voice4 nari_happy_laugh3 noloop
    ns "We've exchanged brief greetings exactly three and a half times."
    scene sm1cs_ns_tl001-07 mc-ns-tl-walk_c1 with dissolve
    play voice3 girl24_surprised_what2 noloop
    tl "You counted?"
    scene sm1cs_ns_tl001-07 mc-ns-tl-walk_c2 with dissolve
    play voice4 nari_disappointed_eeh noloop
    ns "*nods* I find data collection quite helpful for social integration."
    # MC looks between the two.
    scene sm1cs_ns_tl001-08 mc-ns-tl-look_c2 with dissolve
    play voice2 mc_happy_a1 noloop volume 1.6
    mc "Why don't you two make breakfast together? Could be a good bonding experience."
    scene sm1cs_ns_tl001-08 mc-ns-tl-look_c1 with dissolve
    play voice3 girl24_no_nah noloop
    tl "I work better solo. Too many cooks and all that shit."
    #ns agreeing that it might not be the best.
    scene sm1cs_ns_tl001-09 mc-ns-tl-talk_c2 with dissolve
    play voice4 nari_disappointed_eh noloop
    ns "I wouldn't want to interfere with Taisia's process. My culinary skills are rudimentary at best."
    #mc urging them to try it
    play voice2 mc_hey_hey3 noloop
    mc "Come on. You're going to be living together, potentially filming together, but you can't make pancakes together?"
    #tl is not buying it
    scene sm1cs_ns_tl001-08 mc-ns-tl-look_c1 with dissolve
    play voice3 girl24_arrogant_huh2 noloop
    tl "*raises eyebrow* Your point?"
    scene sm1cs_ns_tl001-08 mc-ns-tl-look_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "If we're building a real team here, we need to figure out how to exist in the same space without walking on eggshells."
    play voice4 nari_thinking_oh noloop
    ns "Actually, walking on eggshells is quite stable depending on their orientat—"
    scene sm1cs_ns_tl001-09 mc-ns-tl-talk_c1 with dissolve
    play voice3 girl24_happy_laugh5 noloop
    tl "*laughs* Jesus Christ, you're literal."
    # Taisia glances at Nari, then sighs.
    tl "Fine. Nari, you want to help? You can measure the flour. Two cups, level."
    scene sm1cs_ns_tl001-09 mc-ns-tl-talk_c2 with dissolve
    play voice4 nari_yes_emotional noloop
    ns "*perks up* Yes. I can do that."
    # As Nari reaches for the measuring cups, Taisia gives MC a look.
    play voice3 girl24_thinking_emm1 noloop
    tl "And you're just gonna stand there looking pretty?"
    tl "*smirks* Very progressive of you, having the women make your breakfast while you do fuck all."
    scene sm1cs_ns_tl001-10 mc-ns-tl-help_c1 with dissolve
    if player.get_choice("sm1xc_ns_tl_001_interaction_character") == "tl":
        #mc is like - you invited me - tl is having none of it
        play voice2 mc_no_nah2 noloop
        mc "Now, hold on. {i}You{/i} invited {i}me{/i}."
        scene sm1cs_ns_tl001-11 mc-ns-tl-cooking_c1 with dissolve
        play voice3 girl24_hey_greeting noloop
        tl "Invitation doesn't mean you can't grab a spatula, Captain."
        play voice2 mc_thinking_mmm4 noloop
        mc "Point taken. But let the record show that this is entrapment."
        # MC grabs a spatula and starts helping.
    else:
        #mc is like, I'm innocent
        play voice2 mc_arrogant_huh1 noloop
        mc "Why the hell am I catching strays? There's already enough potential chaos with two people in here."
        mc "*smirks* Besides, I figure we'll get plenty of threeway action later once you two figure out your rhythm."
        scene sm1cs_ns_tl001-11 mc-ns-tl-cooking_c1 with dissolve
        # Nari nearly drops her measuring cup.
        play voice4 nari_surprised_ehh noloop
        ns "I— That's—"
        play voice3 girl24_arrogant_hah noloop
        tl "*smirks* Ha! Bold of you to assume we'd need your input."
        ns "*whispers* I would still want your input..."
    # A mini montage of them three cooking starts. It's interspaced with small interactions.
    # INTERACTION 1: Nari carefully measures flour.
    scene sm1cs_ns_tl001-12 mc-ns-tl-cooking2_c1 with dissolve
    play voice4 nari_disappointed_huh noloop
    ns "The recipe states we need precisely 2 cups of flour, 1.5 teaspoons of baking powder—"
    # Taisia just drops the ingredients in.
    play voice3 girl24_yes_aga noloop
    tl "Or you just eyeball it until it looks right."
    #ns is worried
    scene sm1cs_ns_tl001-13 mc-ns-tl-cooking3_c1 with dissolve
    play voice4 nari_disappointed_woof noloop
    ns "*distressed* But that introduces too many variables for—"
    #tl has her fly by the seat of her pants attitude
    scene sm1cs_ns_tl001-13 mc-ns-tl-cooking3_c2 with dissolve
    play voice3 girl24_arrogant_pff noloop
    tl "Variables schmariables. Cooking's not coding, Nari. Sometimes you gotta feel it out."
    #They both reach for the same whisk.
    scene sm1cs_ns_tl001-14 mc-ns-tl-cooking4_c2 with dissolve
    play voice3 girl24_arrogant_hm3 noloop
    tl "I got it—"
    scene sm1cs_ns_tl001-14 mc-ns-tl-cooking4_c1 with dissolve
    play voice4 nari_disappointed_oh noloop
    ns "Oh, sorry—"
    # Their hands touch briefly. Taisia casually withdraws her hand.
    play voice3 girl24_disappointed_neh noloop
    tl "All yours."
    ns "*blushes* Thank you."
    #Taisia heats up the pan and demonstrates her technique by flipping a test pancake high in the air and catching it.
    scene sm1cs_ns_tl001-15 mc-ns-tl-cooking5_c2 with fade
    play voice3 girl24_happy_wooh noloop
    tl "Boom! This is the second best part of making pancakes. Batter seems ready."
    # Nari shows her phone timer.
    scene sm1cs_ns_tl001-15 mc-ns-tl-cooking5_c1 with dissolve
    play voice4 nari_arrogant_hm noloop
    ns "That pancake cooked for only ninety-seven seconds. The optimal cooking time is one hundred and twenty seconds per side."
    play voice3 girl24_arrogant_yeah3 noloop
    tl "Tell that to the perfectly golden pancake, time cop."
    # INTERACTION 4: Nari takes over cooking while Taisia pipes the batter and gets the syrup. MC cleans up some of the utensils.
    scene sm1cs_ns_tl001-16 mc-ns-tl-cooking6_c2 with fade
    play voice4 nari_hey_calm noloop
    ns "Do you listen to anything while you cook?"
    scene sm1cs_ns_tl001-16 mc-ns-tl-cooking6_c1 with dissolve
    play voice3 girl24_surprised_why3 noloop
    tl "Eh, usually whatever's on. Why?"
    scene sm1cs_ns_tl001-16 mc-ns-tl-cooking6_c2 with dissolve
    play voice4 nari_disappointed_mff noloop
    ns "I enjoy true crime podcasts during repetitive tasks. They provide interesting analysis of behavioral patterns."
    #tl is interested by that. she likes crime drama
    play voice3 girl24_surprised_huh4 noloop
    tl "No shit? Me too. Listen to anything about the Zodiac copycat?"
    play voice4 nari_sexphrase_yes1 noloop
    ns "Yes! The statistical anomalies in the case were fascinating!"
    #tl and ns warming up to each other
    scene sm1cs_ns_tl001-16 mc-ns-tl-cooking6_c1 with dissolve
    play voice3 girl24_yes_yeah noloop
    tl "Hell yeah, statistics. Gruesome shit though. Hopefully they get the bastard."
    scene sm1cs_ns_tl001-16 mc-ns-tl-cooking6_c3 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "*smiles* Look at you two, finding common ground...over horrifying murders."
    play voice3 girl24_hey_sexy noloop
    tl "Hey, if it works."
    # The TV plays a commercial that catches their attention
    scene sm1cs_ns_tl001-17 mc-ns-tl-look_c2 with dissolve
    pause
    #tl scowls at the tv, ns holding her mouth near her hand as she laughs
    scene sm1cs_ns_tl001-17 mc-ns-tl-look_c1 with dissolve
    play voice3 girl24_disgust_boeagh1 noloop
    tl "That commercial is such bullshit. Nobody is that happy about yogurt."
    scene sm1cs_ns_tl001-18 mc-ns-tl-look2_c2 with dissolve
    play voice4 nari_happy_laugh1 noloop
    ns "*laughing* I know what you mean. That yogurt is not—"
    scene sm1cs_ns_tl001-19 mc-ns-tl-look3_c2 with hpunch
    play voice4 nari_scared_ho noloop
    ns "Oh!"
    # Batter splashes onto Nari's cheek.
    scene sm1cs_ns_tl001-20 mc-ns-tl-close_c1 with dissolve
    play voice3 girl24_arrogant_huh1 noloop
    tl "You've got a little something on your cheek. Want help?"
    scene sm1cs_ns_tl001-20 mc-ns-tl-close_c2 with dissolve
    play voice4 nari_yes_sad noloop
    ns "Yes, please. I don't want to get batter on my—"
    # Taisia leans in without warning and slowly licks the batter from Nari's cheek.
    scene sm1cs_ns_tl001-21 mc-ns-tl-lick_c1 with dissolve
    play voice4 nari_sex_closedmoan1 noloop
    play voice3 girl24_sex_sucking1 noloop
    ns "..."
    scene sm1cs_ns_tl001-21 mc-ns-tl-lick_c2 with dissolve
    play voice4 nari_surprised_ah noloop
    ns "*freezes and blushes* That— That's highly unhygienic! Raw flour can harbor bacteria and— and—"
    scene sm1cs_ns_tl001-22 mc-ns-tl-look_c1 with dissolve
    play voice3 girl24_arrogant_kgh1 noloop
    tl "*grins* Honey, that doesn't even register on the scale of \"unhygienic\" things I could do to you."
    # Nari is so distracted she forgets about the pancake in the pan.
    scene sm1cs_ns_tl001-22 mc-ns-tl-look_c2 with dissolve
    play voice4 nari_pain_aaa1 noloop
    ns "I—{w} Oh no, the pancake!"
    # Smoke rises from the burning pancake.
    scene sm1cs_ns_tl001-23 mc-ns-tl-help_c1 with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "Whoa there."
    # MC helps Nari scrape off the burnt pancake while Taisia looks smug.
    mc "Taisia, no flirting with the line cook until service is over. We just got the place done up nice."
    scene sm1cs_ns_tl001-23 mc-ns-tl-help_c2 with dissolve
    play voice3 girl24_happy_laugh2 noloop
    tl "*shrugs and smirks* No promises. She's cute, and it's fun making her blush."
    scene sm1cs_ns_tl001-23 mc-ns-tl-help_c3 with dissolve
    play voice4 nari_surprised_oh noloop
    ns "*blushing harder* The temperature control on this stove is imprecise!"
    # They finish the last few pancakes, grab their plates, and move to the couch.
    scene sm1cs_ns_tl001-24 mc-ns-tl-help2_c1 with dissolve
    mc and tl "Hahaha."
    # They watch a cooking competition show on TV.
    scene sm1cs_ns_tl001-25 mc-ns-tl-tv_c1 with fade
    play voice3 girl24_happy_laugh4 noloop
    tl "*laughs* Look at this asshole. Who puts truffles on pancakes?"
    play voice4 nari_happy_mmm noloop
    ns "The combination of flavors would be discordant. Truffles have an earthy profile that would clash with sweet maple syrup."
    scene sm1cs_ns_tl001-26 mc-ns-tl-talk_c2 with dissolve
    play voice3 girl24_thinking_hmm6 noloop
    tl "Speaking of which..."
    # Taisia drizzles maple syrup liberally over her stack.
    scene sm1cs_ns_tl001-27 mc-ns-tl-talk2_c1 with dissolve
    play voice4 nari_disgust_brrgh noloop
    ns "*wrinkles nose* That's...excessive."
    play voice3 girl24_thinking_ah noloop
    tl "Let me guess, you're not a syrup fan?"
    ns "I prefer honey. Maple syrup overwhelms the palate."
    scene sm1cs_ns_tl001-27 mc-ns-tl-talk2_c2 with dissolve
    play voice3 girl24_yes_ugu noloop
    tl "*passes honey jar* Here. Weird pancake girl."
    play voice4 nari_thinking_hmm3 noloop
    ns "It's not as weird as wanting to be choked during sex. Statistically, that's a far greater deviation from the norm."
    scene sm1cs_ns_tl001-28 mc-ns-tl-talk3_c1 with hpunch
    # Taisia drops her fork with a clatter. MC chokes on his coffee.
    play voice3 girl24_surprised_what1 noloop
    tl "...The fuck did you just say?"
    play voice2 mc_pain_cough2 noloop
    mc "Where...where did that come from?"
    scene sm1cs_ns_tl001-28 mc-ns-tl-talk3_c3 with dissolve
    play voice4 nari_thinking_emm noloop
    ns "From your video. I analyzed the micro-expressions during the climactic scene."
    ns "The data suggests a strong correlation between asphyxiation and Taisia's pleasure centers."
    # Taisia just stares, completely stunned, before letting out a sharp bark of laughter.
    scene sm1cs_ns_tl001-29 mc-ns-tl-talk4_c2 with dissolve
    play voice3 girl24_happy_laugh3 noloop
    tl "*laughs* You analyzed my fucking 'O'-face? You're a goddamn lunatic."
    tl "I love it."
    scene sm1cs_ns_tl001-29 mc-ns-tl-talk4_c1 with dissolve
    play voice4 nari_happy_laugh6 noloop
    ns "*beams* I'm glad my analysis was well-received!"
    # They continue eating and watching random stuff on TV.
    scene sm1cs_ns_tl001-32 mc-ns-tl-look_c1 with fade
    pause
    scene sm1cs_ns_tl001-32 mc-ns-tl-look_c3 with dissolve
    play voice4 nari_happy_relief noloop
    ns "I've never actually lived with non-family roommates before."
    scene sm1cs_ns_tl001-32 mc-ns-tl-look_c2 with dissolve
    play voice3 girl24_disappointed_eeh1 noloop
    tl "First for us both then. I've never stayed in one place long enough to have \"roommate traditions.\""
    scene sm1cs_ns_tl001-32 mc-ns-tl-look_c1 with dissolve
    play voice4 nari_thinking_oh noloop
    ns "Like communal breakfast?"
    play voice3 girl24_yes_yap noloop
    tl "Yeah. It's...not terrible."
    play voice2 mc_thinking_hmm3 noloop volume 1.5
    mc "And these turned out great."
    tl "We didn't burn the place down, so that's a win."
    # The three of them sit comfortably on the couch, plates balanced on their laps, the TV casting a soft glow on their satisfied expressions.
    scene sm1cs_ns_tl001-32 mc-ns-tl-look_c3 with dissolve
    play voice4 nari_disappointed_eeh noloop
    ns "The success rate was approximately 98%%, accounting for the one burnt specimen."
    scene sm1cs_ns_tl001-33 mc-ns-tl-walk_c1 with dissolve
    play voice3 girl24_happy_laugh1 noloop
    tl "*laughs* You quantify everything, don't you?"
    scene sm1cs_ns_tl001-33 mc-ns-tl-walk_c2 with dissolve
    play voice4 nari_yes_yeah noloop
    ns "*small smile* It helps me make sense of the world."
    # They finish eating and head back to the kitchen to clean up.
    # Taisia washes, Nari rinses and dries in a surprisingly smooth system.
    scene sm1cs_ns_tl001-34 mc-ns-tl-clean_c1 with dissolve
    play voice3 girl24_thinking_emm2 noloop
    tl "So what's the worst cooking disaster you've ever had?"
    scene sm1cs_ns_tl001-34 mc-ns-tl-clean_c2 with dissolve
    play voice4 nari_arrogant_fff noloop
    ns "I once attempted to make kimchi and the fermentation process became...explosive."
    scene sm1cs_ns_tl001-35 mc-ns-tl-clean2_c1 with dissolve
    play voice3 girl24_happy_laugh5 noloop
    tl "*laughs* Ha! That's awesome."
    scene sm1cs_ns_tl001-35 mc-ns-tl-clean2_c2 with dissolve
    play voice4 nari_yes_emotional noloop
    ns "It was. But my mother's kitchen ceiling needing to be repainted was...less so. What about you?"
    scene sm1cs_ns_tl001-36 mc-ns-tl-clean3_c1 with dissolve
    play voice3 girl24_disgust_ooh1 noloop
    tl "Tried making my own moonshine when I was 16. Nearly blinded myself."
    scene sm1cs_ns_tl001-36 mc-ns-tl-clean3_c3 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Why am I not surprised?"
    # Couple renders of them cleaning up. The trio looks more relaxed.
    scene sm1cs_ns_tl001-37 mc-ns-tl-close_c1 with dissolve
    play voice3 girl24_thinking_hmm3 noloop
    tl "Not half-bad on the pancakes, newbie. You might actually be useful in the kitchen."
    scene sm1cs_ns_tl001-37 mc-ns-tl-close_c2 with dissolve
    play voice4 nari_happy_yay noloop
    ns "*excited* Thank you! I enjoyed working with you too."
    # MC leans against the counter, watching them with a smile.
    scene sm1cs_ns_tl001-37 mc-ns-tl-close_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Maybe we should make this a regular thing. Team breakfasts."
    scene sm1cs_ns_tl001-38 mc-ns-tl-talk_c1 with dissolve
    play voice3 girl24_yes_simple1 noloop
    tl "*shrugs* We'll see if it sticks. As long as I don't have to be up at Nari's asscrack-of-dawn hours."
    scene sm1cs_ns_tl001-38 mc-ns-tl-talk_c2 with dissolve
    play voice4 nari_thinking_hmm1 noloop
    ns "Studies show that communal meals strengthen social bonds. So, yes. I would enjoy that very much."
    scene sm1cs_ns_tl001-38 mc-ns-tl-talk_c1 with dissolve
    play voice3 girl24_arrogant_kgh2 noloop
    tl "*smirks* You know, \"communal meals\" aren't the only thing that strengthens social bonds."
    # Taisia moves a little closer to Nari.
    play voice4 nari_surprised_ehh noloop
    ns "*blushes* Oh my."
    play voice3 girl24_thinking_mff noloop
    tl "Haha."
    scene sm1cs_ns_tl001-38 mc-ns-tl-talk_c3 with dissolve
    play voice2 mc_thinking_hmm2 noloop volume 1.4
    mc "See? You two are already finding your rhythm."
    scene sm1cs_ns_tl001-39 mc-ns-tl-talk2_c1 with dissolve
    play voice3 girl24_happy_yeah3 noloop
    tl "*grins* Guess so. Looking forward to seeing where else we can find a rhythm."
    # They finish up and the last dish gets put away.
    tl "Alright, I've got shit to do. But this wasn't terrible."
    scene sm1cs_ns_tl001-39 mc-ns-tl-talk2_c2 with dissolve
    play voice4 nari_surprised_huh1 noloop
    ns "That sounds like high praise."
    scene sm1cs_ns_tl001-39 mc-ns-tl-talk2_c3 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "The highest."
    scene sm1cs_ns_tl001-40 mc-ns-tl-wave_c1 with dissolve
    play voice3 girl24_hey_bye2 noloop
    tl "*playful eye roll* Later, nerds."
    scene sm1cs_ns_tl001-40 mc-ns-tl-wave_c2 with dissolve
    ns "Have a good day, Taisia."
    # Taisia exits with a casual wave, but not before giving Nari a quick wink.
    scene sm1cs_ns_tl001-41 mc-ns-tl-end_c1 with dissolve
    play voice4 nari_surprised_huh2 noloop
    ns "She's...not what I expected."
    scene sm1cs_ns_tl001-41 mc-ns-tl-end_c2 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "In a good way?"
    scene sm1cs_ns_tl001-41 mc-ns-tl-end_c1 with dissolve
    play voice4 nari_yes_confident noloop
    ns "*nod and smiles* Yes. Definitely in a good way."

    return
