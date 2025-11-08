label sm1fs_t007:

    #questlog - "Talk to Bruce to start the show on Saturday Evening"
    # Interaction with Bruce to start the show.

    # Backstage. MC is now dressed in black shirt, black pants, black shoes. He wears a headset. The space buzzes with pre-show energy. Actors in costume, props being checked, nervous laughter, the works.
    # Denise stands center stage of the backstage area, clipboard in hand, addressing the assembled cast.
    scene sm1fs_t007-01 mc-tl-dch-cast1_c1 with dissolve
    dvh "Listen up."
    dvh "This is just another show. We've been preparing, and I have done my best to take you from weak, unmolded clay into something exquisite."
    #alt angle - showing the cast members, tl, vs, km
    scene sm1fs_t007-01 mc-tl-dch-cast1_c2 with dissolve
    dvh "I know what it's like to be where you are standing."
    dvh "You want sleep. Want to quit. You're worried you'll screw up."
    #dvh giving them a pep talk
    scene sm1fs_t007-02 mc-tl-dch-cast2_c1 with dissolve
    dvh "But you wouldn't be here if I didn't expect you could do this!"
    # A few nervous laughs from the cast.
    scene sm1fs_t007-02 mc-tl-dch-cast2_c2 with dissolve
    dvh "Tonight, you're awake. Tonight, you're sharp!"
    dvh "Tonight we are going to bring the magic alive."
    #dvh holds her hand in a fist
    scene sm1fs_t007-03 mc-tl-dch-cast3_c1 with dissolve
    dvh "I want you to leave it all on the stage."
    dvh "Do that, and the whole town will be buzzing about our newest show."
    #dvh small smile
    dvh "Now...{w} are you ready to fly?"
    # The cast responds with various affirmations.
    scene sm1fs_t007-03 mc-tl-dch-cast3_c2 with dissolve
    kw "Yes, ma'am!"
    vs "We've got this!"
    tl "Let's kill it."
    # Denise notices MC in the wings and gives him a curt nod.
    scene sm1fs_t007-04 mc-tl-dch-cast4_c1 with dissolve
    dvh "Bruce, [mcname], let's make this seamless."
    scene sm1fs_t007-04 mc-tl-dch-cast4_c2 with dissolve
    dvh "Places in ten minutes."
    # The cast disperses. Veronica bounces over to MC, already in her sexy party dress.
    scene sm1fs_t007-05 mc-tl-dch-cast5_c2 with dissolve
    vs "Oh my God, I'm so nervous! Are you nervous?"
    #vs looking caring - but she's got that like hyper bubbly energy
    scene sm1fs_t007-06 mc-tl-dch-talk_c2 with dissolve
    vs "You look nervous.{w} Or maybe that's just your face."
    vs "Are you sick, don't be sick, [mcname]."
    scene sm1fs_t007-06 mc-tl-dch-talk_c1 with dissolve
    mc "Uh..."
    menu:
        "I'm a little nervous, yeah" (hint="sm1fs_t007_m01_h01"):
            $ player.set_choice("sm1fs_t007_nervous")
            $ CharacterController.get_character("vs").add_point()
            scene sm1fs_t007-07 mc-tl-dch-talk2_c1 with dissolve
            mc "I'm a little nervous, yeah. First opening night and all."
            # Veronica squeezes his arm reassuringly.
            scene sm1fs_t007-07 mc-tl-dch-talk2_c2 with dissolve
            vs "Oh good! I mean, not good that you're nervous, but good that I'm not alone."
            vs "*beams* We're gonna crush this together!"

        "I'm terrified" (hint="sm1fs_t007_m01_h02"):
            $ player.set_choice("sm1fs_t007_terrified")
            scene sm1fs_t007-09 mc-tl-dch-talk4_c2 with dissolve
            mc "I'm terrified. This headset is the only thing keeping me from running out the door."
            # Veronica laughs, relaxing slightly.
            scene sm1fs_t007-08 mc-tl-dch-talk3_c1 with dissolve
            vs "*laughs* Don't sweat it, [mcname]. I have faith in you."
            vs "You practiced just as much as the rest of us."
            #vs looking confindent
            scene sm1fs_t007-09 mc-tl-dch-talk4_c1 with dissolve
            vs "I'm sure you could do this blindfolded."
            #vs thinking - well maybe not
            vs "Probably. Maybe. Hopefully."

        "You're going to kill it" (hint="sm1fs_t007_m01_h03"):
            $ player.set_choice("sm1fs_t007_kill_it")
            $ CharacterController.get_character("vs").add_point()
            scene sm1fs_t007-09 mc-tl-dch-talk4_c2 with dissolve
            mc "Me? I'm just moving curtains. You're going to kill it out there."
            # Veronica beams at him.
            scene sm1fs_t007-10 mc-tl-dch-talk5_c1 with dissolve
            vs "*laughs* Haha. I know!"
            #vs glad he isn't nervous
            vs "But I'm glad you're not letting your nerves get to you."
            scene sm1fs_t007-10 mc-tl-dch-talk5_c2 with dissolve
            mc "Who said I'm nervous."
            #vs using a hand to wave down mc's body
            scene sm1fs_t007-11 mc-tl-dch-talk6_c1 with dissolve
            vs "Just your eyes, your head movements, your general aura."
            vs "But it's okay. I know you can do this."
            #vs smiling
            vs "It's just acting after all."
            #vs dumb blonde moment
            vs "Oh wait, I mean. It's just pulling ropes and moving stuff."
            scene sm1fs_t007-10 mc-tl-dch-talk5_c2 with dissolve
            mc "Thanks."

    # Bruce's voice crackles over the headset.
    scene sm1fs_t007-12 mc-tl-dch-talk7_c3 with dissolve
    sb "*via headset* [mcname], I need you at the curtain. We open in five."
    # MC gives Veronica a quick thumbs-up.
    scene sm1fs_t007-12 mc-tl-dch-talk7_c2 with dissolve
    mc "Break a leg."
    scene sm1fs_t007-12 mc-tl-dch-talk7_c1 with dissolve
    vs "You too!"
    # MC hustles to his position at the main stage curtain mechanism in the wings, stage right.
    # Through a gap in the curtain, MC can see the audience filing in. He spots Nelson and Maya entering. Nelson in a too-tight button-up, Maya in a simple black dress.
    scene sm1fs_t007-13 mc-tl-dch-talk8_c2 with dissolve
    pause
    scene sm1fs_t007-13 mc-tl-dch-talk8_c1 with dissolve
    mct "Oh, whoa."
    mct "Nelson and Maya made it to opening night."
    #mc a little worried
    mct "I really need this show to be good. Or I might get fired from this job, and Wurst Delivery."
    # MC's headset crackles. - ms is listening
    scene sm1fs_t007-14 mc-tl-dch-talk9_c1 with dissolve
    dvh "*via headset* House is at ninety percent capacity. We're holding for two more minutes, then we go."
    dvh "*via headset* [mcname], on my mark, you open the curtain. Smooth and steady."
    mc "*whispers into headset* Copy that. Smooth and steady."
    # The house lights dim. A hush falls over the audience.
    scene sm1fs_t007-14 mc-tl-dch-talk9_c2 with dissolve
    dvh "*via headset* And...go."
    # MC pulls the lever/ pulls on rope.
    #The curtain glides open smoothly, revealing the brightly lit "Pizza World" set with checkered tablecloths and neon signs.
    # The opening scene begins. We see the beginnings of Veronica and the other actors celebrate a promotion party.
    # Bruce appears beside MC in the wings, giving him an approving nod.
    scene sm1fs_t007-15 mc-tl-dch-pause_c1 with dissolve
    pause
    scene sm1fs_t007-16 mc-tl-dch-pause2_c1 with dissolve
    pause
    scene sm1fs_t007-17 mc-tl-dch-talk_c1 with dissolve
    sb "*whispers* Clean open. Good work."
    #ruce giving instrutions
    scene sm1fs_t007-17 mc-tl-dch-talk_c2 with dissolve
    sb "*whispers* Next task. Stage left lighting rig. Second light from the back is flickering."
    sb "*whispers* You've got about eight minutes before the next scene change."
    mc "On it."
    # MC nods and quietly makes his way through backstage to stage left.
    # Small new location - the lighting rig area - main thing we'd neeed is like a section of the metal support strucure
    #MC climbs a small ladder to the lighting rig
    #mc carefully unscrews the hot bulb using a rag. He replaces it with a fresh one.
    # The flickering stops.
    #MC descends
    # mc sees bruce giving him a thumbs-up from across the stage.
    scene black
    show screen scene_transition(_("After fixing the light"))
    with Fade(0.5, 0.5, 0.5)
    scene sm1fs_t007-19 mc-tl-dch-look_c1 with fade
    hide screen scene_transition
    sb "*via headset* Nicely done. Now get to the quick-change station."
    sb "*via headset* Veronica's coming off in ninety seconds, and her mic was cutting in and out."
    # MC positions himself at the quick-change area. It's a cramped corner cordoned off by black curtains.
    # Veronica rushes in, pulling off her party dress as a costume assistant helps her into her Pizza World delivery uniform.
    vs "*slightly breathless* [mcname]! Thank God. My mic keeps—"
    "*crackles*"
    # Static crackles from her body pack.
    scene sm1fs_t007-19-1 mc-tl-dch-dress_c1 with dissolve
    vs "—doing that."
    scene sm1fs_t007-20 mc-tl-dch-look2_c1 with dissolve
    mc "Let me take a look."
    # MC kneels beside her, opening the battery compartment of her wireless mic pack.
    if player.has_played_scene("sm1cs_vs003"):
        # Veronica leans in close, her lips near his ear.
        scene sm1fs_t007-21 mc-tl-dch-close_c1 with dissolve
        vs "*whispers, playful* You're so focused. It's kinda hot."
        # As MC adjusts the wire near her collarbone, Veronica shifts, pressing her chest forward so his hand grazes her breast.
        scene sm1fs_t007-21 mc-tl-dch-close_c2 with dissolve
        mc "*whispers, slightly flustered* Veronica, I'm trying to—"
        vs "*whispers, teasing* I know exactly what you're trying to do."
        menu:
            "Stay professional" (hint="sm1fs_t007_m02_h01"):
                $ player.set_choice("sm1fs_t007_stay_professional")
                # MC gently moves his hand away and finishes the adjustment.\
                mct "Not the time, not the place. Denise would murder us both."
                # Veronica pouts but doesn't push.
                scene sm1fs_t007-22 mc-tl-dch-close2_c1 with dissolve
                vs "*whispers* Spoilsport."

            "Give her breast a squeeze" (hint="sm1fs_t007_m02_h02"):
                $ player.set_choice("sm1fs_t007_squeeze_breast")
                $ CharacterController.get_character("vs").add_point()
                # MC gives a quick, teasing squeeze and a light tickle.
                # Veronica stifles a giggle and bites her lip.
                scene sm1fs_t007-23 mc-tl-dch-close3_c1 with dissolve
                vs "Ooooh."
                vs "*breathy* Mmm. I love getting excited before a big scene."
                #mc smiling at her
                scene sm1fs_t007-23 mc-tl-dch-close3_c2 with dissolve
                mc "*whispers* You're impossible."
                scene sm1fs_t007-25 mc-tl-dch-close_c1 with dissolve
                vs "*whispers* And you love it."
    else:
        # Veronica just watches him work, tapping her foot nervously.
        scene sm1fs_t007-24 mc-tl-dch-look_c1 with dissolve
        vs "Is it fixed? I can't go on if it's cutting out. Denise will murder me."
        scene sm1fs_t007-24 mc-tl-dch-look_c2 with dissolve
        mc "Almost...there. Test it."

    # Veronica whispering in
    scene sm1fs_t007-22 mc-tl-dch-close2_c1 with dissolve
    vs "*whispers* Test test."
    #mc is like - it's working. vs is excited
    scene sm1fs_t007-22 mc-tl-dch-close2_c2 with dissolve
    mc "You're good to go."
    vs "You're a lifesaver!"
    # She pecks him on the cheek
    scene sm1fs_t007-26 mc-tl-dch-walk_c1 with dissolve
    pause
    #veronica rushes back toward the stage entrance.
    scene sm1fs_t007-26 mc-tl-dch-walk_c2 with dissolve
    pause
    # MC returns to the wings, stage left. Denise stands with arms crossed, watching the stage.
    scene sm1fs_t007-27 mc-tl-dch-pause_c1 with dissolve
    pause
    scene sm1fs_t007-27 mc-tl-dch-pause_c2 with dissolve
    # On stage: Kellie (Mercutio) and Sue Johnson (Tybalt) circle each other with prop switchblades.
    mct "And here is the epic duel between Mercutio and Tybalt."
    scene sm1fs_t007-28 mc-tl-dch-pause2_c1 with hpunch
    # The fight choreography is sharp and aggressive. Sue and Kellie circle each other with blades raised.
    pause
    scene sm1fs_t007-28 mc-tl-dch-pause2_c2 with hpunch
    # Sue lunges forward with a vicious slash. Kellie barely parries, their blades clashing.
    pause
    scene sm1fs_t007-29 mc-tl-dch-pause3_c1 with hpunch
    # They break apart, both breathing hard, circling again.
    pause
    scene sm1fs_t007-29 mc-tl-dch-pause3_c2 with hpunch
    # Sue feints left, then drives the blade forward into Kellie's side.
    pause
    scene sm1fs_t007-30 mc-tl-dch-pause4_c1 with dissolve
    # Kellie gasps, eyes wide with shock, her hand moving to the wound.
    pause
    scene sm1fs_t007-30 mc-tl-dch-pause4_c2 with dissolve
    # Kellie stumbles backward, then collapses to the ground dramatically, her body going limp.
    pause
    scene sm1fs_t007-31 mc-tl-dch-pause5_c1 with dissolve
    # The audience gasps in shock.
    pause
    scene sm1fs_t007-31 mc-tl-dch-pause5_c2 with dissolve
    # Kai (Romeo) bursts onto stage from stage left, face twisted in anguish and rage.
    pause
    scene sm1fs_t007-32 mc-tl-dch-pause6_c1 with dissolve
    # Kai drops to his knees beside Kellie's body, cradling her for a brief moment.
    pause
    scene sm1fs_t007-32 mc-tl-dch-pause6_c2 with dissolve
    # Kai's expression hardens. He rises to his feet, fury in his eyes, and reaches into his jacket.
    pause
    scene sm1fs_t007-33 mc-tl-dch-pause7_c1 with vpunch
    # Kai pulls out a prop pistol, gripping it tightly.
    pause
    scene sm1fs_t007-33 mc-tl-dch-pause7_c2 with dissolve
    # Kai raises the pistol, aiming it directly at Sue with a trembling hand.
    pause
    scene sm1fs_t007-34 mc-tl-dch-knee_c1 with dissolve
    pause
    scene sm1fs_t007-34 mc-tl-dch-knee_c2 with dissolve
    pause
    scene sm1fs_t007-35 mc-tl-dch-stand_c1 with dissolve
    pause
    scene sm1fs_t007-36 mc-tl-dch-point_c1 with dissolve
    pause
    scene sm1fs_t007-37 mc-tl-dch-point2_c1 with dissolve
    pause
    # BANG. The prop gun fires.
    scene sm1fs_t007-38 mc-tl-dch-pouse_c1 with hpunch
    "*gunshot*"
    scene sm1fs_t007-39 mc-tl-dch-pouse2_c1 with vpunch
    pause
    # Sue jerks backward violently, her eyes going wide.
    sj "*death cry*"
    scene sm1fs_t007-39 mc-tl-dch-pouse2_c2 with dissolve
    pause
    # Sue clutches her chest, blood spreading across her Pizza World uniform.
    # Sue collapses to the ground, her body crumpling in a heap.
    scene sm1fs_t007-40 mc-tl-dch-pouse3_c2 with dissolve
    # The stage lights snap to black.
    dvh "*via headset* [mcname], you're up. Get Mercutio off stage. Fifteen seconds before lights up."
    # MC moves onto the darkened stage.
    scene sm1fs_t007-40 mc-tl-dch-pouse3_c1 with dissolve
    pause
    #He crouches beside Kellie and lifts up
    scene sm1fs_t007-41 mc-tl-dch-pouse4_c1 with dissolve
    pause
    #mc carrying km off stage with a fireman's carry.
    scene sm1fs_t007-42 mc-tl-dch-pouse5_c1 with dissolve
    km "*whispers, deadpan* If you drop me, I will really break your leg."
    mc "*whispers* Noted."
    scene sm1fs_t007-43 mc-tl-dch-walk_c1 with dissolve
    # MC carries her offstage
    pause
    # lights turn back on just as the lights turn back on
    scene sm1fs_t007-44 mc-tl-dch-down_c1 with dissolve
    pause
    # MC sets Kellie down gently in the wings.
    scene sm1fs_t007-45 mc-tl-dch-stand_c1 with dissolve
    #She stretches and rolls her shoulders.
    km "*sighs* Every damn production, I'm always the character who dies."
    #km worrying
    km "One day, I have to get a leading role..."
    #mc being supportive
    scene sm1fs_t007-45 mc-tl-dch-stand_c2 with dissolve
    mc "If it's any consolation, your death really played well."
    mc "I heard the audience gasping."
    scene sm1fs_t007-46 mc-tl-dch-talk_c1 with dissolve
    km "*small smirk* Yeah, well. Dying's easy, [mcname]."
    if player.has_played_scene("sm1cs_km006"):
        # Veronica, now in her sexy party dress again, approaches.'
        scene sm1fs_t007-46 mc-tl-dch-talk_c2 with dissolve
        pause
        #veronica complimenting kellie
        scene sm1fs_t007-47 mc-tl-dch-talk2_c2 with dissolve
        vs "Kellie! That was incredible! The way you stumbled before you went down?"
        #vs does a 'chef's kiss' with her hands and lips
        vs "It was awesome."
        # Kellie softens visibly.
        scene sm1fs_t007-48 mc-tl-dch-talk3_c1 with dissolve
        km "Thanks. You don't think the audience was just humoring me, Veronica?"
        scene sm1fs_t007-48 mc-tl-dch-talk3_c2 with dissolve
        vs "What? No way."
        vs "I heard someone in the third row whisper, \"Oh my God, is she okay?\""
        # Kellie chuckles.
        scene sm1fs_t007-49 mc-tl-dch-talk4_c1 with dissolve
        km "*chuckles* Good."
        # Veronica glances at MC, then back at Kellie.
        scene sm1fs_t007-49 mc-tl-dch-talk4_c2 with dissolve
        vs "*playful* We make a good team, huh? The three of us."
        scene sm1fs_t007-50 mc-tl-dch-kiss_c2 with dissolve
        km "*smirking* I guess we do."
        km "On stage.{w} And off."
        # MC catches the subtext and smiles.
        scene sm1fs_t007-50 mc-tl-dch-kiss_c1 with dissolve
        vs "Mmmmuah."
        #vs smiling
        scene sm1fs_t007-52 mc-tl-dch-look_c1 with dissolve
        vs "Kisses for great success."
        #vs kisses mc - quick kiss on lips
        #vs looking at km - km nervous
        km "I don't know."
        vs "Yes, you do."
        #km takes lead and kisses vs
        scene sm1fs_t007-51 mc-tl-dch-kiss2_c1 with dissolve
        km "Mmmmm."
        vs "Ooooh."
        #vs smiles after kiss
        scene sm1fs_t007-53 mc-tl-dch-walk_c1 with dissolve
        vs "Knew you had it in you."
        km "Hehe. Hush now. We don't want the mics to pick up anything."
        vs "Oh yeah."
        #km and vs head off
    # Bruce hands MC a small, ornate glass vial filled with colored water.
    scene sm1fs_t007-54 mc-tl-dch-walk2_c2 with fade
    sb "Here is the vial."
    sb "*whispers* Don't drop it. It's the only one we have."
    sb "If this one breaks, we're going to have to improvise with a Dixie cup."
    mc "*whispers* Shit, no pressure."
    # MC crosses to Taisia, dressed in a male priest's cassock and white collar.
    scene sm1fs_t007-56 mc-tl-dch-look2_c2 with fade
    # MC hands her the vial. She checks the weight.
    tl "*whispers* Thanks. This thing better not leak."
    scene sm1fs_t007-56 mc-tl-dch-look2_c1 with dissolve
    mc "*whispers* I sure hope it won't. Toi toi toi."
    #tl grinning
    scene sm1fs_t007-57 mc-tl-dch-walk_c1 with dissolve
    tl "Merde."
    # Taisia steps onto stage as her cue comes
    #The lights come up on the priest's chamber set.
    scene sm1fs_t007-58 mc-tl-dch-knee_c1 with dissolve
    # On stage: Veronica (Juliet) kneels before Taisia (Priest Lawrence).
    vs "*desperate* Father Lawrence, I can't marry him. I won't. I'd rather die!"
    scene sm1fs_t007-58 mc-tl-dch-knee_c2 with dissolve
    tl "*calmly* Then perhaps...we arrange a death. A temporary one."
    # Taisia holds up the vial. The stage light catches the liquid inside.
    scene sm1fs_t007-59 mc-tl-dch-look_c1 with dissolve
    tl "Drink this tonight. You'll sleep as if dead for forty-two hours."
    tl "Your family will mourn. Romeo will come to retrieve you from the Winnebago."
    scene sm1fs_t007-59 mc-tl-dch-look_c2 with dissolve
    tl "And you'll wake in his arms, free."
    #vs holding the vial - worried
    scene sm1fs_t007-60 mc-tl-dch-look2_c2 with dissolve
    vs "*takes vial, trembling* And if I wake alone?"
    #tl reassuring her
    scene sm1fs_t007-60 mc-tl-dch-look2_c1 with dissolve
    tl "Then we pray the text message gets through."
    # The scene continues. MC watches from the wings, impressed.
    scene sm1fs_t007-60 mc-tl-dch-look2_c3 with dissolve
    mct "Taisia's actually... really good."
    mct "For a moment, I forgot she is the badass, badmouth troublemaker"
    scene sm1fs_t007-61 mc-tl-dch-dead_c1 with fade
    pause
    scene sm1fs_t007-61 mc-tl-dch-dead_c2 with dissolve
    pause

    jump sm1fs_t007_end_of_play

