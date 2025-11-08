label sm1cs_am008:

    #mc is at nice restaurant - we used this restaurant from Dahlia ending - nice restaurant. - mc is talking to a waiter - Timeslot - Just before Nighttime
    scene sm1cs-am008-1-01 mc-ap-entry1_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Uhh. I'm supposed to meet a date here."
    mc "April Mercer."
    #waiter brings him toward a table
    scene sm1cs-am008-1-01 mc-ap-entry1_c2 with dissolve
    play voice4 boy5_yes_ugu1 noloop
    pause
    #am  dressed up in a nice dress standing near the table
    scene sm1cs-am008-1-02 mc-ap-entry2_c1 with dissolve
    pause
    #am brushes a hand back through her hair
    scene sm1cs-am008-1-03 mc-ap-talk_c2 with dissolve
    play voice3 girl22_hey_simple noloop
    am "Hey."
    menu:
        "She looks jaw droppingly gorgeous" (hint = "sm1cs_am008_m01_h01"):
            $ player.set_choice("sm1cs_am008_jaw_dropping")
            scene sm1cs-am008-1-04 mc-ap-talk2_c1 with dissolve
            play voice2 d3s7_mcemm noloop
            mc "..."
            mc "April. You look."
            #nice shot of april - she looks a bit nervous
            mc "Gorgeous."
            #am talking to him
            scene sm1cs-am008-1-04 mc-ap-talk2_c2 with dissolve
            play voice3 girl22_thinking_hmm2 noloop
            am "Quick gawking at me like a sweaty convention goer seeing a cosplayer."
            am "I wore this to have a nice meal."
            am "Not to get drooled on."
            scene sm1cs-am008-1-07 mc-ap-sit_c2 with dissolve
            #am smiles
            play voice3 girl22_thinking_hmm1 noloop
            am "Thank you."

            jump sm1cs_am008_continue

        "She's been replaced by a pod person" (hint = "sm1cs_am008_m01_h02"):
            $ player.set_choice("sm1cs_am008_pod_person")
            #mc is suspicious - mc talking
            scene sm1cs-am008-1-05 mc-ap-talk3_c1 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "Wait a minute."
            mc "Is this a trap? I feel like I'm about to get pie on my face."
            #am is confused
            scene sm1cs-am008-1-04 mc-ap-talk2_c2 with dissolve
            play voice3 girl22_surprised_huh2 noloop
            am "What?"
            #am is a bit embarrassed
            am "I was just trying to-"

            jump sm1cs_am008_second_menu

label sm1cs_am008_second_menu:

    am "Do something nice."
    menu:
        "I'm sorry" (hint = "sm1cs_am008_m02_h01"):
            $ player.set_choice("sm1cs_am008_apologise")
            #mc realizing he was acting stupid
            scene sm1cs-am008-1-04 mc-ap-talk2_c1 with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "I'm sorry, April."
            mc "I just... I don't know if I ever expected to see you in a dress like this."
            #am rolls her eyes
            scene sm1cs-am008-1-05 mc-ap-talk3_c2 with dissolve
            play voice3 girl22_thinking_oh noloop
            am "What a pleasure to know you think you know everything about me, [mcname]."
            #am neutral and mc worried
            #am smiles
            am "I'm just busting your balls. Figuratively."
            scene sm1cs-am008-1-07 mc-ap-sit_c1 with dissolve
            play voice2 mc_happy_laugh2 noloop
            mc "Ah. Haha. Let's sit down before I say something else dumb."
            #am moving to sit down
            scene sm1cs-am008-1-07 mc-ap-sit_c2 with dissolve
            play voice3 girl22_yes_aga1 noloop
            am "Good idea."
            #mc sits down

        "Nice isn't your natural state" (hint = "sm1cs_am008_m02_h02"):
            $ player.set_choice("sm1cs_am008_nice_not_natural")
            #am sits down with a bit of a huff
            scene sm1cs-am008-1-07 mc-ap-sit_c1 with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "Nice isn't your natural state."
            #am looks up at mc
            scene sm1cs-am008-1-07 mc-ap-sit_c2 with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "Well come on. You can't eat dinner standing up."
            #mc approaches the table.

    jump sm1cs_am008_continue

