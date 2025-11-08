label sm1xc_ns_tl_001_1i:

    $ player.set_choice("sm1xc_ns_tl_001_interaction_character", "tl")

    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "annoyed01") as lit_tl_annoyed01
    tl "Fuck me, I'm starving. You want some real breakfast, [mcname]?"
    mc "Sure, whatcha thinking?"
    hide lit_tl_annoyed01
    show expression cc.get_expression_image("tl", "ask01") as lit_tl_ask01
    tl "*stretches* Something not from a box. Maybe pancakes. I've got a craving."
    mc "Sounds delectable. Lead the way."

    return

label sm1xc_ns_tl_001_2i:

    $ player.set_choice("sm1xc_ns_tl_001_interaction_character", "ns")

    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    ns "Good morning, [mcname]."
    mc "Good morning. Aren't you a real early bird."
    ns "Yes, I've been up since 5:43 AM. I find I'm most productive in the early hours."
    mc "I can understand that. On the...{i}rare{/i} occasions that I wake up early, I feel pretty energized as well."
    hide lit_ns_smile01
    show expression cc.get_expression_image("ns", "embarrassed01") as lit_ns_embarrassed01
    ns "*stomach growls loudly* Oh. Excuse me. I've been too focused on debugging my side project to eat."
    mc "Why don't you grab some breakfast? I could go for something too."
    hide lit_ns_embarrassed01
    show expression cc.get_expression_image("ns", "nervous01") as lit_ns_nervous01
    ns "*hesitates* I...believe Taisia is already in the kitchen. I'm not certain that my presence would be welcome in her workspace."
    mc "You live here now too, Nari. You have every right to use the kitchen."
    hide lit_ns_nervous01
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    ns "Yes, logically that is correct. However, social dynamics often defy pure logic."
    mc "*chuckles* Alright, c'mon. I'll go with you."

    return