label sm1fs_t007_end_of_play:

    scene black
    show screen scene_transition(_("At the end of the play"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1fs_t007-62 mc-tl-dch-look_c1
    with fade
    pause
    # Optional Montage: Couple more renders of the play's finale if we have time.
    #black screen white text "At the end of the play."
    # TIME SKIP: The play has concluded. #vs and kay are dead from poison and self-inflicted wound
    scene sm1fs_t007-62 mc-tl-dch-look_c2 with dissolve
    pause
    # The full cast stands on stage in a line, holding hands. The lights come up to thunderous applause.
    scene sm1fs_t007-62 mc-tl-dch-look_c3 with dissolve
    pause
    # MC is in the wings, clapping. Bruce claps beside him.
    # Cut to audience: Nelson is on his feet, clapping enthusiastically.
    #A single, solitary tear drips down his cheek.
    nr "I never thought I'd cry about a story of love and tragedy..."
    nr "And pizza and brats."
    #Maya claps beside him, enjoying the moment that her boss got so emotional, and that the play was decent
    scene sm1fs_t007-63 mc-tl-dch-look2_c1 with dissolve
    pause
    # The cast bows in unison.
    # Denise walks onto stage. The applause swells.
    "*audience clapping*"
    scene sm1fs_t007-63 mc-tl-dch-look2_c2 with dissolve
    pause
    scene sm1fs_t007-64 mc-tl-dch-talk_c1 with dissolve
    dvh "Thank you. Thank you all for coming to our opening night."
    dvh "This production has been a labor of love—and occasionally rage—for all of us."
    #alt angle as dvh keeps talking
    scene sm1fs_t007-64 mc-tl-dch-talk_c2 with dissolve
    dvh "This is our main show for the foreseeable future. So tell your friends,{w} tell your enemies,{w} tell anyone who enjoys Shakespeare, pizza, or bratwurst."
    #dvh does a flourish and bow
    dvh "Good night."
    scene sm1fs_t007-65 mc-tl-dch-bow_c1 with dissolve
    # The audience laughs and applauds. The cast takes a final bow.
    pause
    # The lights fade. The curtain closes smoothly.
    scene sm1fs_t007-66 mc-tl-dch-walk_c1 with dissolve
    pause
    # The house lights come up. The audience files out.
    scene sm1fs_t007-67 mc-tl-dch-look_c2 with dissolve
    # MC steps into the lobby area, still in his blacks, headset around his neck.
    # Nelson and Maya approach.
    nr "[mcname]! There he is. Hell of a production."
    nr "Really...uh...intense. *coughs*"
    #mc smiles and talks
    scene sm1fs_t007-67 mc-tl-dch-look_c1 with dissolve
    mc "Yeah, Denise doesn't halfass anything."
    scene sm1fs_t007-68 mc-tl-dch-talk_c2 with dissolve
    nr "*chuckles nervously* I'll say. A lot of death, though."
    #nr didn't know what to expect
    nr "I mean, I knew it was Romeo and Juliet, but...damn. Everyone died."
    #mas reassuring him that it will sell
    scene sm1fs_t007-68 mc-tl-dch-talk_c3 with dissolve
    ms "*deadpan* Only violence and sex sell these days, Nelson."
    ms "This had violence. If they'd added a sex scene, people wouldn't shut up about it for a month."
    if player.has_played_scene("sm1cs_mas003"):
        # Maya catches MC's eye and gives him a subtle, knowing wink.
        ms "[mcname] knows a thing or two about what people like to see on screen."
        ms "And on stage, I bet."
        # MC tries not to react, mc thinking
        scene sm1fs_t007-69 mc-tl-dch-talk2_c1 with dissolve
        mct "Is she...hinting at the sorority thing?"
    scene sm1fs_t007-70 mc-tl-dch-talk3_c3 with dissolve
    nr "Anyway, pass on my thanks to the director and the team. Great work, kid."
    #nr is glad that he invested. he thinks it will get a big return for his store
    # Nelson claps MC on the shoulder and starts toward the exit.
    if player.has_played_scene("sm1cs_mas003"):
        # Maya lingers, stepping close to MC and lowering her voice.
        scene sm1fs_t007-71 mc-tl-dch-talk4_c1 with dissolve
        ms "*low, teasing* You look good in all black, by the way. Very... mysterious."
        # She lets the comment hang, then turns and follows Nelson.
        mct "...I cannot crack what is going on with her."
    # TIME SKIP: The theater is now empty. A single work light illuminates the stage.
    # MC is backstage, moving the sets back to the backstage area. Bruce coils cables nearby.
    scene sm1fs_t007-71 mc-tl-dch-talk4_c2 with dissolve
    pause
    scene sm1fs_t007-73 mc-tl-dch-look_c2 with Fade(0.5, 0.5, 0.5)
    sb "You did well tonight, [mcname]. Real good."
    sb "I can finish up here. You've earned your pay. Head home."
    #mc checks to make sure he is okay
    scene sm1fs_t007-73 mc-tl-dch-look_c1 with dissolve
    mc "You sure? I don't mind helping."
    scene sm1fs_t007-74 mc-tl-dch-walk_c2 with dissolve
    sb "*tiredly* I'm sure. Besides, Denise already signed off on your hours. Get out of here."
    # MC nods, sets the broom aside, and heads toward the exit.
    scene sm1fs_t007-74 mc-tl-dch-walk_c1 with dissolve
    pause
    # As MC walks through the wings and onto the stage, he notices someone in the audience seats.
    scene sm1fs_t007-75 mc-tl-dch-look_c1 with dissolve
    pause
    # Taisia sits in the third row, still in her priest costume—cassock unbuttoned, revealing a tank top. She holds a mostly empty bottle of whiskey.
    scene sm1fs_t007-75 mc-tl-dch-look_c2 with dissolve
    # She raises the bottle in a mock toast.
    tl "*hollers, voice echoing* Oi! Stagehand!"
    tl "Get your ass over here!"
    # MC chuckles and makes his way down into the audience, sliding into the seat next to her.
    scene sm1fs_t007-76 mc-tl-dch-look2_c1 with dissolve
    mc "Celebrating?"
    scene sm1fs_t007-76 mc-tl-dch-look2_c2 with dissolve
    tl "Getting piss drunk. Same thing."
    # She takes a swig and offers the bottle to MC.
    pause
    menu:
        "Take a drink" (hint="sm1fs_t007_m03_h01"):
            $ player.set_choice("sm1fs_t007_take_drink")
            $ CharacterController.get_character("tl").add_point()
            # MC takes a swig. The whiskey burns his throat.
            scene sm1fs_t007-80 mc-tl-dch-swig_c1 with dissolve
            pause
            scene sm1fs_t007-81 mc-tl-dch-cough_c1 with dissolve
            mc "*coughs slightly* Strong."
            #tl grinning
            scene sm1fs_t007-81 mc-tl-dch-cough_c2 with dissolve
            tl "Good for what ails you."


        "Politely decline" (hint="sm1fs_t007_m03_h02"):
            $ player.set_choice("sm1fs_t007_politely_decline")
            scene sm1fs_t007-79 mc-tl-dch-shrug_c2 with dissolve
            mc "I'm good, thanks."
            # Taisia shrugs
            scene sm1fs_t007-79 mc-tl-dch-shrug_c1 with dissolve
            tl "Suit yourself."
            scene sm1fs_t007-77 mc-tl-dch-ask_c2 with dissolve
            pause
            #tl takes another sip

    scene sm1fs_t007-82 mc-tl-dch-talk_c1 with dissolve
    tl "So. What'd you think? Honestly."
    scene sm1fs_t007-82 mc-tl-dch-talk_c2 with dissolve
    mc "Of what?"
    scene sm1fs_t007-83 mc-tl-dch-talk2_c1 with dissolve
    tl "Oh, what? Of me, dummy!"
    menu:
        "You were incredible" (hint="sm1fs_t007_m04_h01"):
            $ player.set_choice("sm1fs_t007_tl_incredible")
            $ CharacterController.get_character("tl").add_point()
            scene sm1fs_t007-83 mc-tl-dch-talk2_c2 with dissolve
            mc "You were incredible. I couldn't take my eyes off you."
            # Taisia looks briefly uncomfortable with the praise.
            scene sm1fs_t007-84 mc-tl-dch-talk3_c1 with dissolve
            tl "*smirks* Yeah, well. I'm a professional."
            tl "*quieter* But...thanks."

        "You looked hot in that outfit" (hint="sm1fs_t007_m04_h02"):
            $ player.set_choice("sm1fs_t007_tl_hot_outfit")
            $ CharacterController.get_character("tl").add_point()
            scene sm1fs_t007-84 mc-tl-dch-talk3_c2 with dissolve
            mc "You looked hot in that priest outfit."
            #mc grinning
            mc "Very \"forgive me, Father for I have sinned\" vibes."
            scene sm1fs_t007-87 mc-tl-dch-talk_c1 with dissolve
            # Taisia barks a laugh and shakes her head.
            tl "*laughs* You're such a perv. But I can respect that."
            # tl thinking
            tl "Maybe I just gave you a new idea for a porno."
            tl "If I did, I want a producer credit."
            #mc laughing
            scene sm1fs_t007-87 mc-tl-dch-talk_c2 with dissolve
            mc "Haha. Sure."

        "It was solid" (hint="sm1fs_t007_m04_h03"):
            $ player.set_choice("sm1fs_t007_solid")
            scene sm1fs_t007-85 mc-tl-dch-look_c2 with dissolve
            mc "It was solid. Everyone brought their A-game."
            # Taisia nods.
            scene sm1fs_t007-86 mc-tl-dch-look2_c1 with dissolve
            tl "Damn right we did."

    # Taisia leans back, staring up at the dark stage lights.
    scene sm1fs_t007-85 mc-tl-dch-look_c1 with dissolve
    tl "You busted your ass tonight. Denise noticed. Bruce noticed."
    tl "That's good. You showed them you're not just some dipshit playing dress-up."
    #mc is amused by her priase
    scene sm1fs_t007-85 mc-tl-dch-look_c2 with dissolve
    mc "High praise coming from you."
    scene sm1fs_t007-86 mc-tl-dch-look2_c1 with dissolve
    tl "*smirks* Don't let it go to your head."
    # She takes another drink, then looks at him more seriously.
    tl "But real talk? Theater's great for the resume and the \"craft\" or whatever."
    #tl is excited to be working at mc's porn studio
    scene sm1fs_t007-87 mc-tl-dch-talk_c1 with dissolve
    tl "But the real money—the fun money—is waiting for us back at the studio."
    if not player.get_choice("pirates_movie_done") and not player.get_choice("scifi_movie_done") and player.has_played_scene("sm1mv01s01"):
        scene sm1fs_t007-87 mc-tl-dch-talk_c2 with dissolve
        mc "You know I'm not sitting around."
        mc "This pirate movie is going to be great."
        #tl about to sip
        scene sm1fs_t007-88 mc-tl-dch-talk2_c1 with dissolve
        tl "I'm counting on it."
        tl "Counting on you too."
        #tl sips drink
    if player.get_choice("pirates_movie_done") and not player.get_choice("scifi_movie_done"):
        scene sm1fs_t007-88 mc-tl-dch-talk2_c2 with dissolve
        mc "I'm already working on another film. We've got momentum."
        scene sm1fs_t007-89 mc-tl-dch-cheer_c1 with dissolve
        tl "*perks up* Yeah? Good. Keep that shit rolling. I need another paycheck."
    elif player.get_choice("scifi_movie_done") and player.get_choice("pirates_movie_done"):
        scene sm1fs_t007-89 mc-tl-dch-cheer_c2 with dissolve
        mc "Don't worry. As long as the films we've made start selling, you'll keep getting roles."
        mc "You're our star."
        #tl raises the bottle.
        scene sm1fs_t007-90 mc-tl-dch-swig_c1 with dissolve
        tl "*raises bottle in toast* That's what I like to hear."
        #tl takes a sip
        #tl done drinking
        tl "I hope we can do films for a while. You and I."
        tl "Don't fuck it up."
    else:
        scene sm1fs_t007-89 mc-tl-dch-cheer_c2 with dissolve
        mc "We're working on it. Trust me."
        scene sm1fs_t007-90 mc-tl-dch-swig_c1 with dissolve
        tl "Uh-huh. Just don't leave me hanging. I like eating regularly."
    # Taisia finishes the bottle and stands,
    #tl stretching
    scene sm1fs_t007-91 mc-tl-dch-help_c1 with fade
    tl "Alright. I'm out. Later, loser."
    scene sm1fs_t007-91 mc-tl-dch-help_c2 with dissolve
    mc "Later."
    # She saunters up the aisle and tosses the empty bottle into a recycling bin with perfect accuracy.
    # MC sits alone for a moment in the empty theater.
    #mc looks around thinking
    scene sm1fs_t007-92 mc-tl-dch-stand_c1 with dissolve
    pause
    scene sm1fs_t007-94 mc-tl-dch-walk_c1 with dissolve
    pause
    scene sm1fs_t007-94 mc-tl-dch-walk_c2 with hpunch
    pause
    scene sm1fs_t007-94 mc-tl-dch-walk_c3 with dissolve
    mct "How cool would it be if I ever showed one of my films on the big screen?"
    mct "A whole theater full of people who come to see my ideas."
    mct "Well, Stacy and my ideas."
    #mc smiling
    scene sm1fs_t007-95 mc-tl-dch-walk2_c1 with dissolve
    mct "I'm sure she wouldn't mind."
    # He stands and heads for the exit.
    # Fade to black.
    #timeslot retuned to is Saturday Nightfall

    $ StoryController.end_scene(THEATER_STORY_LINE)
    return