label sm1cs_am008_continue:

    #mc handing a menu to the waiter - talking to waiter - there is glasses of wine at the table now
    scene sm1cs-am008-1-09 mc-ap-talk_c1 with fade
    play voice2 mc_yes_yes1 noloop
    mc "That sounds great. Thanks."
    scene sm1cs-am008-1-09 mc-ap-talk_c2 with dissolve
    play voice4 boy5_thinking_hmm7 noloop
    "Waiter" "Very good sir. I shall return to check on your glasses in a moment."
    #waiter leaves
    #am looks a little uncomfortable.
    scene sm1cs-am008-1-11 mc-ap-talk3_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Everything alright?"
    #am looks up at him
    scene sm1cs-am008-1-11 mc-ap-talk3_c2 with dissolve
    #am puts on a nervous smile
    play voice3 girl22_thinking_eeh noloop
    am "I've felt more comfortable in a bra and gym shorts at a code session at Orbix."
    #mc laughing
    scene sm1cs-am008-1-12 mc-ap-talk3_c1 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Now that's a sight to imagine."
    #am holds up her glass
    scene sm1cs-am008-1-12 mc-ap-talk3_c2 with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "I don't know how people do this all the time."
    am "I can code a subroutine to hunt through thousands of lines of code in two hours flat."
    #pull back shot showing the two of them - am and mc drinking
    scene sm1cs-am008-1-13 mc-ap-wine_c1 with dissolve
    pause
    scene sm1cs-am008-1-13 mc-ap-wine_c2 with dissolve
    pause
    scene sm1cs-am008-1-14 mc-ap-talk_c2 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "But make small talk? Kill me now."
    scene sm1cs-am008-1-14 mc-ap-talk_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Can't do that."
    scene sm1cs-am008-1-14 mc-ap-talk_c2 with dissolve
    play voice3 girl22_hey_attention noloop
    am "Come on, do me a solid."
    #mc grinning
    scene sm1cs-am008-1-15 mc-ap-talk2_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I was raised never to kill a girl."
    mc "And besides, if I did that, I'd get stuck with the check."
    #am takes a deep breath
    scene sm1cs-am008-1-15 mc-ap-talk2_c2 with dissolve
    play voice3 girl22_happy_relief noloop
    am "You're not as dumb as you look."
    scene sm1cs-am008-1-16 mc-ap-talk3_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "Nice of you to finally notice."
    # am thumbing her glass
    scene sm1cs-am008-1-15 mc-ap-talk2_c2 with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "Alright. I'm diving in."
    am "You said you were raised well. Does your family live in the city?"
    scene sm1cs-am008-1-16 mc-ap-talk3_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes."
    #am asking another question
    scene sm1cs-am008-1-16 mc-ap-talk3_c2 with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "What are they?{w} I mean who are they?"
    #am worrying
    am "God. I mean... like. {w}Parents and siblings?"
    scene sm1cs-am008-1-17 mc-ap-talk4_c1 with dissolve
    if persistent.is_special:
        play voice2 mc_thinking_hmm5 noloop
        mc "Mother and a sister."
        #am plays a finger on her wine glass' rim
        scene sm1cs-am008-1-17 mc-ap-talk4_c2 with dissolve
        play voice3 girl22_yes_yeah4 noloop
        am "Close with them?"
        #mc thinks for a minute
        scene sm1cs-am008-1-18 mc-ap-talk5_c1 with dissolve
        play voice2 mc_surprised_oh1 noloop
        mc "Oh as close as you can be."
        mct "Now is definitely not the time to tell her I live with my sister and occasionally bang her on a big bed."
    else:
        #mc doesn't talk about his family much.
        play voice2 mc_yes_yeah1 noloop
        mc "Yeah..."
        #am taking a sip from her glass
        scene sm1cs-am008-1-18 mc-ap-talk5_c2 with dissolve
        play voice3 girl22_yes_yeah4 noloop
        am "Yeah? Doesn't sound like you're close."
        scene sm1cs-am008-1-19 mc-ap-talk6_c1 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "Close enough."
        #mc taking a drink from his cup
        mc "Recently got some pushback when I left college."
        scene sm1cs-am008-1-19 mc-ap-talk6_c2 with dissolve
        play voice3 girl22_yes_aga4 noloop
        am "Had to expect that, right?"
        #am smiling and talking to mc
        am "Or did they always know you were thickheaded?"
        scene sm1cs-am008-1-20 mc-ap-waiter_c1 with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "I think they had some clue."
        #am laughing
        scene sm1cs-am008-1-20 mc-ap-waiter_c2 with dissolve
        play voice3 girl22_happy_laugh1 noloop
        am "Haha."
    #plates arrive for am and mc - fade in
    scene sm1cs-am008-1-21 mc-ap-talk_c1 with fade
    #mc eating some of his meal
    play voice2 mc_surprised_uh2 noloop
    mc "What about you?"
    #am kind of sighs
    scene sm1cs-am008-1-21 mc-ap-talk_c2 with dissolve
    play voice3 girl22_disappointed_oh noloop
    am "I try to keep in touch with a sister who never learned how to stay still."
    am "Dad is gone. My mom is uh..."
    #am is a little uncomfortable talking about her mom - but she pushes through
    am "She's fine. But to this day, she wishes she never let me touch a computer."
    #mc laughing
    scene sm1cs-am008-1-21-1 mc-ap-talk2_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.7
    mc "Haha."
    mc "Why is that?"
    #am knows exactly why her mom doesn't like her style
    scene sm1cs-am008-1-21-1 mc-ap-talk2_c2 with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "I imagine she wishes me or my sister was more cookie-cutter normal."
    #am preparing to take another bite
    scene sm1cs-am008-1-21-2 mc-ap-talk3_c2 with dissolve
    play voice3 girl22_disgust_meeh noloop
    am "Tea parties. Cheer practice."
    am "No college. Just a high-school degree that would sit on the shelf after getting married at eighteen."
    menu:
        "Nothing wrong with that" (hint = "sm1cs_am008_m03_h01"):
            $ player.set_choice("sm1cs_am008_nothing_wrong")
            #mc kind of sees it as parents being parents
            scene sm1cs-am008-1-22 mc-ap-talk2_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "A little planning isn't too bad, right?"
            #am doesn't think of this as a good plan
            scene sm1cs-am008-1-21-3 mc-ap-talk4_c2 with dissolve
            play voice3 girl22_surprised_oh noloop
            am "*sarcastically* Oh sure. Nice to have your life planned out from five to fifty."
            am "Is that what you want, [mcname]?"
            #am really doesn't like the idea
            am "Your life set out in a nice little package. No excitement. Nothing unexpected."
            am "Just talking about it makes me ready to fall asleep."
            #am happy
            scene sm1cs-am008-1-21-4 mc-ap-talk5_c2 with dissolve
            play voice3 girl22_thinking_hmm2 noloop
            am "But the universe is a chaotic place. Or at least the kind of place that wanted..."
            #am shrugged
            am "Or expects more out of me."
            #am's face is building to a smile
            scene sm1cs-am008-1-21-5 mc-ap-talk6_c2 with dissolve
            play voice3 girl22_surprised_eh1 noloop
            am "I had a tutor three times a week. One day, they got sick."
            am "My mom was desperate. A missed lesson is like losing a month of school."
            #am's smile grows big
            am "The sub that came in couldn't teach me my regular lessons."
            am "But they were very skilled in the arena of coding."

        "That is oddly specific" (hint = "sm1cs_am008_m03_h02"):
            $ player.set_choice("sm1cs_am008_nothing_wrong")
            scene sm1cs-am008-1-22 mc-ap-talk2_c1 with dissolve
            play voice2 mc_thinking_hmm7 noloop
            mc "That sounds oddly specific, April."
            scene sm1cs-am008-1-21-5 mc-ap-talk6_c2 with dissolve
            play voice3 girl22_surprised_oh noloop
            am "Clever boy."
            am "My mom had a plan for both my sister and I."
            scene sm1cs-am008-1-21-4 mc-ap-talk5_c2 with dissolve
            play voice3 girl22_thinking_hmm2 noloop
            am "My sister started going down the left hand path first. And that just meant that my mom pushed me harder."
            am "For a while I played ball."
            am "Until one night, my usual tutor was sick so a sub was brought to the house."
            scene sm1cs-am008-1-21-3 mc-ap-talk4_c2 with dissolve
            play voice3 girl22_surprised_eh1 noloop
            am "They were... ill prepared for my regular lessons."
            am "But they knew a lot about coding."

        "Parents think they know best" (hint = "sm1cs_am008_m03_h03"):
            $ player.set_choice("sm1cs_am008_know_best")
            scene sm1cs-am008-1-22 mc-ap-talk2_c1 with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "Parents never get tired of thinking they know best."
            #am very happy to agree with him
            scene sm1cs-am008-1-21-5 mc-ap-talk6_c2 with dissolve
            play voice3 girl22_yes_yeah3 noloop
            am "A-fucking-men."
            am "But one day, the least likeliest thing happened."
            #am enjoying the memory
            scene sm1cs-am008-1-21-4 mc-ap-talk5_c2 with dissolve
            play voice3 girl22_thinking_hmm2 noloop
            am "I had a tutor that came to give me lessons."
            am "But one day they got sick. They sent in a sub who wasn't prepared at all."
            #alt angle
            am "Fortunately for me, they knew a lot about coding, and liked to talk about it."

    #am smiling
    scene sm1cs-am008-1-21-2 mc-ap-talk3_c2 with dissolve
    play voice3 girl22_happy_mmm noloop
    am "It was so... different than anything else I had known before."
    #mc understanding her a bit more
    scene sm1cs-am008-1-23 mc-ap-ask_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "So that's how coding started for you."
    scene sm1cs-am008-1-23 mc-ap-ask_c2 with dissolve
    play voice3 girl22_yes_happy noloop
    am "Yes. I couldn't get enough of it. Even when my mom found my books and hid them, I just ended up spending afternoons in the library."
    am "That first rebellion began my descent into the loveable troublemaker you see before you."
    #mc and am laughing
    scene sm1cs-am008-1-24 mc-ap-talk_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "Hahah."
    play voice3 girl22_happy_laugh3 noloop
    am "*chuckles*"
    #mc asks her about her music
    mc "What about your music."
    #am gives him a subtle smile
    scene sm1cs-am008-1-24 mc-ap-talk_c2 with dissolve
    play voice3 girl22_thinking_oh noloop
    am "Remembered that did you?"
    scene sm1cs-am008-1-25 mc-ap-talk2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "I never forget a beautiful musician."
    #am using knife and fork on her steak
    scene sm1cs-am008-1-25 mc-ap-talk2_c2 with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "You must be talking about someone else."
    play voice2 mc_no_nope1 noloop
    mc "Nope."
    #am is amused
    am "Take a bite from your steak or do something that stops you from looking at me like that."
    menu:
        "Like what?" (hint = "sm1cs_am008_m04_h01"):
            $ player.set_choice("sm1cs_am008_like_what")
            scene sm1cs-am008-1-26 mc-ap-talk3_c1 with dissolve
            play voice2 mc_surprised_what1 noloop
            mc "Like what?"
            scene sm1cs-am008-1-26 mc-ap-talk3_c2 with dissolve
            play voice3 girl22_sex_closedmoan1 noloop
            am "Like a hungry wolf."
            #mc laughing
            play voice2 d3s11b_mcheh noloop volume 1.4
            mc "*chuckles*"

        "I can't help it" (hint = "sm1cs_am008_m04_h02"):
            $ player.set_choice("sm1cs_am008_cant_help_it")
            $ CharacterController.get_character("am").add_point(2)
            #mc enjoying the moment
            scene sm1cs-am008-1-27 mc-ap-ask_c1 with dissolve
            play voice2 mc_disappointed_off2 noloop
            mc "I can't help it."
            #am smiling

    #am eating some food
    scene sm1cs-am008-1-27 mc-ap-ask_c2 with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "My mom's... passionate drive for my selective education gave me a strong impulse to rebel."
    am "You may have noticed...{w} I'm a 'fight fire with fire' kind of girl."
    #cleavage shot of am's boobs - not too close, and shot from the side
    am "And it only got more intense when I started getting better at coding than a lot of guys my age."
    scene sm1cs-am008-1-28 mc-ap-waiter_c1 with dissolve
    #mc curious
    play voice2 mc_arrogant_heh1 noloop
    mc "Heh. Do you fight fire with fire with your bandmates?"
    #am loves her bandmates, but they frustrate her
    scene sm1cs-am008-1-28 mc-ap-waiter_c2 with dissolve
    play voice3 girl22_disappointed_geh noloop
    am "They uh... they're frustrating. But I do my best to keep a cool head."
    am "Pepper and even Mitch... {w} They both helped me curb some of my bad impulses."
    #mc eating and listening to am tell her story
    am "Before I wound up in Orbix, my modus operandi was all about learning new tricks and tips for coding."
    am "Stuff that gave me an edge over other code monkeys, either to embarrass them or land a job over them."
    #am doesn't like talking about this
    scene sm1cs-am008-1-29 mc-ap-ask_c2 with dissolve
    play voice3 girl22_disappointed_ehh1 noloop
    am "I started hanging out with some people. The kind of people who-"
    am "Well, they use computer skills to cause problems."
    #am prefers to leave things unsaid
    am "Let's leave it at that."
    scene sm1cs-am008-1-29 mc-ap-ask_c1 with dissolve
    #mc figures it out - am is like what did I just tell you?
    play voice2 mc_thinking_hmm6 noloop
    mc "So... like, real hackers."
    scene sm1cs-am008-1-29 mc-ap-ask_c2 with dissolve
    play voice3 girl22_hey_scared noloop
    am "What did I just say, [mcname]?"
    #mc asking a thing - am is like - please dont
    scene sm1cs-am008-1-30 mc-ap-ask2_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Sorry. {w}Can I ask one thing?"
    play voice3 girl22_yes_aga11 noloop
    am "Must you?"
    mc "Did you ever do anything criminal?"
    #am is serious - mc is glad to hear it
    scene sm1cs-am008-1-30 mc-ap-ask2_c2 with dissolve
    play voice3 girl22_no_questioning noloop
    am "No. {w}Well, nothing that hurt anyone. And nothing that I could get arrested for."
    #mc is glad to hear that
    scene sm1cs-am008-1-31 mc-ap-look_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Good."
    mc "So you met these people and raised a little hell with them."
    scene sm1cs-am008-1-31 mc-ap-look_c2 with dissolve
    play voice3 girl22_yes_yeah1 noloop
    am "Yeah. And I started... I really liked it too."
    am "It was easy..."
    #am kind of sexy look
    am "Being {b}bad{/b}."
    #am bittersweet smile
    scene sm1cs-am008-1-29 mc-ap-ask_c2 with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "Luckily, Pepper saw what I was turning into me. She's known me the longest and accepted me when I started becoming a coder."
    am "She pulled me out, convinced me that I was going down a path that would change me."
    #am talking about how at first she resisted Pepper
    am "At first I told her to 'fuck off'. But she kept trying."
    am "Like, I don't think I've ever met someone so annoying."
    #am bitter sweet smile
    scene sm1cs-am008-1-30 mc-ap-ask2_c2 with dissolve
    play voice3 girl22_happy_mmm noloop
    am "But she didn't quit. She kept texting me, telling me I didn't need to let my anger control me."
    am "And one night it clicked. That I should use my knowledge to create instead of destroy."
    #am drinks
    scene sm1cs-am008-1-32 mc-ap-drink_c2 with dissolve
    #am is done drinking
    play voice3 girl22_thinking_eeh noloop
    am "Pepper convinced me to pick up my music lessons where I had left off, and join her band."
    #am is amused
    am "Good thing too. That same group I was working with kept on keeping on."
    am "Almost exactly two months after I left them, one nearly died in a car crash and one got arrested."
    #mc asks if it was bad luck
    scene sm1cs-am008-1-33 mc-ap-talk_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Bad luck?"
    scene sm1cs-am008-1-33 mc-ap-talk_c2 with dissolve
    play voice3 girl22_no_simple noloop
    am "No. They were doing something very stupid."
    #am thinking how close she was to still being a part of the stupid group
    am "I probably would have gotten caught up in it too, if I didn't listen to Pepper."
    #mc just thinking - that's a lot
    scene sm1cs-am008-1-34 mc-ap-talk2_c1 with dissolve
    #mc talking
    play voice2 mc_happy_a1 noloop
    mc "I see now why you struggle so much with leaving your band."
    scene sm1cs-am008-1-34 mc-ap-talk2_c2 with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "Yeah..."
    #am kind of embarrassed now, not sure if she should be so vulnerable
    am "Fuck. I shouldn't have told you."
    scene sm1cs-am008-1-35 mc-ap-ask_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "It's alright, April. Sometimes it's good to get things off your chest."
    scene sm1cs-am008-1-35 mc-ap-ask_c2 with dissolve
    play voice3 girl22_yes_yep4 noloop
    am "Maybe."
    #am appreciating that hey are similar
    am "We're kind of kindred spirits in this, aren't we?"
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Huh?"
    am "You left college right? It was a big change, but you wanted to start a new path."
    scene sm1cs-am008-1-32 mc-ap-drink_c1 with dissolve
    menu:
        "Something like that?" (hint = "sm1cs_am008_m05_h01"):
            $ player.set_choice("sm1cs_am008_something_like_that")
            play voice2 mc_thinking_hmm5 noloop
            mc "Something like that."
            mc "I just hope it is the right one."
            scene sm1cs-am008-1-32 mc-ap-drink_c2 with dissolve
            play voice3 girl22_thinking_oh noloop
            am "I think it is. If you hadn't come to Orbix, we wouldn't have met."
            am "It feels like the numbers crunched out a positive."
            am "For both of us."

        "You had a choice. I didn't" (hint = "sm1cs_am008_m05_h02"):
            $ player.set_choice("sm1cs_am008_you_had_choice")
            $ CharacterController.get_character("am").deduct_point()
            play voice2 mc_thinking_hmm5 noloop
            mc "It's not the same."
            mc "I had to leave that part of my life behind."
            mc "You had a choice."
            scene sm1cs-am008-1-32 mc-ap-drink_c2 with dissolve
            play voice3 girl22_thinking_oh noloop
            am "You're right."
            #am looks at him earnestly
            am "Sorry. I just like... thinking of what we have in common."

    #am is happy
    scene sm1cs-am008-1-33 mc-ap-talk_c2 with dissolve
    play voice3 girl22_thinking_hmm2 noloop
    am "I think {b}that{/b} is what started this crush...{w} You reminded me that I am more than just coding."
    am "And bitchiness."
    #mc is glad that she is opening up - shot of the two of them
    scene sm1cs-am008-1-34 mc-ap-talk2_c2 with dissolve
    play voice3 girl22_happy_relief noloop
    am "I have other sides of me. {w}I want to share one with you."
    #mc asks her a question - am looks amused
    scene sm1cs-am008-1-34 mc-ap-talk2_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "What side is that?"
    scene sm1cs-am008-1-34 mc-ap-talk2_c2 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "Don't get chicken on me. It's a side I've shown you before."
    am "And I'm pretty sure you liked it."
    #mc smiling
    scene sm1cs-am008-1-36 mc-ap-look_c1 with dissolve
    play voice2 d9s2_ugu noloop volume 1.7
    mc "You bet I did."
    #am likes the sound of that
    #the two finish up their meals
    #waiter takes their plates away
    scene sm1cs-am008-1-37 mc-ap-waiter_c2 with dissolve
    #am talking to the waiter
    play voice3 girl22_yes_aga4 noloop
    am "Bill it to room two-two-seven, please."
    scene sm1cs-am008-1-37 mc-ap-waiter_c1 with dissolve
    play voice4 boy5_yes_ugu2 noloop
    "Waiter" "Of course, madam."
    #am gets up, mc gets up too
    #am strokes his chest - enjoying the look of him
    scene sm1cs-am008-1-38 mc-ap-stand_c2 with dissolve
    #am looks up at mc
    play voice3 girl22_hey_simple noloop
    am "Follow me."
    scene sm1cs-am008-1-40 mc-ap-walk_c2 with dissolve
    pause
    ###Part 2 - The Hotel Room
    #mc and am walking into a luxury hotel room - Timeslot - Night time
    scene sm1cs-am008-2-00 hotel_fun_mc_talk with Fade(0.5, 0.5, 0.5)
    play voice2 mc_surprised_wow4 noloop
    mc "Nice."
    scene sm1cs-am008-2-01 hotel_fun_am_talk with dissolve
    play voice3 girl22_yes_yep5 noloop
    am "Perks of working for the premier IT company in the state."
    #am taking off her shoes
    scene sm1cs-am008-2-02 hotel_fun_am_talk_shoesoff with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "They don't know what to pay me, so I high-balled them and they went for it."
    scene sm1cs-am008-2-03 hotel_fun_am_talk_holdshoesdown with dissolve
    play voice3 girl22_happy_relief noloop
    am "Ooof. Finally."
    #am holding the nice high heels
    am "I think I'd rather walk through fire than where shoes like these all the time."
    #mc holds her hand and the shoes
    scene sm1cs-am008-2-04 hotel_fun_mc_talk_holdshand with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "They looked great on you."
    scene sm1cs-am008-2-05 hotel_fun_am_talk with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "I'm more than just my looks, you mug."
    #mc puts the shoes down
    scene sm1cs-am008-2-06 hotel_fun_mc_talk_up with dissolve
    #mc is back up, looking at her, touching her gently - am liking it
    play voice2 mc_thinking_hmm4 noloop
    mc "I know."
    #mc looks at her forehead
    mc "You got that big melon that won't stop ticking."
    scene sm1cs-am008-2-08 hotel_fun_am_talk_horny with dissolve
    #am looks horny for a moment
    play voice3 girl22_sex_closedmoan2 noloop
    am "Mmm."
    #am looks mad at mc, but it is playful - she steps away from him - turning her shoulder towards him - turning her body too
    scene sm1cs-am008-2-09 hotel_fun_am_talk_turnplayful with dissolve
    play voice3 girl22_no_uhuh1 noloop
    am "Don't think you're getting the full menu so easily."
    am "I'm still mad at you."
    #mc is confused
    scene sm1cs-am008-2-10 hotel_fun_mc_talk_confused with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "For what?"
    scene sm1cs-am008-2-11 hotel_fun_am_talk_earlier with dissolve
    #am talking about earlier - when he first saw her in the dress
    play voice3 girl22_disappointed_ehh2 noloop
    am "When you saw me, I thought you'd..."
    #am embarrassed - looking to the side - nervous awkward
    am "I don't know. Come kiss me."
    am "And what did I get? Not even a peck on the cheek."
    #mc says he froze up
    scene sm1cs-am008-2-12 hotel_fun_am_talk_embarrassed with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I think seeing you, it reset me to factory defaults."
    mc "I froze up."
    #am enjoys hearing that
    scene sm1cs-am008-2-14 hotel_fun_am_talk_happy with dissolve
    play voice3 girl22_yes_questioning noloop
    am "I look that good, do I?"
    #am turns her body - kind of reaching out her hands, doing a little flourish
    scene sm1cs-am008-2-15 hotel_fun_am_talk_turn_hand with dissolve
    play voice3 girl22_happy_mmm noloop
    am "Like a sexy alien spy seducing the wicked jailor."
    scene sm1cs-am008-2-16 hotel_fun_mc_talk_turn with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "You think I'm wicked?"
    #am believes there is something more to him
    scene sm1cs-am008-2-17 hotel_fun_am_talk with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "Mmm. Not wicked. But I think there are parts of you that you keep locked up."
    #mc comes closer to her again
    scene sm1cs-am008-2-19 hotel_fun_mc_talk_hip with dissolve
    play voice2 mc_no_no6 noloop
    mc "I'm an open book."
    #mc's hands touching her hips
    mc "But some chapters are further than just the opening few."
    #am is getting horny again
    scene sm1cs-am008-2-20 hotel_fun_am_talk with dissolve
    play voice3 girl22_yes_yep1 noloop
    am "Fair."
    #am is a little nervous, breathing harder
    scene sm1cs-am008-2-22 hotel_fun_am_talk_turnaway with dissolve
    play voice3 girl22_sex_closedmoan3 noloop
    am "But... we don't need to keep talking about books, do we, [mcname]?"
    am "I like this dress."
    #am turns to face away from mc
    am "But I also want to see how much of an effect it has on you."
    #am turns back to look at him
    scene sm1cs-am008-2-23 hotel_fun_am_talk_turnback with dissolve
    play voice3 girl22_surprised_huh1 noloop
    am "Can you... help me out here?"
    #mc removes the dress - underneath is black lingerie
    scene sm1cs-am008-2-24 hotel_fun_mc_talk_dress with dissolve
    pause
    scene sm1cs-am008-2-26 hotel_fun_mc_talk with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Woah."
    scene sm1cs-am008-2-27 hotel_fun_am_talk with dissolve
    play voice3 girl22_angry_cough noloop
    am "Don't stare."
    play voice2 mc_no_uhuh1 noloop
    mc "I'm not."
    am "I can feel it, idiot."
    scene sm1cs-am008-2-28 hotel_fun_mc_talk with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Well damn, April. You are wearing sexy as fuck lingerie."
    scene sm1cs-am008-2-29 hotel_fun_am_talk with dissolve
    play voice3 girl22_disappointed_geh noloop
    am "Shut up."
    #mc turns her around
    scene sm1cs-am008-2-30 hotel_fun_mc_talk_makeme with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Make me."
    scene sm1cs-am008-2-31 hotel_fun_am_talk with dissolve
    play voice3 girl22_sex_closedmoan5 noloop
    am "Eeep."
    #mc kisses her - shot from the side - intense passionate kiss of the two
    scene sm1cs-am008-2-32 hotel_fun_am_talk_kiss with dissolve
    play sound dahlia_kiss_french1
    play voice3 girl22_sex_closedmoan6 noloop
    am "Mmmm."
    #am's eyes close - alt shot of the kiss
    scene sm1cs-am008-2-33 hotel_fun_am_talk_kiss with dissolve
    queue sound mc_kiss1
    play voice2 d1s1_mmm noloop
    pause
    #end of the kiss - april is a bit breathless
    scene sm1cs-am008-2-34 hotel_fun_am_talk_panting with dissolve
    play voice3 girl22_angry_breathing noloop
    am "*panting*"
    am "Woah."
    #mc reaches to undo her lingerie."
    scene sm1cs-am008-2-35 hotel_fun_mc_talk_undo bra with dissolve
    play voice2 mc_thinking_mmm2 noloop
    pause
    #am stops him
    scene sm1cs-am008-2-36 hotel_fun_am_talk_stop with dissolve
    play voice3 girl22_hey_attention noloop
    am "Wait. I have one more thing."
    #am goes over to around to the other side of the bed
    scene sm1cs-am008-2-37 hotel_fun_am_talk_walksidebed with dissolve
    pause
    #am bends over - showing her ass
    scene sm1cs-am008-2-39 hotel_fun_mc_talk_takeoff with dissolve
    pause
    #mc takes off his jacket
    scene sm1cs-am008-2-40 hotel_fun_mc_talk_walkback_shirtoff with dissolve
    pause
    #mc lays jacket down on chair - am is coming back with something.
    scene sm1cs-am008-2-42 hotel_fun_mc_talk_holdouthand with dissolve
    #am holds the thing behind her back - she is playing at being cute
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Got something for me?"
    scene sm1cs-am008-2-41 hotel_fun_am_talk with dissolve
    play voice3 girl22_yes_questioning noloop
    am "Maybe?"
    mct "She's... acting bashful?"
    #mc holds out a hand
    scene sm1cs-am008-2-42 hotel_fun_mc_talk_holdouthand with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Give it to me."
    scene sm1cs-am008-2-43 hotel_fun_am_talk with dissolve
    play voice3 girl22_no_happy noloop
    am "No."
    mct "Mmmm. She wants to give it to me."
    mct "But she wants me to act a certain way."
    mct "Like in the car."
    #mc leans in a bit closer to her
    scene sm1cs-am008-2-44 hotel_fun_mc_talk_closer with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "April, if you want to be a good girl, you'll give me what you have."
    #am gulps down nervously - he is turning her own
    scene sm1cs-am008-2-45 hotel_fun_am_talk_sigh with dissolve
    play voice3 girl22_disappointed_ehh1 noloop
    am "*sighs and shivers*"
    #am handing him a spiked collar - close up of her handing it to mc's hands
    scene sm1cs-am008-2-46 hotel_fun_am_talk_handovercollar with dissolve
    pause
    #mc puts the collar on her
    scene sm1cs-am008-2-47 hotel_fun_am_talk_collaron with dissolve
    play voice3 girl22_sex_closedmoan4 noloop
    am "Mmmm."
    scene sm1cs-am008-2-48 hotel_fun_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Too tight?"
    scene sm1cs-am008-2-49 hotel_fun_am_talk with dissolve
    play voice3 girl22_no_nope4 noloop
    am "No. It's just right."
    #mc is back from her - focus on april now, wearing the spiked collar
    scene sm1cs-am008-2-50 hotel_fun_am_talk_collaron with dissolve
    #am talking
    play voice3 girl22_sex_closedmoan3 noloop
    am "You can... ummm."
    scene sm1cs-am008-2-51 hotel_fun_mc_talk_am_bite_lip with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Don't be nervous."
    #am is nervous, and bites her bottom lip - head down
    scene sm1cs-am008-2-52 hotel_fun_am_talk with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "Can we try some pet play?"
    am "You calling me a {b}good girl{/b}. Your sexy puppy?"
    #am brushing a hand through her hair
    scene sm1cs-am008-2-53 hotel_fun_am_talk_brushhair with dissolve
    play voice3 girl22_disappointed_ah noloop
    am "Ah forget it."
    am "It would be too much."
    menu:
        "Yes to 'pet play' with April" (hint = "sm1cs_am008_m06_h01"):
            $ player.set_choice("sm1cs_am008_pet_play")
            #mc telling her if she is comfortable, so is he
            scene sm1cs-am008-2-54 hotel_fun_mc_talk_menu with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "If you're okay with it, so am I."
            #am thinking
            scene sm1cs-am008-2-55 hotel_fun_am_talk_menu_thinkning with dissolve
            play voice3 girl22_yes_simple noloop
            #am is excited
            am "Yes."
            if player.get_choice("sm1cs_am004_am_safeword"):
                scene sm1cs-am008-2-56 hotel_fun_mc_talk_safeword with dissolve
                play voice2 mc_thinking_hm noloop
                mc "Sabre is your safe word right?"
                scene sm1cs-am008-2-57 hotel_fun_am_talk with dissolve
                play voice3 girl22_thinking_hmm1 noloop
                am "You remembered."
                #mc grinning
                scene sm1cs-am008-2-58 hotel_fun_mc_talk_grinning with dissolve
                play voice2 mc_arrogant_heh3 noloop
                mc "Safety first."
                #am amused
                scene sm1cs-am008-2-59 hotel_fun_am_talk_amused with dissolve
                play voice3 girl22_happy_laugh1 noloop
                am "Except for cumming in me."
                scene sm1cs-am008-2-60 hotel_fun_mc_talk with dissolve
                play voice2 mc_thinking_emm1 noloop
                mc "Hah. Well. I mean yeah."
            else:
                scene sm1cs-am008-2-56 hotel_fun_mc_talk_safeword with dissolve
                play voice2 mc_thinking_hm noloop
                mc "We should have a safe word."
                #am thinking
                scene sm1cs-am008-2-57 hotel_fun_am_talk with dissolve
                play voice3 girl22_thinking_hmm1 noloop
                am "Hmmm."
                am "Sabre. Short, easy to remember."
                scene sm1cs-am008-2-58 hotel_fun_mc_talk_grinning with dissolve
                play voice2 mc_thinking_emm1 noloop
                mc "Got it."
                #mc touching her cheek - am closing her eyes - she is in heaven
                mc "Alright... are you ready for Master to play with you?"
                scene sm1cs-am008-2-59 hotel_fun_am_talk_amused with dissolve
                play voice3 girl22_sex_closedmoan2 noloop
                am "Mmmhmmm!"

        "No to 'pet play' with April" (hint = "sm1cs_am008_m06_h02"):
            $ player.set_choice("sm1cs_am008_no_pet_play")
            pass

label sm1cs_am008_sex:

    scene sm1cs-am008-2-64 hotel_fun_mc_talk_lingerieoff with dissolve
    #mc taking off her lingerie
    pause
    scene sm1cs-am008-2-65 hotel_fun_am_talk_naked with dissolve
    play voice3 girl22_surprised_oh noloop
    #am is now naked and just has the spiked collar on - she is excited
    am "Ooooh."
    #mc is naked in front of her - touching his cock
    scene sm1cs-am008-2-66 hotel_fun_mc_talk_tongueout with dissolve
    #am has her mouth open and her tongue out
    play voice2 mc_thinking_mmm7 noloop
    mc "My good girl is all horny for my cock."
    scene sm1cs-am008-2-67 hotel_fun_am_talk with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "*whispers* Yes."
    scene sm1cs-am008-2-68 hotel_fun_mc_talk with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "What was that?"
    #am looking needy and desperate
    scene sm1cs-am008-2-69 hotel_fun_am_talk with dissolve
    play voice3 girl22_sexphrase_yes noloop
    am "Yes, I want your cock..."
    scene sm1cs-am008-2-70 hotel_fun_mc_talk_guide with dissolve
    #mc guides am to the bed
    play voice2 mc_thinking_mmm4 noloop
    mc "Over here."
    #am is on the bed - mc spreading her legs - mc is on her knees
    scene sm1cs-am008-2-71 hotel_fun_am_talk_spreadlegsknees with dissolve
    play voice3 girl22_angry_breathing noloop
    am "Ah-huaah..."
    #mc leans close to her pussy
    scene sm1cs-am008-2-73 hotel_fun_am_talk_doesnt with dissolve
    play voice3 girl22_surprised_ohmy noloop
    am "Oh god."
    #am telling him he doesn't have to
    am "[mcname], you don't have to."
    scene sm1cs-am008-2-74 hotel_fun_mc_talk with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "I know.{w} But I want to."
    #mc touches her pussy with his cum
    scene sm1cs-am008-2-75 hotel_fun_mc_talk_tongue with dissolve
    play voisex2 mc_sex_sucking_slow1
    play voisex3 girl22_sex_openmoans1
    mc "*licks*"
    #am likes it
    scene sm1cs-am008-2-76 hotel_fun_am_talk with dissolve
    am "Ahuah..."
    #mc looking up at her
    stop voisex2 fadeout 1.0
    scene sm1cs-am008-2-77 hotel_fun_mc_talk with dissolve
    play voisex2 mc_happy_oof1 noloop
    mc "I want to taste all of you."
    #mc licks her again
    scene sm1cs-am008-2-79 hotel_fun_am_talk_animation1_pussy with dissolve
    play voisex2 mc_sex_sucking_slow1
    play voisex3 girl22_sex_openmoans1
    am "Ahu-huaa...hahua.. ohauhah..."
    #animation 1 -
    # mc on his knees eating am's pussy out
    if player.get_choice("sm1cs_am008_pet_play"):
        am "*happily moaning*"
        am "O-Oh... Master..."
        #alt angle anim 1
        mc "Mmmm. My good girl likes this."
        am "Yes, she does."
        am "*deep moaning*"
        #alt angle anim1
        am "She's never been treated like this."
        am "By someone who loves her..."
        am "Without hangups."
        #alt angle anim1
    else:
        mc "You're so cute, April."
        am "Ehu-ahuah... I'm not."
        mc "You are."
        #alt angle anim1
        am "Shut-haua... up-oohuaha.."
        am "I'm not like... Nari..."
        #alt angle anim1
        am "Fuck-ah... or Claire."
        am "I'm regular-iihuaaah."
        mc "Not even close."
        #alt angle anim1
        mc "You're my spectacular...{w} Sometimes bitch..."
        mc "But otherwise amazing girlfriend."
        #alt angle anim 1
        am "Ouhah... dork."
        am "You sound... *gasp* Like you're describing a superhero."
        #alt angle anim 1
    #end of anim 1
    #am leans up
    stop voisex2 fadeout 1.0
    scene sm1cs-am008-2-80 hotel_fun_am_talk_leanup_grabarms with dissolve
    play voisex3 girl22_hey_scared noloop
    #am pulls mc's arms forward
    am "Come on!"
    am "Up up up!"
    #am puts mc on his back
    scene sm1cs-am008-2-81 hotel_fun_mc_talk_onback with dissolve
    if player.get_choice("sm1cs_am008_pet_play"):
        scene sm1cs-am008-2-82 hotel_fun_am_talk_lick with dissolve
        play voisex3 girl22_sex_closedmoans1
        play voisex2 mc_sex_openmoans1
        play voisex4 girl22_sex_licking
        am "Muaha... ahuah..."
        #am licking his neck
        stop voisex2 fadeout 1.0
        stop voisex4 fadeout 1.0
        scene sm1cs-am008-2-84 hotel_fun_am_talk with dissolve
        play voisex3 girl22_surprised_eh1 noloop
        am "Master. Are you going to punish me...?"
        am "Or make love to me?"
        #mc touching her
        scene sm1cs-am008-2-85 hotel_fun_mc_talk with dissolve
        play voisex2 mc_thinking_hmm1 noloop
        mc "I guess that depends..."
        mc "If you keep being a good girl."
        #am is bashful - not licking
        scene sm1cs-am008-2-86 hotel_fun_am_talk_bashful with dissolve
        play voisex3 girl22_yes_yep4 noloop
        am "I'm doing my best."
        scene sm1cs-am008-2-87 hotel_fun_mc_talk with dissolve
        play voisex2 mc_yes_aga1 noloop
        mc "I know.{w} Keep going."
        #am licks his chest again
        scene sm1cs-am008-2-88 hotel_fun_am_talk_lick_again with dissolve
        if player.get_choice("sm1cs_am007_lick_armpits_both") or player.get_choice("sm1cs_am007_lick_armpits_am"):
            #am pulls up his arm
            play voisex3 girl22_sex_closedmoans1
            play voisex2 mc_sex_openmoans1
            play voisex4 girl22_sex_licking
            am "I want to taste more of you."
            #am licks his armpit
            stop voisex2 fadeout 1.0
            stop voisex4 fadeout 1.0
            scene sm1cs-am008-2-89 hotel_fun_am_talk_armup with dissolve
            play voisex3 girl22_sex_closedmoan3 noloop
            am "Yes. Master... tastes so good."
            #am smiling at him
            am "One day... I could just lick you all over."
            #am long lick across his chest
            scene sm1cs-am008-2-91 hotel_fun_am_talk_smiling with dissolve
            play voisex3 girl22_arrogant_yeah noloop
            am "Would you like that?"
            #mc smiles
            scene sm1cs-am008-2-94 hotel_fun_mc_talk_smile with dissolve
            play voisex2 mc_yes_yeah1 noloop
            mc "Sounds good to me, my cute little puppy."
            play voisex3 girl22_happy_mmm noloop
            am "*happy humming*"
    elif player.get_choice("sm1cs_am007_lick_armpits_both") or player.get_choice("sm1cs_am007_lick_armpits_am"):
        play voisex3 girl22_sex_closedmoans1
        play voisex2 mc_sex_openmoans1
        play voisex4 girl22_sex_licking
        scene sm1cs-am008-2-90 hotel_fun_am_talk_armpitlick with dissolve
        am "Oh fuck."
        #am smiling at him
        stop voisex2 fadeout 1.0
        stop voisex4 fadeout 1.0
        scene sm1cs-am008-2-91 hotel_fun_am_talk_smiling with dissolve
        play voisex3 girl22_happy_mmm noloop
        am "I should have had you do some jumping jacks."
        #am long lick across his chest
        am "Your sweat is just not the same without working out first."
        #mc smiles
        scene sm1cs-am008-2-94 hotel_fun_mc_talk_smile with dissolve
        play voisex2 mc_arrogant_heh2 noloop
        mc "We should have done the licking after."
        scene sm1cs-am008-2-95 hotel_fun_am_talk_happy with dissolve
        play voisex3 girl22_happy_laugh2 noloop
        am "Haha."
    #am on her back - sucking her bottom lip, squeezing her tits together with her hands
    scene sm1cs-am008-2-96 hotel_fun_am_talk_onback with dissolve
    play voisex3 girl22_sex_closedmoan4 noloop
    am "Ahuah..."
    scene sm1cs-am008-2-97 hotel_fun_am_talk_touchpussy with dissolve
    if player.get_choice("sm1cs_am008_pet_play"):
        play voisex3 girl22_sexphrase_please noloop
        am "Please. I'm ready."
        am "I want to feel your cock inside of me again."
        #am touching her pussy
        scene sm1cs-am008-2-99 hotel_fun_am_talk_annoyed with dissolve
        play voisex3 girl22_disappointed_mmm noloop
        am "I'm such a naughty puppy..."
    else:
        play voisex3 girl22_disappointed_mmm noloop
        am "Mrrah... I've been thinking about this again."
        scene sm1cs-am008-2-98 hotel_fun_mc_talk with dissolve
        play voisex2 mc_surprised_what7 noloop
        mc "Thinking about what?"
        #am unimpressed and annoyed
        scene sm1cs-am008-2-99 hotel_fun_am_talk_annoyed with dissolve
        play voisex3 girl22_angry_heergh noloop
        am "Just shove your dick inside of me, [mcname]."
    #mc gets in position above april- cock is just outside
    scene sm1cs-am008-2-100 hotel_fun_mc_talknposition with dissolve
    play voisex2 mc_thinking_hmm8 noloop
    mc "Like this?"
    #mc lowers his body and goes inside her pussy
    scene sm1cs-am008-2-102 hotel_fun_am_talk_wantskiss with dissolve
    play voisex3 girl22_sex_scream2 noloop
    am "Ahuwaah... yes..."
    #am wants to be kissed
    am "Come on."
    #mc kissess her
    scene sm1cs-am008-2-103 hotel_fun_am_talk_kiss_animation with dissolve
    play voisex3 girl22_sex_closedmoans1
    play voisex2 mc_sex_closedmoans1
    play sound dahlia_kiss_french1
    am "*moaning*"
    #animation 2
    # - mc missionary april - no kissing - but am has her legs hooked around his legs and is holding his neck and ass - NO KISSING but am is moaning and looking at him with lovey dovey eyes
    scene sm1cs-am008-2-105 hotel_fun_mc_talk with dissolve
    play voisex3 girl22_sex_openmoans1
    play voisex2 mc_sex_openmoans2
    am "Fuck. Fuck-huaaah."
    if player.get_choice("sm1cs_am008_pet_play"):
        mc "That's my good girl."
        mc "You like taking all of your Master's dick."
        am "Yes..."
        #alt angle
        mc "Yes, what?"
        am "I like taking all of your dick in my pussy."
        am "Muaah-errah... it's so thick."
        #alt angle
        mc "You're my slutty little puppy girl aren't you?"
        am "No. I'm not slutty."
        mc "Come on."
        am "I'm not... I just... like you a lot, Master."
        #alt angle
        am "Hahu-rrahuaa... Oh my fucking god."
        am "You're going to make me explode!"
    else:
        mc "Fuck, that feels so good, April."
        am "Thanks?{w} Whu-fahuah..."
        am "It's strange... talking during this."
        #alt angle
        mc "You don't talk during sex?"
        am "I mean... I haven't had a lot of sex before."
        #alt angle
        mc "Than I feel especially honored."
        am "Jesus. Such a dork."
        am "Huaha... Fuhaa-haah..."
        #alt angle
        am "Still... I'm glad you feel so... comfortable."
        am "I'm very... *moans* Happy with {i}you{/i}, [mcname]."
        mc "I feel the same, April."
        #alt angle
    #end of animation 2
    #am asking him if they can switch places
    stop voisex2 fadeout 1.0
    scene sm1cs-am008-2-104 hotel_fun_am_talk_switchplaces with dissolve
    play voisex3 girl22_sex_scream1 noloop
    am "I want to try being on top."
    play voisex2 mc_yes_okay2 noloop
    mc "Knock yourself out."
    #they are now in position for cowgirl - am is still above his cock - it's not inside yet - fade in
    scene sm1cs-am008-2-106 hotel_fun_am_talk_cowgirlposition with dissolve
    pause
    #am looking back - touching mc's cock
    scene sm1cs-am008-2-107 hotel_fun_am_talk_touchbreast with dissolve
    play voisex3 girl22_happy_laugh3 noloop
    am "Haha. It's all sticky."
    #am rubs her fingers on his cock
    scene sm1cs-am008-2-108 hotel_fun_am_talk_mouth with dissolve
    play voisex3 girl22_sex_closedmoans1
    play sound girl22_sex_licking loop
    am "Ooohua..."
    #am takes the hand that was rubbing her fingers and rubs her tit
    #am then takes the same hand and touches her fingers to her mouth
    am "Mmm... Your scent... is outside and inside me."
    #am finally guides his cock inside her pussy
    stop sound fadeout 1.0
    scene sm1cs-am008-2-109 hotel_fun_am_talknside_animation_cowgirl with dissolve
    play voisex2 mc_sex_openmoans1
    play voisex3 girl22_sex_openmoans1
    am "Muaah..."
    #am's head leans forward - that nearly made her cum
    am "Oh-hhuaah-oooha..."
    #animation 3
    # - april riding him - am reverse cowgirl - facing away from mc. Mc is spanking her ass now and then. am is moaning even more than before.
    if player.get_choice("sm1cs_am008_pet_play"):
        am "How do I look, Master?"
        #alt angle - mc's pov watching am in front of him
        mc "Incredible."
        mc "A wild creature hellbent on driving me insane."
        pause
        #alt angle - am's face and boobs
        am "I'm not hurting you am I?"
        mc "No. I would let you know."
        am "So... it feels good?"
        am "Your puppy's pussy?"
        #alt angle
        mc "I fucking love it."
        mc "I wish I could pound you like this in the office."
        play voisex3 girl22_sex_openmoans2
        am "Hahah-huaah..."
        #alt angle
        am "We'd get in trouble, Master... Hhuaah..."
        am "Unless we were extra sneaky."
        am "Faaaak-ug-gaah!"
    else:
        am "This is better."
        am "You were really starting to pound me before."
        #alt angle
        mc "I just love driving into this tight pussy."
        am "Oh yeah?"
        am "What's your favorite part of it?"
        #alt angle
        play voisex3 girl22_sex_openmoans2
        mc "It's tight and so wet."
        mc "*grunts* And warm."
        #alt angle
        am "You want warm, you should try this dick-huaah."
        am "Oh god... It's making me snap all over, [mcname]!"
    #end of anim 3
    #am cumming and rubbing her pussy
    play voisex3 [girl22_sex_scream5, girl22_sex_scream4] noloop
    stop voisex2 fadeout 1.0
    scene sm1cs-am008-2-110 hotel_fun_am_talk_rubbing_pussy  with vpunch
    am "Oh my god-huaaah!"
    #am doesn't squirt - but her mouth is open and her tongue is out
    play voisex3 girl22_sex_scream3 noloop
    scene sm1cs-am008-2-111 hotel_fun_am_talk_tongueout with vpunch
    am "*loud moaning*"
    #am's eyes roll up a bit - she grabs her nipples
    play voisex3 girl22_angry_breathing noloop
    scene sm1cs-am008-2-112 hotel_fun_am_talk_rolleyes_touchnipples with vpunch
    am "*panting and shivering*"
    #am's body sliding forward - she's kind of faint
    scene sm1cs-am008-2-113 hotel_fun_mc_talk_leaningforward with dissolve
    play voisex2 d2s12_emmm noloop
    #am is just kind of leaning forward
    mc "April?"
    #mc untangle himself from her
    scene sm1cs-am008-2-114 hotel_fun_mc_talk_rubleg with dissolve
    #mc rubbing her leg
    play voisex2 mc_hey_hey2 noloop
    mc "You okay?"
    #am recovers
    scene sm1cs-am008-2-115 hotel_fun_am_talk_smile with dissolve
    #am smiling back at mc
    play voisex3 girl22_yes_aga11 noloop
    am "Better than okay."
    am "That was probably the best orgasm I've had."
    #am thinking - still horny and panting
    scene sm1cs-am008-2-116 hotel_fun_am_talk_thinkinghorny with dissolve
    play voisex3 girl22_disappointed_oof noloop
    am "I wonder if there is a machine that can record endorphin releases."
    #mc laughing
    scene sm1cs-am008-2-117 hotel_fun_mc_talk_laugh with dissolve
    play voisex2 mc_arrogant_heh3 noloop
    mc "You had me worried there."
    #mc relaxing
    mc "Sounds like we need to stop for a moment."
    #am shakes her head - 3 renders
    scene sm1cs-am008-2-119 hotel_fun_am_talk_shakehead with dissolve
    #am looking horny - begging
    if player.get_choice("sm1cs_am008_pet_play"):
        play voisex3 girl22_sexphrase_please noloop
        am "Please, Master."
        am "I can take it."
        am "It wouldn't be fair if only one of us got to cum."
    else:
        play voisex3 girl22_arrogant_pff noloop
        am "Pssssh. I didn't say that."
        am "*deep breath* I still got a bit left in me."
        #am smiling
        am "So don't stop on my account, [mcname]."
    #am on hands and knees but with her ass up like this
    #am spreading her body forward to she is flat on her belly
    scene sm1cs-am008-2-124 hotel_fun_am_talk_shakehead_begging with dissolve
    play voisex3 girl22_sex_closedmoan6 noloop
    am "Mmmm... Unless..."
    scene sm1cs-am008-2-126 hotel_fun_am_talk_assup with dissolve
    play voisex3 girl22_arrogant_hm noloop
    am "This is what you want to see."
    #am moving her body again to put her ass up, offering up her pussy to mc like an animal
    am "Me... wiggling my ass..."
    scene sm1cs-am008-2-127 hotel_fun_am_talk_assup_wiggle with dissolve
    pause
    scene sm1cs-am008-2-128 hotel_fun_am_talk_bitelip with dissolve
    play voisex3 girl22_sex_closedmoan5 noloop
    am "Shoving my bare pussy towards you."
    am "Like an animal."
    #am looking worried, biting her lip, hungry for more cock
    #am talking - not looking at mc
    scene sm1cs-am008-2-129 hotel_fun_am_talk_lookaway with dissolve
    play voisex3 girl22_disappointed_ah noloop
    if player.get_choice("sm1cs_am008_pet_play"):
        am "Please, Master."
        am "I need to feel you inside me some more..."
        #shot of am's wet pussy
        am "*horny whimpering*"
    else:
        am "Come on."
        am "You don't have to worry about me."
        scene sm1cs-am008-2-131 hotel_fun_am_talk_spreadpussy with dissolve
        play voisex2 mc_thinking_hmm6 noloop
        mc "Well I do. It's part of being together."
        #am likes that a lot
        #am teases him
        play voisex3 girl22_arrogant_ha noloop
        am "Hah. A gentleman and a coder."
        am "Well, then that makes me a lady."
        #shot of am using her hand to spread her pussy wide
        am "And you wouldn't keep a lady waiting, would you?"
        #mc grins and moves into position
        mct "I guess she really is ready for more."
    #animation 4 - doggystyle
    # - april's body should be swinging back and forth to slam her ass up against mc's cock. her movement is minor compared to mc's thrusting
    play voisex3 girl22_sexphrase_yes noloop
    scene sm1cs-am008-2-132 hotel_fun_mc_talk_smileposition with hpunch
    am "Yes! Give it to me."
    scene sm1cs-am008-2-133 hotel_fun_mc_talk_animation4doggystyle with dissolve
    play voisex3 girl22_sex_openmoans2
    play voisex2 mc_sex_openmoans1
    if player.get_choice("sm1cs_am008_pet_play"):
        #alt angle
        am "Yes. My pussy is spilling with your love juices, Master."
        am "Break me. Make my pussy yearn for your thick cock!"
        #alt angle - pulled back to show a bit of mc and april
        mct "I fucking love seeing this side of April."
        mct "It's like all her bitterness and angst is gone."
        mct "She's just showing me her animal side."
        #alt angle
        am "Muah-rhuaha... I can feel my pussy twitching."
        am "I'm going to cum again!"
        #alt angle - am's face
        am "But I... Huah.. .eraah..."
        am "I want to feel your load inside me again."
        am "Give your puppy girl a nice salty treat-huaaaah!"
        #alt angle
    else:
        am "Ohua-ha fuck!"
        am "It's coming again!"
        mc "Yeah... I can feel it."
        #alt angle
        mc "You're holding onto me so tight."
        #alt angle
        #alt angle
        am "Don't pull out!"
        mc "Huh?"
        #alt angle
        am "*panting and whimpering*"
        am "Just cum inside of me again."
        am "It's safe."
        #alt angle
        am "Mbuaa-huaaha... Please. I want you to fill me up. [mcname]!"
    #end of animation 4
    #mc pulls april up - about to kiss her
    scene sm1cs-am008-2-134 hotel_fun_mc_talk_pullcloseforkiss with dissolve
    mc "Nuaah."
    scene sm1cs-am008-2-135 hotel_fun_am_talk_pullcloseforkiss with dissolve
    play voisex3 girl22_surprised_ohmy noloop
    am "Oh god!"
    #am and mc get in position like this refeerence
    scene sm1cs-am008-2-136 hotel_fun_am_talk_kiss with dissolve
    play voisex3 girl22_sex_closedmoans1
    play voisex2 mc_sex_closedmoans1
    play sound2 dahlia_kiss_french1 noloop
    #am and mc kiss
    am "Mrrrr-ffffffummm... ohhhmmmm."
    #am is dones kissing - am's tongue is out as she cums
    scene sm1cs-am008-2-137 hotel_fun_am_talk_kiss with dissolve
    am "Ffffuaaa-huaaah..."
    scene sm1cs-am008-2-138 hotel_fun_mc_talk_orgasm with dissolve
    play voisex3 girl22_sex_openmoans2
    play voisex2 mc_sex_openmoans3
    am "So good-huaaah."
    #mc groaning as he cums - am loves watching him
    play voisex3 girl22_sex_orgasm1 noloop
    play voisex2 mc_sex_orgasm4 noloop
    scene sm1cs-am008-2-140 hotel_fun_am_talk_side with hpunch
    mc "*groans*"
    am "Yes!"
    #side shot of their bodies - hpunch
    queue voisex3 girl22_sexphrase_fuck noloop
    scene sm1cs-am008-2-141 hotel_fun_mc_talk_creampie with hpunch
    am "Fuck. Yes yes yes..."
    #shot from below if we can - showing cum leaking out from where they are connected + creampie
    scene sm1cs-am008-2-142 hotel_fun_am_talk_leanforward with dissolve
    queue voisex3 girl22_sex_scream4 noloop
    #am leans her body forward
    am "Mmuaaa-huaaah."
    #am goes prone in front of mc
    scene sm1cs-am008-2-143 hotel_fun_am_talk_prone with dissolve
    pause
    #mc rubbs her ass
    #mc pulling her asscheek open to see her cream-filled pussy
    if player.get_choice("sm1cs_am008_pet_play"):
        scene sm1cs-am008-2-143-1 hotel_fun_mc_talk_rubass with dissolve
        play voisex2 mc_thinking_hmm7 noloop
        mc "There you go."
        mc "How does my little puppy girl feel?"
        #am smiling back at him
        scene sm1cs-am008-2-146 hotel_fun_am_talk_smile with dissolve
        play voisex3 girl22_angry_breathing noloop
        am "Incredible."
        am "Thanks, Master..."
        #am rubbing a hand on her ass
        scene sm1cs-am008-2-144 hotel_fun_mc_talk_rubass with dissolve
        play voisex3 girl22_happy_mmm noloop
        am "It feels so nice. Your thick, warm cum inside me."
    else:
        #am is just spent but very happy
        play voisex3 girl22_angry_breathing noloop
        scene sm1cs-am008-2-146 hotel_fun_am_talk_smile with dissolve
        am "Oh lord..."
        am "You absolutely wrecked me."
        #am rubs her ass
        scene sm1cs-am008-2-144 hotel_fun_mc_talk_rubass with dissolve
        play voisex3 girl22_happy_mmm noloop
        am "Mmm... I kind of want to..."
        am "Leave it in."
    #am is cuddled up with mc - fade in - am's eyes closed
    scene sm1cs-am008-2-148 hotel_fun_am_talk_cuddle with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "Mmmmm."
    am "Thinking of running for the hills?"
    #mc smiles
    scene sm1cs-am008-2-149 hotel_fun_mc_talk_smile with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "It's like you don't even know me."
    #am bittersweet smile
    scene sm1cs-am008-2-150 hotel_fun_am_talk_smile with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "I've known... other people."
    am "But I don't think any of them understand me like you do, [mcname]."
    #am is happy
    scene sm1cs-am008-2-151 hotel_fun_am_talk_hair with dissolve
    play voice3 girl22_hey_simple noloop
    am "I'm really glad you joined Orbix. We... kind of work together well there."
    am "But we really work together, {i}here{/i}."
    #mc playing with her hair
    am "I mean, you understood me, without knowing all the fucked up stuff behind me."
    scene sm1cs-am008-2-152 hotel_fun_mc_talk_hair with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I bet other people would like you if they saw the 'real' you."
    #am doesnt think so
    scene sm1cs-am008-2-153 hotel_fun_mc_talk_doesntthinkso with dissolve
    play voice3 girl22_no_uhuh1 noloop
    am "I...{w} I don't think so, [mcname]."
    ### Part X - The Ending
    #am goes to take a shower.
    scene sm1cs-am008-2-154 hotel_fun_am_talk_toshower with dissolve
    pause
    #mc getting ready to leave bed
    scene sm1cs-am008-2-155 hotel_fun_mc_talk_getingup with dissolve
    play voice2 d1s2_hmm noloop
    mc "Cleaning off? I'll join you?"
    #am smiles back at him
    scene sm1cs-am008-2-156 hotel_fun_am_talk_smile with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "I may be your bitch in bed, but we're not a pack that needs to groom together."
    scene sm1cs-am008-2-157 hotel_fun_mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Fair. And I don't think of you as my bitch."
    #am is playful
    scene sm1cs-am008-2-158 hotel_fun_am_talk with dissolve
    play voice3 girl22_thinking_oh noloop
    am "Ooooh. Am I your slut then? Your tramp?"
    menu:
        "No label" (hint = "sm1cs_am008_m07_h01"):
            $ player.set_choice("sm1cs_am008_no_label")
            #mc talking
            scene sm1cs-am008-2-159 hotel_fun_mc_talk with dissolve
            play voice2 mc_no_nah1 noloop
            mc "You're just April. My Girlfriend."
            play voice3 girl22_yes_aga4 noloop
            am "Good."
            #am likes that

        "You are my Sex Puppy" if player.get_choice("sm1cs_am008_pet_play") (hint = "sm1cs_am008_m07_h02"):
            $ player.set_choice("sm1cs_am008_sex_puppy")
            scene sm1cs-am008-2-159 hotel_fun_mc_talk with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "You are my Sex Puppy."
            #am mulling it over
            scene sm1cs-am008-2-160 hotel_fun_am_talk_shrug with dissolve
            play voice3 girl22_yes_happy noloop
            am "Yes. That's perfect."
            #am shrugs
            am "But it's just for us in our private moments."
            #am holds up a finger - warning him
            scene sm1cs-am008-2-161 hotel_fun_am_talk_finger with dissolve
            play voice3 girl22_angry_dagh noloop
            am "Call me that at work, and we're done."
            scene sm1cs-am008-2-162 hotel_fun_mc_talk with dissolve
            play voice2 mc_no_no2 noloop
            mc "No need to worry about that."
            #mc relaxing
            mc "I know how to handle sensitive subjects."
            scene sm1cs-am008-2-163 hotel_fun_am_talk with dissolve
            play voice3 girl22_arrogant_he noloop
            am "Haha. Sure."

    scene sm1cs-am008-2-164 hotel_fun_am_talk_leave with dissolve
    pause
    scene sm1cs-am008-2-165 hotel_fun_am_talk_comingback_shower_phonemc with fade
    #am coming back - naked and using a towel to dry her hair. mc is on his phone - fade in
    play voice3 girl22_yes_yep5 noloop
    am "All yours."
    #mc gets up
    scene sm1cs-am008-2-166 hotel_fun_mc_talk_getup with dissolve
    pause
    #mc meets april in the middle - pulling her close
    scene sm1cs-am008-2-167 hotel_fun_m_talk_close with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "Ooh."
    #mc holds her tightly and kisses her
    scene sm1cs-am008-2-168 hotel_fun_mc_talk_kiss with dissolve
    play voice2 d1s1_mmm noloop
    play sound dahlia_kiss_french1
    mc "Mmm."
    scene sm1cs-am008-2-169 hotel_fun_am_talk_kiss with dissolve
    play voice3 girl22_sex_closedmoan2 noloop
    play sound mc_kiss2
    am "Ammmm."
    #mc stroking her face
    mc "..."
    scene sm1cs-am008-2-171 hotel_fun_am_talk with dissolve
    play voice3 girl22_disappointed_oh noloop
    am "You're going to get me sticky again."
    #mc laughing - letting her go
    scene sm1cs-am008-2-172 hotel_fun_mc_talk_laughing with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "I just wanted to thank you for a great date night."
    scene sm1cs-am008-2-173 hotel_fun_am_talk_playfullook with dissolve
    play voice3 girl22_yes_aga6 noloop
    am "Glad we could do it."
    #am playful look
    am "I think it's safe to say... my uh... crush."
    am "Well it might be upgrading into something more."
    #mc is playful smiling
    scene sm1cs-am008-2-174 hotel_fun_mc_talk_playfullook with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Like what?"
    #am points toward the bathroom
    scene sm1cs-am008-2-175 hotel_fun_am_talk_point_bathroom with dissolve
    play voice3 girl22_happy_laugh1 noloop
    am "Go and clean up you horndog."
    #am looks at his phone
    #am gets curious
    #am pulls up the phone
    #am holds her phone nearby mc's phone
    scene sm1cs-am008-2-176 hotel_fun_am_talk_lookphone with dissolve
    pause
    scene sm1cs-am008-2-177 hotel_fun_am_talk_curiousholdphone with dissolve
    pause
    scene sm1cs-am008-2-178 hotel_fun_am_talk_unlockphone with dissolve
    #mc's phone unlocks
    play voice3 girl22_thinking_hmm1 noloop
    am "I'll have to show him better security than a pin code."
    #am finds the video of Hana talking about the end of fetish locator. Mc saved the video on his phone
    scene sm1cs-am008-2-179 hotel_fun_am_talk_video with dissolve
    hr "Despite only existing for a few weeks, the Fetish Locator app devastated dozens of lives."
    play voice3 girl22_arrogant_hm noloop
    am "Hmmm."
    #just more footage of Hana talking
    scene sm1cs-am008-2-180 hotel_fun_am_talk with dissolve
    hr "Behind the scenes it proved much more devious - manipulating and exploiting people for the sexual gratification of a single person."
    hr "While the mastermind behind it is safely behind bars, we can only speculate at the traumatic experiences of the victims and how they may be coping."
    #am thinking - putting the two pieces together.
    scene sm1cs-am008-2-181 hotel_fun_am_talk_lookup with dissolve
    #am talking
    play voice3 girl22_surprised_what noloop
    am "Fetish Locator?"
    #am looks up - mc is coming back
    #am puts the phones back in place
    #mc finds her on her phone taking a picture of him
    scene sm1cs-am008-2-182 hotel_fun_am_talk_picture with dissolve
    "Click"
    #mc grins at her
    scene sm1cs-am008-2-183 hotel_fun_mc_talk_grin with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "What is that for?"
    #am smiles at him
    scene sm1cs-am008-2-184 hotel_fun_am_talk_smiles with dissolve
    play voice3 girl22_surprised_eh2 noloop
    am "For your new profile picture on my phone."
    #mc climbs up on bed with her
    scene sm1cs-am008-2-185 hotel_fun_mc_talk_climbbed with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Haha."
    mc "Just don't let anyone else see it."
    #am smiles at him
    scene sm1cs-am008-2-186 hotel_fun_am_talk_smile with dissolve
    play voice3 girl22_no_nope2 noloop
    am "Nope. This is just for me."
    #fade in - location change - mc is back at the studio - morning time slot
    scene sm1cs-am008-2-187 hotel_fun_mc_talk_studio with fade
    #mc stretching and thinking
    play voice2 mc_angry_errr7 noloop
    mct "*groanding* Was still strange spending a date with April."
    mct "It was nice, but she got pretty quiet, and then left a bit after I showered."
    #mc kind of accepting that april will definitely tell him if he pissed her off somehow
    scene sm1cs-am008-2-188 hotel_fun_mc_talk_accepting with dissolve
    play voice2 mc_thinking_hm noloop
    mct "At least she's not going to make me do guesswork if I really made her angry."
    mct "I'm sure she'll tell me when the time is right..."
    #mc ready for a new day
    scene sm1cs-am008-2-189 hotel_fun_mc_talk_newday with dissolve
    play voice2 d14s16_smell noloop
    mct "For now, I should probably get some work done."
    mct "Can't just be all sex and games around here..."
    #time used - half the energy of a day
    #summary of time - This event will take players back to the studio and have them be at he studio in the early morning time slot.

    $ StoryController.end_scene(AM_STORY)
    return
