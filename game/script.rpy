# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ayu = Character("{color=#ff6699}Ayu{/color}")
define Cosmos = Character("{color=#99ddff}Cosmos{/color}")
define Marina = Character("{color=#e62e00}Marina{/color}")
define Hiroki = Character("{color=#6666cc}Hiroki{/color}")
define Hifumi = Character("{color=#ebbd63}Hifumi{/color}")
define Hazel = Character("{color=#29c467}Hazel{/color}")
define Yue = Character("{color=#865cbd}Yue{/color}")
define Elizabeth = Character("{color=#abbdd9}Elizabeth{/color}")
define Stephania = Character("{color=#6a9feb}Stephania{/color}")
define Alice = Character("{color=#757575}Alice{/color}")

define Hisabeth = Character("{color=#6666cc}Hiroki{/color} & {color=#abbdd9}Elizabeth{/color}")
define Marinayu = Character("{color=#e62e00}Marina{/color} & {color=#ff6699}Ayu{/color}")

define MC = Character("MC")
define Crowd = Character("Crowd")
define Boy = Character("Boy #1")
define Boyy = Character("Boy #2")
define Boyyy = Character("Boy #3")
define Boyyyy = Character("Boy #4")
define Girl = Character("Girl #1")
define Girll = Character("Girl #2")
define Girlll = Character("Girl #3")
define Girllll = Character("Girl #4")

define W = Character("???")
define JK = Character("Schoolgirl #1")
define JKK = Character("Schoolgirl #2")
define JKKK = Character("Schoolgirl #3")
define JKKKK = Character("Schoolgirl #4")

define Maid = Character("Maid #1")
define Maidd = Character("Maid #2")
define Maiddd = Character("Maid #3")
define Maidddd = Character("Maid #4")
define Maiddddd = Character("Maid #5")

# nvl
define nv = Character(None, kind=nvl)

# The game starts here.

label start:

    $ succ_points = 0

    stop music fadeout 1.0
    scene black
    with fade
    $ renpy.pause(0.5)
    window show dissolve

    play music "bgm/succubus_pensive_loop.ogg" fadein 1.0

    Hiroki "Mm, nn..."
"I sigh as I nuzzle my cheek against my futon. It's warm and soft, and it feels like I'm being enveloped in a gentle embrace."
"I'd be content enough to lie here, cocooned by warmth, but unfortunately..."
W "Excuse me? Are you awake yet, Hiroki?"
"I can hear an angelic voice calling out to me."
"I'd like to turn over and go back to sleep, but I just can't."
"I don't want to upset whoever it is who owns this voice."
W "Hiroki...?"
Hiroki "Yeah, mm... I'm sorry. I'm getting up. I didn't mean to keep you."
"I press a hand to my mouth, stifling a yawn, then pull myself into a sitting position."
"I'm sure my hair must be messy, after spending a night tossing and turning."
"I doubt I look at my best, but I guess that's to be expected. I {i}have{/i} just woken up."

stop music fadeout 1.0

"Blinking white spots away from my field of vision, I turn my head to greet the angel who has awoken me, and..."

window hide dissolve
play music "bgm/succubus_stephania_loop.ogg" fadein 1.0
if persistent.adult==True:
    scene cg1_a with circleirisin
else:
    scene cg1 with circleirisin
$ achievement.grant("early_to_rise")
$ renpy.pause()
window show dissolve

Hiroki "Ah..."
"The vision sitting before me has golden hair which tumbles about her shoulders in twin cascades, which are loosely tied back in a pair of pigtails."
"Her apple green eyes are fringed with long lashes which are every bit as golden as her hair, and her skin is smooth and soft and creamy."
"She's undeniably adorable - and, of course, I know who she is."
Stephania "Hiroki...?"
"This woman is, believe it or not, none other than Stephania Sofia Maria Isabella of Astoria: the princess of the small European country Astoria, which borders Germany and the Netherlands."
"Stephania's European-ness is pretty apparent, even at a glance, based on her striking blonde hair."
"You don't see many Japanese women who look like that: not unless they bleach their hair."
"Based on her appearance alone, Stephania doesn't look like the kind of woman who should be any good at Japanese, but her proficiency in the language is really quite remarkable."
"Stephania's Japanese sounds very natural: almost like a native speaker's."
"She doesn't have much in the way of an accent at all, and neither does her maid, Elizabeth."
"As for why this is, well, it's a bit of a long story."
"Stephania, despite being Astoria's princess, is actually a huge fan of Japanese culture."
"She's been obsessed with our media, music, and fashion from a young age, and she took great pains to learn how to speak Japanese to a fluent level, despite never having been to Japan before..."
"Until now, that is."
"Stephania is very much in Japan at this moment: in Tokyo, to be more precise, in my apartment."
"Talk about a wild wake-up call."

if persistent.adult==True:
    scene cg1_2_a with dissolve
else:
    scene cg1_2 with dissolve
window show dissolve

Stephania "Good morning, Hiroki, darling!"
Stephania "I'm very sorry to wake you - you looked so sweet, I thought about letting you rest - but the hour is getting on."
Stephania "I wouldn't want you to waste the day!"
Stephania "Lizzie always says it's important to get an early start: especially in the winter. The days are short, so we need to enjoy as much of the daylight as we can!"
Hiroki "That's a very sensible thing to say. Lizzie - I mean, Elizabeth, sure is wise."
Stephania "Indeed, she is! I would scarcely know what to do without her, hehe."
Stephania "Certainly, I never would have been able to travel to Japan without her help. I am quite hopeless without her!"
"Speaking of Elizabeth, I wonder where she is. I can't see hide nor hair of her."
"I guess, given how proficient she is, she'll have dressed already, in her maid's attire, and she'll probably be engaged in housework as we speak."
"I told Elizabeth last night, before we slept, that she didn't need to fuss about the state of my apartment, but Elizabeth insisted."
"She's pretty serious when it comes to keeping things tidy."
Stephania "Hey, Hiroki..."
Stephania "I just wanted to thank you for letting Lizzie and I stay here. You really have been good to us."
Stephania "As much as I depend on my dear Lizzie, I fear I might be beginning to depend upon you a bit too much, too..."

window hide dissolve

menu:
    with dissolve

    "Maybe you should be a bit more independent.":

        window show dissolve

        $ succ_points -= 1

        Hiroki "Yeah, maybe you're right."
        Hiroki "You're an adult, so you should try being a bit more independent..."
        Hiroki "But I don't mind if you want to lean on me for help while you're in Japan, at least."
        Hiroki "You don't know your way around, so it's obvious you'll need some guidance."
        Stephania "You are not wrong about that, hehe."
        Stephania "This country {i}is{/i} very new to me, for all I have read about it, but I am very interested in learning more about it."
        Stephania "I cannot wait to traverse its streets with you."
        Stephania "Now!"
        "Stephania beams."
        Stephania "Why don't we see what it is Lizzie has made us for breakfast?"
        Stephania "I do not know about you, but I am starving!"

        jump merge1

    "It's fine. You can rely on me all you want.":

        window show dissolve

        $ succ_points += 3

        Hiroki "It's fine if you want to depend on me. I don't mind."
        Stephania "A-Are you quite certain?"
        Hiroki "Of course! You're my girlfriend now, aren't you, Steffy?"
        Stephania "I-I suppose that is true, yes, but... Goodness. T-To hear it out loud, so early in the morning..."
        "Stephania shifts upon the futon, her bare thighs rubbing together suggestively."
        "I know Stephania doesn't mean to seduce me - she's guileless like that, and awfully unworldly - but, damn, she really {i}does{/i} look good."
        "I can't help but remember, either, the memories of what we did last night."
        "I got {i}very{/i} intimately acquainted with Stephania back then, on this futon - and Elizabeth, too."
        "I don't think I'll forget that in a hurry."
        Stephania "F-For some reason, hearing you say that makes my heart skip a beat..."
        Hiroki "In a good way, I hope?"
        Stephania "Oh, yes! I am very happy to be your girlfriend. It is a great honor, though I fear I am still unaccustomed to it."
        Stephania "I think it will take me a while to get used to such affectionate appellations, hehe..."
        Stephania "But I do not dislike it: not at all!"
        Stephania "I'm very, very happy that I came to Japan to see you... {w}and I'm very, very happy, too, that we can spend more time together."
        Stephania "I know I might appear somewhat awkward - I've never spent this much time outside of the royal palace before - but I really am thankful I was able to meet you!"
        Hiroki "I don't think I'm all that amazing, really - but, if you think so, who am I to tell you otherwise?"
        Hiroki "Thanks, Steffy."
        "Gently, I ruffle the top of Stephania's blonde head."
        Hiroki "I'm glad that I was able to meet you, too."
        "That's not a lie, either. I really {i}do{/i} like her, though this whole situation still smacks of surreality."
        "I can scarcely believe, even now, that I was woken up by the princess of a European country: even a lesser-known one."
        "It's pretty wild."
        "My whole life, in fact, is a wild one."
        "I used to fancy myself, once upon a time, as a thoroughly ordinary guy, but I don't think I can describe myself as ordinary anymore."
        "If I tried, I think my work colleagues would lynch me..."
        "Not, I'm sure, that there's much protecting me from a near-future lynching as there is."
        "My work colleagues are all aware of my licentious relationships with a slew of famous women: Stephania Sofia Maria Isabella of Astoria being but one of my newest \"acquisitions\" (though phrasing it like that sounds seedy)."
        "I'm also dating the esteemed businesswoman, Wakatsuki Marina; the beloved idol, Ikue Ayu; the famous social media star, Cosmos Moretti; and..."
        "Well."
        "I'm getting ahead of myself."
        "I guess, if I'm to properly explain my circumstances (though who I'm explaining my circumstances to, exactly, I'm uncertain), I need to take it slow."
        "Ahem."
        "I used to be an ordinary guy, like I said: your average corporate slave who lived to work, and who spent most of the day either sitting in the office, or else commuting to it."
        "My life was a constant cycle of working, eating, and sleeping. It repeated incessantly, over and over, until I felt like a hamster running around in a wheel."
        "I'd had a few relationships over the years, but I was so busy with work - and so tired from it, too - I was never able to keep these relationships up for very long."
        "I was prepared to live out my unremarkable, uninteresting days alone, until my body broke down from the strain of constant work, and I collapsed - but then I met Marina."
        "...Well, I actually met Ayu first, but our initial encounter wasn't a particularly pleasant one. She fell on top of me, she hit me, and then she called me a pervert."
        "Marina, meanwhile, was far more accommodating."
        "We met at a bar, which was playing this jazzy arrangement. It was all very classy."
        "I was surprised to see Marina, given her status as a well-known, respected businesswoman: the CEO of her own company."
        "I never imagined I'd one day run into her, or that Marina would invite me to drink with her."
        "That whole encounter, in that smoky bar, felt a bit like a dream."
        "After sipping a few drinks, Marina invited me back to her office, and we..."
        "Well."
        "It would be indelicate to document what happened next."
        "Over the course of seeing Marina, however, she told me that she was a succubus."
        "I later learned that Ayu and Cosmos were succubi, too - and, attracted by my \"scent\" (it is, apparently, appealing to succubi), I amassed quite the harem."
        "I've gone from being a regular every man to being some sort of Casanova; beloved by a whole harem of women."
        "My boss is aware of my many relationships, and he means to use them to his advantage."
        "I've become, since I began to date Marina, quite beloved by my boss, on account of the sizeable monetary donations she's been sending to my workplace."
        "My colleagues, meanwhile, despise me for my good fortune, and I can hardly blame them."
        "If I were in their shoes, I would despise me, too."
        "I mean, where do I get off, being so beloved by so many beautiful, wealthy, talented women?"
        "I worry, if I'm not careful, my co-workers really might try to off me."
        "I'm skirting a dangerous line between pleasure and pain, but I wouldn't trade my newfound life for the world."
        "I love every single member of my harem - and, right now, I'm particularly struck by how pretty Stephania looks in my button-up shirt."
        Stephania "Hiroki..."
        "Stephania peers at me, her eyes wide."
        Stephania "I know it is still early, and I would hate to be too insistent, but... Um..."
        Stephania "W-Would it be alright if I could be close to you, if only for a few moments, while Lizzie is otherwise occupied?"
        Hiroki "Well, of course it's alright! You don't need to ask - and you don't need to look so anxious, either. I don't bite."
        Stephania "I-I know that, but..."
        "Stephania toys awkwardly with her hair."
        Stephania "I-I fear my request may be a brazen one. I know I am not acting as a princess ought to act, and I am not dressed as a princess ought to be dressed, either."
        Stephania "I do not wish to show such a slovenly side of myself to you, but awaking in the same room as you, wh-while wearing your clothes..."
        Stephania "I-It is almost more than my heart can bear. I-I feel as though I am burning up."
        Stephania "I like you so much, I hardly know what to do...!"
        Hiroki "Well, that's very lucky. I like you a lot, too - and I know {i}exactly{/i} what I want to do with you."
        Stephania "Y-You do?"
        Hiroki "Of course. Just let me take the lead."
        Hiroki "I'll look after you, Steffy. I promise."

        if persistent.adult==True:
            jump adult1
        else:
            jump merge1

label merge1:

    stop music fadeout 1.0
    window hide dissolve
    scene black with fstartgame
    $ renpy.pause(0.3)
    scene skyd with fstartgame
    window show dissolve

    "Once Stephania and I have finished getting up, Stephania has a quick shower, then dresses herself."
"I shower after Stephania does (it's only polite to let your guest go first, especially when said guest just so happens to be a princess) and dress myself."
"Newly-shaven and my hair brushed, I head into the kitchen, where I meet Elizabeth."

window hide dissolve
play music "bgm/succubus_palace_loop.ogg" fadein 1.0
$ achievement.grant("maid_to_serve")
if persistent.adult==True:
    scene cg2_a with wipedown_slow
else:
    scene cg2 with wipedown_slow
$ renpy.pause()
window show dissolve

Elizabeth "Greetings, Mr. Ogasawara."
"Elizabeth, Stephania's maid, greets me with a cursory glance over her shoulder."
"I'm sure Elizabeth would offer me a curtsy (as Stephania's self-proclaimed \"top maid\", Elizabeth is careful to always mind her manners), but she's otherwise occupied at the moment."
"She's standing at my kitchen counter, attired in her usual black and white maid's garb."
"In one hand she holds a spatula, and the fingers of her other hand are curled deftly about the handle of a frying pan."
"Elizabeth's red eyes are narrowed in concentration as she works on whatever it is she's cooking."
"The scent of batter lingers in the air, which leads me to believe she's whipping up some pancakes."
"It's pretty nice, I ponder, as I take a seat at the table, to have a maid about like Elizabeth to take care of the cooking and the cleaning."
"I'm not bad at cooking myself (I've lived on my own long enough that I've learnt how to manage the basics), but I don't often have the time to cook, nor the inclination."
"I have to wake up early most mornings to commute to work, and I'm often too tired to bother cooking."
"As a result, I've been subsiding on food purchased from the convenience store for a while."
"Convenience store food might, as the name suggests, be convenient, but it isn't particularly glamorous."
"I've had so many chicken cutlet sandwiches in my time that they've begun to taste a bit like cardboard."
"There's something hearty about home-cooked meals that store-bought food can never hope to compare to, what with all its plastic packaging."
"I guess it's lacking in heart?"
"I'm very grateful, therefore, for Elizabeth's presence, though I do feel somewhat guilty."
Hiroki "You really don't have to attend to all the chores, you know. I thought you and Steffy came here to relax?"
Elizabeth "Milady came here to relax, yes, and to spend time with you, but I cannot allow myself to do the same."
Elizabeth "As milady's maid, it is my duty to look after her, no matter where we might be."
Elizabeth "I would never be able to forgive myself if I did not do all in my power to ensure that she has a pleasant time in Japan."
Stephania "Oh, Lizzie! You don't need to be so serious! It makes me feel bad, seeing you work so hard for my sake!"
Elizabeth "It is quite alright. Please, do not worry, milady."
Elizabeth "You ought to know that there is nothing I enjoy more than making you happy."
Elizabeth "If I cannot dote upon you, then I know not what it is I would do with myself."
Elizabeth "I can think of nothing else I would rather do with my time."
Elizabeth "Now..."

scene kitchen
$ sface='smile'
$ sbody='cas1'
$ lface='serious'
$ lbody='maid1'
call s_stefeli from _call_s_stefeli_123421
$camera_move(400,300,200,0,0,'dissolve')
with dissolve

"Elizabeth steps away from the stove, then gently levers the contents of the pan onto a plate."
"This task accomplished, Elizabeth then presents this to Stephania with a flourish."
$ lbody='maid2'
show lizzie flip at c2
Elizabeth "Your breakfast is ready, milady."
"It's just as I thought. There, upon the plate, lies a perfect pancake: thick and fluffy, with an even, golden-brown surface."
"Elizabeth next pipes some whipped cream upon the surface of this perfectly-formed pancake, then decorates it with some strawberries."
show lizzie flip at c1
Elizabeth "I hope this is to your liking?"
$ sface='happy'
show steffy at c4
Stephania "Oh, it looks wonderful! I cannot wait to dig in!"
$ lface='smile'
show lizzie flip at c3
Elizabeth "Good. I am glad to hear it."
$ lbody='maid1'
$ lface='serious'
show lizzie flip at c4
Elizabeth "I have enough batter to make more pancakes, so please let me know if you want more."
Elizabeth "Would you like me to prepare you a pancake too, Mr. Ogasawara?"
Hiroki "Oh, yeah, uh, if you don't mind...?"
"I'm not a big fan of sweets, but that pancake of Stephania's does look good - and it smells good, too. My stomach's starting to rumble."
$ lface='smile'
show lizzie flip at c1
Elizabeth "I do not mind in the slightest. It is my pleasure, after all, to serve."
$ lbody='maid2'
show lizzie flip at c3
Elizabeth "If there is anything you want from me, do not hesitate to ask."
Elizabeth "I would be only too willing to come to your aid."

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyd with fstartgame
window show dissolve

"Our pancakes consumed, Elizabeth makes a start on the washing up."
"She washes the dishes swiftly but effectively, and once finished, she once more takes her place at the table."
"With the busywork, as Elizabeth termed it, finished (for the present, at least), Elizabeth then says..."

play music "bgm/succubus_slife_of_life_2_loop.ogg" fadein 1.0
scene kitchen
$ sface='smile'
$ sbody='cas1'
$ lface='serious'
$ lbody='maid1'
call s_stefeli from _call_s_stefeli_1
$camera_move(400,300,200,0,0,'dissolve')
with wipedown_slow

Elizabeth "So, what is on the agenda for today? What are your plans for us, Mr. Ogasawara?"
$ sface='shock'
show steffy at c4
Stephania "Oh, yes, I am intrigued about that, too!"
Stephania "I have never before been to Japan, and there is such a great deal I wish to do and see!"
$ sface='worried'
show steffy at c1
Stephania "I fear I do not have enough time, before my inevitable return to Astoria, to take in as much of your country's culture as I would desire..."
$ sface='smile2'
$ sbody='cas2'
show steffy at c3
Stephania "But during the scant week afforded to me, I would very much like to make the most of it!"
"That's fair enough. Stephania, as she said, has never been to Japan before in her life. In fact, I'm not sure if she's ever left Astoria."
"As a huge fan of Japan and its culture, it makes sense that she would want to maximize her time here."
"I, unfortunately, am not the best at planning out vacations/"
"Before making connections with Marina, which offered me some leverage in the office, I was afforded so little free time I hardly ever went out."
"When I wasn't at work, I was asleep, and when I wasn't asleep I was at work."
"I know about a few tourist locations, but most of Tokyo's charms remain a mystery to me."
"I wouldn't know where to take Stephania without an intensive amount of research."
"As such, I decided to offset some of the responsibility of playing tour guide onto a woman who knows Tokyo far better than I do."
"This woman is none other than Cosmos Moretti."
"Cosmos's job centers around taking photographs of herself in all kinds of locations: cute cafés, hotel rooms, and hot springs to name a few."
"Cosmos also vlogs her day-to-day life, and posts these as videos on MyTube. Her \"follow me around\" videos get a lot of views, as she films herself in theme parks, aquariums, and shopping centers."
"Cosmos is intimately familiar with all the most popular locations in Tokyo."
"If anybody's qualified to be Stephania's guide during her stay in Japan, she is."
$ sface='smile'
$ sbody='cas1'
show steffy at c2
Stephania "I wonder when Miss Moretti will arrive..."
"Stephania, who was notified about my plans ahead of time, looks to the clock on the wall with expectation."
$ sface='happy'
show steffy at c4
Stephania "I cannot wait to meet her!"
Hiroki "You aren't jealous that I'll be spending time with her?"
$ sface='shock'
$ sbody='cas2'
show steffy at c3
Stephania "Oh, no! I am not the jealous type - and, in any case, if you are fond of Miss Moretti, I am sure she must be a wonderful woman."
Hiroki "She's... {w}an interesting woman, if nothing else."
"Cosmos might be a social media star on paper, but in actuality, she makes the majority of her money taking lewd photographs of herself for her army of online fans."
"I don't have an issue with Cosmos's line of work, but maybe Stephania and Elizabeth would disapprove of it?"
"Stephania isn't a judgmental person, but she {i}is{/i} royalty. I'm concerned that Cosmos might be a bit too much for her to handle."
"Part of me thought it might be better to enlist Hifumi's help in this enterprise instead, or maybe Marina's, but the both of them were too busy with their own work to take the time off to see Stephania."
"Cosmos was the only member of my retinue readily available."
"I'm glad she agreed to help out, given I called at such short notice, but I do have to wonder if everything will be OK."

stop music fadeout 1.0

"I'm busy pondering this, when..."

play music "bgm/succubus_weird_loop.ogg" fadein 1.0
$camera_move(0,0,0,0,4,'ease')
$ cface='laugh'
$ cbody='wcas1'
$ sface='smile'
$ sbody='cas2'
$ lface='serious'
$ lbody='maid2'
call s_elicostef from _call_s_elicostef_1

Cosmos "Meowdy, everyone. It's very good to meet you all."
"My front door opens and everybody's favorite cat-eared succubus enters."
"She's ditched the short shorts she usually wears, and the ostentatious cheerleader outfit she donned before my departure to Astoria, and, instead, she's gone for a more normal outfit..."
"Well. \"Normal\" by Cosmos's standards, at least."
"She's still wearing those cat ears she loves so much, but she's coupled them with clothes that don't look too ill-suited for winter."
"She's wearing a purple vest with a coat, and a matching denim skirt."
"This attire is significantly less showy than Cosmos's cosplay outfits. I'm relieved she's not come in a bunny outfit, or a nurse's uniform, though perhaps part of me is a little disappointed about that?"
"Oh well."
"I'm glad Cosmos took my memo to heart, and dressed a bit more conservatively for Stephania's sake."
"My worries might've been in vain, however, because Stephania doesn't look at all put out by Cosmos's appearance."
"Instead, smiling, Stephania says..."
Stephania "I take it you are Miss Cosmos Moretti?"
$ cface='smile'
show cosmos at c2
Cosmos "Ding, ding. That's correct! If we were on a TV show, you'd get a prize, hehe."
$ cface='joke'
$ cbody='wcas5'
show cosmos at c1
Cosmos "Did Hiroki tell you about me?"
$ sface='happy'
show steffy at c2
Stephania "He did, yes. He said that you were a dear companion of his, and that you would be showing Lizzie and me around Tokyo."
Stephania "This is my first time in Tokyo, so I'm very excited!"
$ cface='laugh'
show cosmos at c4
Cosmos "You should be! There's a lot in Tokyo to see. I was a bit overwhelmed when I first came here myself, but now it feels like I'm right where I belong."
$ cface='joke'
show cosmos at c3
Cosmos "I'll be sure to show you a good time, or my name isn't Cosmos."
$ lbody='maid1'
show lizzie flip at c4
Elizabeth "{i}Is{/i} your name really Cosmos? It is quite strange."
$ cface='laugh'
show cosmos at c1
Cosmos "I get that a lot, hehe, but it really is my name. It's what my mamma called me."
$ cface='smile'
$ cbody='wcas1'
show cosmos at c2
Cosmos "It's written on my birth certificate, in fact, if you'd like me to dig it out and show you it?"
$ lface='angry'
show lizzie flip at c5
Elizabeth "Oh, no, that would be fine. I was simply curious."
$ lface='smile'
show lizzie flip at c1
Elizabeth "Thank you in any case, Miss Moretti, for making milady and I so welcome."
Elizabeth "Milady has been fond of Japan, and of its rich culture, ever since she was a young girl."
Elizabeth "I know she regards this opportunity to explore is environs as a great blessing."
$ cface='sweatdrop'
show cosmos at c4
Cosmos "Well, I don't know if I can bless you..."
$ cface='smile'
$ cbody='wcas5'
show cosmos at c3
Cosmos "I'm not officially ordained, although I {i}do{/i} have a nun outfit. It is quite skimpy, though."
Cosmos "I don't think real nuns wear PVC..."
"No, I'm sure they don't: not outside of adult videos, at least..."
"And I don't think the nuns in those videos are devout followers of any kind of faith, really."
$ cface='sweatdrop'
show cosmos at c1
Cosmos "And you don't have to call me \"Miss Moretti\", ehehe. It sounds too formal!"
$ lface='serious'
show lizzie flip at c1
Elizabeth "Is it?"
$ cface='smile'
show cosmos at c3
Cosmos "Yeah. Nobody's ever called me that before. My fans usually call me \"Cosmos-tan\", or \"my waifu\", or \"my cute kitty\", or \"Cosette\"..."
Hiroki "\"Cosette\"?"
"I frown."
Hiroki "That's a bit of a strange nickname, isn't it?"
$ cface='laugh'
show cosmos at c2
Cosmos "The guy who calls me that is a big fan of musicals."
Hiroki "And French revolutions?"
$ cface='neutral'
show cosmos at c1
Cosmos "He is, yeah. How did you know?"
Hiroki "Oh, it was just a lucky guess..."
"I can only hope, for Cosmos's sake, this intriguing fan of hers doesn't want to see her dressed in rags while singing wistfully about wanting to live in a castle on a cloud."
$ lface='angry'
show lizzie flip at c2
Elizabeth "My apologies."
Elizabeth "I called you \"Miss Moretti\" out of habit - it is my way, you see, to be polite to everybody - but if you dislike that appellation, I can dispense with the \"Miss\"."
$ lface='serious'
show lizzie flip at c3
Elizabeth "I have no desire, after all, to make you uncomfortable."
Elizabeth "Would \"Cosmos\" be more suitable?"
$ cface='grin'
show cosmos at c4
Cosmos "That feels a lot better, hehe."
$ sface='smile2'
show steffy at c4
Stephania "Then I shall call you \"Cosmos\", too! I apologize for the offense!"
$ cface='smile2'
$ cbody='wcas1'
show cosmos at c3
Cosmos "It's alright. You haven't offended me. In fact, you don't have to call me \"Cosmos\" at all: not if you don't want to."
Cosmos "Ayu always calls me \"idiot\" instead. It's a friendly nickname she gave me because we're so close!"
$ sface='worried'
show steffy at c3
Stephania "Goodness me!"
Stephania "That sounds like an awfully mean thing to say to one's friend, but perhaps this is a normal manner of address in Japan?"
$ sface='sad'
$ sbody='cas2'
show steffy at c1
Stephania "Should I start calling people idiots if I wish to make their acquaintance, Hiroki?"
$ lface='worried'
$ lbody='maid1'
show lizzie flip at c4
Hisabeth "No, you absolutely should not."
$ lface='serious'
show lizzie flip at c1
Elizabeth "There is nothing wrong with the way you speak as it is, milady. Your fine manners are a credit to you."
Elizabeth "Please, do not call people idiots. It would break my heart."
Hiroki "It's not a normal thing to call people, either. Cosmos's idea of what constitutes \"normalcy\" is a bit different to most people's."
$ sface='smile2'
show steffy at c3
Stephania "Oh, right. I see. I suppose I let myself get carried away, hehe."
$ sface='smile'
$ sbody='cas1'
show steffy at c2
Stephania "Then I shall simply call you \"Cosmos\". Once again, it is a pleasure to meet you!"
$ cface='laugh'
show cosmos at c1
Cosmos "The pleasure is all mine. I've never seen a princess before: not outside of fairytales."
$ cface='smile2'
$ cbody='wcas1'
show cosmos at c3
Cosmos "You are just as pretty as Hiroki said you were. I can see why he likes you so much."
Cosmos "You look just like an illustration from a story, with all your lovely blonde hair."
$ cface='laugh'
show cosmos at c1
Cosmos "You're adorable!"
$ sface='shy'
show steffy at c1
Stephania "W-Well, thank you."
Stephania "A lot of people have blonde hair in Astoria. It is a common coloration."
$ sbody='cas2'
show steffy at c3
Stephania "I believe my looks are quite average, really."
$ lface='smile'
$ lbody='maid2'
show lizzie flip at c4
Elizabeth "And {i}I{/i} believe, as I have often said, that you are being too modest, milady. Miss Mo- Cosmos, I mean, is quite right. You are truly a treasure."
$ cface='smile'
show cosmos at c4
Cosmos "A sparkling jewel!"
$ lbody='maid1'
show lizzie flip at c3
Elizabeth "A rare flower."
$ cface='grin'
show cosmos at c3
Cosmos "A top tier waifu!"
$ lface='worried'
show lizzie flip at c1
Elizabeth "\"Waifu\" What is that?"
$ cface='smile2'
show cosmos at c1
Cosmos "It's a character from an anime or a visual novel whose design and personality are so moe, you can't help but want to look after her."
$ lface='serious'
show lizzie flip at c3
Elizabeth "Oh, I see."
Elizabeth "I cannot say I am as familiar with Japanese media as milady is, but if that is the true definition of a \"waifu\", then I believe milady suits it. I do, indeed, wish to look after her."
$ cface='smile'
show cosmos at c3
Cosmos "And then, once you've given your waifu lots of pats on the head, and held her hand..."
"Cosmos smiles coyly."
$ cface='grin'
show cosmos at c2
Cosmos "...it's only natural that you'd take her to your room, and lay her on your bed, and then fu-"
Hiroki "Right! Now that you're here, Cosmos, and we're all getting along, do you want to head out?"
Hiroki "I'm sure there's a lot you wish to do during your trip to Japan, isn't there, Steffy?"
$ sface='happy'
show steffy at c1
Stephania "Oh, yes! I can hardly wait!"
$ cface='smile2'
$ cbody = 'wcas5'
show cosmos at c3
Cosmos "Then we won't wait. I can take you out, if you want. I have a lot of plans up my sleeve, nyehehe."
$ cface='smile'
show cosmos at c4
Cosmos "I want to show off all the best parts of Japan and our culture to you, Steffy, so you have the bestest trip imaginable!"
$ sface='worried'
show steffy at c3
Stephania "Goodness! That is very sweet of you! I hope you don't feel too pressured to show me around, though?"
$ cface='smile2'
show cosmos at c3
Cosmos "Not at all. I'm happy to help. I can't turn down a request from a cute girl like you!"
$ sface='happy'
show steffy at c2
Stephania "You're being too nice, really. I think you're much cuter than I am. Your cat ears are adorable!"
$ cface='laugh'
$ cbody='wcas1'
show cosmos at c2
Cosmos "I'm glad you think so!"
Cosmos "Ayu says they make me look like a \"try-hard loser too immature to accept the responsibility of being a normal human being\"..."
"Ouch. Now {i}that's{/i} scathing, even coming from Ayu!"
"At least \"try-hard loser\" is better, I suppose, than \"furry degenerate\"?"
"Cat ears are kind of ostentatious, yeah, but they're a step below wearing collars, tails, and crawling around on all-fours, at least..."
"Though, now that I think about it, Cosmos {i}did{/i} let me walk her around the street on a leash that one time, didn't she?"
"Granted, she was pretending to be a dog back then, not a cat, but it was still pretty lewd..."
$ cface='smile2'
show cosmos at c1
Cosmos "...but I am glad you think my ears are cute, Steffy!"
$ sface='smile'
$ sbody='cas1'
show steffy at c3
Stephania "They are cute! They are very cute!"
$ cface='smile'
show cosmos at c3
Cosmos "Well, so are you!"
$ sface='worried'
show steffy at c1
Stephania "No, you!"
Hiroki "Geez..."
"I smile as I watch Stephania and Cosmos bicker, amused by the back-and-forth nature of their argument."
"I was worrying, before Cosmos arrived, that she and Stephania mightn't get along, owing to how different their upbringings are, but I can see I was mistaken."
"Cosmos is so kind, she can get along with anybody..."
"Or, well. {i}Almost{/i} anybody."
"The day has yet to properly commence, but I'm quietly optimistic as to how it'll progress."
"I'm sure, with Cosmos leading the way, we'll have a great time. It's hard not to have fun when she's around."

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
play music "bgm/succubus_slife_of_life_2_loop.ogg" fadein 1.0
scene cafe
$ cface='smile'
$ cbody='wcas1'
call s_cosmos from _call_s_cosmos_1
$camera_move(0,400,300,0,0,'dissolve')
with wiperight_slow
window show dissolve

Cosmos "Here we are!"
"Cosmos announces cheerfully as our small party arrives at our destination: a cute café Cosmos and I have frequented on numerous occasions."

scene cafe:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 30.0 crop (400, 120, 1280, 720)
with wiperight_slow

"This café was the first place, actually, that Cosmos and I had a proper conversation."
"I actually met Cosmos on the train, during my commute to work, but we didn't really talk back then."
"The train's compartment was far too cramped and noisy for any kind of meaningful back-and-forth, and Cosmos had more than dialogue on her mind during that particular encounter."
"We might've gotten pretty personal on that train, but I barely knew a thing about Cosmos back then."
"It wasn't until Cosmos took me to this café that I was able to get a proper look at her."
"It was while we were sitting about one of these tables, Cosmos chowing down on an ice cream sundae, that Cosmos decided she wanted to make me her boyfriend."
"This was almost a year ago now, and I can scarcely imagine my life without Cosmos now."
"We've been through an awful lot together, from an unplanned jaunt to the succubus realm to a holiday at Ayu's fancy beach house."
"It's been a while since we came back to this café together, and it's steeped in nostalgia. I can't help but feel sentimental as I glance about at the familiar décor."

scene cafe
$ sface='shock'
$ sbody='cas1'
$ eface='serious'
$ ebody='maid1'
$ cface='smile'
$ cbody='wcas1'
call s_elicostef from _call_s_elicostef_23423422
$camera_move(0,0,0,0,0,'dissolve')
with wipeleft_slow

Stephania "Goodness me...!"
"Stephania, however, has no such associations with this café, fond or otherwise. She's never been here before. It's all quite new to her, as is indicated by her look of surprise."
$ sbody='cas2'
show steffy at c2
Stephania "Is this one of those fabled \"maid cafés\" I have heard so much about?"
$ cface='joke'
$ cbody='wcas5'
show cosmos at c1
Cosmos "Indeed, it is!"
$ cface='smile'
show cosmos at c4
Cosmos "I thought you might want to see it, Steffy. Maids are an important part of Japanese culture."
Cosmos "They're a cornerstone of our society!"
Hiroki "They are if we're talking specifically about nerd culture, maybe..."
"While Japan might be synonymous with maid cafés overseas, most Japanese people do not, in fact, make a point of frequenting venues such as this. They're considered kind of embarrassing, actually."
"I know I never would've come here, were it not for Cosmos's insistences."
"Despite the way I look (I know my glasses aren't particularly fashionable), I'm not waist-deep in the mire that is nerd culture: not like Cosmos."
"I don't watch anime, I don't read manga (save for a few popular fighting series that I loved as a kid), and I certainly don't read lewd visual novels that feature scantily-clad heroines."
"My tastes have always been more pedestrian: \"normie\", if you will."
"I'm passionate about photography, I used to dabble in music, and I enjoy converting carbon dioxide into oxygen."
"All told, I'm incredibly average - at least, I {i}was{/i}, before meeting a harem of succubi."
"Now, I'd be hard-pressed to call myself \"average\", but my interests remain fairly standard."
"I can't deny that the maids who work in this café {i}are{/i} pretty cute, though"
"Their short skirts reveal a lot more skin than Elizabeth's own demure black and white attire does, and the ruffled headpieces are a particularly nice touch."
"I'm not so stuck-up I consider myself above appreciating a pretty maid every once in a while."
$ sface='smile'
show steffy at c4
Stephania "Are you familiar with this place, Hiroki?"
Stephania "Do Japanese men such as yourselves often visit establishments like this to eat?"
Hiroki "No, uh, not really. It's not that common..."
$ cface='shock'
$ cbody='wcas1'
show cosmos at c3
Cosmos "Huh? Isn't it common?"
Hiroki "Of course not! Why are you asking me that? You're not a tourist. You {i}live{/i} in Japan!"
"Though, if Ayu were here, I'm sure she'd say something scathing, to the tune of: \"{i}Does{/i} Cosmos live in Japan? I thought she lived in her own fantasy land.\""
"I don't always agree with Ayu, but the fictitious Ayu conjured up in my mind's eye might have a point there."
$ cface='sad'
show cosmos at c2
Cosmos "Maybe so, but I don't understand why anybody would want to eat anywhere else, when maid cafés exist."
Cosmos "The waitresses are so cute, it would be a shame to go anywhere else."
$ cface='smile2'
show cosmos at c1
Cosmos "I like it when they pipe hearts on your omelette rice, and when they do little spells to make the food taste even yummier."
Cosmos "The waitresses at family restaurants don't do that, and their outfits aren't as frilly."
$ cface='sweatdrop'
show cosmos at c3
Cosmos "Family restaurants are really boring."
Hiroki "I think your tastes are just unique..."
"Now I'm getting curious."
Hiroki "Don't tell me you {i}only{/i} eat at maid cafés?"
$ cface='neutral'
show cosmos at c2
Cosmos "I do most of the time, yes. Why?"
Hiroki "Why, you ask..."
"I frown."
Hiroki "The waitresses at these places might be cute, I guess-"
$ cface='laugh'
$ cbody='wcas5'
show cosmos at c1
Cosmos "They {i}are{/i} cute; very much so. I am glad you agree!"
Hiroki "-but the food is always subpar. It's nothing special, and it's overpriced for what it is."
Hiroki "When you come to a place like this, you're paying for the experience, rather than the actual food."
Hiroki "It's fine every once in a while, but eating out all the time must get expensive, mustn't it?"
$ cface='smile'
show cosmos at c4
Cosmos "It's OK, Hiroki. I would rather be broke and happy and surrounded by cute maids than rich and sad without any maids to attend to me."
"Now, that seems like a pretty dangerous way of thinking."
"I guess it's a good thing Cosmos is such a popular social media star, or she'd be in real danger of bankrupting herself in her eternal pursuit of knee socks and white aprons."
$ cface='joke'
$ cbody='wcas1'
show cosmos at c3
Cosmos "Besides, I have plenty of money. I can afford to eat sub-par omelettes every day, if I want."
Hiroki "So, you admit the food here is sub-par?"
$ cface='smile2'
show cosmos at c2
Cosmos "I would never say otherwise. I'm not delusional."
"Not completely, at least."
$ cface='neutral'
show cosmos at c1
Cosmos "I know better food exists, but as these restaurants don't employ maids, I am not interested in them."
$ cface='smile2'
show cosmos at c4
Cosmos "Even a plain, lukewarm omelette can taste good if it's served to you by a pretty woman in a frilly dress."
$ cface='laugh'
$ cbody='wcas5'
show cosmos at c3
Cosmos "I am sure Hazel would agree with me!"
Hiroki "You're probably not wrong about that..."
"I know exactly how Hazel feels about maids, thanks to a few of the lecherous comments she made re: Elizabeth back in Astoria."
"...Geez."
"Are all the members of my succubus harem weak against maids? Is this a shared fetish they all have?"
"Even Hifumi's dressed up as a maid before to appease me, though her maid outfit was more traditionally Japanese than the Western-style get-ups the maids in this café are sporting."
$ cface='smile'
show cosmos at c2
Cosmos "Anyway! I like this café a lot, so I thought you would too, Steffy. Like I said, maid cafés are the pinnacle of Japanese culture!"
Hiroki "I'm sure a lot of people would be offended if they heard you say that..."
"I sigh."
"What about our country's rich history? Our beautiful temples; our verdant forests; our majestic hills?"
"I guess all that is irrelevant to Cosmos. Forget all of our cultural landmarks and our geographic wonders."
"Maids are where it's all at."
$ cface='smile2'
show cosmos at c4
Cosmos "Hiroki and I have come here a lot, despite Hiroki's protests, and we're both very fond of it."
Cosmos "It was here, in fact, that Hiroki and I went on our first date!"
$ lface='angry'
show lizzie flip at c1
Elizabeth "Is it, now?"
$ sface='shy'
show steffy at c2
Stephania "Oh my!"
$ sbody='cas1'
show steffy at c1
Stephania "Th-This café must possess a lot of emotional significance for the pair of you!"
Stephania "Is it really alright that I am here now? I would not wish to intrude upon your fond memories!"
$ cface='smile2'
show cosmos at c3
Cosmos "It's fine. You're Hiroki's girlfriend too, so I thought you should come here. It feels only right."
$ cbody='wcas1'
show cosmos at c1
Cosmos "I want you to know what going on a proper date in Japan feels like..."
$ cface='laugh'
show cosmos at c4
Cosmos "And, of course, I want to show you a real, genuine Japanese maid."
Cosmos "I am sure these maids are very different to the ones in the palace!"
$ lface='serious'
$ lbody='maid2'
show lizzie flip at c4
Elizabeth "Yes, indeed, they are. The attire of these maids is not at all appropriate. They are revealing rather too much skin."
"This seems like a bit of a hypocritical complaint, given the cut-outs at the side of Elizabeth's own outfit, but I don't mention that."
"Elizabeth looks so perturbed, I'm afraid any attempts to call her out on her hypocrisy would net me a nasty glare."
"I've been on the receiving end of Elizabeth's glares a few times, and it's not a pleasant experience."
"Elizabeth might be a maid, but she's a little scary."
$ lface='angry'
show lizzie flip at c3
Elizabeth "Their outfits are very gaudy, too."
$ lface='serious'
show lizzie flip at c1
Elizabeth "As a maid, I find their apparel most ill-fitting. Maids ought not to display their bodies, but they should, instead, strive to remain unobtrusive."
$ lface='worried'
show lizzie flip at c2
Elizabeth "Maids exist solely to serve others. Their serving should be a quiet, understated kind of affair, conducted without any unnecessary pomp."
Elizabeth "These women, meanwhile, seem determined to draw as much attention to themselves as possible."
$ lface='angry'
show lizzie flip at c4
Elizabeth "They are not at all professional."
$ lface='serious'
$ lbody='maid1'
show lizzie flip at c3
Elizabeth "I fear I do not think very much of these Japanese maids, although..."
"Elizabeth exhales."
$ lface='angry'
show lizzie flip at c2
Elizabeth "I suppose I must reserve my judgment until I have been served by one of these so-called maids. I will be able to determine their worth then."
$ lface='serious'
show lizzie flip at c1
Elizabeth "As a top maid myself, however, I fear I will be let down."
$ lface='very angry'
show lizzie flip at c3
Elizabeth "These little girls can never hope to measure up to me."
Hiroki "Ulp..."
"I'm starting to feel a little afraid on behalf of the maids assembled in this café."
"Cosmos only brought Stephania and Elizabeth here for a bit of fun, but it looks like Elizabeth's taking this very, very seriously."
"How will she react, I wonder, if the unlucky maid assigned to serving us makes a mistake?"
"I almost dread to think of it."

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyd with fstartgame
window show dissolve

"Half an hour later..."

play music "bgm/succubus_weird_loop.ogg" fadein 1.0
scene cafe
$ sface='shock'
$ sbody='cas1'
$ lface='serious'
$ lbody='maid2'
$ cface='smile'
$ cbody='wcas1'
call s_elicostef from _call_s_elicostef_2
with wipedown_slow

Elizabeth "Hmph. So, {i}this{/i} is the quality of the service at this so-called \"maid café\", is it?"
"An irate Elizabeth examines the curry she was recently served, by a brightly-beaming maid in a skimpy outfit."
"Cosmos seems pretty taken with her food - she's positively drooling over it, and over the maid, who's sasheying away from our table - but Elizabeth looks less impressed."
"Elizabeth's arms are folded beneath her chest and her eyes are narrowed in obvious disapproval."
$ sface='worried'
show steffy at c2
Stephania "Lizzie...?"
$ sbody='cas2'
show steffy at c1
Stephania "Is something the matter?"
$ lface='angry'
show lizzie flip at c4
Elizabeth "I would say so, yes."
$ cface='sad'
show cosmos at c2
Cosmos "Don't you like Japanese curry, Lizzie? Is it too mild for you?"
$ lface='serious'
show lizzie flip at c2
Elizabeth "I do prefer my curry to have a bit of a kick to it, yes, but that is not the issue here."
$ cface='neutral'
show cosmos at c1
Cosmos "Would you have preferred it if our maid had written something cute on it, then, like she did with my omelette rice?"
Cosmos "Maids will usually draw pictures with ketchup on your food, if you ask them to. It's part of the service."
$ cface='sweatdrop'
show cosmos at c4
Cosmos "It's a bit difficult to do that with curry, though."
$ cface='smile2'
show cosmos at c2
Cosmos "That's why I always order omelettes at these restaurants. They feel more personal, hehe."
$ lface='angry'
$ lbody='maid1'
show lizzie flip at c1
Elizabeth "No, it is quite alright. You needn't offer me any of your food."
Elizabeth "My issue is not that my curry lacks a cute illustration. I do not think pointless flourishes such as ketchup hearts of flowers add any significant worth to a meal."
$ cface='shock'
show cosmos at c1
Cosmos "P-Pointless flourishes?!"
"Cosmos stares at Elizabeth, her expression aggrieved."
$ cface='sad'
show cosmos at c4
Cosmos "But these \"pointless flourishes\" are what the appeal of cafés like this hinge upon!"
$ cbody='wcas5'
show cosmos at c3
Cosmos "If it weren't for these \"pointless flourishes\", this café would be no different from a family restaurant!"
$ lface='serious'
show lizzie flip at c3
Elizabeth "Perhaps we ought to have gone to a family restaurant, then, if their standards are higher."
$ lface='angry'
show lizzie flip at c2
Elizabeth "The presentation of my meal leaves much to be desired. I would not be surprised if the roux was bought from a shop, and the vegetables have been cut very roughly."
$ lface='serious'
show lizzie flip at c1
Elizabeth "No amount of ketchup hearts would be able to save this meal. It looks like something made by a child, and a particularly clumsy child at that."
$ lbody='maid2'
show lizzie flip at c4
Elizabeth "I would sooner stick pins beneath my fingernails than serve a dish like this to milady."
Elizabeth "It is not fit for human consumption."
$ sface='shock'
show steffy at c4
Stephania "I-I think you're being a bit too harsh, Lizzie!"
Stephania "This food doesn't look as extravagant as the food served in the palace, but that is only to be expected! Our cooks are professionals who trained for many years in Paris!"
$ sface='sad'
$ sbody='cas2'
show steffy at c3
Stephania "It would be unfair to expect a similar level of quality in a small café like this!"
$ lface='angry'
show lizzie flip at c2
Elizabeth "Indeed, you are correct. Perhaps I am being somewhat unfair - but how can you blame me, milady, when I want only the best for you?"
$ lface='serious'
show lizzie flip at c1
Elizabeth "While I do not doubt that this food is edible, that is not great praise."
Elizabeth "\"Edible\" is not the baseline I search for when it comes to assessing the quality of a meal."
$ lbody='maid1'
show lizzie flip at c3
Elizabeth "I would rather some real passion be put into the food I consume, particularly after paying for it."
$ lface='angry'
show lizzie flip at c1
Elizabeth "It is clear that whomsoever made this meal did not care about its recipient. It is too clumsily fashioned. There is no love in it."
$ lface='serious'
show lizzie flip at c4
Elizabeth "Moreover..."
"Elizabeth's lip curls."
Elizabeth "It took more than twenty minutes for this food to arrive - and that, I fear, is far too long."
$ lbody='maid1'
show lizzie flip at c3
Elizabeth "Our waitress - I cannot bring myself to call her a \"maid\" - might have smiled when she served us, but her smiles are not enough to excuse the tardiness of our meal."
$ lface='worried'
show lizzie flip at c2
Elizabeth "Why, my curry is already beginning to get cold!"
$ lface='serious'
show lizzie flip at c1
Elizabeth "I can abide such sloppiness: not as a maid myself."
$ lface='very angry'
show lizzie flip at c4
"Elizabeth slams her palm against the tabletop."
"She slams it so hard, in fact, that our plates and our drinks shake."
Elizabeth "The service here is slow, the servers are dressed inappropriately, and the price for this so-called \"experience\" is exorbitant!"
Elizabeth "Milady deserves much, much better!"
$ sface='worried'
show steffy at c1
Stephania "I-I'm fine, Lizzie! Please, don't worry so much! I'm looking forward to eating my food...!"
$ lface='serious'
show lizzie flip at c3
Elizabeth "You are too kind, milady. You ought to stand up for yourself, though. You deserve to be treated better than this."
$ lbody='maid2'
show lizzie flip at c2
Elizabeth "You {i}know{/i} that you deserve better than this."
show lizzie flip at c1
Elizabeth "I wish only for you to be happy, wherever you go, and so..."
"Elizabeth rises purposefully to her feet, the legs of her chair scraping against the floor."
$ lface='angry'
show lizzie flip at c3
Elizabeth "I must knock some sense into the so-called \"maids\" who work at this establishment."
$ lface='serious'
show lizzie flip at c2
Elizabeth "It is high time I showed these maids how they ought to be interacting with their customers."

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyd with fstartgame
window show dissolve

"A little while later..."

play music "bgm/succubus_comedy_loop.ogg" fadein 1.0
scene cafe
$ lface='serious'
$ lbody='maid1'
call s_lizzie from _call_s_lizzie_1
$camera_move(0,400,300,0,0,'dissolve')
with wipedown_slow

Maid "Excuse me, Miss Elizabeth, but does my posture look alright?"
Maidd "Miss Elizabeth, there's a new order for table seven!"
$ lbody='maid2'
show lizzie at c4
Maiddd "Miss Elizabeth, my ribbon is crooked! Would you fix it for me?"
Maidddd "Am I addressing the customers with enough respect, Miss Elizabeth?"
Maidd "Miss Elizabeth, can you help me?!"
$ lface='angry'
show lizzie at c3
Maid "Ooh! The way you serve your customers is so elegant and regal, Miss Elizabeth!"
Maiddd "Your hair is so silky, Miss Elizabeth! What conditioner do you use?"
Maidddd "Your skin is so soft and smooth, Miss Elizabeth! I'm jealous!"
Maidd "I don't know how I ever got by without you, Miss Elizabeth! You really have opened my eyes!"
$ lface='smile'
show lizzie at c2
Maid "We love you, Miss Elizabeth! Don't ever leave us!"
Hiroki "...Well, I'll be."
"I watch as Elizabeth walks briskly through the café, dispensing with advice, when so asked, by the gaggle of needy maids flocking her, while occasionally pausing to take orders."
"Elizabeth appointed herself as this café's head maid less then fifteen minutes ago, and the maids have already fallen under her thrall."
"They seem quite taken by her, despite her forcefulness..."
"Or maybe they're taken with her {i}because{/i} of it?"
"Maybe these maids are all masochists who like being pushed around. That'd certainly explain why they let Elizabeth walk all over them so easily."
$ lface='serious'
show lizzie at c3
Maid "Miss Elizabeth, you really are amazing!"
Maidd "Please, show me what to do!"
$ lface='smile'
$ lbody='maid1'
show lizzie at c1
Maiddd "You're the bestest maid I've ever seen!"
"Elizabeth has adapted to her role of maid-cum-mentor awfully well, like a duck to water."
"Maybe she was made to lead others?"
"Could she be related, in some distant manner, to Joan of Arc?"
"Now, {i}that{/i} would be pretty badass."
"Elizabeth herself seems pretty badass, in fact, despite her maid outfit. She makes her black-and-white attire look like battle armour: something to be worn before riding, on horseback, into the fray."
"I can't help but be impressed."
"I always knew Elizabeth took her job seriously, but I never realized she was quite {i}this{/i} passionate!"

$camera_move(0,400,300,0,3,'ease')
hide lizzie with dissolve
$ sface='worried'
$ sbody='cas1'
call s_steffy from _call_s_steffy_1

"Stephania, meanwhile, seems a bit embarrassed by this affair."
"Her face is flushed and, awkwardly, she sinks down in her chair."
$ sface='sad'
show steffy at c2
Stephania "I-I must apologize for Lizzie's behavior, everybody. I know she's being very forceful."
$ sbody='cas2'
show steffy at c4
Stephania "I did try to tell her to calm down, but she didn't listen."
Stephania "It can be hard to make her see sense when she gets like this."
$ sface='worried'
show steffy at c3
Stephania "I hope you aren't too offended, Hiroki, Cosmos."

window hide dissolve

menu:
    with dissolve

    "I'm not offended at all.":

        window show dissolve

        $ succ_points += 2

        Hiroki "Oh, no, it's fine. Why would I be offended?"
        $ sface='shock'
        show steffy at c1
        Stephania "Because you and Cosmos brought us here so that we might have a good time!"
        Stephania "I know you wanted us to relax, but Lizzie isn't relaxing at all."
        Stephania "She's working even harder than she does back in the palace...!"
        $ sface='worried'
        show steffy at c3
        "Stephania sighs."
        Stephania "She was rude about the food too, and about the service. She didn't have a single nice thing about this experience."
        $ sface='sad'
        show steffy at c2
        Stephania "That must have been awkward for you, surely?"
        Hiroki "Nah. I was plenty negative about this café myself, before I sat down. I find these kinds of establishments pretty gimmicky, if I'm being quite honest."
        Hiroki "My feelings are more aligned with Elizabeth's than Cosmos's, although..."
        "I smile sheepishly."
        Hiroki "I'd never presume to try and tell the maids at this place how to do their jobs. That'd be going a step too far."
        $ sface='angry'
        $ sbody='cas1'
        show steffy at c1
        Stephania "Elizabeth really {i}is{/i} going too far, isn't she? She can be so impossible sometimes!"

    "I do wish she'd chill out a bit, yeah.":

        window show dissolve

        Hiroki "I'm not offended, but I do wish she'd chill out a bit."
        Hiroki "I don't want her stressing herself out."
        Hiroki "I thought she was supposed to be on holiday."
        $ sface='angry'
        $ sbody='cas1'
        show steffy at c1
        Stephania "Those are my thoughts exactly!"
        Stephania "I love Lizzie, but she can be so stubborn sometimes!"

Maid "Miss Elizabeth, I cut my finger! Would you kiss it better for me?"
Maidd "Miss Elizabeth, the button on the front of my blouse has come undone! Could you fasten it, please?"
Maiddd "Miss Elizabeth, my ribbon is crooked again! If you could fix it, I would be forever in your debt!"
Hiroki "...Hahaha. Well."
"I laugh, amused, as the maids of this humble establishment twitter in Elizabeth's wake, like so many starlings."
Hiroki "These maids don't seem to have any objections about her involvement."
"These maids have gotten so attached to Elizabeth they're only a step short of groveling at her feet."
"They're looking at Elizabeth like she's some sort of goddess."
"Maybe they'll fashion effigies of her and kowtow before them in the privacy of their own homes?"
"I wouldn't be surprised."
$ sface='worried'
show steffy at c3
Stephania "Perhaps these maids do not mind too much, but what about you, Cosmos? You have been very quiet."
Stephania "You aren't upset by this turn of events, are you?"

$camera_move(400,300,200,0,4,'ease')
$ cface='smile2'
$ cbody='wcas1'
call s_stefmos from _call_s_stefmos_1

Cosmos "Not at all! I think this is very cool, actually!"
$ sface='worried'
show steffy flip at c4
Stephania "In what manner?"
$ cface='neutral'
show cosmos at c2
Cosmos "Well, let me see..."
$ cbody='wcas5'
show cosmos at c1
Cosmos "It's a bit hard to explain, really. I'm not very good with words, but... Hmm."
$ cface='sad'
show cosmos at c4
Cosmos "I suppose I feel a bit...{w} guilty?"
$ sface='shock'
show steffy flip at c2
Stephania "Why do you feel guilty?"
$ cface='sad'
show cosmos at c3
Cosmos "It's just... Well."
$ cbody='wcas1'
show cosmos at c2
Cosmos "I've been to a lot of maid cafés in my time, and I like them a lot. I thought I knew a lot about maids, because of this, but now that I think about it..."
Cosmos "I don't think I've ever seen a maid work as seriously as Lizzie is: not in any of the cafés I've visited. She's on a whole other level."
$ sface='worried'
show steffy flip at c1
Stephania "Lizzie is nothing if not passionate, yes. She always does her best."
$ cface='smile2'
show cosmos at c1
Cosmos "I know that. I can tell. That's why she's so cool."
$ cface='shock'
show cosmos at c3
Cosmos "I used to think that the maids at these cafés were incredible, but now I am beginning to see the error of my ways."
$ cbody='wcas5'
show cosmos at c5
Cosmos "Clothes do not, as they say, make the man, and in this case, the maid's dress does not make a maid."
$ cface='sad'
show cosmos at c2
Cosmos "A woman might {i}look{/i} like a maid, but that does not mean she really is one: not in her heart."
Cosmos "To be a proper maid, one must feel it in their soul, like Lizzie does."
$ cface='angry'
show cosmos at c1
Cosmos "Maids are serious business..."
$ cbody='wcas1'
$ cface='shock'
show cosmos at c4
Cosmos "...and now I understand that I have not given them the respect they deserve!"
$ cface='sad'
show cosmos at c3
Cosmos "I feel guilty, now, for ever thinking that the imitation maids at these cafés were \"good enough\", and I feel guilty that I ever thought myself worthy of dressing as a maid myself during my photo shoots!"
Cosmos "I have besmirched the true meaning of being a maid and I never even realized it."
$ cface='shock'
show cosmos at c2
Cosmos "Lizzie's fervor has shown me, however, the error of my ways!"
$ cbody='wcas5'
show cosmos at c1
Cosmos "It is time for me to repent on my past actions and atone!"

hide steffy with dissolve
$ lface='serious'
$ lbody='maid1'
call s_lismos from _call_s_lismos_2

"Cosmos approaches Elizabeth, who's in the midst of serving another customer, then bows down."
"Kneeling before Elizabeth upon the floor of the café, she presses her forehead to the floor and cries..."
$ cface='sad'
show cosmos at c3
Cosmos "Please, Lizzie, take me under your wing! Show me how to be a real maid just like you!"
Cosmos "I am willing to work hard, to unlearn all the erroneous thoughts I ever had about your noble profession!"
$ cbody='wcas1'
show cosmos at c5
Cosmos "I know now that real maids are worth much, much more than frilly dresses..."
$ cface='shock'
show cosmos at c2
Cosmos "And I want to become a sophisticated, self-confident maid just like you!"

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyd with fstartgame
window show dissolve

"And so, in the end..."

play music "bgm/succubus_weird_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("cat_cafe")
if persistent.adult==True:
    scene cg3_a with wipedown_slow
else:
    scene cg3 with wipedown_slow
$ renpy.pause()
window show dissolve

Cosmos "Hi, everyone! It's your favorite cute cat-maid, Cosmos, and I'm here to serve you with a smile!"
Cosmos "Is there anything that you would like? Something delicious to eat? Something refreshing to drink? Or, perhaps..."
"Cosmos smiles deviously."
Cosmos "Me?"
Elizabeth "Oh, {i}please.{/i} That isn't what I told you to say, Cosmos, and you know it."
Cosmos "It isn't?"
Elizabeth "No. If you are to be a proper maid, you cannot go offering yourself to the customers as though you yourself are a delicious dessert to be consumed. It simply isn't seemly."
Elizabeth "Maids ought to be unobtrusive, remember?"
Elizabeth "We exist as vassels who answer to the orders of others, but we should not seek to stand in the spotlight ourselves."
Elizabeth "If you wish to be a true maid, you must learn some decorum - although..."
"Elizabeth's sharp gaze sweeps over Cosmos, and while examining her, she sighs."
Elizabeth "I fear that may not, perhaps, be possible: not when the so-called \"maid outfits\" the girls at this café wear show off such a large amount of skin."
Elizabeth "These outfits are far too gaudy to be worthy of any genuine maid, and I am uncertain as to your choice to pair your attire with those cat ears and that tail."
Elizabeth "It seems uncouth."
Cosmos "Ehehe. I'm sorry, Lizzie. I just can't {i}not{/i} wear cat ears. I don't feel like myself without them."
Cosmos "They're my charm point."
Elizabeth "Charm point?"
Cosmos "That's right. My fans all say they love my cat ears. They are what make me {i}me{/i}, even when I'm trying to work as a maid."
Cosmos "I will always be a catgirl first and foremost. It would not do to deprive my meowsters of my unique appeal!"
Elizabeth "If your \"meowsters\" had any respect for the work we maids do, they would not demand that you make yourself look like a fool..."
Elizabeth "But never mind. If you insist upon the cat ears, I suppose they can stay, though they are not at all a practical design choice."
Elizabeth "I will try to put your appearance to one side, no matter how difficult that may be, and focus, instead, upon your mannerisms."
Elizabeth "Now, maids ought to smile when serving their masters, but do not smile {i}too{/i} much."
Elizabeth "You should not, as I said, make a spectacle of yourself."
Elizabeth "You need to be demure, mild-mannered, and respectful. Do you think you can manage that?"
Cosmos "I'll do my best! My attitude is better than Ayu's, at least."
Cosmos "I think I'm cut out for serving people, but I'm not very good at talking to people."
Cosmos "I don't always know what to say. Sometimes, I feel kind of lost."
Cosmos "I don't think I'm as competent as you, Lizzie. When you serve others, you seem to shine."
Elizabeth "Well, thank you very much. It comes with a good deal of practise, I assure you."
Elizabeth "I have been working as a maid for a long while, and I take my job seriously."
Elizabeth "Serving others is second nature to me now. If you wish to catch up, I fear it will take you a long time. Are you prepared to try hard?"
Cosmos "Yes, Miss Elizabeth! I will do my best!"
Cosmos "I'll become the best maid a clumsy NEET like me could ever hope to be!"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
scene skyd with wiperight_slow
window show dissolve

"Time passes, and the day eventually comes to a close."
"The sun begins to sink, and when it does, Cosmos suggests we cap our date off with bubble tea."
"Our bubble tea secured (man, it's expensive. Where do these trendy cafés get off, charging such exorbitant prices for their drinks?), we then head to a nearby park."
"I'm content to drink my bubble tea (which is taro flavor, by the by) the normal way - namely, with the cup in my hand, and my mouth about the straw - but..."

play music "bgm/succubus_lewd_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("booba_tea")
if persistent.adult==True:
    scene cg4_a with wipedown_slow
else:
    scene cg4 with wipedown_slow
$ renpy.pause()
window show dissolve

Stephania "I-Is this really how girls drink bubble tea nowadays?"
Cosmos "That's right!"
"Cosmos, it seems, has other ideas."
"She told Stephania about an exciting trend which gone about on social media a while back: namely, about balancing one's bubble tea upon one's bosom."
"That's what Cosmos is doing, and she's making quite a valiant attempt at it, too, given her chest isn't particularly pronounced."
"Stephania, seeing what Cosmos was up to, decided to join in, I guess because she didn't want to miss out."
"Would youngsters call that FOMO?"
"...Whatever."
"Obviously, I don't understand what youngsters are into anymore, or what's popular."
"Am I getting old?"
"...At least Elizabeth seems to share my sentiments, because she looks rather dubious about this whole affair herself."
Elizabeth "I don't understand how this is supposed to aid in the drinking of my bubble tea. It is simply making things more difficult."
Elizabeth "I have faith in my coordination, but it's rather hard to balance."
Elizabeth "I hope my drink doesn't spill."
"I hope these drinks don't spill, either."
"Sure, it might be appealing if the fronts of Cosmos's, Stephania's, and Elizabeth's shirts were to get damp, but you could get the same effect with tap water, and that's free."
"These bubble teas, however, were anything but."
"They were eye-wateringly expensive, and I was the muppet who had to buy them."
"I know it's customary for guys to foot the bill when going on dates, but it's not customary for guys to go on dates with three girls at once."
"Is this the (quite literal) price I have to pay for my philandering ways?"
"{i}Sob, sob.{/i}"
"Oh, well. At least Cosmos, Stephania, and Elizabeth all look pretty good right now."
"I can't deny, they're attractive..."
Stephania "O-Oh, this really is difficult! I-I'm afraid I'm not very good at this."
Stephania "I must have lived in the palace too long. I'm so sheltered, I don't know how ordinary girls are supposed to act!"
Elizabeth "With all due respect, milady, I don't think there's anything ordinary about this."
Elizabeth "It all seems a bit salacious to me."
"I'm inclined to agree with the maid. She speaks sense, at least!"
Cosmos "Ehehe, it's OK. Nobody's that good at this on their first attempt. I had to practice a lot to get this juuust right."
Cosmos "I must have gone through at least a dozen cups of bubble tea!"
"What, Cosmos has practised this? {i}Seriously?{/i}"
"I guess I admire her dedication, but doesn't she have better ways to spend her time and her money?"
"...Maybe not."
Stephania "Goodness me! That really is amazing! You work so hard, Cosmos!"
Cosmos "I do my best, hehe~"
Elizabeth "At silly endeavors, maybe, that are of no practical benefit to anybody."
"A bemused Elizabeth sighs, and rightfully so. I really can't blame her for looking so fed up."
Elizabeth "Maybe I should drink this normally. I wouldn't want to make a mess."
Cosmos "Maybe, but, first!"
"Cosmos fishes her phone out of her pocket, then holds it up."
Cosmos "Let's take a selfie! We need to commemorate this moment!"
Elizabeth "Do we really?"
Cosmos "Of course. It isn't every day that I get to drink bubble tea with the princess of a small European country."
Cosmos "Now, big smile, Steffy! I'm going to take it!"
Stephania "R-Right! It would be my pleasure!"
Elizabeth "I suppose I can play along myself..."
Elizabeth "But if you share these photos on social media, I will be very unhappy."
Elizabeth "The only one allowed to gawp at milady's chest is me - and Mr. Ogasawara, on occasions."
Elizabeth "The internet does not need to see this!"
Stephania "Oh, Lizzie, thank you for being so considerate! You really are sweet!"
Elizabeth "Of course. I do worry about you, milady. I {i}have{/i} to, given you never seem to worry about yourself."
Elizabeth "You really are an airhead..."
Elizabeth "But that only adds to your appeal."
"Yeah, I think I have to agree with Elizabeth there. Stephania manages to look innocent no matter what she's doing: even when balancing bubble tea on her chest."
"It's a pretty incredible skill."
"Stephania's pretty incredible in general..."
Cosmos "Alright, everybody! Say cheese!"
"But Cosmos might be even more so."

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
play music "bgm/succubus_stephania_loop.ogg" fadein 1.0
scene park
$ cface='smile'
$ cbody='wcas3'
$ lface='serious'
$ lbody='maid1'
$ sface='smile'
$ sbody='cas1'
call s_elicostef from _call_s_elicostef_4
with fstartgame
window show dissolve

Cosmos "So, how has your day been, Steffy? Have you been enjoying yourself?"
$ sface='happy'
$ sbody='cas2'
show steffy at c2
Stephania "Oh, yes! You've been very kind to me! I am most looking forward to tomorrow!"
$ cface='grin'
show cosmos at c1
Cosmos "Yay. I'm glad to hear it!"
Cosmos "We should have even more fun then. I've arranged something very exciting: just wait and see."
Hiroki "Something exciting...?"
"For some reason, I have a bad feeling about this."
"What constitutes as \"exciting\", I wonder, in Cosmos's world?"
"She sure seemed to enjoy it when I walked her through the streets on a leash, but we're not going to have a repeat performance of that little display, surely?"
"Not in front of Astoria's princess...!!!"
"Japan's relationship with Astoria could be irrevocably ruined in the face of such a social faux pas!"
$ cface='smile'
$ cbody='wcas6'
show cosmos at c4
Cosmos "Yes, something exciting!"
$ cface='smile2'
show cosmos at c3
Cosmos "Ayu has the day off work tomorrow, so I asked her if she wouldn't mind tagging along."
$ cface='grin'
show cosmos at c1
Cosmos "I thought we could all hang out together. It'll be a blast!"
Hiroki "Ayu, huh...?"
"Great. Now I feel even more uneasy."
"Nothing good seems to come of Ayu's company."
"Will this really be alright?"
"I don't want Ayu being rude to Stephania. That really {i}might{/i} splinter the peace between Japan and Astoria: more so than walking Cosmos outside on a leash would!"
$ sface='smile'
$ sbody='cas1'
show steffy at c4
Stephania "You have mentioned this Ayu before, but I am not familiar with her. Is she a friend of yours?"
Hiroki "Ayu might contest that..."
"I have my reservations on the matter of Cosmos's and Ayu's \"friendship\" (it's complicated), but Cosmos sounds pretty enthused, if her reply is anything to go by."
$ cface='laugh'
show cosmos at c4
Cosmos "Yes, that's right! Ayu is my very good friend."
$ cface='smile'
show cosmos at c3
Cosmos "She's my {i}best{/i} friend, in fact, and she's really quite sweet, though she can be a little awkward at times, ehehe."
"\"A little awkward\"? Isn't that something of an understatement?"
"I'm {i}sure{/i} Ayu's told me to drink bleach on more than one occasion!"
$ cbody='wcas3'
show cosmos at c2
Cosmos "I'm sure the two of you will get along well. Ayu can be a bit prickly, but you just need to be nice to her."
Cosmos "She'll warm up to you soon enough, hehe."
$ sbody='cas2'
show steffy at c2
Stephania "Like a cat, you mean?"
$ cface='sweatdrop'
show cosmos at c1
Cosmos "Yes, a little like that. Ayu always says that my cat ears look stupid, though..."
$ sface='happy'
show steffy at c1
Stephania "Well, then! She sounds like an interesting woman indeed. I would love to meet her."
$ sface='shy'
show steffy at c3
Stephania "I only hope that she likes me..."
$ lface='smile'
$ lbody='maid2'
show lizzie flip at c4
Elizabeth "I am certain that she will, milady. You are very charming, after all."
$ lface='serious'
show lizzie flip at c2
Elizabeth "If she does take against you, however, then..."
"An ominous expression crosses Elizabeth's face, and smiling grimly, she cracks her knuckles."
$ lface='very angry'
show lizzie flip at c1
Elizabeth "I will have to have a little word with her."
"Eeep. I'm starting to feel afraid on Ayu's behalf."
"Elizabeth isn't going to snap her spine, is she...?"
$ sface='worried'
show steffy at c2
Stephania "Lizzie, please. While I know you care for me, I do wish that you wouldn't threaten others indiscriminately."
Stephania "Snapping spines is no way to make new friends!"
"...Wait, what? I was only kidding around, but Stephania sounded pretty serious there."
"Elizabeth hasn't {i}really{/i} snapped any spines for Stephania's sake, has she?"
"I'm almost afraid to ask..."
$ lface='angry'
show lizzie flip at c4
Elizabeth "...Alright, fine. I will try to behave myself. If this \"Ayu\" girl gives you any trouble, however, I will not hesitate to make her pay."
"Geez. That sure sounded like a threat."
"I might have to send Ayu a text later, reminding her to keep her more critical remarks to herself."

stop music fadeout 1.0

"I'm busy pondering this, when..."

play music "bgm/sak_suc_alice_loop.ogg" fadein 1.0
scene park:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 30.0 crop (400, 120, 1280, 720)
with wiperight_slow

Hiroki "Hmm?"
"Maybe it was just my imagination, but I'm sure I heard something just now: something other than the breeze through the trees, that is."
"It's hard to say, but it sounded a little like footsteps."
"Is somebody watching us?"
"With narrowed eyes, I sweep my gaze across the park, but..."
Hiroki "..."
"I can't see anything."
"Maybe I'm imagining things."
"It's pretty late, and it's starting to get dark. I must be getting tired, hearing things like that - or {i}thinking{/i} I was hearing things, at least."
"Now, I'm not at all convinced there was anything {i}to{/i} hear."
"I'm being silly. That's all it is."
"There's nothing to worry about... {w}right?"

scene park
$ cface='smile'
$ cbody='wcas3'
$ lface='serious'
$ lbody='maid1'
$ sface='sad'
$ sbody='cas1'
call s_elicostef from _call_s_elicostef_5
with wipeleft_slow

Stephania "Hiroki...?"
"Stephania, who was busy sipping on her bubble tea, sets the plastic container down upon the bench, then looks at me curiously."
$ sbody='cas2'
show steffy at c1
Stephania "Are you alright?"
Hiroki "Oh, I'm fine. Don't worry, Steffy. I was just spacing out."
$ cface='neutral'
show cosmos at c4
Cosmos "Spacing out, hmm?"
"Cosmos echoes my words, her expression thoughtful."
$ cface='sweatdrop'
$ cbody='wcas6'
show cosmos at c2
Cosmos "Ayu says I do that a lot, too. Apparently, I'm so spacey, I might as well live on Mars, hehe."
$ lface='angry'
show lizzie flip at c1
Elizabeth "Ayu might have a point there. You do, indeed, often seem to be in your own world."
Elizabeth "It is unusual for you, however, to drift off like that, Mr. Ogasawara. Are you sure nothing is the matter?"
$ lface='sad'
show lizzie flip at c4
Elizabeth "Your face looks awfully pale. Why, it is almost as though you have seen a ghost!"
$ cface='smile2'
show cosmos at c3
Cosmos "You'd better not mention ghosts around Marina, ehehe. She can't stand them."
"The mention of this sinister word - \"ghost\" - sends another shiver down my spine."
"What if we really {i}were{/i} being observed by a ghost?"
"It'd certainly explain the disquietening sense of {i}wrongness{/i} I felt earlier, and my attempts to find the culprit came up empty-handed."
"Did our mysterious observer simply disappear?"
$ lface='serious'
show lizzie flip at c3
Elizabeth "Mr. Ogasawara...?"
"But, no, I'm being ridiculous. Succubi might exist, but ghosts definitely do not."
"There was nothing there. I can tell there's nothing there."
"I let myself get worked up over nothing, and now I'm making Stephania and Elizabeth worry."
$ sbody='cas1'
show steffy at c4
Stephania "Hiroki...?"
Hiroki "...I'm fine. Don't worry about me. I'm just tired is all."
"At least, I {i}hope{/i} that's what the issue is."
"If we really {i}were{/i} being observed, then...{w} Well."
"I don't know if I want to think about that, so I won't."
"I'll put it from my mind."
"I don't want to spoil a wonderful day with my silly, misplaced anxiety."
"I'm sure everything will be alright."
"That's what I try to tell myself, but..."
Hiroki "..."
"Why do I feel so uneasy?"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
play music "bgm/succubus_slife_of_life_1_loop.ogg" fadein 1.0
scene skyn with wiperight_slow
window show dissolve

"With their bubble tea consumed and my own anxieties assuaged (for the moment, at least), I return to my apartment along with Stephania, Elizabeth, and Cosmos."
"Stephania is tired after the day's events, and she excuses herself with a sleepy, \"I think I will get an early night. Thank you very much for showing me around, though, Cosmos! I had a lot of fun!\""
"Elizabeth, meanwhile, makes a beeline for my kitchen-cum-living room, where she seems to spend a lot of her time."
"Once there, Elizabeth begins to take a quick inventory of the contents of my cupboards, and the contents of my fridge."
"She scans all of the foodstuffs available and, finding my selection lacking, she frowns."

scene kitchen_n
$ lface='serious'
$ lbody='maid1'
call s_lizzie from _call_s_lizzie_12
$camera_move(0,400,300,0,0,'dissolve')
with wipedown_slow

Elizabeth "Well, well."
$ lface='angry'
show lizzie at c4
Elizabeth "This will {i}never{/i} do."
Hiroki "What won't?"
$ lbody='maid2'
show lizzie at c2
Elizabeth "The ingredients available to me."
$ lface='serious'
show lizzie at c1
Elizabeth "As I made a European-style breakfast this morning, I was thinking I should attempt a more traditional Japanese-style breakfast come tomorrow morning."
Elizabeth "Given I am in Japan now, it would seem only fitting. I would very like to expand my repertoire when it comes to cooking, and I also believe Japanese food would be more to your tastes."
$ lface='angry'
show lizzie at c3
Elizabeth "I have something of a quandary, however. You are running low on miso paste, and soy sauce, and you have no fresh fish."
Hiroki "You want fish?"
"Elizabeth nods."
$ lface='serious'
show lizzie at c2
Elizabeth "I was thinking of tomorrow's menu while walking back here, and I am rather struck upon the idea of braising some salmon."
Elizabeth "I can hardly do that, however, without any salmon to braise."
$ lbody='maid1'
show lizzie at c4
Elizabeth "Perhaps I ought to go to shopping."
show lizzie at c3
Elizabeth "There is a convenience store in the immediate vicinity, is there not?"
Hiroki "Yeah, there is. The closest store's less than a ten minute walk away, but are you sure you want to step out at this hour?"
"It's black as pitch outside, and the sky is strewn with stars."
"I don't much like going out when it's this late, and I'm a guy who knows this area pretty well."
"Elizabeth, meanwhile, is a woman, and while she isn't delicate, her unusual attire and her very pale hair immediately mark her out as being a foreigner."
"The area I live in isn't particularly unsafe (at least, when succubi aren't breaking into my apartment), but I'd still worry about letting Elizabeth go out on her own."
Hiroki "Maybe it'd be better if you went out tomorrow morning, after the sun's risen?"
$ lface='angry'
show lizzie at c1
Elizabeth "No, I can't do that. Tomorrow would be to late. I need these ingredients now, so I can let the salmon marinate overnight. Otherwise, it won't taste as good."
$ lface='serious'
show lizzie at c4
Elizabeth "I must go now, for the sake of making a truly delicious breakfast."
Elizabeth "As a maid, I would not forgive myself if I did not put all of my effort into this venture."
Hiroki "Well, alright. You can go if you insist."
"It's not like I can stop Elizabeth. She is, like Stephania said, very stubborn."
"Maybe I ought to offer to accompany her, though...?"

window hide dissolve

menu:
    with dissolve

    "Ask Elizabeth if she wants you to go with her.":

        window show dissolve

        $ succ_points += 3

        Hiroki "Do you want me to come with?"
        $ lbody='maid2'
        show lizzie at c3
        Elizabeth "That is very kind, but you needn't worry. I do not need to be chaperoned. I am more than capable of buying these ingredients myself."
        Hiroki "But what if you get lost, or mugged?! I'd never be able to forgive myself!"
        $ lface='smile'
        show lizzie at c1
        Elizabeth "Heh."
        $ lbody='maid1'
        show lizzie at c4
        Elizabeth "Are you truly that concerned for my welfare, Mr. Ogasawara?"

        $camera_move(400,300,200,0,3,'ease')
        $ cface='smile'
        $ cbody='wcas1'
        call s_lismos from _call_s_lismos_1

        Cosmos "Hiroki worries about everybody. He's a really nice guy, hehe."
        Cosmos "That's why he's my boyfriend. I'm proud that I'm dating such a stud!"
        show lizzie flip at c4
        Elizabeth "I would have to agree with you on that score. Mr. Ogasawara is, indeed, a very nice man, but you are worrying unnecessarily."
        $ lface='serious'
        show lizzie flip at c2
        Elizabeth "Do you {i}really{/i} think, knowing me as you do, that I am the type of woman to get lost?"
        Hiroki "Well, no, but-"
        $ lface='smile'
        show lizzie flip at c4
        Elizabeth "And-"
        "Elizabeth continues, her voice archly amused."
        $ lbody='maid1'
        show lizzie flip at c3
        Elizabeth "-do you really think I am the sort of woman who would stand by and let myself get mugged?"
        Hiroki "I don't suppose you do, no, but it isn't a matter of \"letting yourself\" get mugged. If a group of men came at you with knives, then..."
        $ cface='shock'
        show cosmos at c4
        Cosmos "Wow. That sounds scary. Could that really happen?"
        Hiroki "There's always a chance. That's why it's best to be careful."
        $ lface='angry'
        show lizzie flip at c2
        Elizabeth "It's an unlikely chance. I would sooner get hit by a car crossing the road than I would fall foul of a group of knife-wielding hoodlums - and, even if that {i}should{/i} come to pass, which it won't, I will be quite alright."
        $ lface='very angry'
        show lizzie flip at c1
        Elizabeth "I would not let anybody get the better of me: not an army of five, or five hundred."
        Elizabeth "No puny human can stand against me: not when I have breakfast to prepare."
        $ cface='laugh'
        show cosmos at c2
        Cosmos "Ooh. How impressive. I'm in awe!"
        $ lface='smile'
        show lizzie flip at c4
        Elizabeth "Thank you. You are too kind."
        "I must admit, I feel pretty impressed by that speech of Elizabeth's, too. I am a little disturbed to, however, at the sake token."
        "Did she just say \"puny human\"?"
        "Doesn't that imply that Elizabeth herself is not, in fact, human, but something rather more powerful?"
        "Just what {i}is{/i} Elizabeth, anyway?"
        "This isn't the first time I've found myself questioning the exact nature of Elizabeth's existence - but, before I'm able to question her, she sweeps past me."
        $ lface='serious'
        show lizzie flip at c2
        Elizabeth "Now, if all your objections have been nullified, I think I will head out."

    "Don't say anything.":

        window show dissolve

        "...I guess there's no point offering, really."
        "I'm sure Elizabeth will be fine on her own."
        "She doesn't need my help."
        $ lbody='maid1'
        show lizzie at c4
        Elizabeth "Now, I shall head out. Goodbye, you two."

        $camera_move(400,300,200,0,3,'ease')
        $ cface='smile'
        $ cbody='wcas1'
        call s_lismos from _call_s_lismos_1000

        Cosmos "Goodbye, Lizzie! Stay safe!"
        $ lface='smile'
        show lizzie flip at c4
        Elizabeth "I shall."

Elizabeth "Behave yourselves, you two, and do not do anything I would not..."
$ lface='smile'
show lizzie flip at c1
Elizabeth "Which gives you quite a bit of leeway, I suppose."
$ cface='grin'
$ cbody='wcas5'
show cosmos at c3
Cosmos "Hehe. Are you trying to say you're quite wild deep down, Miss Elizabeth?"
show lizzie flip at c3
Elizabeth "Well. Perhaps. Who knows? A woman must have some secrets..."
$ lbody='maid2'
show lizzie flip at c2
Elizabeth "And, I flatter myself, I am full of them. Ufufu~"

stop music fadeout 1.0
$camera_move(0,400,300,0,3,'ease')
hide lizzie with dissolve
call s_cosmos from _call_s_cosmos_3

"So saying (or laughing, rather), Elizabeth slides her shoes on, then takes her leave."
"I eye the door in Elizabeth's absence, then look at Cosmos."
"Cosmos looks back at me, her arms behind her back, a devious smile playing about her face."

play music "bgm/succubus_romance_loop.ogg" fadein 1.0

$ cface='smile'
show cosmos at c4
Cosmos "So, Hiroki..."
Hiroki "Yes?"
$ cface='smile2'
show cosmos at c2
Cosmos "It looks like I have you all to myself now, at long last. It feels like it's been too long."
Hiroki "Were you hoping to get me on my own?"
$ cface='smile'
show cosmos at c1
Cosmos "Maybe..."
"Cosmos takes a step towards me, then curls her fingers against the front of my shirt."
$ cface='neutral'
show cosmos at c4
Cosmos "I like Steffy and Lizzie a lot, but it {i}has{/i} been a while since we could spend any quality time together."
Cosmos "I missed it."
$ cface='sad'
show cosmos at c3
Cosmos "I missed you."
Hiroki "You did?"
show cosmos at c1
Cosmos "A lot, yes, when you were in Astoria."
show cosmos at c3
Cosmos "I wanted to text you every day, to see how you were, but I didn't. I was afraid I might look clingy."
Cosmos "I didn't want to be a bother."
Hiroki "You {i}aren't{/i} a bother, Cosmos."
Hiroki "You could've texted me if you'd wanted to talk. I would've liked to have heard from you."
$ cface='shock'
$ cbody='wcas5'
show cosmos at c2
Cosmos "Really...?"
"Cosmos sighs, as I stroke her scalp."
$ cface='sad'
show cosmos at c1
Cosmos "Ayu said it would be a bother, and she's usually right about these things. I worry I'm not very good at talking to people: not even you."
Cosmos "I get awkward, and I second-guess myself."
$ cbody='wcas1'
show cosmos at c4
Cosmos "You mean a lot to me, Hiroki, and I don't want you to dislike me."
show cosmos at c2
Cosmos "I would be very sad if you turned against me."
Hiroki "You don't have to worry about that, silly. I'd never stop liking you: not even if you sent me dozens of texts a day."
$ cface='sweatdrop'
show cosmos at c1
Cosmos "Or hundreds?"
Hiroki "Well, {i}that{/i} might be going a bit too far..."
$ cface='smile'
show cosmos at c4
Cosmos "Ehehe... I knew it. I don't want to seem like a creepy stalker."
Hiroki "If you want to talk to me, though, you can. I'm your boyfriend, remember. You shouldn't ever feel like a burden."
Hiroki "I might be busy, but I'll always try to find time for you, no matter how awkward you say you are."
Hiroki "I get along with you just fine."
$ cface='smile2'
show cosmos at c3
Cosmos "Hehe. I'm glad to hear it. You're so nice to me...."
$ cface='neutral'
show cosmos at c2
Cosmos "But, then again, you're nice to everybody."
Cosmos "That's why Ayu likes you so much, though she says she doesn't, and it's why Steffy flew all the way from Astoria to spend time with you."
Hiroki "I thought Ayu liked me because I smelt good?"
$ cface='smile2'
show cosmos at c1
Cosmos "You do smell good to us succubi, but I don't think Steffy is a succubus."
Cosmos "She's a human woman, but she fell in love with you regardless."
show cosmos at c4
Cosmos "She fell for you... {w}because you're special."
show cosmos at c3
Cosmos "And I think you're special, too."
$ cface='smile'
show cosmos at c2
Cosmos "I worked hard as your tour guide today, so I think I deserve some sort of reward."
Hiroki "And what sort of reward would this be, hmm?"
$ cface='neutral'
show cosmos at c1
Cosmos "You know what I mean. I want you to kiss me, and to hold me..."
$ cface='sweatdrop'
show cosmos at c3
Cosmos "And I want to feel your body against mine."
$ cface='sad'
show cosmos at c2
Cosmos "Would that... {w}be alright?"
Hiroki "Aaaah. I see."
Hiroki "If that's what you want, then..."
"I smile."
Hiroki "Sure thing. I'll kiss you, I'll hold you, and we can do lots more fun things together, too."
Hiroki "You're so cute, I can't help but want to pamper you."
"I lean in, cupping Cosmos's cheek with one hand. My lips part, and then..."
$ cface='smile2'
show cosmos at c1
Cosmos "Mm, chh..."
Hiroki "Mm..."
"I capture Cosmos's mouth in my own in a soft, tender kiss."

if persistent.adult==True:
    jump adult2
else:
    jump merge2

label merge2:

    stop music fadeout 1.0
    window hide dissolve
    scene black with fstartgame
    $ renpy.pause(0.3)
    scene skyn with fstartgame
    window show dissolve

    "Later that night..."

play music "bgm/succubus_palace_loop.ogg" fadein 1.0
scene kitchen_n
$ lface='serious'
$ lbody='maid1'
call s_lizzie from _call_s_lizzie_4
$camera_move(0,400,300,0,0,'dissolve')
with wipedown_slow

Elizabeth "I am happy to report that I have accomplished my errands with no issue, Mr. Ogasawara. We should have miso paste enough, now, for breakfast, and the salmon I wanted, although..."
$ lbody='maid2'
show lizzie at c4
Elizabeth "Did something happen during my absence?"
Hiroki "Wh-What? Oh, uh..."
"I try to sound unconcerned, but this proves to be a difficulty: particularly given it wasn't all that long ago that Cosmos and I were entwined on the kitchen floor."
"Cosmos has since gone home, and not a moment too soon (she left about ten minutes before Elizabeth's return), but I'm anxious some trace of our former dalliances might remain."
"I cleaned up the floor when I was finished, but I'm anxious some of the smell might remain."
"Elizabeth doesn't know what it was we were getting up to, does she?"
"Can she tell?"
Hiroki "N-Nothing happened."
$ lface='angry'
show lizzie at c3
Elizabeth "Are you certain?"
"Elizabeth looks me up and down, her lips pursed together in disbelief."
$ lface='serious'
show lizzie at c2
Elizabeth "Do you not have anything you wish to tell me?"
Hiroki "N-No, of course not. Wh-What would I have to tell you?"
$ lface='angry'
show lizzie at c1
Elizabeth "Oh, {i}I{/i} don't know. I can't pretend to know how you spend your time, Mr. Ogasawara, when I am not around."
Elizabeth "It would not bother me, either, if you and Cosmos had a bit of fun, but..."
$ lface='serious'
$ lbody='maid1'
show lizzie at c3
"Elizabeth takes a single step towards me, her voice dropping to a whisper, then says..."
Elizabeth "If you have any \"urges\" that you need taking care of, it might be for the best if you told milady about them."
show lizzie at c4
Elizabeth "She is very fond of you, and I am sure she would have no qualms in satiating your desires."
$ lface='angry'
show lizzie at c3
Elizabeth "It would make her happy, in fact, if she knew she could help you. She might be a princess, but she still wishes to serve you."
$ lface='serious'
show lizzie at c1
Elizabeth "Am I making myself plain?"
Hiroki "Y-Yes, um..."
Hiroki "I understand. I'll be sure to, uh, let Steffy know, if I ever get... {w}worked up?"
$ lface='angry'
show lizzie at c2
Elizabeth "Good."
$ lface='serious'
show lizzie at c4
Elizabeth "I understand you have other women who make demands upon your time, but if you could keep milady in your mind, I would appreciate it."
$ lbody='maid2'
show lizzie at c3
Elizabeth "Milady's joy, after all, is my own. She is very dear to me, and nothing will ever change that."
$ lface='smile'
show lizzie at c2
Elizabeth "I really do love her."

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyn with fstartgame
window show dissolve

"I have a bath later that night, to wash off Cosmos's scent from my body, then retreat to my bedroom."

play music "bgm/succubus_romance_loop.ogg" fadein 1.0
scene mc_room_n with wipedown_slow

"Stephania is already there, curled up on the futon I spread out for her."
"She's long since fallen asleep, and her golden eyelashes are matted together."
"Her chest, which is clad in my cast-off button-down shirt, rises and falls in sleep, and her lips are pursed."
"Stephania looks so sweetly innocent my heart floods with fondness when I see her."
"Elizabeth, meanwhile, is still in the kitchen, cleaning up. I'm sure she'll retreat to my bedroom herself once she's ready for bed."
"For the present, however, it's just the sleeping Stephania and I."
"I strip off, changing into my nightclothes, then slide beneath my own futon."
"Stephania is so deeply asleep she shouldn't be aware of my presence, but I think I can see her lips twitch into a smile."
"Maybe she can tell I'm here after all?"
Hiroki "Hey, Sleeping Beauty."
"I reach out, then brush a few strands of Stephania's hair behind her ear."
"I do this gently, not wanting to disturb her, my fingertips grazing her cheek."
Hiroki "Did you have a good day?"
Stephania "Mm, nn... Zz..."
"Stephania doesn't answer - she can't, given she's snoozing - but I'd like to take that as a \"yes\"."
"Certainly, she looks quite content, dreaming as she is."
"I wonder what she's dreaming about?"
"Could she be thinking about all of the fun she had today?"
"If I did feature in Stephania's dreams, I'd consider myself a fortunate guy indeed."
"Stephania is so cute, I can hardly believe she's interested in me: so much so, she took a spontaneous trip to Japan despite her many duties in Astoria."
"She must have it pretty bad for me."
"Maybe Elizabeth's right. The next time I feel touch-starved, I should probably go to Stephania."
"She won't be staying in Japan for very long, so I ought to make the most of every moment we can spend together."
"She deserves it."
"After all..."
Hiroki "It's impossible not to like you. You really {i}are{/i} sweet."
Hiroki "That's why I want to show you a good time. I'll take care of you, so don't worry."
Hiroki "I'll make your trip to Japan an experience you'll never forget."

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
play music "bgm/succubus_slife_of_life_1_loop.ogg" fadein 1.0
scene skyd with clockwipe
window show dissolve

"The following morning soon arrives, and I awake, once more, in my futon, alongside a half-clothed Stephania."
"After greeting me sleepily, with a small smile, Stephania rises, then retreats to the bathroom."
"She showers, brushes her teeth, and changes in double-quick time: conscious, I think, that I'm waiting for her."
"I freshen up myself once Stephania has finished, then make my way to the kitchen."
"This morning, just like the last, finds Elizabeth by the stove, cooking our breakfast."
"Elizabeth prepared pancakes yesterday, but today, she seems determined to use the miso paste she bought last night, during her trip to the store."
"Today's breakfast, once Elizabeth is finished with it, is fashioned in the traditional Japanese style: miso soup, white rice, pickled plums, and the braised salmon she spoke about so passionately the night prior."
"The meal is hearty, and it tastes authentic enough, despite Elizabeth being staunchly European."

scene kitchen
$ lface='serious'
$ lbody='maid1'
$ sface='smile'
$ sbody='cas1'
call s_stefeli from _call_s_stefeli_12
$camera_move(400,300,200,0,0,'dissolve')
with wipedown_slow

Elizabeth "What do you think of today's repast, milady? Mr. Ogasawara? Is it to your liking?"
$ sface='happy'
show steffy at c2
Stephania "Indeed, it is! I think your food is perfectly delicious, Lizzie. Nobody is better at cooking than you!"
$ lface='smile'
show lizzie flip at c4
Elizabeth "That, I am afraid, a touch hyperbolic. While I know I am skilled enough in the kitchen, I am by no means the best cook around: particularly not when it comes to Japanese dishes."
$ lface='angry'
show lizzie flip at c2
Elizabeth "I fear I still need more practice. I am not accustomed to using these kinds of ingredients, nor these flavor profiles."
Elizabeth "Miso, in particular, is rather unique."
$ lface='serious'
show lizzie flip at c4
Elizabeth "What do you think about it, Mr. Ogasawara? You are more familiar with Japanese flavor profiles than either milady or myself, so you would be a better judge on the matter."
$ lbody='maid2'
show lizzie flip at c3
Elizabeth "Is the food I cooked acceptable?"

window hide dissolve

menu:
    with dissolve

    "I think it tastes great!":

        window show dissolve

        $ succ_points += 1

        Hiroki "It's more than \"acceptable\". It tastes great! I don't think it'd be out of place in a restaurant. although..."
        $ lbody='maid1'
        show lizzie flip at c2
        Elizabeth "Although what?"

    "It's not bad, but...":

        window show dissolve

        Hiroki "There's nothing wrong with your food, but..."
        $ lbody='maid1'
        show lizzie flip at c2
        Elizabeth "But what?"

$ lface='angry'
show lizzie flip at c1
Elizabeth "If you have any complaints, no matter how small, please let me know. I fear I will not be able to improve otherwise."
Elizabeth "Do no worry about sparing my feelings. I wish only to know your honest opinion."
Hiroki "Well..."
Hiroki "Though the food does taste good, I think the flavor of the miso soup is a bit understated. I think you could have been more generous with the miso paste."
Hiroki "It isn't quite as good as my mother's miso soup - or Hifumi's..."
"I smile."
Hiroki "But maybe you could ask Hifumi for pointers, if you ever get the chance? She's {i}really{/i} good at cooking, especially when it comes to Japanese food."
Hiroki "I'm sure she'd be able to give you more actionable advice than I can."
$ sface='shock'
$ sbody='cas2'
show steffy at c4
Stephania "My, my! Is my mistress truly that talented at cooking?"
Hiroki "I think she is. She prepares fairly simple dishes, but she imbues them with so much flavor. They're to die for!"
$ sface='happy'
show steffy at c3
Stephania "Ooh. Now I wish I could try my mistress's miso soup myself!"
$ sface='smile'
show steffy at c2
Stephania "I knew my mistress was a talented karuta player, and a proficient actress, but I'd no idea she was talented in the kitchen, too!"
Stephania "I suppose this should not come as too much of a surprise, though. My mistress really is an amazing woman! She can do anything!"
$ sface='happy'
$ sbody='cas1'
show steffy at c1
Stephania "Hifumi is so amazing! I can only hope to be as talented as she is!"
$ lface='serious'
show lizzie flip at c4
Elizabeth "I see."
$ lbody='maid1'
show lizzie flip at c3
Elizabeth "Thank you for the feedback, Mr. Ogasawara. It is most appreciated."
Elizabeth "If I am to prepare further Japanese dishes for you and milady in the future, I shall try not to be so stingy with my flavor profiles."
$ lface='angry'
show lizzie flip at c2
Elizabeth "I wish to prepare food that is worthy of your discerning palates: worthy, even, of being prepared by Yamamoto Hifumi herself."
$ lface='serious'
show lizzie flip at c1
Elizabeth "I can tell I have a long way to go, but I shall not be disheartened. I vow, henceforth, that I shall do my very best."
$ sface='smile2'
$ sbody='cas1'
show steffy at c4
Stephania "You always do, Lizzie! You're such a hard worker!"
$ lface='angry'
show lizzie flip at c4
Elizabeth "You say that as though it is commendable, but I assure you, it is not. As your top maid, I ought to work hard. I would not forgive myself if I did not."
Hiroki "So you say, but this food is plenty edible. It's better than my sorry attempts at cooking. I always half-ass things."
$ sface='shy'
show steffy at c3
Stephania "I am not very good in the kitchen myself, I must confess, hehe. I always seem to make pots and pans explode."
$ sbody='cas2'
show steffy at c1
Stephania "My parents banned me from using the palace's kitchens after my attempt at making cookies set the oven on fire..."
Hiroki "What? Did that really happen?"
$ sface='worried'
show steffy at c4
Stephania "Oh, yes. I almost singed my eyebrows off when I tried to take my cookies out of the oven."
$ sface='sad'
show steffy at c2
Stephania "The cookies were, of course, unsalvageable. They were burnt to a crisp..."
$ sbody='cas1'
show steffy at c1
Stephania "Oh, it was such a pity. I wanted to bake Lizzie something for her birthday, you see, but it resulted in an utter failure."
$ sface='worried'
show steffy at c4
Stephania "Lizzie tried one of my cookies, blackened though it was, and she {i}said{/i} it was good, but I know she was only trying to spare my feelings."
Stephania "Lizzie is very considerate like that."
$ lface='serious'
show lizzie flip at c3
Elizabeth "I was not being considerate, milady. I tried one of your cookies because I wished to, knowing that it was something you created with your own two hands."
Elizabeth "Though its flavor was not the best-"
$ sface='sad'
show steffy at c2
Stephania "That is a nice way of saying that it was unspeakably awful."
$ lface='smile'
show lizzie flip at c1
Elizabeth "-I still enjoyed it, and I appreciated it, because you made those cookies with me in mind."
Elizabeth "It was a very precious, valuable gift: one I shall not forget in a hurry."
show lizzie flip at c2
Elizabeth "I was immensely flattered."
$ sface='worried'
show steffy at c1
Stephania "I'm glad to hear it, though you {i}did{/i} fall ill after forcing that cookie down. You were bed-bound for two whole days."
"Wow. Were Stephania's cookies really {i}that{/i} awful?"
"Color me intrigued. Just how bad could they have tasted?"
"I almost want to try one myself, but maybe that'd be akin to signing my own death warrant..."
$ sface='smile'
show steffy at c1
"The three of us continue to eat, all while engaged in idle chatter."
$ lface='serious'
show lizzie flip at c4
"The minutes slip by, and eventually we clear our plates."
"Elizabeth collects our dishes, then begins to wash them."
"Stephania offers to help, but Elizabeth rejects her offer, like she always does."
"I guess Elizabeth doesn't need any help when it comes to household chores anyway, because she finishes the clean-up in double-quick time, then begins to sweep the kitchen."

stop music fadeout 1.0

"A few minutes pass by, as denoted by the clock upon my wall, when..."

$camera_move(0,0,0,0,4,'ease')
play music "bgm/succubus_weird_loop.ogg" fadein 1.0
$ cface='smile'
$ cbody='wcas1'
call s_elicostef from _call_s_elicostef_121

Cosmos "Good morning, everynyan! How are you? I'm doing fine, thank you!"
$ cface='laugh'
show cosmos at c4
Cosmos "I hope you didn't miss me too much, hehe. It's very good to see you again!"
$ sface='smile2'
$ sbody='cas2'
show steffy at c2
Stephania "Cosmos! I'm very glad to see you too! The pleasure is all mine."
$ lface='smile'
show lizzie flip at c4
Elizabeth "Likewise."
$ lface='serious'
show lizzie flip at c3
Elizabeth "You proved to be a most competent tour guide during yesterday's excursion. I am looking forward to experiencing today's itinerary - as, I believe, is milady."
$ sface='happy'
show steffy at c1
Stephania "Oh, yes! Of course! I can hardly wait, hehe!"
$ cface='smile2'
show cosmos at c3
Cosmos "I'm glad to hear it."
"Cosmos shoots both Elizabeth and Stephania a thumbs up."
$ cface='laugh'
show cosmos at c1
Cosmos "I'll do my best. I don't want to let either of you down!"
$ cface='sweatdrop'
$ cbody='wcas5'
show cosmos at c4
Cosmos "Why, if I disappoint you, you might behead me!"
$ sface='worried'
show steffy at c4
Stephania "Wh-Why would I do something like that?"
$ cface='neutral'
show cosmos at c2
Cosmos "Well, {i}I{/i} don't know. You are a princess. If anybody could issue an order to behead me, you could."
$ cface='sweatdrop'
$ cbody='wcas1'
show cosmos at c1
Cosmos "I know what royalty are like. One minute, it's all, \"let them eat cake\", and the next it's, \"off with their heads.\""
$ sface='angry'
show steffy at c3
Stephania "I-I think you might have the wrong idea about me, a-and about Astoria in general."
$ sface='sad'
show steffy at c2
Stephania "I-I'm not a tyrant. I would never order anybody's execution - and, even if I wanted to, I couldn't."
$ sbody='cas1'
show steffy at c1
Stephania "Capital punishment is illegal in Astoria. We haven't executed anybody in over a century!"
$ Cface='smile'
show cosmos at c4
Cosmos "Really? I didn't know that, ehehe."
$ cface='grin'
$ cbody='wcas5'
show cosmos at c3
Cosmos "I guess I don't need to worry quite so much about incurring your wrath, then! That means I can relax!"
Hiroki "When are you anything other than relaxed?"
"I smile at Cosmos, then glance around my kitchen curiously."
Hiroki "Where's Ayu? I thought she was supposed to be coming with you?"
$ cface='smile'
$ cbody='wcas1'
show cosmos at c2
Cosmos "Oh, Ayu is here. She was just too shy to introduce herself. I think she was afraid that Steffy here might be some kind of haughty, aloof princess."
$ cface='grin'
show cosmos at c1
Cosmos "Well!"
$ cface='smile2'
show cosmos at c4
Cosmos "Now we know Steffy has never, and {i}would{/i} never, execute anybody, there's nothing to worry about."
Cosmos "You can come out, Ayu. Say hello. Don't be shy, now."

stop music fadeout 1.0

$ cface='laugh'
$ cbody='wcas5'
show cosmos at c3
Cosmos "Here, Ayu, there's a good girl!"

play music "bgm/succubus_stephania_loop.ogg" fadein 1.0
$camera_move(400,300,200,0,4,'ease')
hide lizzie
hide cosmos
with dissolve

$ aface='shy'
$ abody='wcas1'
call s_stefyu from _call_s_stefyu_1

Ayu "Alright, alright..."
"I hear a familiar voice, drifting from the doorway, then see a familiar face."
"A very pink, pastel Ayu steps into the kitchen, her hands on her hips."
"I think Ayu's trying to appear cool and unaffected, but I can see two pink spots on her cheeks."
"Is she embarrassed?"
$ aface='angry'
show ayu at c4
Ayu "You don't need to call after me, Cosmos, like I'm some kind of dog. {i}You're{/i} the one who thinks you're an animal, not me."
Ayu "I would {i}never{/i} demean myself by wearing a silly pair of animal ears."
"Ayu harrumphs, her expression haughty, before she turns her attention to Stephania and Elizabeth."
$ aface='urgh'
show ayu at c2
Ayu "I don't know what Cosmos has told you about me, if anything, but please don't judge me based on her spotty testimony. I was {i}not{/i} anxious about meeting you: not at all."
$ aface='cute'
$ abody='wcas2'
show ayu at c1
Ayu "I am {i}not{/i} an anxious person in general, really. What do I have to be anxious about when I'm so very wonderful?"
$ aface='smug'
show ayu at c4
Ayu "Ohohoho!"
"Oof. Talk about forced laughter. It's obvious Ayu's trying to put up a front, but this front of hers is awfully flimsy."
"She was {i}totally{/i} panicking before she came here."
"In fact, I think she's still panicking. Otherwise, her laughter wouldn't sound that high-pitched."
$ aface='smile'
show ayu at c3
Ayu "Now, please let me introduce myself, on the off-chance - unlikely though it is - that you do not know who I am."
$ aface='smug'
show ayu at c2
Ayu "Ahem."
$ aface='wink'
$ abody='wcas1'
show ayu at c1
Ayu "My name is Ikue Ayu, and I am a famous idol, beloved by all. My songs are all at the top of the charts, and there is nary a man or woman in Tokyo - no, in all of Japan - who does not know my name!"
$ aface='smile'
show ayu at c4
Ayu "I'm incredibly busy, of course, owing to my immense, overwhelming popularity, but I was able to take some time from my schedule to pay the pair of you a visit."
$ aface='grin'
show ayu at c2
Ayu "Consider yourselves grateful, peons, that I would be generous enough to bestow my exalted presence upon you!"
Ayu "Bow at my feet, and offer me tribute, and-"
$ sface='shock'
$ sbody='cas2'
show steffy at c4
Stephania "Oh my gosh...!"
"Stephania cuts Ayu off, her eyes wide with shock."
$ sbody='cas1'
show steffy at c3
Stephania "Are you really Ikue Ayu? {i}The{/i} Ikue Ayu?"
$ aface='shy'
show ayu at c1
Ayu "Wh-What? Um, y-yes, I am. Er..."
$ aface='drop'
show ayu at c3
Ayu "Is there a problem with that?"
$ sface='smile'
show steffy at c2
Stephania "Oh, no, there's no problem! It is quite the contrary, in fact! You see..."
$ sface='happy'
show steffy at c1
Stephania "I am a big, big fan of your music!"
$ aface='surprised'
show ayu at c4
Ayu "E-Eh?! Y-You are?!"
$ sface='smile'
show steffy at c3
Stephania "Yes, indeed! I love all of your CDs: particularly your debut! I have listened to it so many times, I know all the words from every song off by heart!"
$ aface='shy'
show ayu at c3
Ayu "W-Wow, um... N-No way..."
$ abody='wcas2'
show ayu at c2
Ayu "I-I didn't think anybody from Astoria would have heard of my music. I'd no idea I was that well-known..."
$ sface='sad'
show steffy at c2
Stephania "Most people in Astoria are ignorant of you, alas..."
$ sface='angry'
show steffy at c1
Stephania "But, then again, most of Astoria's citizens are ignorant of karuta, too!"
$ sbody='cas2'
show steffy at c4
Stephania "They do not understand how wonderful Japan is!"
$ sface='smile'
show steffy at c3
Stephania "I am not like the masses, however. I am a big fan of your country, and of its culture - and, of course, I am a big fan of you, too!"
$ sface='smile2'
show steffy at c2
Stephania "It was my interest in your music, in fact, which first helped me learn how to speak Japanese!"
$ sface='smile'
$ sbody='cas1'
show steffy at c1
Stephania "I owe you a good deal, Ayu - or can I call you Ayu-Ayu?"
Stephania "You're so cute, and your songs are so upbeat and full of energy! I can't help but love you!"
$ aface='cute'
show ayu at c1
Ayu "H-Huh? You love me?"
$ sface='shy'
show steffy at c4
Stephania "Yes! I love you a lot, although..."
$ sbody='cas1'
show steffy at c3
Stephania "I hope I am not being too forward. I know, in Japan, it is not customary to be quite so effusive, but I am such a big fan of yours, Ayu, I felt incapable of controlling myself."
Stephania "If you do not like my compliments, however, I will try to curb my impulses."
$ sface='sad'
show steffy at c1
Stephania "I do not wish to make you feel uncomfortable!"
$ aface='shy'
show ayu at c3
Ayu "Oh, no, um... I don't mind, I-I suppose?"
$ sface='shock'
show steffy at c4
Stephania "You don't?"
$ aface='smug'
show ayu at c2
Ayu "No. I'm used to my fans fawning over me. As a top idol, I would expect nothing less, really."
$ aface='smile'
show ayu at c1
Ayu "I-In fact, I shouldn't be so surprised. I-It only makes sense, knowing now that you have heard of me, that you would love me!"
$ aface='wink'
$ abody='wcas2'
show ayu at c4
Ayu "I mean, who {i}doesn't{/i} adore Ikue Ayu? I'm so gosh-darned cute, it's impossible not to!"
Ayu "Ohohoho!"
$ sface='happy'
show steffy at c3
Stephania "Oh, I quite agree! You really {i}are{/i} adorable!"
$ sface='smile'
show steffy at c2
Stephania "I've always thought you were cute, just from looking at your photographs, but you're even lovelier in person!"
Stephania "I'm used to seeing you in your frilly idol outfits, of course, but your casual clothes are very cute, too! You know exactly how to dress to flatter your body type!"
$ sface='embarrassed'
show steffy at c1
Stephania "You're so pretty, I'm almost jealous..."
$ sface='shock'
show steffy at c4
Stephania "And your hair is so sleek and long and glossy, too! It must take such a long time to dry!"
$ sface='happy'
$ sbody='cas1'
show steffy at c2
Stephania "You really are dedicated!"
$ aface='shy'
show ayu at c3
Ayu "W-Well, of course. As an idol, it would not do if I were careless when it comes to my appearance. I wouldn't want to let my fans down."
Ayu "They all want me to be their cute, lovely Ayu-Ayu, and who am I to deny them of that?"
$ aface='smug'
show ayu at c2
Ayu "Even when I'm not performing, I must take great care to ensure I look like the number one idol I am."
$ aface='smile'
show ayu at c1
Ayu "Bad hair days are a big no-no!"
$ aface='smile2'
show ayu at c4
Ayu "As such, I brush my hair one hundred times morning and night, when waking and before sleeping!"
$ sface='shock'
show steffy at c5
Stephania "Oh my goodness! That sounds like such a hassle!"
$ aface='smile'
show ayu at c3
Ayu "It can be, but no amount of effort is too much: not when it comes to the pursuit of beauty!"
$ aface='grin'
show ayu at c2
Ayu "One doesn't simply become Japan's top idol by accident! It's a crown I've had to fight for, tooth and nail!"
$ aface='smug'
show ayu at c1
Ayu "Ohohoho!"
$ sface='shock'
show steffy at c4
Stephania "Waah..."
$ sface='happy'
$ sbody='cas2'
show steffy at c3
Stephania "You're amazing, Ayu! I really am glad I was able to meet you!"
Stephania "I am not worthy!"
$ sface='smile'
show steffy at c2
Stephania "If Hifumi was not already my mistress, then I would bow before your exalted feet in a second!"
$ aface='angry'
show ayu at c4
Ayu "Hifumin...?"
"Ayu frowns, perturbed, for a few moments, before..."
$ abody='wcas1'
show ayu at c3
Ayu "Oh, yes. I remember that."
"Ayu was with me in Marina's home a month prior, when Hifumi faced off against Stephania in the karuta championships."
"She saw, therefore, just as I did, how Stephania bowed before Hifumi, after her defeat, and begged to become her disciple."
"Stephania and Hifumi grew even closer, during Hifumi's stay in Astoria, and Stephania is well and truly in awe of her."
"Stephania continues to call Hifumi her \"mistress\", despite Hifumi's personal desire to be more a big sister figure."
"I guess Stephania's the sort who, despite being a princess, gets starstruck easily."
"First, she lost her mind over Hifumi, and now she looks almost as impressed by Ayu."
"Her hero worshipping is kind of cute, actually..."
"Though, while Hifumi might be deserving of respect, I'm less certain about Ayu."
"Personally, I find Ayu a little too rancorous to want to bow down before her. Her moods are way too mercurial."
"I think I'd be afraid she'd step on me."
$ abody='wcas2'
show ayu at c1
Ayu "You're close to Hifumin, aren't you?"
$ sface='shy'
show steffy at c1
Stephania "I-I would not like to make presumptions about my mistress's feelings, but... I-I suppose we are somewhat close, yes."
$ sface='shock'
show steffy at c3
Stephania "I am very fond of my mistress, but please, do not get the wrong idea!"
Stephania "I am sure, with time, I will become very fond of you too, Ayu-Ayu!"
$ sbody='cas1'
show steffy at c2
Stephania "You mightn't be my mistress, but I think you are very incredible too! You are a true diva!"
Hiroki "Oh, Ayu's a diva alright, in more than one sense of the word..."
"I murmur under my breath, not that anybody seems to hear me. Ayu is too busy eyeing up Stephania."
$ aface='smug'
show ayu at c4
Ayu "W-Well, of course I'm incredible. I'm well aware of how wonderful I am: so much so, you hardly need to tell me!"
$ aface='embarrassed'
show ayu at c3
Ayu "Being complimented so much can be rather boorish when one has heard all these compliments so many times before!"

$camera_move(0,0,0,0,5,'ease')
$ cface='smile'
$ cbody='wcas1'
call s_stefayuco from _call_s_stefayuco_3

Cosmos "So you say, but you're blushing."
"Cosmos smiles, then nudges Ayu in the side with her elbow."
$ cface='grin'
show cosmos at c4
Cosmos "I think you're happy, really, that Steffy likes you so much. Don't you feel relieved?"
$ aface='angry'
show ayu at c2
Ayu "O-Of course not. I-It's not like I was worried or anything. I-I know I'm irresistible, although..."
$ aface='embarrassed'
$ abody='wcas2'
show ayu at c3
Ayu "Wh-While I am the recipient of a good many compliments, it is rare that these compliments come from pretty women, let alone princesses."
$ aface='smile'
show ayu at c1
Ayu "I suppose there is something a bit surreal about being fawned over by a genuine member of royalty."
$ aface='smug'
show ayu at c4
Ayu "It's strange, but it really isn't a bad feeling."
$ aface='smile'
show ayu at c3
Ayu "Your affection is, of course, expected, but...{w} Well."
$ aface='smile2'
$ abody='wcas1'
show ayu at c2
Ayu "Th-Thank you for being so welcoming, your highness. I am most pleased to make your acquaintance."
$ sface='happy'
show steffy at c4
Stephania "I am very pleased to make your acquaintance too, though you needn't call me \"your highness\". That sounds awfully stuffy!"
$ aface='smile'
$ abody='wcas2'
show ayu at c1
Ayu "How should I refer to you, then? What would be the most appropriate manner of address?"
$ cface='smile2'
$ cbody='wcas5'
show cosmos at c1
Cosmos "Oh, I know! You should call her \"Steffy\", Ayu, just like I do!"
$ aface='shy'
show ayu at c4
Ayu "Isn't that a bit too personal? She {i}is{/i} a princess, after all..."
$ cface='grin'
show cosmos at c2
Cosmos "Steffy might be a princess, but she's really, really cute - and, because she's cute, she deserves a cute nickname."
$ cface='smile'
show cosmos at c1
Cosmos "\"Stephania\" is too much of a mouthful, so to me, she's \"Steffy\". It's perfect!"
$ abody='wcas1'
show ayu at c3
Ayu "I don't know..."
"Ayu glances at Elizabeth."
$ aface='angry'
show ayu at c1
Ayu "Would her maid permit that?"

hide steffy with dissolve
$ lface='serious'
$ lbody='maid1'
call s_lizayuco from _Call_S_lizayuco_1

Elizabeth "I confess, I had my misgivings, when first I met you. I thought your boastful, pompous style of speech perfectly repellent..."
"Ha! So, I'm not the only one!"
"Ayu's never deigned to pay me much heed, when I tried to upbraid her over her better-than-thou style of speech, but maybe she'll be more inclined to take Elizabeth seriously."
"Elizabeth, despite her frilly outfit, has an indomitable aura. She's the sort of person who seems to demand respect."
$ lface='smile'
show lizzie at c1
Elizabeth "...but, after spending more time with you, it appears your earlier attitude was naught but a front."

stop music fadeout 1.0

$ lbody='maid2'
show lizzie at c4
Elizabeth "I suspect, deep down, you are a kind, considerate girl, if a touch awkward."

play music "bgm/succubus_comedy_loop.ogg" fadein 1.0

$ cface='laugh'
show cosmos at c3
Cosmos "That sounds like Ayu alright, hehe. For such a beloved idol, you really are awkward!"
$ aface='urgh'
show ayu at c4
Ayu "A-Awkward?"
"Ayu scowls."
$ aface='shock'
$ abody='wcas2'
show ayu at c2
Ayu "I-I am {i}not!{/i} You take that back!"
$ cface='joke'
show cosmos at c1
Cosmos "I can't. I won't. It's true, after all."
$ aface='drop'
show ayu at c1
Ayu "No, it isn't!"
$ cface='smile'
show cosmos at c4
Cosmos "It is."
$ aface='angry'
show ayu at c4
Ayu "Isn't!"
$ cface='joke'
show cosmos at c3
Cosmos "It {i}is!!!{/i}"
$ lface='angry'
show lizzie at c3
Elizabeth "Ahem."
$ lface='serious'
show lizzie at c2
Elizabeth "Are you two quite done?"
$ aface='sad'
$ abody='wcas1'
show ayu at c2
Ayu "O-Oh, yes... My apologies, Miss Elizabeth."
$ lface='angry'
show lizzie at c1
Elizabeth "Good."
$ lface='serious'
$ lbody='maid1'
show lizzie at c3
Elizabeth "Now, then. Though you did not make the best first impression upon me, Miss Ikue, I sense that you are not all bad."
"Elizabeth's right there. Ayu isn't all bad: she's only {i}mostly{/i} bad."
"I'd say she's at least 70%% rotten, though the remaining 30%% of her is rather sweet."
"If only Ayu could be a sweetheart 100%% of the time!"
$ lface='smile'
show lizzie at c1
Elizabeth "That being the case, I do not mind if you wish to become closer to milady."
$ lbody='maid2'
show lizzie at c4
Elizabeth "While I would never dream of calling her \"Steffy\" myself, you may. I think milady might appreciate it."
$ aface='shy'
show ayu at c4
Ayu "O-Oh, very well, then. I-I do not care for such closeness myself, but... Ahem."
$ aface='smile'
show ayu at c3
Ayu "I-It is very good to meet you, St-Steffy."
Ayu "You seem very sweet, though your maid has quite the sharp tongue, and I hope that this will be the beginning of a wonderful acquaintance between the pair of us."
$ aface='smile2'
show ayu at c1
Ayu "I have never spoken to a noble before, other than Lady Yue, but you seem far more agreeable than she is."
Ayu "I would be flattered if we could spend more time together."

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
scene skyd with wiperight_slow
window show dissolve

"An hour later..."

play music "bgm/succubus_sports_loop.ogg" fadein 1.0
scene themepark
$ sface='shock'
$ sbody='cas2'
$ cface='smile'
$ cbody='wcas3'
call s_stefmos from _call_s_Stefmos_2
$camera_move(400,300,200,0,0,'dissolve')
with wipedown_slow

Stephania "Oh my goodness! Is this one of these much vaunted \"theme parks\" I've heard so much about?"
$ cface='laugh'
show cosmos at c4
Cosmos "That's right! This is Yumemiru Land: a theme park full of love, hopes, dreams, and very fast roller coasters!"
$ cface='smile'
show cosmos at c3
Cosmos "I've been here a few times before, to make vlogs for my MyTube channel, hehe."
$ cbody='wcas6'
show cosmos at c2
Cosmos "I've even livestreamed here a few times. One of my fans kept tipping me, to make me eat a bunch of corn dogs, and then they had me go on the spinning cups five times in a row."
$ cface='laugh'
show cosmos at c1
Cosmos "I don't really understand why they did that, but it was a lot of fun!"
Hiroki "Hm... I wonder..."
"I've a sneaking suspicion as to why this so-called \"fan\" of Cosmos's might've asked her to eat a bunch of junk food, then go on a fast, spinny ride several times in succession, but I'll keep it to myself."
"Cosmos, for all the lewd outfits she often dresses up in, seems pretty innocent when it comes to the true depths of perversion some people can sink."
"If she can't gauge what this fan was {i}really{/i} after, then I'll leave her to her ignorance."

$camera_move(0,0,0,0,4,'ease')
$ aface='urgh'
$ abody='wcas1'
call s_stefayuco from _call_s_stefayuco_1

Ayu "Wow. Some of your fans sure are freaky..."
"Ayu seems to have come to the same conclusion as me, because her nose wrinkles."
$ aface='angry'
show ayu at c4
Ayu "I feel almost sorry for you, Cosmos."
$ cface='neutral'
show cosmos at c4
Cosmos "Why's that? I don't get it."
Cosmos "I had a really good time that day. I got to eat a lot of yummy food, and go on a lot of fun rides, and I even got paid for it."
$ cface='laugh'
show cosmos at c2
Cosmos "It was a blast!"
$ aface='drop'
show ayu at c3
Ayu "So long as it didn't make you feel queasy, I suppose..."
$ cface='smile'
$ cbody='wcas6'
show cosmos at c3
Cosmos "Oh, you don't need to worry about that. I never feel sick. I'm tough, hehe."
$ sface='shock'
$ sbody='cas2'
show steffy at c1
Stephania "Goodness! Is it possible for these rides to make their passengers feel unwell?"
$ aface='angry'
show ayu at c1
Ayu "It is, yeah, especially if you're not used to them - and even more so if you've been paid to eat your body weight in corn dogs beforehand."
"Ayu shoots Cosmos a withering look, who seems blissfully ignorant of it."
"That's just Cosmos in a nutshell, really: \"blissfully ignorant\". It's rare to see her without a smile, though her smile is one that suggests she doesn't fully understand what's going on in the world."
"Maybe, given how innocent Cosmos is, that's for the best?"
$ aface='surprised'
$ abody='wcas2'
show ayu at c2
Ayu "Have you never been to a theme park before, Stephania?"
$ sface='sad'
show steffy at c4
Stephania "Sadly, no. I was never before given the opportunity. I spent much of my childhood in Astoria's palace, and was rarely allowed out."
$ sface='happy'
$ sbody='cas1'
show steffy at c3
Stephania "This is all very new to me!"
$ sface='smile'
show steffy at c4
Stephania "Oh, I cannot wait to try out these rides! I am sure they will be most diverting!"
$ aface='drop'
show ayu at c3
Ayu "Are you sure?"
$ abody='wcas1'
show ayu at c2
Ayu "Going on a big roller coaster right off the bat mightn't be the best idea. You might make yourself ill."

hide ayu with dissolve

$ lface='serious'
$ lbody='maid1'
call s_stefelicos from _call_s_stefelicos_1

Elizabeth "That is a prescient concern. I would not want you to suffer, milady."
$ sface='happy'
show steffy at c2
Stephania "Oh, I am sure I will be fine! I myself am tougher than I look, just like Cosmos - and, {i}un{/i}like her, I wasn't asked to eat a lot of corn dogs, hehe."
$ sface='smile'
show steffy at c4
Stephania "I think I can handle these rides!"
$ sface='smile2'
$ sbody='cas2'
show steffy at c3
Stephania "Now, let us begin at once, without further delay! I want to sample all the delights this theme park has to offer!"
Stephania "I want to go on as many rides as I can: the bigger, the better!"
$ cface='laugh'
show cosmos at c4
Cosmos "I agree! Bigger {i}is{/i} better, isn't it?"
$ cface='grin'
show cosmos at c2
Cosmos "Let's go on that coaster first, then! It's one of the biggest in the park, and it's really exhilarating! I'm sure you'll love it, Steffy!"
$ sface='smile'
show steffy at c1
Stephania "I'm sure I will, too! It looks like a lot of fun!"
$ sface='smile2'
$ sbody='cas1'
show steffy at c3
Stephania "This is going to be the best!"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
play music "bgm/succubus_comedy_loop.ogg" fadein 1.0
scene skyd with wiperight_slow
window show dissolve

"\"It looks like a lot of fun\", Stephania said. \"This will be the best,\" Stephania said."
"Well, it's been almost two hours since then, and we've been stuck in a queue for this coaster the whole time."
"I've no idea how \"exhilarating\", to use Cosmos's sales pitch, this ride is meant to be, given I've yet to get within thirty feet of it."

scene themepark with wipedown_slow

"I can hear excitable whoops and squeals and cheers about me, as people fortunate enough to get into the queue earlier are loaded into their cars, then sent rattling off down the track, but this does little to assuage my mood."
"It's starting to feel like we'll be trapped in this queue for eternity."
"We've {i}already{/i} been waiting a small eternity, in fact (two hours is nothing to sneeze at), and it doesn't feel like we're making any progress."
"This sucks."
"To further compound how uncomfortable this situation is, the queue is jam-packed."
"I've been jostled by elbows more time than I care to count, and one woman even stood on my foot, though she did apologize after this."
"I don't think it was a pre-meditated act of maliciousness, but it still hurt."
"It doesn't help that my party has been stuck behind this gaggle of very loud high school girls throughout the whole queueing experience."
"Their voices are so shrill they're making my ears ache."
"I've gleaned an awful lot during the last couple of hours: something about \"Takahiro\" (whoever he is) being a cheating jerk."
"This \"Takahiro\" must be something of a player, who's been dating his way through all the girls in his year."

scene themepark:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 30.0 crop (400, 120, 1280, 720)
with wiperight_slow

JK "I can't believe he, like, ever confessed to me! What an asshole!"
JKK "He really {i}is{/i} an asshole! He said I was his one and only, and then I saw him hooking up with Ariya!"
JKKK "Ariya? But why? She isn't, like, even pretty!"
JKK "I know, right! Tell me about it!"
JK "I can't believer I ever gave Takahiro the time of day!"
JKK "And then - get this - he even had the audacity to ask me if I'd be interested in, like, being part of his harem!"
JKKK "A harem?!"
JK "No way!"
JKK "Yes, way! It was like he thought he was a character in some lewd game or something!"
JKK "Who has a harem in {i}real{/i} life? It's, like, so stupid!"
JKKK "Oh, totally!"
JKKKK "What a loser!"
JK "I'm so glad to be rid of him!"
JKK "Takahiro really is the worst! He might be hot, but he's, like, {i}sooo{/i} not worth the attention!"
"Oof. Takahiro's getting verbally eviscerated here, not that I have much sympathy for the guy. I've never met him."
"Still."
"I wonder what this gang of vicious high schoolers would think about me if they knew the nature of {i}my{/i} harem?"
"Would they try to gouge my eyes out with their sharp, acrylic fingernails?"
"It's a bit of an uncomfortable thought..."
JK "Guys who want to sleep around are, like, absolute scum!"
JKKK "They're the worst!"
JKKKK "They should be executed!"
JKK "I wish they'd, like, all get orchitis!"
"Orchitis? What's that...?"
"I'm not sure, but I'm not so very curious I want to look it up. I get the feeling it'll be something nasty."
"Yeesh. High school girls sure are scary."
"Next, they'll whip a voodoo doll of Takahiro out of their bags, then start stabbing it with pins."

stop music fadeout 1.0

"I'm glad they don't know anything about my private life. I'm starting to feel like I'm being judged here..."

play music "bgm/succubus_stephania_loop.ogg" fadein 1.0
scene themepark
$ sface='smile'
$ sbody='cas1'
call s_steffy from _call_s_steffy_132
$camera_move(800,400,300,0,0,'dissolve')
with wipeleft_slow

Hiroki "Hey, Steffy."
"I tear my attention away from the anti-Takahiro committee, then look at my blonde-haired, blue-blooded companion."
Hiroki "Are you alright? You're not getting tired, are you?"
$ sface='happy'
show steffy at c4
Stephania "Oh, no! I am having a wonderful time!"
Hiroki "Are you sure? We've not really done anything. We've just been standing around for ages."
$ sface='smile'
show steffy at c3
Stephania "We have, it is true, but queueing is all part of going to a theme park. I am happy to experience it: particularly with you, hehe!"

$camera_move(400,300,200,0,5,'ease')
$ cface='smile2'
$ cbody='wcas3'
call s_stefmos from _call_S_stefmos_32423

Cosmos "That's the spirit. Waiting for things always makes them even more satisfying."
$ sface='happy'
$ sbody='cas2'
show steffy at c4
Stephania "I agree! Now I feel more excited than ever before!"
Hiroki "Well, I'm glad you're both having fun..."
"Though I don't really get it myself."
"I'm bored out of my skull, and listening to the high school girls in front of me devise ways to murder Takahiro - I think we're on \"put fire ants down the back of his shirt\" - is only so diverting."
"My feet are starting to ache, too."
"Stephania's bearing this way better than I thought she would. Maybe that's because Cosmos has been keeping her occupied, taking a whole slew of selfies of them together?"
"Elizabeth, meanwhile, is quiet, like a statue. Is she meditating?"
"That's one way to deal with the tedium of waiting in line, I guess."
"As for Ayu, meanwhile..."

$camera_move(800,400,300,0,4,'ease')
hide cosmos
hide steffy
with dissolve

$ aface='sad'
$ abody='wcas2'
call s_ayu from _call_s_ayu_342423

Hiroki "Are you OK?"
$ aface='surprised'
show ayu at c4
Ayu "What? Oh, yes, I'm fine. Why are you asking?"
Hiroki "I was just curious, is all. I know waiting in line isn't very much fun - and, well, you {i}have{/i} been rather quiet."
$ aface='shy'
$ abody='wcas1'
show ayu at c2
Ayu "Have I?"
Hiroki "Yeah, you have."
"{i}Unusually so,{/i} I append inside my head, {i}since most of the time, you never shut up.{/i}"
$ aface='angry'
show ayu at c1
Ayu "Well, excuse {i}me{/i} if I'm not being very chatty right now."
$ aface='urgh'
show ayu at c4
Ayu "I don't feel much in the mood to talk: not when we've been standing around for so long. There isn't very much {i}to{/i} discuss."
"Well, she's not wrong about that. I can't blame Ayu for being so quiet, but it is strange."
Hiroki "Are you sure there isn't anything bothering you?"
$ aface='surprised'
$ abody='wcas2'
show ayu at c3
Ayu "Like what?"
Hiroki "I don't know. Maybe you're jealous Cosmos has been taking selfies with Steffy, rather than you?"
$ aface='angry'
show ayu at c2
Ayu "Hmph!"
"Ayu turns her nose up in the air, her arms folded."
$ aface='shy'
show ayu at c1
Ayu "Of course I'm not jealous. Why would I be? It's not like I particularly {i}want{/i} Cosmos to take any photos of me or anything..."
"Alright, that settles it. Ayu's {i}definitely{/i} jealous of how well Stephania and Cosmos has been hitting it off."
$ aface='angry'
show ayu at c4
Ayu "A-And it's not like I'm afraid about going on this stupid ride or anything."
$ aface='urgh'
show ayu at c3
Ayu "I-I really couldn't care less, s-so don't get the wrong idea. I'm not anxious, and I most definitely {i}don't{/i} feel like throwing up."
Ayu "I'll be just fine!"
Hiroki "I, uh, never said that you wouldn't be..."
Hiroki "But thank you for the head's up. I'd no idea you were afraid of roller coasters."
$ aface='shock'
show ayu at c1
Ayu "I-I am {i}not{/i} afraid! I just said I wasn't, Hiroki, you idiot!"
Hiroki "I know that's what you {i}said{/i}, but the words that come out of your mouth don't often map onto reality."
$ aface='angry'
$ abody='wcas1'
show ayu at c4
Ayu "Wh-Why, you..."
"Ayu scowls at me - but, before she can retort, Cosmos reaches out, then takes hold of her hand."

$camera_move(400,300,200,0,4,'ease')
$ cface='smile2'
$ cbody='wcas6'
call s_ca from _Call_s_ca_3242

Cosmos "The queue is beginning to move. We're finally making some progress!"
$ cface='laugh'
show cosmos at c4
Cosmos "Come on, Ayu. Let's go!"
$ aface='shy'
show ayu at c2
Ayu "R-Right. Sure. I-It's about time. Hmph."
$ abody='wcas2'
$ aface='urgh'
show ayu at c1
Ayu "As the famous idol Ikue Ayu, there is nothing I despise more than being kept waiting."
$ aface='disgusted'
show ayu at c4
Ayu "This is so boring."
"Ayu tries to sound unconcerned, but I can see that her legs are shaking."
"Despite her protests, she's {i}totally{/i} afraid."
"Maybe I shouldn't derive so much pleasure from Ayu's discomfort, but I can't help myself."
Hiroki "Heh..."
"Now, {i}this{/i} ought to be interesting."

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyd with fstartgame
window show dissolve

"Half an hour later..."

play music "bgm/succubus_cheerful_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("gotta_go_fast")
if persistent.adult==True:
    scene cg5_a with wipedown_slow
else:
    scene cg5 with wipedown_slow
$ renpy.pause()
window show dissolve

Cosmos "Whoo! This is so much fun!"
Cosmos "Isn't that amazing, Ayu? Can't you feel the wind in your hair?"
Cosmos "This really is incredible!"
Cosmos "Yahoooo!"
Ayu "I, nn, ah..."
Ayu "Hyaaaaaaa!!!!!"
Cosmos "Oh? That was quite the loud scream. Aren't you having fun?"
Ayu "N-No, I'm fine! This is fine! I'm not scared at all, stupid Cosmos!"
Ayu "I am the great idol, Ikue Ayu! I'm not afraid of something as silly as heights! I'm not an idiot!"
Ayu "I'm absolutely fine, you see! There's nothing wrong!"
Cosmos "Well, if you're certain, hehe..."
Cosmos "But, if you {i}are{/i} scared, you can always cling to me. I don't mind. I'll look after you!"
Ayu "A-As if I need {i}you{/i} to watch out for {i}me{/i}, you stupid wannabe catgirl! You really {i}must{/i} have hairballs for brains!"
Ayu "I'd sooner {i}die{/i} than turn to {i}you{/i} for comfort!"
Ayu "I'd rather bite my tongue off and bleed to death!"
Cosmos "Really? That's kind of intense..."
Cosmos "But, if you're sure you're fine, then I guess it's alright, hehe."
Cosmos "Oh, look! We're coming up to a loop next - and it's a really big one!"
Cosmos "Isn't this fun?"
Ayu "A-A loop? What? O-Oh no...! I don't want to go upside-down!"
Cosmos "Silly Ayu! Didn't you look at the track before we went on the ride? It's {i}supposed{/i} to go upside-down!"
Ayu "I know that, but the loop is so high! Wh-What if I fall out of the train?"
Cosmos "You won't fall out, Ayu. Don't worry. You're very secure."
Ayu "Yes, but what if?!"
Cosmos "Well, if you do fall out, you should be alright. You're a succubus, so you can fly. You have wings, remember?"
Cosmos "Everything will work out OK!"
Ayu "D-Don't be stupid! I-I can't transform into my succubus form here: n-not in front of all of these people!"
Ayu "If I fall out of the car I'll plummet to my death!"
Ayu "I'll die! I'll seriously die, and my cute corpse will get smooshed on the asphalt like a mosquito!"
Ayu "I don't want that to happen! I'm too young and cute and beautiful to perish!"
Ayu "I have so much left to give!"
Cosmos "Alright, Ayu, the loop is coming up! Let's go!"
Ayu "Nooo! I don't want to go!"
Ayu "{size=+15}KYAAAAAAA!!!{/size}"
Cosmos "Yahoo!!!"
Ayu "Somebody, please stop this thing! I wanna get off! I can't stand thiiis!"
Ayu "My life is flashing before my eyes!!!"
Cosmos "This is so much fun, I feel like I'm gonna die!"
Ayu "And I feel like I'm seriously going to die!"
Ayu "{size=+25}AAAAAAH!!!!!{/size}"

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyd with fstartgame
window show dissolve

"Two minutes later..."

play music "bgm/succubus_slife_of_life_2_loop.ogg" fadein 1.0
scene themepark
$ cface='laugh'
$ cbody='wcas3'
$ sface='smile'
$ sbody='cas2'
$ lface='serious'
$ lbody='maid2'
call s_elicostef from _call_s_elicostef_100
$camera_move(0,0,0,0,0,'dissolve')
with wipedown_slow

Cosmos "Aaah, that really was fun! I can't get enough of fast rides like that, hehe. They're so exciting!"
$ cface='smile2'
show cosmos at c4
Cosmos "What about you, Steffy? Did you enjoy yourself?"
$ sface='happy'
$ sbody='cas2'
show steffy at c2
Stephania "Oh, yes! That truly was an amazing experience!"
$ sface='smile'
show steffy at c1
Stephania "I admit, I was somewhat afraid before I stepped on that ride, but it was most invigorating! I feel as though I have been reborn!"
Stephania "My heart simply won't stop pounding!"
$ lface='sad'
show lizzie flip at c4
Elizabeth "Dear me. I hope you do not feel unwell, milady?"
Elizabeth "If your heart is pounding as much as you claim it is, perhaps you ought to sit down. I would not want you to over-exert yourself."
$ sface='happy'
show steffy at c4
Stephania "Oh, no, I'm fine! Don't worry about me so much, please, Lizzie."
Stephania "My heart is pounding, but that is only because I had such a good time. I do not think I am about to keel over: not any time soon, at least."
$ lface='angry'
show lizzie flip at c3
Elizabeth "I hope not. If anything ill were to befall you, I would feel quite awful."
$ lface='serious'
$ lbody='maid1'
show lizzie flip at c1
Elizabeth "As your maid, it is my duty to protect you, above all else."
$ sface='smile'
show steffy at c3
Stephania "I know it is, and you do a wonderful job at it. I know I'm in safe hands when I am with you, Lizzie!"
$ lbody='maid2'
show lizzie flip at c4
Elizabeth "So you say..."
$ lface='sad'
show lizzie flip at c3
Elizabeth "But if an accident were to occur upon one of these rides, I fear there would be little I could do to help you."
Hiroki "Were you worrying about that?"
"Now, it's my turn to reassure Elizabeth. I offer her a small smile, then say..."
Hiroki "If you're afraid about the safety of the rides, you needn't be."
Hiroki "Roller coasters are checked rigorously by a team of people every single day, to ensure they're in tip-top shape."
Hiroki "You're statistically less likely to get into an accident on a roller coaster than you are in a car, regardless of what certain horror movies might have you think."
Hiroki "They're pretty safe."
$ lface='serious'
show lizzie flip at c2
Elizabeth "Is that so...?"
$ lbody='maid1'
show lizzie flip at c3
Elizabeth "I did not know that, though I suppose that does make sense."
$ lface='angry'
show lizzie flip at c1
Elizabeth "These theme parks seem like popular tourist destinations. This park is teeming with people."
$ lface='serious'
show lizzie flip at c4
Elizabeth "It stands to reason, given how much money one would stand to make from operating a business such as this, that the rides would be subject to a great degree of scrutiny."
$ lbody='maid2'
show lizzie flip at c3
Elizabeth "Nobody would wish to pay the (frankly quite exorbitant) entrance fee this park demands if the rides were not totally safe."
Elizabeth "If the guests all died, these parks would soon close."
Hiroki "Well, you're not wrong there..."
Hiroki "Though that's a pretty mercenary way of looking at things."
Hiroki "I'd like to think the guys in charge of this park, whoever they are, would care about their guests' safety, even without worrying about profiteering."
$ lface='angry'
show lizzie flip at c4
Elizabeth "You may believe that if you wish, though if you do, I fear that you are very naïve."
Elizabeth "There are few people in this world who act solely for the benefit of others."
$ lface='serious'
show lizzie flip at c1
Elizabeth "Most relationships - particularly those between business owners and consumers - are built upon profit margins."
Hiroki "Wow, uh... That sure is cynical..."
$ lface='serious'
show lizzie flip at c4
Elizabeth "But it is the truth."
$ cface='grin'
show cosmos at c2
Cosmos "I dunno what you're talking about, but I've been having a blast. Do you want to go on even more rides, Steffy?"
$ sface='happy'
show steffy at c2
Stephania "Yes, indeed! That roller coaster was very diverting, but it looks like there are even more of them over there!"
$ sface='smile'
$ sbody='cas2'
show steffy at c1
Stephania "Shall we go?"
$ cface='joke'
$ cbody='wcas6'
show cosmos at c3
Cosmos "Yes, let's! I want to go on every single roller coaster this place has to offer, and then some!"
$ lface='angry'
show lizzie flip at c3
Elizabeth "I cannot say I see the appeal of being jerked about through the air at inhuman speeds, or in going upside-down..."
$ lface='smile'
show lizzie flip at c1
Elizabeth "But if you find enjoyment in this, milady, then I can accompany you."
$ lface='worried'
show lizzie flip at c4
Elizabeth "I only ask that we interspace some of these larger roller coasters with some more easily digestible experiences."
$ cface='smile2'
show cosmos at c1
Cosmos "In that case, maybe we could try the teacups? They're a very popular ride, and they aren't too scary. Even children love them!"
$ sface='shock'
show steffy at c4
Stephania "The teacups?"
"Stephania claps her hands together."
$ sface='smile'
show steffy at c3
Stephania "How whimsical! I cannot imagine what such an attraction might look like, but I am keen to find out!"
$ cface='laugh'
show cosmos at c4
Cosmos "Let's do that, then! We can also go on the swings, if you want - ooh, and the carousel! The little horseys are so cute, hehe~"
$ cface='smile'
show cosmos at c3
Cosmos "What do you think, Ayu? Do you want to tag along with us?"

hide lizzie with dissolve
$ aface='surprised'
$ abody='wcas1'
call s_ayucostef from _call_s_ayucostef_1

Ayu "What? Oh..."
"It looks like Ayu was spacing out a little, because she blinks, then glances to Cosmos."
$ aface='shy'
show ayu at c4
Ayu "O-Of course. I don't mind what we go on next. I can take any ride you want to throw at me, no matter how tall it might be, or how fast it might go."
$ aface='smile2'
show ayu at c1
Ayu "I'm not at all afraid of heights. That last ride was child's play, really! Ohohoho!"
$ sface='sad'
show steffy at c4
Stephania "But nobody asked if you were afraid of heights, Ayu..."
$ aface='surprised'
show ayu at c2
Ayu "What? They didn't?"
$ sface='smile'
show steffy at c2
Stephania "No - and we aren't planning to go on a roller coaster next. Cosmos was talking about the teacups?"
$ cface='smile2'
show cosmos at c2
Cosmos "Yeah, Ayu. Pay attention, hehe."
$ cface='smile'
show cosmos at c1
Cosmos "I know that last ride freaked you out, but you should try to look lively."

stop music fadeout 1.0

$ aface='urgh'
$ abody='wcas2'
show ayu at c4
Ayu "Ggk..."
"Ayu takes a sharp step back, her face flooding scarlet, and scowls."

play music "bgm/succubus_comedy_loop.ogg" fadein 1.0

$ aface='shock'
show ayu at c3
Ayu "Th-That last ride did {i}not{/i} \"do a number on me\", y-you stupid catgirl! I was totally fine! I'm {i}still{/i} fine, in fact!"
$ aface='disgusted'
show ayu at c2
Ayu "It's not like I was scared: not at all!"
$ cface='sweatdrop'
$ cbody='wcas6'
show cosmos at c4
Cosmos "But Ayu, you were screaming so loud you almost ruptured my eardrums."
$ sface='smile2'
show steffy at c3
Stephania "I {i}did{/i} think I heard you shouting, though I wasn't sure. Lizzie and I were in a different car, after all, but your voice really does carry."
Stephania "That must be because you're a professional idol! You have a very powerful set of lungs, hehe~"
$ cface='neutral'
show cosmos at c3
Cosmos "She sure does. I would know. I had to listen to her yelling during the whole ride."
Cosmos "Weren't you just a little bit afraid?"
$ aface='shy'
show ayu at c1
Ayu "N-No, I wasn't afraid; not even a little!"
$ cface='joke'
show cosmos at c2
Cosmos "Then why were you shouting?"
$ abody='wcas1'
show ayu at c4
Ayu "Th-That was just... It was..."
$ cface='grin'
show cosmos at c1
Cosmos "Yes? What was it?"
$ aface='surprised'
show ayu at c3
Ayu "I, um... I might have been screaming, just a little..."
"Ah-haa. So, the truth {i}finally{/i} comes out, like it always does whenever anybody starts needling Ayu."
"She's such an awful liar, it often makes me wonder why she even bothers."
$ aface='shy'
show ayu at c2
Ayu "B-But I wasn't screaming because I was scared. I just, um, wanted to warm up my vocal chords."
$ cface='neutral'
show cosmos at c4
Cosmos "Your vocal chords...?"
$ aface='cute'
show ayu at c1
Ayu "Yes! That's what I was doing! I was warming up my voice, for my future concerts!"
$ aface='wink'
show ayu at c4
Ayu "As an idol, it's very important that I utilize my angelic voice whenever I can, so it doesn't begin to deteriorate!"
$ aface='smug'
show ayu at c3
Ayu "I thought riding that coaster was as good a chance as any to limber up!"
"\"Limber up\"? {i}Please{/i}. I don't know much (or anything) about vocal training, but I know that story's a load of baloney."
"For one thing, who warms up their voice on a roller coaster, of all things - and, for another, aren't singers generally discouraged from shouting a lot?"
"This story is so flimsy, I can't believe anybody would fall it."
"It's an obvious skein of fantasy to me, but..."
$ sface='shock'
show steffy at c1
Stephania "Oh, I see!"
Stephania "I was worrying you might not have been enjoying yourself, Ayu, but I am glad to know, now, that this is not the case!"
$ sface='smile'
$ sbody='cas2'
show steffy at c3
Stephania "You really are dedicated, though, to train even while riding a roller coaster! That is very impressive!"
$ sface='happy'
show steffy at c2
Stephania "Your passion for your craft is incredible!"
"...Darn. Stephania really swallowed that lie hook, line, and sinker, didn't she?"
"She fell for Ayu's excuse so easily, I feel somewhat stunned - as, I think, does Ayu."
$ aface='disgusted'
show ayu at c2
Ayu "..."
"Ayu looks at Stephania askance for a few moments, her brow furrowed, in a way that clearly says, \"Wait, let me get this straight: did you {i}really{/i} buy that...?\""
"But a few seconds elapse, and with them, Ayu is able to arrange her facial features into a breezy smile."
$ aface='wink'
show ayu at c1
Ayu "Well, {i}of course{/i} I'm dedicated. I can't afford to take any time off, you know: not when I have so many fans!"
$ aface='smile'
show ayu at c4
Ayu "They expect me to do my very best, at all times, so I can't afford to slack of!"
Ayu "It's only natural that I would think about work, no matter where I am! That's how we idols are!"
$ aface='smug'
$ abody='wcas2'
show ayu at c3
Ayu "Ohohoho!"

hide steffy
hide cosmos
with dissolve

$camera_move(400,300,200,0,3,'ease')
$ lface='serious'
$ lbody='maid1'
call s_lizyu from _call_s_lizyu_1

Elizabeth "How impressive."
$ lface='smile'
show lizzie at c4
Elizabeth "I thought you might be somewhat flaky, but I can see my earlier assessment of you was in error. You truly are a hard worker."
$ lface='happy'
show lizzie at c1
Elizabeth "In that regard, perhaps you and I are not so very dissimilar after all."
Elizabeth "I, like you, am dedicated to serving milady, to such a degree she is all I can think of."
$ lface='smile'
$ lbody='maid2'
show lizzie at c3
Elizabeth "It is somewhat nice, in a way, to know you feel similarly towards your own work."
"...Geez. Don't tell me Elizabeth's fallen for Ayu's very obvious lie too?"
"I thought Elizabeth was supposed to be smart!"
"Maybe I gave her too much credit..."

$camera_move(800,400,300,0,3,'ease')
hide ayu
hide lizzie
with dissolve

$ cface='neutral'
$ cbody='wcas3'
call s_cosmos from _call_s_cosmos_232

Cosmos "Hey, Hiroki..."
"Cosmos sidles up to me and, quietly, she mumbles..."
$ cface='sweatdrop'
show cosmos at c4
Cosmos "You don't believe Ayu, do you, when she said she wanted to train her voice?"
Hiroki "No, of course not. She was obviously lying."
$ cface='sad'
show cosmos at c2
Cosmos "That is what I thought, but Steffy and Lizzie both seem very taken."
Hiroki "Maybe it's because they're Astorian. They might be too earnest to detect when somebody else is lying."
$ cface='neutral'
show cosmos at c1
Cosmos "Maybe so..."
"Cosmos frowns."
$ cface='sweatdrop'
show cosmos at c3
Cosmos "Does that mean we're not earnest enough, then?"
Hiroki "No, it means we're familiar with Ayu and her ways. We both know she's awful at telling the truth."
$ cface='neutral'
show cosmos at c1
Cosmos "I suppose that's true. As much as I like Ayu, I wouldn't trust her as far as I can throw her."

window hide dissolve

menu:
    with dissolve

    "Same here.":

        window show dissolve

        Hiroki "Same here - though I reckon it wouldn't be too hard to throw her a fair distance. Her pigtails give you something good to grab onto."
        $ cface='grin'
        show cosmos at c4
        Cosmos "Pfft..."
        "Cosmos snorts."
        $ cface='smile2'
        show cosmos at c2
        Cosmos "Don't tell Ayu that. She wouldn't like it."

        stop music fadeout 1.0

        Hiroki "I wasn't planning on it. I don't have a death wish."

    "Oh, I don't think Ayu's that bad.":

        window show dissolve

        Hiroki "I don't think Ayu's completely untrustworthy."
        Hiroki "She can be sweet when she wants..."
        "I frown."
        Hiroki "But she doesn't seem to want to do that very often."
        $ cface='neutral'
        show cosmos at c2
        Cosmos "Tell me about it. She's so stubborn."
        Cosmos "It's almost like she {i}wants{/i} to make herself look bad."

        stop music fadeout 1.0

        Cosmos "I really don't get her sometimes."


play music "bgm/succubus_slife_of_life_2_loop.ogg" fadein 1.0
scene themepark2:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 30.0 crop (400, 120, 1280, 720)
with wiperight_slow

"Our conversation concluded, the five of us begin to make our way to the teacups."
"The park is pretty crowded, like Elizabeth said earlier, and people keep jostling me."
"I do my best not to step on any toes, but it's hard when the walkways are all so congested."
"The sounds of excitable shrieks fill the air, mingled with the mechanical whirr of the roller coasters that surround us."
"It's a pretty warm day, despite it being early February, and the sun is beating down upon the top of my head."
"I'm starting to get kind of sweaty."
"I knew there was a reason why I don't come to theme parks very often..."
"I try to navigate my way through the crowds as best I can, but..."

scene themepark2
with wipeleft_slow

Hiroki "Oof!"
"In my attempts to keep pace with Cosmos, who's weaving her way lithely through the crowds, I bump into somebody."
"I stagger back, none the worse for wear, but the person I bumped isn't so lucky."
W "Eeek!"
"I hear a panicked, high-pitched squeal, which can only belong to a woman, and then a dull {i}thud{/i}."
"Did I knock her over?"
Hiroki "Gosh, I'm so sorry...!"

stop music fadeout 1.0

"Shame-faced, I look down, and then..."

play music "bgm/sak_suc_alice_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("meet_cute")
if persistent.adult==True:
    scene cg6_a with wipedown_slow
else:
    scene cg6 with wipedown_slow
$ renpy.pause()
window show dissolve

Hiroki "Ulp..."
"I soon come face-to-face with a beauty."
"The woman I knocked over is, without a doubt, gorgeous, despite being sprawled inelegantly upon the asphalt."
W "..."
"This girl's face is so fair, it wouldn't seem out of place hanging on the wall of an art gallery."
"She looks like the kind of woman painters would flock to."
"Heck, I feel pretty drawn to her myself."
"I'm not a painter, but I do have something of an artistic eye, being a photographer, and hers is a face I'd look to take a few snapshots of."
"Something about her appearance puts me in mind of a vampire - maybe it's the pale skin and the dark clothes - but there's a sweetness to her, too: a certain kind of vulnerability."
"She looks very cute indeed..."
Hiroki "...!"
"But, wait a moment: what am I doing? Now isn't the time to stand around gawping!"
"Thanks to my clumsiness, I bowled this poor girl over!"
"I ought to apologize to her, at the very least!"
Hiroki "Are you alright?"
"I extend my hand to the girl who's still sprawled on the ground."
Hiroki "Can you stand? Let me help you, please. I really am sorry."
W "What...? Oh, no."
W "You don't need to worry about me. I-I am fine, um..."

scene themepark2
$ alface='embarrassed'
$ albody='cas3'
$camera_move(800,400,300,0,0,'dissolve')
call s_alice from _call_s_alice_1
with wipeup_slow

"The girl waves aside my offer to help, and my outstretched hand, and instead gets to her feet of her own volition."
"Her face flushing, she brushes down her skirts, then offers me a bow."
$ alface='shy2'
show alice at c3
W "I-I am, um, v-very sorry for getting in your way, Mr. Ogsawara. Pl-Please, forgive me for my clumsiness."
Hiroki "Oh, don't be like that! {i}I{/i} was the one who bumped into {i}you!{/i}"
Hiroki "Do you want me to take you to the restrooms? Maybe you need some tissue, to wipe yourself down?"
Hiroki "I wouldn't want your dress to get dirty!"
$ albody='cas2'
show alice at c4
W "N-No, um... I-It's fine, r-really. I, um, d-don't want to take up too much of your time."
$ alface='shy'
show alice at c2
W "Y-You have been too good to me already. I-I could not ask for more."
$ alface='embarrassed'
show alice at c1
W "I-I am very glad that you thought to pay me any attention at all, so, um... Th-Thank you for being so kind."
$ albody='cas1'
show alice at c4
W "I really must be going now, however. I, um, h-hope you enjoy the rest of your day!"

$camera_move(0,0,0,0,0,'ease')
hide alice with dissolve

"The girl bows to me, then hastens to leave."
Hiroki "Hey, wait...!"
"I call after her, still a little worried, but she seems determined to leave."
"She departs, and soon she disappears: her slender back disappearing altogether into the crowd."
"I can't see any trace of her now. It's almost like she never existed."
"I stand there for a few moments, frowning."
"I'm not sure why, exactly, but something felt a little off about that whole encounter, and not just because of how unexpectedly beautiful that girl was."
"There was something strange about her."
"It takes me a few moments to pinpoint what, exactly, is perturbing me, but when it does..."
Hiroki "Aaah..."
"I gasp with newfound understanding."
Hiroki "How did that girl know my name...?"

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.4)
scene skyd with fstartgame
window show dissolve

"An hour later..."

play music "bgm/succubus_slife_of_life_1_loop.ogg" fadein 1.0
scene themepark2
$ aface='urgh'
$ abody='wcas1'
call s_ayu from _call_s_ayu_23432234233
$camera_move(0,400,300,0,0,'dissolve')
with wipedown_slow

Ayu "Aaaah. All this walking is tiring me out."
"A perturbed Ayu slumps down on a bench by the merry-go-round, which our party just disembarked from."
"Folding one leg over the other, Ayu looks at me from beneath her eyelashes, then stabs a finger in my direction."
$ aface='disgusted'
show ayu at c4
Ayu "Hey, you! Hiroki!"
Hiroki "Yes, that's my name. What do you want?"
$ aface='angry'
show ayu at c3
Ayu "I'm hungry. Go and buy me something."
Hiroki "Oh, OK...?"
"This request doesn't sound like it'll be too difficult to carry out."
"I was worried Ayu would ask me to do something truly outrageous like, I don't know, bow down before her on the ground, so she can use me as a footrest."
"I wouldn't put it past her."
"Procuring food for her should, by contrast, be a relatively simple task - and a far less embarrassing one, too."
Hiroki "Is there anything you want?"
$ abody='wcas2'
show ayu at c1
Ayu "Hmm..."
$ aface='smug'
show ayu at c4
Ayu "Ice cream."
Hiroki "It's February, though. Are you sure?"
$ aface='angry'
show ayu at c3
Ayu "{i}Yes{/i}, I'm sure. I want something that isn't too heavy: something that'll melt in my mouth."
$ aface='wink'
$ abody='wcas1'
show ayu at c1
Ayu "I don't get to eat ice cream all that often but, since I'm here, I thought I might as well treat myself."
Ayu "I deserve it, for working so gosh-darned hard all the time."
$ aface='drop'
show ayu at c4
Ayu "Don't tell me you're worried about me putting on a few pounds?"

window hide dissolve

menu:
    with dissolve

    "Well, as an idol, you need to watch your figure...":

        window show dissolve

        $ succ_points -= 2

        Hiroki "Well, as an idol, you do need to watch your figure..."
        $ aface='urgh'
        show ayu at c3
        Ayu "Hmph! And who asked you, anyway?!"
        Hiroki "Um, {i}you{/i} just did?"
        Ayu "M-Maybe I did, but it's not like you needed to be so rude about it!"
        $ aface='shock'
        show ayu at c2
        Ayu "That's no way to speak to a lady!"
        Ayu "You really are thoughtless, Hiroki!"

        stop music fadeout 1.0

        Ayu "I have no idea what I see in you, really. I'm already stressed about this stupid Mihama Shizuru situation, without you making it worse!"

    "I think you look fine.":

        window show dissolve

        $ succ_points += 2

        Hiroki "I'm not worried about that. I think you look fine as-is, and I know you're a hard worker. I'm sure you'll shed any extra pounds soon enough..."
        "{i}Not,{/i} I append inside my head, {i}that a single ice cream should have such a drastic effect on your weight anyway.{/i}"
        $ aface='urgh'
        show ayu at c3
        Ayu "Yes, indeed. You're quite right. There's no issue with me eating ice cream when I want to: none at all."

        stop music fadeout 1.0

        $ aface='disgusted'
        $ abody='wcas2'
        show ayu at c1
        Ayu "It's not like I've ben stressed about this stupid Mihama Shizuru situation: not at all!"

play music "bgm/succubus_weird_loop.ogg"
$camera_move(400,300,200,0,4,'ease')
$ cface='smile'
$ cbody='wcas3'
call s_ca from _call_s_ca_32423

Cosmos "Oh?"
"Cosmos's ears perk up at this (her normal, flesh-colored, human ones, not the cat ears balanced atop her head), and grinning, she takes a seat next to Ayu on the bench."
$ cface='joke'
show cosmos at c4
Cosmos "Are you {i}sure{/i} you've not been worried about Shizuru, Ayu?"
$ aface='shock'
show ayu at c2
Ayu "Yes, I'm sure!"
$ cface='smile'
show cosmos at c2
Cosmos "Really? You say that, but you {i}do{/i} talk about her quite a lot."
$ cface='grin'
show cosmos at c1
Cosmos "Didn't you call me the other day, in tears, because Shizuru got a spot on a talk show you had been angling to go on for a while?"
$ cface='joke'
$ cbody='wcas6'
show cosmos at c4
Cosmos "I think you were eating ice cream then, too, and you said-"
$ aface='shock'
show ayu at c4
Ayu "O-Oh, shut up, Cosmos!"
$ cface='shock'
show cosmos at c3
Cosmos "Eeek!"
"Cosmos squeaks, alarmed, as Ayu drives her elbow into her side."
$ aface='angry'
show ayu at c3
Ayu "None of that matters! {i}Shizuru{/i} doesn't matter! It's all ancient history!"
$ cface='neutral'
$ cbody='wcas3'
show cosmos at c1
Cosmos "It happened last week, though..."
$ aface='urgh'
show ayu at c1
Ayu "Exactly! Last week might as well be a century away! I've already put it from my mind, and so should you!"
$ aface='shock'
show ayu at c5
Ayu "My newfound fondness for ice cream has absolutely {i}nothing{/i} to do with Shizuru, do you hear me? It's irrelevant!"
Ayu "{i}She's{/i} irrelevant!"
$ aface='urgh'
$ abody='wcas2'
show ayu at c4
Ayu "It's not like I want her to get hit by a bus or anything!"

$camera_move(0,0,0,0,4,'ease')
$ sface='shock'
$ sbody='cas2'
call s_stefayuco from _call_s_stefayuco_3242

Stephania "Shizuru...?"
"Stephania, who's none the wiser about the subject of Ayu's ramblings, looks at me curiously."
$ sface='sad'
show steffy at c1
Stephania "Just who is \"Shizuru\?"
Hiroki "She's-"
$ aface='angry'
show ayu at c2
Ayu "She doesn't matter! She's nobody!"
$ cface='joke'
show cosmos at c1
Cosmos "For a \"nobody\", her latest CD sure has sold a lot of units. She seems to be very popular."
$ aface='urgh'
show ayu at c4
Ayu "If she's popular, it's only because she's riding on the coattails of her former fame!"
$ aface='disgusted'
$ abody='wcas2'
show ayu at c3
Ayu "I thought she had dropped out of the industry altogether, until she came back after that huge hiatus with a brand new CD - which, of course, she {i}had{/i} to release a week after my own!"
Ayu "It's like she did it on purpose, just to piss me off!"
$ aface='angry'
show ayu at c2
Ayu "Now people are saying \"Ayu-Ayu is a has-been\" and \"is Shizuru going to steal Ayu's crown?\", like I'm not almost two decades younger than Shizuru is!"
$ aface='shock'
show ayu at c1
Ayu "{i}She's{/i} the has-been!"
show ayu at c4
Ayu "Old hags like her shouldn't be singing pop music at all! She should've bowed off the stage back in the 90s!"
Ayu "I don't want to share any attention with a busted-up MILF like her!"
$ aface='disgusted'
show ayu at c3
Ayu "No, she isn't even a MILF! That implies she's attractive to some degree, but she isn't!"
Ayu "Shizuru's just, like, totally past it! She isn't cute at all!"
$ abody='wcas1'
show ayu at c2
Ayu "What do people see in her, anyway?!"
"...Ooh. That was a particularly animated performance from Ayu there."
"I knew she was upset that Mihama Shizuru, the once-popular idol from the 90s, had released a new CD to rapturous acclaim, but I didn't realize she was quite {i}this{/i} upset."
"And Ayu says Shizuru's a \"nobody\"."
"For a nobody, she sure has Ayu riled up."
Hiroki "...Right. So, you want an ice cream, do you?"
$ aface='angry'
show ayu at c1
Ayu "Yes, please."
Hiroki "And what flavor ice cream do you want?"
$ aface='shy'
show ayu at c3
Ayu "...Strawberry."
Hiroki "Got it. And what about the rest of you? Do you want something?"
$ cface='smile'
show cosmos at c2
Cosmos "I'd like an ice cream too, if you're offering! I want bubblegum flavor!"
Hiroki "Sure..."
"I've always thought bubblegum was a kind of strange ice cream flavor, given bubblegum itself doesn't really {i}have{/i} a flavor, but, well, Cosmos is a strange girl."
"I guess it makes sense she'd plump for one of the odder flavors on the menu."
Hiroki "And what about you, Steffy? Elizabeth?"
$ sface='shock'
show steffy at c2
Stephania "O-Oh, um... I-If you're offering, and it isn't too much trouble, then I think I would like vanilla."

$camera_move(400,300,200,0,4,'ease')
hide cosmos
hide ayu
with dissolve

$ eface='smile'
$ ebody='maid1'
call s_stefeli from _call_s_stefeli_32423

Elizabeth "As a maid, I really shouldn't indulge in sweet treats: not while I'm working. It would appear slovenly."
$ lface='happy'
show lizzie flip at c4
Elizabeth "As a woman, however, I know it is rude to deny a man when he offers to buy me something. I would not like to hurt your pride, so I suppose I can consent."
$ lbody='maid2'
show lizzie flip at c2
Elizabeth "I would like mint chocolate chip."
Hiroki "Right. I'll be back in a sec."

stop music fadeout 1.0

"I make a quick mental note of these requested flavors - strawberry for Ayu; bubblegum for Cosmos; vanilla for Stephania; mint chocolate chip for Elizabeth - and vacate the bench."

play music "bgm/succubus_sports_loop.ogg" fadein 1.0
scene themepark2:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 30.0 crop (400, 120, 1280, 720)
with wiperight_slow

"The park is pretty crowded, and it doesn't take long before I lose sight of the others."
"I hope I'll be able to find my way back..."
"My sense of direction isn't too bad, but I'm getting pushed and shoved about an awful lot."
Hiroki "Oof..."
"I wince as, inadvertently, a girl nudges me with a sharp, pointy elbow."
"At least, I {i}think{/i} it's inadvertent, but..."
JK "OMG! Did you, like, get a load of that guy just there?"
JKK "The tall, nerdy one with the glasses?"
JK "That's right! Didn't he look a little like Takahiro?"
JKK "Hey! Now that you mention it, he totally does!"
JKKK "That's, like, so freaky... It's like these creepy guys are all, like, one amorphous blob!"
JKKKK "These guys all look the same!"
JKK "D'you think they {i}think{/i} the same, too?"
JK "Who knows? Maybe he also wants his own harem!"
JKKK "Ew! There's, like, no way! That'd be so cringe!"
JKKKK "Guys like that are {i}super{/i} cringe!"
JKK "For real, for real!"
JK "I hope he gets orchitis too!"
JKKK "Hahahaha!"
"...Hmm."
"Maybe that nudge {i}wasn't{/i} so inadvertent after all."
"Geez. That really hurt."
"High school girls nowadays are brutal!"
"And I thought trying to communicate with the dour, aloof Yukie, back in high school, was a challenge."

stop music fadeout 1.0

"Speaking of Yukie..."

play music "bgm/succubus_romance_loop.ogg" fadein 1.0
scene themepark2
$ yface='smile1'
$ ybody='wcas1'
$camera_move(0,400,300,0,0,'dissolve')
call s_yue from _call_s_yue_12321
with wipeleft_slow

W "Well, well. Fancy seeing you here."
Hiroki "Yue...?"
"I do a double-take, my eyes widening, as I spy a familiar face among the crowds."
"It seems a little too perfect that she'd be here, after my thoughts just-so-happened to drift in her general direction, but....{w} Well."
"That's how things often seem to go between the two of us."
"Whenever I start thinking of Yue, she seems to show up, almost like magic."
"Maybe it's some kind of magnetism?"
"I've no idea."
"It's a little creepy though, whatever it is."
"At least Yue herself isn't creepy."
"I'm happy to see her, even if this is quite the surprise."
$ ybody='wcas2'
show yue at c4
"Yue is the ruler of the succubus realm and, being a ruler, she has quite the penetrating gaze."
"Though Yue is younger than Marina and Hifumi, her presence is commanding. It's easy to understand, just by looking at her, how she keeps her subjects under her thumb, and in line."
"Yue was rather authoritative in regards to me, too."
"It wasn't so very long ago that she kidnapped me and forced me to come to the succubus realm with her, where she intended to make me her one and only."
"I was worried, for a while, that I'd be trapped in the succubus realm for the rest of my days, but Ayu was able to talk Yue around."
"It was through Ayu's emphatic, emotional address that Yue eventually changed her mind, and she let me go."
"Now, Yue has consented (albeit, reluctantly) to being just one of my partners."
"She allows me to date the other succubi - including Hifumi, her cousin, and Marina, her mortal enemy - but I still sometimes wonder whether she's wholly happy with this arrangement."
$ yface='neutral'
show yue at c3
"Yue {i}can{/i} be rather clingy, and it doesn't help that, as the ruler of the succubus realm, we can't spend much time together."
"Yue is often in the succubus realm, while I have my own life in Tokyo to live."
"I hope she doesn't feel too left out."
Hiroki "Hey there. What are you doing here?"
$ yface='angry'
show yue at c4
Yue "Should I not be here?"
$ yface='neutral'
$ ybody='wcas1'
show yue at c2
Yue "I thought that I would see how you were getting along, so I decided to pay you a visit."
Yue "Is there any issue with that?"
Hiroki "Of course not. I'm very flattered you'd come all the way here, but are you sure you're alright with this place?"
"I glance about the theme park, and all the crowds of people that throng it, my brow furrowed."
Hiroki "It's pretty crowded - not to mention noisy. I know you don't like these sorts of  places."
"I've been on dates with Yue before, back when she attended my high school and I thought she was called Yukie (it's a long story), but we never went to congested places like theme parks."
"I knew, even back then, that Yue didn't care for people. She made her general disdain for humanity quite apparent."
"When we did go on dates, we often went, instead, to cozy cafés, or for walks in the countryside."
$ yface='angry'
show yue at c4
Yue "I don't like busy places such as this, it is true..."
$ yface='serious'
show yue at c3
Yue "...but I am willing to put up with it, no matter how uncomfortable I find it, for your sake."
$ yface='neutral'
show yue at c2
Yue "I would be prepared to endure an awful lot for you, Hiroki."
Yue "After all..."

window hide dissolve
$ achievement.grant("arm_in_arm")
if persistent.adult==True:
    scene cg7_a with dissolve
else:
    scene cg7 with dissolve
$ renpy.pause()
window show dissolve

"Yue approaches me, then links her arm through mine."
Yue "I {i}have{/i} missed you."
Hiroki "Yue..."
"I sigh, all thoughts of ice cream driven from my mind, as Yue rests her head against my shoulder."
"I can feel her long, sleek hair brushing against my cheek: can smell, too, the distinctive scent of her shampoo."
"Yue feels very soft, not to mention warm."
Hiroki "I missed you too."
Yue "Do you mean that, truly?"
Hiroki "Of course. I wish we could talk more often, though I know there's a few logistical issues there."
Yue "Indeed, there are. If only I didn't have the succubus realm to run, perhaps I would be able to spend more time by your side, but alas..."
"Yue shakes her head."
Yue "Let us not dwell upon such sorry affairs for the present. I would far rather indulge in your company."
Yue "I did not pay the truly exorbitant fare to enter this theme park for us to be maudlin!"
Hiroki "Hm?"
"I quirk an eyebrow at this, amused, as my eyes play across Yue's profile."
Hiroki "Did you pay the entry fee to come here, then?"
Yue "But of course! What do you take me for? I might be a succubus, but I am not a criminal!"
Yue "I have lived among you humans long enough to know that theft is morally wrong! I can hardly indulge in petty criminal vices among you humans: not when, in the succubus realm, it is my duty to uphold law and order!"
Yue "That would make me a hypocrite!"
Hiroki "I guess it would, yeah - but, I'm sorry..."
"I laugh. I can't help myself: not when Yue looks so affronted."
Hiroki "There's something pretty funny about the thought of you paying for a ticket to come here when you could've just teleported past the ticket barrier."
Yue "I could have done that, yes, but it would have been morally wrong!"
Yue "While I mightn't be a human, I want, at least, to act like an upstanding citizen!"
Hiroki "I know you do, and you are. I think you're very upstanding indeed."
Hiroki "It's cute."
Yue "\"Cute\", am I...?"
"Yue harrumphs."
Yue "F-For some reason, that does not feel like a compliment."
Hiroki "No?"
Yue "No. It feels like you are teasing me... {w}but, never mind."
Yue "Why don't we enjoy ourselves for a little while, Hiroki?"
Yue "I know you came here with several others - Ayu and Cosmos included - but now that I am here, I would appreciate it if we could have some time together."
Yue "It is so rare that we get any time alone, after all. I would very much like to show you how much I care for you."
Yue "Would that be agreeable with you?"

window hide dissolve

menu:
    with dissolve

    "Well, I was running an errand for Ayu...":

        window show dissolve

        Hiroki "Well, I {i}was{/i} supposed to be running an errand for Ayu..."
        "I smile."
        Hiroki "But I can make time for you, even if she'll complain about it later."

    "Of course it would.":

        window show dissolve

        Hiroki "Of course it would be."
        "I don't even need to think about it."

Hiroki "How can I say no to my adorable girlfriend?"

if persistent.adult==True:
    jump adult3
else:
    jump merge3

label merge3:

    stop music fadeout 1.0
    window hide dissolve
    scene black with fstartgame
    $ renpy.pause(0.3)
    scene skyd with fstartgame
    window show dissolve

    "Half an hour later..."

play music "bgm/succubus_comedy_loop.ogg" fadein 1.0
scene themepark2
$ aface='shock'
$ abody='wcas1'
call s_ayu from _call_s_ayu_23423432
$camera_move(800,400,300,0,0,'dissolve')
with wipedown_slow

Ayu "Hey, Hiroki!!!"
$ aface='urgh'
show ayu at c4
Ayu "Where in the world {i}were{/i} you? I was waiting for almost an hour!"
$ aface='angry'
show ayu at c3
Ayu "I know this theme park is crowded, but that's {i}no{/i} excuse to keep a lady waiting for {i}that{/i} long!"
$ abody='wcas2'
show ayu at c2
Ayu "What took you, you thoughtless-"
$ aface='surprised'
show ayu at c1
Ayu "Ah...!"

$camera_move(400,300,200,0,4,'ease')
$ yface='neutral'
$ ybody='wcas1'
call s_yc from _call_s_yc_23432

"Ayu's eyes dart to the right, and when they do, her gaze meets Yue's."
"Ayu was so incensed, I guess, at my long, untelegraphed absence, she didn't notice my plus one."
$ abody='wcas1'
show ayu at c4
Ayu "Lady Yue? What are you doing here?"
$ yface='serious'
show yue at c1
Yue "What do you think?"
$ yface='angry'
show yue at c4
Yue "I came here to visit Hiroki. That much should be obvious, given the nature of our relationship. I fail to see why I need to explain myself to you, though."
$ ybody='wcas2'
show yue at c3
Yue "You are but one of my underlings, after all."
$ yface='serious'
show yue at c2
Yue "Now, please, stop gawping. It is uncouth: particularly for an idol."

$camera_move(0,0,0,0,4,'ease')
$ cface='joke'
$ cbody='wcas6'
call s_yuayuco from _Call_s_yuayuco_2

Cosmos "You should be careful, Ayu. If you let your mouth hang open like that, insects will fly in!"
"A giggling Cosmos darts forwards, then accepts her bubblegum ice cream from my outstretched hand."
$ cface='smile2'
$ cbody='wcas3'
show cosmos at c2
Cosmos "Hey there, Lady Yue. I didn't expect to see you, but it's nice you came. I hope you're having a good time?"
$ yface='neutral'
show yue at c1
Yue "I am having a tolerably good time, yes - or, at least..."
$ yface='angry'
show yue at c4
Yue "I {i}was{/i}, until Ayu started glowering at me like that."
$ yface='serious'
show yue at c3
Yue "Should you not be happy, Ayu, to see your queen? If I were you, I would be crying tears of joy."
$ aface='embarrassed'
show ayu at c1
Ayu "O-Oh, yes. I'm ecstatic. Your presence here is wonderful, milady. Truly, I am unworthy of your attention."
$ yface='angry'
show yue at c1
Yue "You really are. If you knew any better, you would kneel before my feet and rub your head against my shoes in supplication..."
$ yface='neutral'
show yue at c2
Yue "But that might not, perhaps, be appropriate, given how crowded it is. I would not want us to draw any undue attention."
$ ybody='wcas1'
show yue at c4
Yue "Now, here."
"Yue hands Ayu her strawberry ice cream, which she was holding."
$ yface='angry'
show yue at c3
Yue "Take it, and be grateful."
$ aface='smile'
show ayu at c4
Ayu "O-Oh, um... Thank you, milady."
$ cface='laugh'
$ cbody='wcas6'
show cosmos at c4
Cosmos "That was good of you, Lady Yue! You really are nice!"
$ yface='smile1'
show yue at c1
Yue "I do my best. Though I long believed ruling with an iron fist was conducive to having loyal, well-behaved servants, I now see there are other ways to earn respect beyond fear-mongering."
$ yface='smile2'
show yue at c4
Yue "Hiroki helped me realize that."
Hiroki "You're giving me too much credit..."
$ yface='angry'
show yue at c2
Yue "I am giving you just as much credit as you deserve: no more, no less."
$ yface='shy'
show yue at c1
Yue "Please, do not shrink away from my praise. Can you not accept that I care about you?"
Hiroki "I can accept it, sure. I'm not boorish enough, at least, to question your feelings, however confusing they might be."
"It's with a smile that I then hand Stephania her vanilla ice cream cone."

stop music fadeout 1.0

Hiroki "Here you go, Steffy. This is what you wanted, right?"

play music "bgm/succubus_stephania_loop.ogg" fadein 1.0
hide ayu with dissolve
$ sface='shock'
$ sbody='cas1'
call s_yusteco from _call_s_yusteco_2

Stephania "Oh, yes! It is, but... Um..."
"Stephania accepts the ice cream cone from me, then shyly, she observes Yue."
$ sbody='cas2'
show steffy at c4
Stephania "I apologize for my ignorance, but who is your companion? I do not believe I have ever met her before?"
$ cface='smile'
show cosmos at c2
Cosmos "That is Lady Yue. Ayu and I respect her a lot. She's, like, our queen!"
$ sface='worried'
show steffy at c2
Stephania "A queen...?"
"Stephania blinks, no doubt impressed."
$ sface='shock'
show steffy at c1
Stephania "Then you are of a higher status than me! I am only a princess, you see. My parents are the ones who rule over Astoria."
$ yface='smile1'
$ ybody='wcas1'
show yue at c4
Yue "Ah, yes. I have heard about you. You are Lady Stephania, are you not?"
$ sface='smile'
show steffy at c3
Stephania "Yes, I am! My name is Stephania Sofia Maria Isabella of Astoria, but you can call me \"Steffy\"! All my friends do - apart from Lizzie, who calls me \"milady\"!"
$ sface='smile2'
show steffy at c2
Stephania "Lizzie would never admit to being my friend, in any case, but she is! She's my best friend, in fact!"
$ sface='smile'
show steffy at c1
Stephania "And what about you? Are you a member of royalty yourself, Lady Yue?"
$ yface='shy'
$ ybody='wcas2'
show yue at c2
Yue "...In a manner of speaking, I suppose."
"Stephania might be a member of my harem, but she has no idea as to the existence of succubi. I've been trying to keep that a secret from her. I don't want to alarm her."
"The same can be said, too, of Elizabeth. She might be Stephania's top maid, but she's also (as far as I can gather) quite ordinary."
"Marina, Hifumi, and Hazel did have a few doubts about her, when we were staying in the royal palace in Astoria, but Elizabeth's not done anything to make me doubt her humanity."
"I don't think Elizabeth is a succubus, at least, but..."

hide cosmos with dissolve
$ lface='serious'
$ lbody='maid1'
call s_yusteli from _call_s_yusteli_1

Yue "Your name is... {w}Elizabeth, is that correct?"
$ lface='angry'
show lizzie at c4
Elizabeth "Yes, it is. It is a pleasure to meet you."
"Elizabeth takes her dark skirts in both hands, then offers Yue a neat curtsy."
"Elizabeth's greeting is perfectly polite, as one might expect from a maid, but Yue looks perturbed by it."
$ yface='neutral'
show yue at c4
Yue "You look awfully familiar..."
$ lface='serious'
show lizzie at c2
Elizabeth "Do I?"
$ ybody='wcas1'
show yue at c2
Yue "Indeed, you do. There is something about the shape of your face, perhaps, or the color of your hair..."
$ yface='neutral'
show yue at c1
Yue "Have we met before, in passing?"
$ lface='angry'
show lizzie at c1
Elizabeth "Perhaps we have. I cannot say for certain."
$ yface='neutral'
show yue at c3
Yue "Hmm. How very curious."
Yue "..."
$ yface='serious'
$ ybody='wcas2'
show yue at c1
Yue "...Well, never mind. Perhaps I am imagining things."
$ yface='serious'
show yue at c2
Yue "I am so very busy with work, it seems unlikely I would have the opportunity to spend time with a woman such as yourself."
$ yface='smile1'
show yue at c4
Yue "I have never before been to Astoria, though I would not mind traveling. It seems a pleasant country, by all accounts."
$ sface='happy'
show steffy at c2
Stephania "Oh, it is! Astoria is very lovely! It is rather small, but it has no shortage of attractions!"
Stephania "I hope you will be able to come there one day, Lady Yue!"
$ ybody='wcas1'
show yue at c3
Yue "Just \"Yue\" is fine."
$ sface='shy'
show steffy at c4
Stephania "I-Is it really?"
show yue at c1
Yue "Of course. If you wish for me to call you \"Steffy\", then I must insist that you dispense with formalities in turn when it comes to me."
$ yface='smile2'
show yue at c2
Yue "There is no need for us to bow and scrape before one another: not when we are both royalty."
Yue "We are of the same status, you and I. As such, I would like it if we could become friends."
$ yface='drop'
show yue at c4
Yue "I have precious few of them, given I spend most of my time interacting with my subjects."
$ sbody='cas2'
show steffy at c3
Stephania "Well, I wouldn't like to be presumptuous..."
$ sface='smile2'
show steffy at c2
Stephania "B-But, if you're alright with that, then I suppose I can call you \"Yue\"!"
$ yface='smile1'
show yue at c3
Yue "Good. Then I shall call you \"Steffy\", provided your maid does not take any issue with that?"
$ lface='smile'
show lizzie at c3
Elizabeth "No, that is quite alright with me. I would be happy if milady could make more friends."
$ ybody='wcas2'
show yue at c2
Yue "I am happy to hear it."
"Yue hands Elizabeth her ice cream, then smiles at Stephania."
$ yface='smile1'
show yue at c1
Yue "Now, would you care to wander the theme park with me, Steffy?"
Yue "I have never been to a place such as this before, but I think experiencing it with you would be fun."
$ yface='smile2'
show yue at c3
Yue "As a fellow noble, there is much, I believe, that we can discuss with one another."
$ yface='smile1'
show yue at c2
Yue "I imagine we will have a lot in common!"
$ sface='smile'
show steffy at c4
Stephania "Oh, that sounds wonderful!"
$ sface='happy'
$ sbody='cas2'
show steffy at c3
Stephania "I look forward to getting to know more about you, and the customs of the country from which you hail."
Stephania "Any friend of Hiroki's is a friend of mine!"

stop music fadeout 1.0
window hide dissolve
scene black with fstartgame
$ renpy.pause(0.3)
scene skyd with fstartgame
window show dissolve

"And so, in the end..."

play music "bgm/succubus_cheerful_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("gotta_go_faster")
if persistent.adult==True:
    scene cg8_a with wipedown_slow
else:
    scene cg8 with wipedown_slow
$ renpy.pause()
window show dissolve

Stephania "Oh my gosh! This is so much fun!"
Stephania "Are you having fun too, Yue?!"
Yue "I've never been on a roller coaster before, but..."
"{i}Wooosh!{/i}"
Stephania "Aaah! Isn't it just the best when there's a sudden drop like that?!"
Stephania "My stomach's lurching, but in a good way!"
Stephania "This is so hype!"
Yue "Well, I am rather inclined to agree with you there, ufufu."
Yue "Unaccustomed as I am to roller coasters, I don't dislike how dynamic this experience is."
Yue "I've never had much of a chance to cut loose, as a monarch..."
"{i}Wooosh!{/i}"
Stephania "Yaaaay!"
Yue "...But I think I could get used to this."
Stephania "I know, right?! Isn't this the best? I'm having a whale of a time, haha!"
Stephania "I'm so glad Hiroki took me here, and d'you know what?"
Yue "What?"
Stephania "I'm glad I could experience this with you too, hehe."
Yue "You... {w}are?"
Stephania "Of course! It's not every day I get to meet another royal! I feel like we have a lot in common!"
Yue "Do you really think so?"
Stephania "Yes! We've both been cooped up in palaces all our lives. Now we've both met Hiroki, though, we can have fun!"
Stephania "We're both doing things that, normally, we'd never be able to do."
Stephania "Don't you think that's special?"
Yue "...Well, when you phrase like that, I suppose it is rather special."
Yue "I'm not sure if we're quite as similar as you seem to think - you're a lot bubblier than I am, for one - but..."
Yue "I'm glad I met you too, Stephania."
Yue "I think you and I could become very good friends."
Stephania "Oh, I do hope so! I'm so happy, I don't know what to do with myself!"
Stephania "This is so much fun...!"
"{i}Woosh!{/i}"
Stephania "I don't want today to {i}ever{/i} end!"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
play music "bgm/succubus_sports_loop.ogg" fadein 1.0
scene skyd with wiperight_slow
window show dissolve

"I wander about Yumemiru Land for a while more with my companions, talking to them all the while."
"Together, we attend various attractions, until, near the end of the day, Ayu makes something of a scene."
"My group winds up going, at Cosmos's behest, to a stage show."
"It's the sort of show they often stage at theme parks: open air, on a dinky little stage set up in front of one of the gentler rides for kids."
"It's a pretty low-budget sort of a show that features actresses dressed up as magical girls from a series I presume must be currently airing."
"These actresses are occupied with defending the world (aka the audience) from \"the forces of evil\" (aka a few more actors dressed up in \"scary\" monster costumes)."
"The magical girls duke it out onstage with the monsters, while jubilant music plays through the loudspeakers, and a narrator stands to one side, appealing to the audience for their help."

scene stage
$camera_move(0,0,0,0,0,'dissolve')
with wipedown_slow

MC "Clap your hands, everybody, and cheer out for Cool Muse and Cool Marine! They're both doing their best to defend us, but they need your help!"
MC "Let's all give them a round of applause!"
"The audience of this show, which mostly comprises of little kids, all begin to cheer enthusiastically - as, too, does Cosmos."

$camera_move(400,300,200,0,4,'ease')
$ aface='urgh'
$ abody='wcas1'
$ cface='smile'
$ cbody='wcas3'
call s_ca from _call_s_ca_1432432

Cosmos "You can do it, Cool Muse! You can do it, Cool Marine! I believe in you!"
Cosmos "Don't let the bad guys get the better of you! You can overcome all ills with the power of friendship!"
$ abody='wcas2'
show ayu at c3
Ayu "Urgh."
$ aface='disgusted'
show ayu at c4
Ayu "I understand little children getting worked up over a silly show like this, but what are {i}you{/i} shrieking for?"
Ayu "Aren't you supposed to be an adult?"
$ cface='sweatdrop'
show cosmos at c1
Cosmos "Nominally, I suppose..."
$ aface='angry'
show ayu at c2
Ayu "So, you admit you really {i}are{/i} a child?"
"Ayu rolls her eyes."
$ aface='urgh'
show ayu at c1
Ayu "That figures. You've always been so immature."
$ cface='shock'
show cosmos at c4
Cosmos "But I don't understand how you can't cheer on Cool Muse and Cool Marine. They're both, like, so awesome."
Cosmos "They're only middle school students, but they have a lot of problems."
$ cface='smile2'
$ cbody='wcas6'
show cosmos at c3
Cosmos "Cool Muse is actually really shy, and Cool Marine has a lot of brothers and sisters to look after, but they don't buckle under their problems."
Cosmos "They continue to do their best, both at school, and when they're fighting the evil dark rangers."
$ cface='laugh'
show cosmos at c1
Cosmos "They worry a lot, and sometimes they think about giving up, but they never do."
$ cface='smile2'
show cosmos at c2
Cosmos "They fight for love, truth, and justice. I think it's very beautiful."
$ cface='grin'
show cosmos at c4
Cosmos "One day, I'd like to grow up to be just like them!"
$ aface='angry'
$ abody='wcas1'
show ayu at c4
Ayu "Right. Well. That's a very beautiful dream, Cosmos-"
$ cface='laugh'
show cosmos at c3
Cosmos "Thank you! I'm glad you think so, hehe."
$ aface='urgh'
show ayu at c3
Ayu "-but you're {i}already{/i} grown up. You're a catgirl, not a kitten, and you shouldn't be worshipping magical girls at your age."
$ aface='drop'
$ abody='wcas2'
show ayu at c2
Ayu "The clue is in the name, dummy: they're magical {i}girls{/i}, not {i}women{/i}. These shows are supposed to appeal to six-year-olds."
Ayu "You're way out of the target demographic. Isn't that right, Lady Yue?"

hide ayu
$ yface='smile1'
$ ybody='wcas1'
call s_yuco from _call_s_yuco_1

"Ayu looks to Lady Yue for support, but..."
$ yface='smile2'
show yue at c2
Yue "You can do it, Cool Marine! Don't give in!"

$camera_move(0,0,0,0,4,'ease')
$ sface='happy'
$ sbody='cas1'
call s_yusteco from _call_s_yusteco_1

Stephania "I'm rooting for you, Cool Muse! You've always been my favorite!"
"Yue, inexplicably, seems to be pretty into this - and so does Stephania."
"Well. I'm not surprised Stephania would be enjoying herself, but Yue's reaction throws me."
Hiroki "Do you like magical girl shows, Yue?"
$ yface='embarrassed'
show yue at c3
Yue "What...?"
"Yue turns to me, somewhat awkwardly, and her face begins to flush."
$ yface='smile2'
show yue at c4
Yue "I-I don't make a habit of watching such shows, of course - they are, like Ayu said, rather childish - but {i}Pretty Cool{/i} is rather nostalgic."
$ ybody='wcas2'
show yue at c3
Yue "I used to watch it in the mornings, when I lived in Japan: back when I still attended high school."
$ yface='smile1'
show yue at c1
Yue "The cools back then were different, of course - they were Cool Ivory and Cool Ebony - but the show's still pretty similar to the way it used to be."
$ yface='embarrassed'
show yue at c2
Yue "I still keep up with the newer seasons when I can. It's an easy way to pass the time."
Yue "I-It's not like I'm really into {i}Pretty Cool{/i} or anything, though..."
"Oh, now that's unusual. Yue's actually blushing."
"I wonder what to make of this..."

window hide dissolve

menu:
    with dissolve

    "It's cute.":

        window show dissolve

        $ succ_points += 1

        "It's pretty adorable, really."
        "I feel like I'm learning a lot about Yue today."

    "It's a bit cringe.":

        window show dissolve

        "...Yeah, I think I'll have to side with Ayu on this one."
        "I don't really get the appeal of shows like this."
        "Aren't they intended for small kids?"
        "Yue's way too old to be getting excited about this stuff!"

$ cface='shock'
show cosmos at c4
Cosmos "Huh? You like {i}Pretty Cool{/i}?"
$ yface='shy'
show yue at c4
Yue "I-It's alright, I suppose. I-I think the fight scenes are a lot of fun..."
$ cface='laugh'
$ cbody='wcas3'
show cosmos at c2
Cosmos "Ooh! Me too, me too! {i}Pretty Cool{/i} {i}is{/i} really awesome, isn't it?"
$ cface='smile2'
show cosmos at c1
Cosmos "I've seen every single season to date! I like it a lot! I think it has a lot of life lessons we could all learn from, hehe."
Cosmos "My favorite season's the fifth one, with Cool Peach and Cool Plum, but the newest season's not bad either. I really, really like Cool Marine, hehe. She's so funny!"
$ cface='laugh'
show cosmos at c3
Cosmos "I was actually working on a cosplay of Cool Marine. I think my fans would like that!"
$ sface='smile'
show steffy at c2
Stephania "I'd like to see that, too! I'm a huge {i}Pretty Cool{/i} fan!"
$ cface='shock'
show cosmos at c1
Cosmos "You are?"
$ sface='happy'
$ sbody='cas2'
show steffy at c1
Stephania "Of course! It's one of Japan's most popular TV shows! I wouldn't be able to call myself a Japanophile if I hadn't seen it!"

hide steffy with dissolve
$ aface='urgh'
$ abody='wcas2'
call s_yuayuco from _Call_s_yuayuco_1

Ayu "...Meanwhile, I'm {i}actually{/i} Japanese, and I {i}really{/i} don't understand the hype. It's just dumb kiddy stuff."
$ cface='joke'
show cosmos at c4
Cosmos "Oh, Ayu. Poor, uneducated Ayu."
$ aface='drop'
show ayu at c2
Ayu "Wh-What? Why are you looking at me like that?!"
$ cface='smile2'
show cosmos at c3
Cosmos "I'm thinking it's rather sad that you don't understand the appeal of {i}Pretty Cool{/i}. You're missing out."
Cosmos "Your heart must be a withered, dried-out old thing indeed."
$ cface='grin'
$ cbody='wcas6'
show cosmos at c1
Cosmos "Without love, it really can't be seen."
$ aface='urgh'
show ayu at c4
Ayu "Wh-What on earth are you babbling about? You're deluded!"
$ aface='angry'
show ayu at c1
Ayu "{i}You{/i} don't get the {i}Pretty Cool{/i} appeal, do you, Hiroki?!"
Hiroki "Not that much, I'll admit..."
Hiroki "But, then again, I {i}am{/i} a guy. I don't think I'm the target audience."
$ aface='shock'
show ayu at c3
Ayu "None of us are! We're {i}all{/i} too old for it!!!"
$ cface='joke'
show cosmos at c4
Cosmos "So, you admit you are getting on in years, then...?"
$ aface='shy'
show ayu at c2
Ayu "What? N-No...! How dare you...!"

stop music fadeout 1.0

"Ayu descends upon Cosmos - meaning, perhaps, to pinch her cheeks - but, before she can eneact her revenge, the MC cries out..."

play music "bgm/succubus_slife_of_life_2_loop.ogg" fadein 1.0
$camera_move(0,400,300,0,4,'ease')
hide yue
hide cosmos
with dissolve

$ aface='shy'
$ abody='wcas1'
call s_ayu from _call_s_ayu_234243

MC "Oh? Is that a familiar face I can spy in the crowd?!"
Crowd "Hmm?"
"At this, the crowd turn en masse. They're all staring - staring, at is soon transpires, at..."
MC "You, over there, in the pink sweater! Are you Ikue Ayu?!"
$ abody='wcas2'
show ayu at c4
Ayu "What? Oh, um..."
"Abashed at the sudden attention, Ayu draws away from Cosmos, then says..."
$ aface='smile'
show ayu at c3
Ayu "Y-Yes, I am. It's me, Ayu-Ayu, in the flesh!"
"A ripple runs through the audience at this announcement. They all seem to know who Ayu is: even the very little kids, who were watching the cools fighting with rapt attention."
"I hear a young boy (at least, I think it's a young boy) a few paces away cry something that sounds like, \"Ayu-Ayu? Is she really here? She's so cute!\", while a girl says, \"Ayu? Where is she? I wanna see her! I wanna hear her sing!\""
"The MC, who really ought to be narrating the cools' valiant fight with their enemies, which is still unfolding onstage, grins, then says..."
MC "Well, isn't this a coincidence? I could hardly believe my eyes when I saw you, but you really must be Ayu!"
MC "I'm actually a huge fan of yours! I never dreamed I might see you one day!"
$ aface='smug'
show ayu at c2
Ayu "H-Heh. Well..."
"Ayu smirks (she seems to have recovered from her initial disorientation), and, flipping one of her pigtails over her shoulders, she says..."
$ aface='wink'
show ayu at c1
Ayu "That goes without saying. I'm Japan's number one idol for a reason. Everybody loves me, and I love everybody else in return!"
$ abody='wcas1'
show ayu at c4
Ayu "I live for my fans!"
$ aface='cute'
show ayu at c3
Ayu "I love all of you!"
MC "I'm glad to hear it!"
MC "Maybe this is a little rude, since you're having a day off and all, but if you {i}really{/i} love us, would you mind coming up onstage?"
MC "The cools could use some moral support, to help them fight off the dark rangers, and I think a song from you should help out!"
MC "That'll give them the boost they need to keep on fighting!"
$ aface='smile'
show ayu at c1
Ayu "You want me to sing, huh?"
$ abody='wcas2'
show ayu at c4
Ayu "I probably shouldn't - not without clearing things with my agency - but..."
$ aface='smile2'
show ayu at c3
Ayu "Oh, what the heck. I'd hate to let all these cute boys and girls down, so I'll do my best!"
$ aface='laughing'
show ayu at c2
Ayu "I want the pretty cools to win, too! I'm a huge fan of theirs!"
Cosmos "You liar..."
"Cosmos murmurs this - but she does it so softly, nobody notices."
$ aface='smile'
$ abody='wcas1'
show ayu at c4
"Ayu, now smiling angelically, walks through the crowd, which parts for her, then ascends onto the stage, with all the self-confidence of a goddess."
MC "Here you go, Ayu-Ayu!"
"The MC hands Ayu a microphone, which she accepts, smiling sweetly all the while."
MC "With your beautiful voice, you should be able to defeat the wicked dark rangers for good, and bring about world peace!"
MC "I believe in you: don't you, boys and girls?"
Crowd "Yes!"
Boy "You can do it, Ayu! I believe in you!"
$ aface='grin'
show ayu at c3
Girl "Do your best!"
Boyy "You're so pretty, Ayu-Ayu!"
Girll "I did my hair just like you, look! I'm your biggest fan!"
$ aface='smile'
show ayu at c2
Girlll "No, {i}me!{/i}"
Boyyy "You're the bestest idol in the whole world!"
Girllll "When I get older, I wanna be you!"
$ aface='smile2'
show ayu at c3
Boy "When I get older, I wanna date you!"
Crowd "You can do it, Ayu!"
$ aface='surprised'
show ayu at c4
Ayu "Oh my..."
"Ayu surveys the crowd of cheering, whooping children with a small smile. Her face looks a little flushed owing to this sudden influx of praise."
"Ayu might talk about her fans in a dismissive manner (in private, at least), but I guess not even she's hard-hearted enough to turn her nose up at a bunch of little kids."
$ aface='smile2'
show ayu at c3
Ayu "It's very gratifying to hear those kind words from you. Thank you very much, everybody!"
$ aface='wink'
show ayu at c1
Ayu "While you might be a little too young to marry me..."
"Ayu catches the eye of the impetuous young boy who all-but proposed, then grins."
$ aface='grin'
show ayu at c3
Ayu "...I can certainly sing for you!"
$ aface='smile'
$ abody='wcas2'
show ayu at c2
Ayu "I'll put my all into this song, and I'll defeat the dark rangers for good!"
Ayu "Now, do you think I can do it, boys and girls?"
Crowd "Yes, you can!"
Girl "There's nothing you can't do, Ayu!"
Girll "You're my hero, Ayu!"
Boy "I love you, Ayu!"
Girlll "You're so cool!"
Crowd "A-yu! A-yu! A-yu!"
$ aface='wink'
show ayu at c4
Ayu "Hehe! That sounds like a \"yes\" to me!"
$ aface='smile'
show ayu at c3
Ayu "Thank you so much for believing in me, everybody. You're being so sweet, how can I not answer your expectations?"
$ aface='grin'
show ayu at c1
Ayu "Now, please listen to my song...!"

stop music fadeout 1.0

"Ayu clears her throat, then brings the mic to her mouth."

play music "bgm/succubus_romance_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("a_rousing_performance")
if persistent.adult==True:
    scene cg9_a with wiperight_slow
else:
    scene cg9 with wiperight_slow
$ renpy.pause()
window show dissolve

Ayu "Ikue Ayu is going to begin!"
"There's a brief pause, during which Ayu mentally prepares - and then, a few seconds later, she begins to sing."
"Ayu's song isn't accompanied by a backing track, as it usually is during her live performances, but that doesn't matter."
"This a capella rendition of her latest single is beautiful in its own right."
"I always thought Ayu's voice was a touch too high-pitched, but now I'm starting to wonder whether I was judging her too harshly."
"I never realized, until today, just {i}how{/i} gifted a singer Ayu is."
"She holds one arm aloft as she sings, a pure, guileless smile upon her face."
"The wind stirs at Ayu's hair, so it shifts about her shoulders."
"Her violet eyes, meanwhile, seem to be sparkling."
"Ayu looks completely in her element, standing upon the stage as she is."
"Her confidence is overwhelming: so much so, I can't tear my eyes away from her, and I'm not the only one."
"The kids in the audience, too, are all staring at Ayu, their mouths open."
"They were cheering pretty loudly before Ayu began to sing, but now she's begun, they've all fallen quiet."
"Nobody talks while Ayu sings."
"I don't think anybody's even {i}thinking{/i} of talking."
"Ayu's singing really is captivating."
"There's something warm about Ayu's voice: something sweet and gentle."
"Listening to it makes me feel protected."
"It's been a long, long time since I felt this relaxed."

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
scene skyd with wiperight_slow
play music "bgm/succubus_slife_of_life_1_loop.ogg" fadein 1.0
window show dissolve

"Time wears on, and the park eventually closes."
"When this happens, I have to leave, alongside my assorted group of succubi, plus one European princess and her ever-dutiful maid."
"Yue wishes me a farewell and returns to the succubus realm, after pressing a quick kiss against my cheek."
"Ayu, Cosmos, Stephania, Elizabeth and I, meanwhile, have to take a train back into central Tokyo, where we all live."
"We wait at the station for about ten minutes until a train arrives, and then we board it, alongside an influx of other guests from the park: all of us spent after our busy day."
"Elizabeth and Stephania sit together, as do Ayu and Cosmos."
"I sit apart from them, and smile while I watch them."
"Stephania is engaged in an animated discussion with Elizabeth about all the rides she went on, and the delicious food she ate, and all the fun she had."
"She's so excited, I can hear her even above the rumbling of the train."
Stephania "Theme parks really are amazing!"
Stephania "I am so glad I was afforded the opportunity to visit one! I never thought I would be able to have such an experience: not while I was growing up in the palace."
Stephania "For once, I feel like an ordinary woman - but, goodness, it is liberating!"
Stephania "Being ordinary has never been more fun!"
"I would have to question Stephania's self-proclaimed \"normalcy\", given she's pontificating about her aforementioned \"normalcy\" to her maid, but I don't cut into her conversation."
"That would seem crass, particularly when she's having such a good time."
"As for Cosmos and Ayu, meanwhile...{w} Well."

window hide dissolve
$ achievement.grant("cozy_cat_nap")
if persistent.adult==True:
    scene cg10_a with wipedown_slow
else:
    scene cg10 with wipedown_slow
$ renpy.pause()
window show dissolve

Ayu "Mm, nn... Zzz..."
Cosmos "Zzz, mm... Meow..."
"They're both fast asleep."
"Ayu's head is resting upon Cosmos's shoulder, while Cosmos's cheek is pressed against Ayu's forehead."
"Ayu's lips are pursed, almost as though she's awaiting a kiss, and her long lashes practically seem to melt together."
"Cosmos's lips, meanwhile, are curved into a small smile."
"The train judders back and forth, the wheels screeching on the metal tracks, but..."
Ayu "Mm, nn..."
Cosmos "Meow..."
"Neither of them stir."
"Now, this is quite the curious sight. I've never seen Ayu cuddled up so closely to Cosmos: not of her own volition, at least."
"If she were awake, there's no way Ayu would stand for this."
"I can easily imagine her springing away from Cosmos, her brow furrowed, an angry cry of..."
Ayu "{i}A-As if I'd {/i}ever{i} cuddle up to you, y-you idiot! I don't want to catch your fleas, or worse!{/i}"
Ayu "{i}For all I know, you might have rabies, you stupid, good-for-nothing catgirl! Get away from me!{/i}"
"Ayu isn't being her usual, aggressive self right now, however. Not even she can maintain her perpetual pissiness when she's passed out, I suppose."
"Right now, cuddled up together like a pair of kittens in a basket, they really do look like best friends..."
"Though I know Ayu, of course, would be infuriated that such a thought ever crossed my mind."
"I'll keep this to myself, so as not to incur the future, awoken Ayu's wrath, but..."
Ayu "Mm, nn..."
Cosmos "Zzz, mm... Meow..."
"They look rather cute together."
Hiroki "And you say you don't like Cosmos, Ayu..."
"I murmur to myself, amused by this turn of events."
Hiroki "I'm sure you must like her deep down. This proves it."
"Compelled by some devious impulse, I fish my phone out of my pocket, then angle it at the pair of sleeping besties."
"I open up my camera function, shift back a little in my seat, then click."
"There."
"Now I have photographic proof of Cosmos and Ayu's closeness saved on my phone for future posterity."
"I've no plans of actually showing this photo to Ayu (I don't want her scratching my eyes out), but she looks so cute right now, it'd be a shame to let the moment pass without commemorating it in some way."
"{i}I'll{/i} always remember this moment, at least, even if Ayu won't."
"I don't want to forget today's events, nor how much fun we've all had together."
"I'm not a big fan of theme parks, but I really did enjoy myself - and I'm enjoying myself all the more, now, after seeing Ayu and Cosmos getting along so well."

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
play music "bgm/succubus_pensive_loop.ogg" fadein 1.0
scene skyn with wiperight_slow
window show dissolve

"The train eventually pulls into our station, and when it does, I rise to my feet; stretching, so my joints click."
"Then, I step off the train, alongside Stephania and Elizabeth."
"Cosmos and Ayu remain on the train, still sitting together, though they've both since awoken from their shared sleep."
"They both live a little further down the line, so they don't join us, though we do share our quick farewells."
"The doors of the train close behind me with a hiss, and then it departs, taking Ayu and Cosmos deeper into the heart of Tokyo."
"Flanked by Stephania and Elizabeth, I wend my way back home, to my cruddy, run-down apartment."
"The sun has well and truly set at this point, and the streets through which I walk are dark: illuminated by the artificial orange glow of the street lamps and the moon which hangs overhead."
"My footsteps fall against the ground with a series of discordant thuds, which mingle with the sharp strikes of Elizabeth's heels."
"Stephania was animated enough on the train, as she chattered nineteen-to-the-dozen with Elizabeth, but I think her energy is beginning to run out."
"She yawns, one hand pressed to her mouth, and her body lists to one side."

scene street_n
$ lface='serious'
$ lbody='maid1'
$ sface='sad'
$ sbody='cas1'
call s_stefeli from _call_s_stefeli_322
$camera_move(400,300,200,0,0,'dissolve')
with wipedown_slow

Elizabeth "Careful, milady."
"Fortunately, Elizabeth is there to catch her, as any good maid ought, before she can careen to the ground."
$ lbody='maid2'
show lizzie flip at c4
Elizabeth "We do not have long to go now. Do try to hang in there."
$ sface='worried'
show steffy at c2
Stephania "O-Oh, yes. My apologies, Lizzie. I do not mean to make you worry for me. I am just... Aaah..."
"Stephania yawns again, more tears beading in the corners of her eyes."
$ sface='sad'
$ sbody='cas2'
show steffy at c1
Stephania "So very tired."
$ lface='angry'
show lizzie flip at c2
Elizabeth "You pushed yourself too hard, milady."
$ lface='serious'
show lizzie flip at c1
Elizabeth "You went on rather too many rides in too short a space of time. It is no wonder that you would be tired."
$ lbody='maid1'
show lizzie flip at c3
Elizabeth "While working too hard is a phenomena everybody is aware of, it is possible to play too hard, too."
Elizabeth "You are not accustomed to cutting loose, so of course you would be weary, after a day spent having so much fun."
$ sface='shy'
show steffy at c4
Stephania "Yes, you might be right. I {i}was{/i} running around an awful lot, ehehe."
$ sface='sad'
show steffy at c3
Stephania "My feet are somewhat sore..."
$ lface='smile'
show lizzie flip at c2
Elizabeth "Would you like me to give them a massage once we return?"
$ sface='shock'
show steffy at c1
Stephania "Would you do that, Lizzie?"
$ lbody='maid2'
show lizzie flip at c1
Elizabeth "For you, milady?"
show lizzie flip at c3
Elizabeth "Of course. There is nothing I would not do for you. You are very dear to me. I wish for nothing save your happiness..."
$ lface='serious'
show lizzie flip at c2
Elizabeth "Though I am aware, of course, that your newfound happiness is largely contingent upon Mr. Ogsawara's."
$ lbody='maid1'
show lizzie flip at c4
Elizabeth "That being the case, I would not be averse to the idea of massaging your feet too, Mr. Ogasawara, would you wish it."
Hiroki "What? Oh, uh..."
"I glance away, a little flustered by Elizabeth's earnest entreaty."
"It seems a bit silly, really, to get so worked up over such a statement, when I've engaged in all manner of intimate relations with all manner of women, but I don't think I've ever had a foot massage before."
"It sounds kind of intimate."
"Is this something I'd be interested in...?"

window hide dissolve

menu:
    with dissolve

    "I'd rather not.":

        window show dissolve

        $ succ_points -= 2

        Hiroki "I-It's alright. I wouldn't want to put you out..."
        $ lface='smile'
        show lizzie flip at c3
        Elizabeth "It is no bother. I would not offer if it was."
        Elizabeth "Though you are not complaining, I am sure your soles must be aching, too. You did a lot of walking yourself, just as milady and I did."
        $ lbody='maid2'
        show lizzie flip at c1
        Elizabeth "You are dear to milady and, as such, your health is very important. Therefore, I wish to offer you the same services I mean to offer to milady."
        $ lface='happy'
        show lizzie flip at c4
        Elizabeth "Now, your feet. Will you let me rub them?"
        Hiroki "Th-That's such a sudden proposition! I need some time to think about it..."
        "And I need some time to control the rapid beating of my heart, too."
        "Wh-Why do I feel so bashful?!"
        "Maybe my mind was swapped out, on the sly, with that of a teenage girl's..."
        "Though in what scenario, I wonder, would a teenage girl be offered a foot massage?"
        "I wonder..."
        $ sface='smile'
        show steffy at c2
        Stephania "If you are anxious, Hiroki, you needn't be."
        Stephania "Lizzie is very, very good at giving foot massages. When she touches me, it feels as though my worries are melting away."
        $ sface='smile2'
        show steffy at c4
        Stephania "Why, I can hardly think of anything else when her hands are upon me!"
        "Yeah, that's kind of the issue. I'm afraid, if I relax into Elizabeth's ministrations too much, it'll cause troubles."
        "I don't want to get off on having my feet touched! That's, like, way too degenerate, isn't it - or is it?"
        "Maybe I'm being judgmental..."
        $ lface='smile'
        show lizzie flip at c3
        Elizabeth "Thank you, milady. You are too kind. I am glad you, at least, appreciate my services."
        $ sface='happy'
        show steffy at c3
        Stephania "I appreciate everything about you, Lizzie. I love you!"
        $ lbody='maid1'
        show lizzie flip at c1
        Elizabeth "I am most grateful to hear it. I love you, too."
        $ lface='sad'
        show lizzie flip at c2
        Elizabeth "I only hope Mr. Ogsawara will grow, one day, to trust me as you do - and to entrust me, too, with his feet."
        Hiroki "Now, why are you so hung up on my feet? You don't have a fetish, do you?"

    "I wouldn't mind.":

        window show dissolve

        $ succ_points += 2

        Hiroki "I wouldn't mind, I guess, but I'm not sure why you seem so enthused."
        Hiroki "You don't have a foot fetish, do you, Elizabeth?"

$ lface='shy'
show lizzie flip at c1
Elizabeth "Not that I know of. My only fetish is serving others, and making them feel good..."
$ lface='happy'
show lizzie flip at c3
Elizabeth "Though, if I get to place my hands all over your cute soles in the process, I would consider it a victory."
Hiroki "\"Cute\"...?"
"That's the last word I'd use to describe feet: my own in particular."
"Geez. I can't tell if Elizabeth is teasing me or not. It's hard to tell when her tone is so impassive."
Hiroki "This is all kinds of weird. I've never met a woman so desperate to stroke my toes before..."
"I shake my head, bemused, and resume my walk to my apartment."
"We're not too far away, now - there's only about five minutes to go - and I feel, despite the strange trajectory of my conversation with Elizabeth, fairly relaxed."

stop music fadeout 1.0

"I'm ready to head back inside and get some much needed shut-eye, when..."

play music "bgm/sak_suc_alice_loop.ogg" fadein 1.0

$ sface='sad'
show steffy at c2

Hiroki "...!"
"Not for the first time, I feel a shiver run down my spine."
"I've felt this way before - and recently, too."
"This is the same sensation that assailed me back at the park, when Cosmos, Elizabeth, and Stephania were sipping on their bubble tea."
"It feels like there's somebody - or something - watching me: something with a truly terrifying presence."
$ lface='serious'
show lizzie flip at c2
Elizabeth "Mr. Ogasawara...?"
$ lface='sad'
show lizzie flip at c1
Elizabeth "Is something the matter? You are not that unnerved at the prospect of me touching your bare toes, are you?"
Hiroki "What? O-Oh, no..."
"If I'm being honest, my feet were the last thing on my mind this last half a minute. The unpleasant sensation which spread through me put all other thoughts from my mind."
"I still feel out of sorts, but..."
Hiroki "..."
"Though I cast my gaze this way and that, I can't see anything which might be causing my discomfort."
"The street is full of shadows, true, which would make perfect places for any interlopers to hide, but I can't detect even the faintest flicker of movement."
"The uncomfortable coldness inside my veins, meanwhile, already seems to have thawed."
"Was I imagining things?"
"I hope hope so."
"There mightn't be any genuine, physical threat, but the lingering \"what if\" has left me feeling tense and edgy."
"What in the world am I getting so worked up about?"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene skyd with clockwipe
window show dissolve

"The following morning..."

play music "bgm/succubus_slife_of_life_1_loop.ogg" fadein 1.0
scene mc_room with wipedown_slow

Hiroki "Nn, mm... Ah...?"
"I awake uneasily from my slumber, after sojourning - or so it felt - in a roiling pit of anxious, uncomfortable dreams."
"I don't remember what I was dreaming about, precisely, but a lingering sense of unease clings to me."
"Though last night passed uneventfully enough, after that sharp spike of anxiety I felt while walking back to my apartment, I still feel tense."
"Not even eight hours' worth of sleep was enough to soothe me."
"Why do I feel so disoriented?"
"My head is throbbing, and it feels oddly fuzzy. My thoughts, meanwhile, are all in a muddle."
"When I swallow, I can taste something akin to iron on my tongue."
"Gross."
"I need to brush my teeth - and my hair, too."
"I sweated a little while I was asleep, too, and my night shirt is clinging uncomfortably to my skin."
"With aching limbs and a dully throbbing skull, I sit up in my futon then glance around."
"Elizabeth, I imagine, will be in the kitchen, working on breakfast."
"As for Stephania, meanwhile..."
Hiroki "Hmm..."
"It's strange that she isn't here."
"She woke me up these last two mornings without fail, smiling as she did like an angel."
"I guess she might have gone to have a shower early, though."
"That makes perfect sense, but..."
Hiroki "..."
"For some reason, Stephania's absence feels kind of ominous."
"I can't help but worry that something is awry - but, no, I try to tell myself, I'm being foolish."
"I shouldn't worry so much."
"{i}Nothing{/i} is wrong."
"That brief feeling of icy discomfort I felt last night was nothing more than baseless paranoia. It has nothing to do with Stephania's disappearance, not that she's disappeared."
"She can't have."
"That's what I try to tell myself, at lest, but..."

stop music fadeout 2.0

Hiroki "Oh...?"
"It's as I'm looking about my room that I notice it."
"There's an envelope lying on the top of Stephania's futon: an envelope with neatly-penned characters on it that read \"Ogasawara Hiroki\"."
"How strange."
"Did Stephania leave me a note?"
"I suppose I'll never know until I take a look, but this handwriting doesn't resemble Stephania's."
"I take the envelope with trembling fingers, then slice it open with my fingernails."

play music "bgm/spooky_loop.ogg" fadein 1.0

"Gently, I lever a letter out of the envelope's interior, then scan through it."
"I process the black characters arranged upon the perfectly white paper, my brow furrowing, and then..."
Hiroki "No way..."
"A startled gasp falls from my lips."
"I can hardly believe it."
"I don't {i}want{/i} to believe it."
"It doesn't feel real, but the critical lack of Stephania in my bedroom lends this letter some credence."
"If Stephania really was here, she would've woken me up."
"She would've wished me good morning, like she did yesterday, and the day before that."
"She would've smiled to me, and she would've thanked me for showing her such a good time yesterday - but, of course, Stephania didn't do any of those things."
"She couldn't - because she isn't here."
"She's been kidnapped."

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
play music "bgm/succubus_pensive_loop.ogg" fadein 1.0
scene kitchen
$ lface='surprised'
$ lbody='maid1'
call s_lizzie from _call_s_lizzie_1231
$camera_move(0,400,300,0,0,'dissolve')
with wiperight_slow
window show dissolve

Elizabeth "Kidnapped...?!"
"Elizabeth stares at me with wide, surprised eyes from the other side of the kitchen table."
"I've since shown Elizabeth the ransom note, and after scanning through it, Elizabeth now looks aghast, and for good reason."
"Her skin, which was already pale, looks positively ghostly: so pale, it reminds me of paper."
"Elizabeth's fingers are gripping the note so tightly, I'm worried she might tear it - and, fearful she might render the instructions written upon it unintelligible, I reach forwards, to tug it smartly from her grasp."
"The note does look a little crumpled, but other than that, it's not too worse for wear."
"I can still see all the most important information written upon the note: namely, that whoever left it has Stephania in their grasp, in an abandoned warehouse by a wharf in Yokohama."
"The kidnapper (or kidnappers, I suppose. There could be more than one of them) wants me to meet them at this warehouse, as specified in this note, later this night, at 21:00."
"The note is very clear, too, that I am to arrive at this rendezvous point alone."
"{i}I want you, Ogasawara Hiroki, to come and see me,{/i} the note specifies, {i}and only you. If you bring anybody else, the princess will pay. Do not force my hand. I have no desire to use violence.{/i}"
"{i}This unpleasant affair can be resolved peaceably - of that, I promise you - so long as you heed my instructions.{/i}"
"The note goes on to specify that I should appear at this abandoned warehouse with a significant sum of cash on my person."
"After handing this cash over to the kidnapper/s, they will let Stephania go free."
"As far as kidnapping scenarios go, it seems fairly standard, not that I know very much about kidnappings. I've never been in a situation like this before."
"I {i}have{/i} seen similar scenarios in movies, though."
"This really does sound like a plot of some bad action movie."
"The contents of the note itself were particularly cliché: so much so, I might've been tempted to consider this whole thing an elaborate prank, if Stephania really wasn't missing."
"That's proof enough, if nothing else, that whoever left this note was being serious: perhaps lethally so."
"What will they do, I can't help but worry, to Stephania? Will she be alright?"
"I'm painfully aware, with every passing second, that Stephania must be at the mercy of these mysterious brigands. I'm sure she must be terrified."
"I want to save Stephania more than anything else, but I'm worried, if I don't heed the letter, I'll only serve to put her in further danger."
"Stephania's welfare is on the line here. I can't afford to screw things up."
"Any wrong move on my part could well prove to be disastrous."
"I need to think about this calmly and logically, but Elizabeth seems too worked up to think about things in terms like that."
$ lface='sad'
show lizzie at c4
Elizabeth "How could this happen...?"
$ lface='surprised'
show lizzie at c1
Elizabeth "How could I have let milady be kidnapped?!"
$ lbody='maid2'
show lizzie at c3
Elizabeth "I'm supposed to be her top maid! Looking after her is my duty! If I cannot do that much, then how much worth do I have?"
Elizabeth "For all I claim to love milady, I truly am a failure!"
$ lface='sad'
show lizzie at c4
Elizabeth "I will never forgive myself for this: not for as long as I live..."
$ lface='angry'
show lizzie at c2
Elizabeth "But all is not lost. I can get her back, and I {i}will{/i}."
Elizabeth "If it is a confrontation this kidnapper wants, then I am not afraid to grant them it! I will not let them intimidate me, despite all of their cowardly threats!"
$ lface='surprised'
show lizzie at c1
Elizabeth "I am not afraid!"
$ lbody='maid1'
show lizzie at c3
Elizabeth "I will storm into their hiding place, and I will retrieve milady using any means at my disposal!"
Elizabeth "Please wait for me, milady! I won't let you suffer on your own!"
"Elizabeth strides forth, perhaps meaning to exit my apartment, but I stop her before she can retreat: resting a restraining hand upon her shoulder."
Hiroki "Whoa! Easy there, Elizabeth. Let's not do anything hasty!"
Hiroki "Can't you take a few deep breaths? We need to think about this logically."
$ lface='serious'
show lizzie at c4
Elizabeth "{i}Logically?{/i}"
"Elizabeth scowls."
$ lface='angry'
show lizzie at c2
Elizabeth "How can I think about {i}anything{/i} logically, Mr. Ogasawara, when milady is missing?"
Elizabeth "For all we know, her kidnappers might be subjecting her to unspeakable torture even as we stand here!"
Elizabeth "We are doing nothing save wasting time!"
$ lface='surprised'
show lizzie at c1
Elizabeth "If you can afford to take deep breaths, then you are clearly not regarding this situation with the degree of seriousness it deserves!"
$ lbody='maid2'
show lizzie at c4
Elizabeth "For shame, Mr. Ogasawara, but I thought you {i}cared{/i} about milady!"
Hiroki "I {i}do{/i} care about her! I care about her immensely! That's why I'm asking you to slow down, and to reconsider!"
Hiroki "There's no guarantee that Stephania is being tortured right now-"
"Grim though it might sound, I'd presume her kidnappers would want to keep her in one piece, at least, until they receive the ransom money."
Hiroki "-but she really {i}might{/i} be in danger if we ignore the warnings in this letter and we both go flying to her rescue!"
Hiroki "The letter states that {i}I'm{/i} the only one who's to meet her! Something awful might happen if we don't heed it!"
$ lface='sad'
show lizzie at c3
Elizabeth "What? But then..."
$ lface='worried'
show lizzie at c2
Elizabeth "What are we do to? How are we supposed to rescue milady?"
Hiroki "We need to give it some thought. I don't much like the idea of hanging around waiting either, so how about this?"
Hiroki "I think we should go and see Marina."
$ lface='serious'
show lizzie at c1
Elizabeth "Miss Wakatsuki, you mean?"
Hiroki "That's right."
Hiroki "Marina's pretty smart. She knows her stuff. If anybody can give us advice, she can..."
"And, I think, if there's really no way to save Stephania, beyond bowing to the kidnappers' whims, then Marina should be able to help us procure the money they asked for."
"I don't much like the thought of rewarding these kidnappers for their wicked scheme, but playing along with them might be the only option available to us."
"The amount of money they requested is truly eye-watering (at least, it is to a poor nobody like myself), but Stephania's welfare is far more important."
"Like Elizabeth herself said, I'm prepared to do anything for her sake."
"The money is no object."
"I just want to ensure that Stephania's alright."

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
play music "bgm/succubus_slow_jazz_loop.ogg" fadein 1.0
scene office
$ mface='serious'
$ mbody='cas1'
$ lface='serious'
$ lbody='maid1'
call s_mariliz from _call_s_mariliz_1
$camera_move(400,300,200,0,0,'dissolve')
with wiperight_slow
window show dissolve

Marina "A kidnapping, hmm?"
"Marina surveys Elizabeth and I from across her desk, her fingers steepled together and her green eyes narrowed."
"Elizabeth and I made a beeline for Marina's workplace after discussing the contents of the ransom note we received."
"After announcing my name to the well-dressed woman at the reception desk, we were soon ushered into Marina's office."
"Marina, fortunately, wasn't in the midst of a meeting, and she welcomed Elizabeth and I genially enough."
"Now, the three of us are sitting together in her plush, high-profile office, located at the very top of a tall building."
"The walls of Marina's office are largely comprised of glass, and beyond them I can see Tokyo spread out beneath me like a diorama."
"The view from Marina's office is breath-taking, and her office itself is awfully fancy."
"It's been a long while since I last found myself in Marina's office, and back then, I didn't have much of an opportunity to look around."
"I was more distracted, instead, with other, more... {w}carnal, shall we say, matters."
"Carnality is the last thing on my mind right now, however, as I survey Marina."
"Marina {i}does{/i} look very attractive in her suit (it's been a while, I think, since I saw her in that get-up), but that's not important right now."
"Neither is Marina's fancy office."
"I'm too worried about Stephania to pay anything else much attention."
$ mface='angry'
show marina at c4
Marina "Dear me. This {i}does{/i} sound like a thorny situation. I can well understand why you are so concerned."
Marina "I know that you care for Stephania a good deal - and I know, too, that Hifumi is very fond of her."
$ mface='serious'
$ mbody='cas2'
show marina at c1
Marina "She would be devastated if any harm were to befall her, as would I."
$ mface='sad'
show marina at c4
Marina "Stephania is a good girl, even if she is a bit of an airhead, and she does not deserve to suffer."
$ lface='surprised'
show lizzie at c4
Elizabeth "Indeed, she does not!"
$ lface='sad'
show lizzie at c3
Elizabeth "That being the case, would you please help us? I do not like to make demands upon others - it is unseemly behavior for a maid - but this matter, I fear, is urgent!"
Elizabeth "Milady's life may well hang in the balance!"
$ lface='worried'
$ lbody='maid2'
show lizzie at c1
Elizabeth "I could not bear it if she was to suffer!"
$ mface='angry2'
show marina at c3
Marina "And do you think I could?"
$ mface='angry'
show marina at c2
Marina "My enemies might think me cold and calculating, but I am not devoid of human emotions. I, too, am rather fond of Stephania, as I believe I mentioned already."
$ mface='sad'
$ mbody='cas1'
show marina at c1
Marina "I do not want any harm to befall her."
$ mface='angry'
show marina at c4
Marina "That being the case..."
"Marina ponders, while crossing one long, lithe leg over the other beneath her desk."
$ mface='serious'
show marina at c3
Marina "I can lend you some money, if you wish, to pay for Stephania's safety. How much did the ransom note specify?"
"I tell Marina the exact number, and she nods."
$ mbody='cas2'
show marina at c2
Marina "That should not be too hard to procure."
Hiroki "Are you sure?"
Hiroki "The kidnapper - or kidnapper{i}s{/i} - asked for a pretty hefty sum..."
$ mface='angry'
show marina at c1
Marina "Indeed, they did - or, at least, they would have, if they had kidnapped a commoner."
$ mface='serious'
show marina at c4
Marina "For a princess, however, the sum is a paltry one: almost curiously so."
Marina "The precise amount of money they demanded is so low, in fact, when contrasted with Stephania's worth, it makes me wonder whether these kidnappers know that they're doing."
Marina "They must be green when it comes to business negotiations."
$ mface='angry2'
show marina at c3
Marina "If they were sitting before me in the boardroom, I would make short work of them."
$ mface='serious'
show marina at c2
Marina "They are hopeless novices, really - and, worse still, they are cowards."
Marina "The money they asked for is but a pittance to a woman of my caliber, but I cannot say I like the thought of rewarding them for their underhanded behavior."
$ mface='angry2'
show marina at c1
Marina "They deserve nothing from me save my scorn."
$ mface='serious'
$ mbody='cas1'
show marina at c3
Marina "While I will give you the money the kidnappers asked for - I will prepare it in a briefcase, in fact, for ease for transportation - I do not intend for this ne'er-do-wells to keep the cash."
Hiroki "What are you suggesting, then...?"
$ mface='angry'
show marina at c2
Marina "I have been devising something of a plan, while we have been sitting here, having this less-than-pleasant conversation."
"So saying, Marina toys with a lock of her pale, silvery hair; twining it about her finger."
$ mface='serious'
show marina at c4
Marina "I have given the matter some thought, and I have decided that I would like to aid you in Stephania's rescue in a more immediate manner, beyond loaning out some money."
$ mbody='cas2'
show marina at c1
Marina "I would like, too, to accompany you to the warehouse where she is being held, to protect her, if need be."
Hiroki "Would you really be willing to do that?!"
$ mface='smile'
show marina at c3
Marina "Naturally."
$ mface='serious'
show marina at c4
Marina "I am sure Ayu and Cosmos would be willing to come along, too, if I asked them."
$ mface='angry'
$ mbody='cas1'
show marina at c2
Marina "Hazel and Hifumi are too busy, unfortunately, and I would not wish to unduly worry Hifumi by informing her of this incident."
Marina "Hifumi is a sweetheart, and knowing that Stephania is in danger would only worry her."
$ mface='serious'
show marina at c1
Marina "Her help should be not be necessary, however."
Marina "With the aid of us three succubi, we should be able to overpower the kidnappers, and retrieve the money - which you would first hand to the kidnappers, of course, as a decoy, Hiroki."
$ mface='smile'
show marina at c3
Marina "How does that sound?"
Hiroki "It sounds like a solid enough plan, if Ayu and Cosmos agree to it, but..."
"I glance over at Elizabeth."
"Didn't Marina let something pretty confidential slip there?"
"She just out and announced herself as a succubus, alongside Ayu and Cosmos!"
"I thought that was supposed to be a secret!"
"I wait on tenterhooks for the moment that Elizabeth, aghast, stares at Marina, and says, \"Egads! What are you {i}really{/i}?\", and yet..."
$ lface='serious'
$ lbody='maid1'
show lizzie at c4
Elizabeth "That sounds like a good plan to me, too."
"Elizabeth nods, her expression unsurprised and unchanging."
"Did she not register that bombshell Marina just dropped?"
"Perhaps she's so concerned about Stephania's welfare, she can't focus on anything else?"
"That'd make sense, I guess, but I thought this revelation that succubi do, in fact, exist, would make a bit more of an impact on her."
Hiroki "Hey, Elizabeth, did you catch what Marina just said?"
$ lface='angry'
show lizzie at c3
Elizabeth "That she would aid me in finding milady? Yes, indeed, I heard it: loud and clear."
Hiroki "No, not that part. I meant more, uh..."
"Now, how can I phrase this?"
"I don't think there's any delicate way to put it, so I guess I'll just throw it out there."
Hiroki "I was talking about the succubus thing."
$ lface='serious'
show lizzie at c2
Elizabeth "Ah, yes. I heard that, but worry not. It comes as no surprise to me."
Hiroki "Are you sure? Most normal people would be freaking out right now, if they heard that succubi exist."
$ lbody='maid2'
show lizzie at c1
Elizabeth "Perhaps most \"normal people\" would, Mr. Ogasawara, but you forget that I am {i}not{/i} normal."
$ lface='smile'
show lizzie at c4
Elizabeth "As milady's indomitable, unflappable maid, it is my duty to take such information, no matter how shocking, in my stride."
$ lface='angry'
show lizzie at c3
Elizabeth "I lost my head before, upon learning that milady was in danger, but I will not let that happen again."
Elizabeth "I will not let {i}anything{/i} disturb me, in my quest to get her back."
$ lface='serious'
show lizzie at c2
Elizabeth "Nothing matters more to me than milady's safety - and, in any case, I already knew that Miss Wakatsuki was a succubus."
$ mface='neutral'
show marina at c4
Marina "Did you, indeed?"
$ lbody='maid1'
show lizzie at c4
Elizabeth "Yes, that is correct."
Elizabeth "The scent of a succubus is unmistakable. It was quite apparent, the moment you stepped foot in Astoria's palace."
$ lface='angry'
show lizzie at c1
Elizabeth "You, and Miss Yamamoto, and Miss Williams..."
$ lface='serious'
show lizzie at c2
Elizabeth "Miss Ikue, too, and Miss Moretti: you are all succubi."
$ lbody='maid2'
show lizzie at c4
Elizabeth "I know. It is no big surprise. Please, do not expect me to gasp in horror, else you will be gravely disappointed."
$ mface='grin'
show marina at c2
Marina "Heh. Well. I thought as much. I knew you were very astute."
$ mface='neutral'
show marina at c1
Marina "Now, I suppose we might as well bring our little tête-à-tête to an end here - but, before that, I have a proposition I would like to make."
$ lbody='maid1'
$ lface='worried'
show lizzie at c3
Elizabeth "And this proposition is...?"
$ mface='happy'
show marina at c3
Marina "My, my! Do not look so mistrustful, please! It would be quite beneficial, I assure you, to all parties."
$ mface='grin'
$ mbody='cas2'
show marina at c2
Marina "You see..."
"Marina smiles, while continuing to toy with her hair."
$ mface='smile'
show marina at c1
Marina "Though we succubi are stronger than ordinary humans, it is still possible for us to be overpowered."
$ mface='serious'
show marina at c3
Marina "With myself, Ayu, and Cosmos present, we should be able to triumph over our adversaries, whoever they may be, but there is always a chance things might go awry."
$ mbody='cas1'
show marina at c2
Marina "Perhaps you are aware of this already, Elizabeth, but we succubi divine much of our strength from... {w}intimate, shall we say, relations with humans."
$ mface='angry'
show marina at c1
Marina "It has been a while since I last indulged myself, and I fear I am not in peak physical condition."
$ mface='grin'
show marina at c4
Marina "This could soon be altered, however, if either you or Hiroki - or both of you! - deigned to spend some quality time with me."
Marina "What do you say?"
$ mface='serious'
show marina at c2
Marina "I know now mightn't be the best time, given you must be worried about the princess, but I am suggesting this for Stephania's sake."
$ mface='angry'
show marina at c1
Marina "If I do come to blows with her kidnappers, I would prefer to do so when I am in optimal form."
Marina "I do not wish to be weakened before a fight. That might impact our chances at retrieving Stephania."
$ lface='serious'
show lizzie at c5
Elizabeth "Hmm..."
"Elizabeth ponders Marina's words for a few moments before, after a pause, she nods."
$ lbody='maid2'
show lizzie at c3
Elizabeth "Very well. If what you are suggesting would aid milady, then I have no option but to consent."
Elizabeth "I, too, wish for nothing save her safety. It is my highest priority."
$ lface='angry'
show lizzie at c1
Elizabeth "I am prepared to perform any task for her sake: indulge in any vice."
$ lface='surprised'
show lizzie at c2
Elizabeth "I will stop at {i}nothing{/i} to get her back."
$ mface='happy'
show marina at c4
Marina "Very good! I like that answer. It is very decisive, and it is full of passion."
Marina "I can see that any entanglement with you would be most diverting... {w}and who knows?"
$ mface='grin'
show marina at c5
Marina "Perhaps it will help to assuage your worries, if only for a few brief moments."
$ lface='serious'
show lizzie at c4
Elizabeth "Perhaps it will. That remains to be seen. I am not, however, consenting because of my own enjoyment."
Elizabeth "I would never normally pursue my own pleasure while milady is in danger."
$ lbody='maid1'
show lizzie at c3
Elizabeth "I am doing this for her."
$ mface='smile'
show marina at c3
Marina "But of course. I would never dare to question otherwise."
$ mface='grin'
show marina at c2
Marina "Now, what do you say about this arrangement, Hiroki? Would you care to join us?"
"I know what Marina's getting at, of course - she's not being exactly subtle - but I'm not sure how I feel right now."
"Do I want to join in...?"

window hide dissolve

menu:
    with dissolve

    "Of course I do!":

        window show dissolve

        $ succ_points += 6

        "...Well, that's a no brainer. It doesn't require much thought at all on my part."
        Hiroki "Of course I'd like to help. I've no issues with this arrangement."
        Hiroki "Now, let's get down to business."

        if persistent.adult==True:
            jump adult4
        else:
            jump merge4

    "I'm not in the mood.":

        window show dissolve

        $ succ_points -= 6

        "I know Marina means well, but I can't bring myself to do this."
        "I'm just not in the mood."
        "I'm far too worried about Stephania to think about anything else."
        "I just hope she'll be alright."
        "Otherwise, I have no idea what I'm going to do."

        jump merge4

label merge4:

    stop music fadeout 1.0
    window hide dissolve
    scene black with wiperight_slow
    $ renpy.pause(0.3)
    scene skyn with wiperight_slow
    window show dissolve

    "Later that night..."

play music "bgm/spooky_loop.ogg" fadein 1.0
scene factory_ex
$ aface='disgusted'
$ abody='succ1'
$ cface='neutral'
$ cbody='succ2'
call s_ca from _call_s_ca_2
$camera_move(400,300,200,0,0,'dissolve')
with wipedown_slow

Ayu "Urgh. This place is, like, seriously scuzzy. It's so dilapidated, and... Ew! Did I just see a {i}rat?{/i}"
$ cface='laugh'
show cosmos at c4
Cosmos "Did you? How lucky!"
$ aface='urgh'
show ayu at c2
Ayu "How is {i}that{/i} lucky, dummy? Since when were rats a sign of good luck?!"
$ cface='smile'
$ cbody='succ2'
show cosmos at c3
Cosmos "I think rats are cute. I like their twitchy noses and their little pink tails."
Cosmos "I wouldn't mind having a rat as a pet, actually."
$ cface='neutral'
show cosmos at c1
Cosmos "Maybe I could lure it out with some cheese..."
$ aface='angry'
show ayu at c4
Ayu "Do you have any cheese on you, Cosmos?"
$ cface='grin'
show cosmos at c4
Cosmos "Of course I do. I'm part Italian. I never go outside without some mozzarella in my pocket."
$ abody='succ2'
show ayu at c2
Ayu "Your succubus outfit doesn't {i}have{/i} any pockets, though."
$ cface='smile'
show cosmos at c3
Cosmos "Oh, yes. I suppose you're right, hehe."
$ aface='urgh'
show ayu at c1
Ayu "Geez. Try to take this a bit more seriously, please. This is a kidnapping case. Stephania could be in real danger!"

$camera_move(0,0,0,0,4,'ease')
$ mface='angry'
$ mbody='succ1'
call s_all from _Call_s_all_1

Marina "I concur. This is very serious indeed. This is no time for japery."
$ aface='grin'
show ayu at c4
Ayu "Pfft... \"Japery\"."
$ mface='angry2'
show marina at c2
Marina "And why, might I ask, are you laughing?"
$ aface='smug'
show ayu at c2
Ayu "Oh, there's no reason. I was just thinking, \"japery\" is such an old-fashioned word."
Ayu "You really {i}are{/i} an old lady, Marina!"
$ mface='shock'
show marina at c4
Marina "O-Old...?!"
"Marina scowls at Ayu, her expression twisting."
$ mface='angry2'
show marina at c3
Marina "W-We'll have less of that, young lady: not if you don't want a smacked bottom!"
Marina "I thought you yourself said this was serious!"

$camera_move(400,300,200,0,4,'ease')
hide ayu
hide cosmos
with dissolve

$ lface='serious'
$ lbody='maid2'
call s_mariliz from _Call_s_mariliz_3

Elizabeth "It {i}is{/i} serious. Please, put your petty squabbles to one side for now, and don't worry about the rats."
Elizabeth "Milady's safety is vastly more important."
$ mface='shy'
show marina at c4
Marina "Y-Yes, indeed... Ahem."
$ mface='angry'
show marina at c3
Marina "Now that we have all assembled here, we should be able to take on these kidnappers, whoever they may be."
Marina "Things might have been dicey with just you and I, Elizabeth, but Cosmos and Ayu should act as decent enough back-up."
$ mface='serious'
$ mbody='succ2'
show marina at c1
Marina "It is hard for ordinary humans to best one succubus, but with three of us, I don't much fancy our assailants' chances, however many of them there might be."
Marina "Our victory is all-but assured, but it doesn't do to be too confident."
Marina "There is always a chance there might be more people involved in Stephania's kidnapping than we are aware."
$ mface='angry'
show marina at c2
Marina "If this is an operation conducted by a large organization - say, the yakuza - then even we will have our work cut out for us."
$ mface='serious'
$ mbody='succ1'
show marina at c1
Marina "That being the case, let us go over our plan once more."
"Shrouded by the shadows of the abandoned warehouses that tower about us, Marina launches once more into a plan."

scene factory_ex:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 30.0 crop (400, 120, 1280, 720)
with wiperight_slow

"As far as plans go, it's pretty simple."
"The five of us - Marina, Ayu, Cosmos, Elizabeth, and I - came out here, to the rendezvous point delineated in that ransom note, to meet the kidnappers who took Stephania, and to negotiate with them."
"Marina, Ayu, and Cosmos have already changed into their succubus attire, and their silhouettes look rather imposing when framed against the moonlight."
"We've yet to enter the warehouse where Stephania is (supposedly) being held, but I know we'll have to do that eventually."
"It's the only way, after all, to get Stephania back."
"Our plan, when it comes to Stephania's retrieval, goes like this."
"I'm to go inside the warehouse first, alone, as was requested in the ransom note. I'll take with me a briefcase full of cash, which the kidnappers also requested."
"I'm to make a show of exchanging the money with the kidnappers and, when they're distracted, Elizabeth will creep into the warehouse to rescue Stephania."
"While this is occurring, Marina, Ayu, and Cosmos will arrive to back me up, and they'll take care of the kidnappers."
"I don't know how many people are behind this operation, but I hope there won't be too many of them."
"Even if there's, say, a dozen men hanging about in that warehouse, it shouldn't be too hard for my succubus companions to dispatch of them."
"I've not seen Marina or the others unleash the full extent of their powers before, but I've no doubts they're stronger than most ordinary people."
"They should be fine."
"I {i}hope{/i} they'll be fine, at least."
"With Stephania rescued and the kidnappers down for the count, it should be a simple enough matter to call the police, and let them take care of the rest."
"This way, we'll get to save Stephania, {i}and{/i} we'll be able to keep the money."
"I can't say I really relish the thought of heading into the warehouse on my own, but Marina said (and Elizabeth agreed) that this was the most sensible course of action."

scene factory_ex
$ mface='angry'
$ mbody='succ2'
call s_all from _call_s_all_132
$camera_move(0,0,0,0,0,'dissolve')
with wipeleft_slow

Marina "Remember, Hiroki: don't do anything to arouse the kidnappers' suspicion."
"Marina informs me, once she's finished going through our plan for the nth time."
$ mface='serious'
show marina at c4
Marina "If this plan is to succeed, we'll need the element of surprise on our side."
$ mbody='succ1'
show marina at c2
Marina "Let the kidnappers think you came alone, as per their note's stipulations."
Marina "If they see you - one unarmed young man - they should let their guards down. That's when we'll step in."
$ cface='laugh'
show cosmos at c2
Cosmos "We'll take them all down, no matter how many men there are! I'll go {i}bam, pow, hi-yah{/i}, like something from an action movie!"
Cosmos "You can all call me Bond, Cosmos Bond, hehe!"
$ aface='disgusted'
show ayu at c1
Ayu "I'm not calling you anything other than \"idiot\". Can't you keep your voice down?"
Ayu "Remember what Marina said. We need to be stealthy!"
$ cface='sweatdrop'
show cosmos at c4
Cosmos "I've never been very good at stealth missions in video games, hehe..."
$ cface='smile2'
$ cbody='succ2'
show cosmos at c3
Cosmos "But, roger. I hear you loud and clear, Ayu - or maybe \"soft and silent\"?"
$ cface='sad'
show cosmos at c1
Cosmos "I don't want Steffy to be hurt, so I'll do my best to stick to the script. I'll do everything to ensure her safety."
$ mface='serious'
show marina at c1
Marina "And we shall do everything we can to ensure {i}your{/i} safety too, Hiroki. You've nothing to worry about."
$ mface='angry2'
$ mbody='succ1'
show marina at c3
Marina "If any nasty miscreant dares to lay so much as a finger upon you, there will be a great reckoning."
Marina "I won't let any blackguard harm {i}my{/i} darling."
$ aface='evil'
show ayu at c4
Ayu "Heh. \"Blackguard\"."
"Once more, Ayu smirks: doubtless amused by this antiquated expression."
$ aface='grin'
$ abody='succ2'
show ayu at c2
Ayu "And you say you're {i}not{/i} an old lady. Everything that comes out of your mouth is, like, so uncool."
$ mface='sadist'
show marina at c4
Marina "I am {i}not{/i} old, and I will thank {i}you{/i} not to talk about what is cool and what is not."
Marina "Aren't {i}you{/i} the one who's being beaten in the charts by a woman who's on the wrong side of 30?"
$ aface='urgh'
show ayu at c1
Ayu "Urk..."
"Ayu winces at this, then presses a hand to her chest."
$ aface='shock'
show ayu at c3
Ayu "You didn't need to go there, Marina, you harpy! I'm still sore about the whole Shizuru thing!"
$ cface='shock'
show cosmos at c4
Cosmos "Really? You're sore about it?"
$ cface='neutral'
$ cbody='succ1'
show cosmos at c5
Cosmos "But I thought you said you didn't care, Ayu."
$ aface='angry'
show ayu at c2
Ayu "I {i}don't{/i} care! Shizuru's popularity doesn't bother me; not in the slightest!"
Ayu "I'm totally chill about it! I'm calm! I'm {i}fine!{/i} I'm not worrying that my career might be crashing and burning, so let's not even talk about it!"
$ aface='urgh'
show ayu at c1
Ayu "Everything's totally fine and dandy!"
$ cface='sweatdrop'
show cosmos at c2
Cosmos "Sure it is. Whatever you say..."


$camera_move(0,400,300,0,5,'ease')
hide ayu
hide cosmos
hide marina
with dissolve

$ lface='serious'
$ lbody='maid2'
call s_lizzie from _call_s_lizzie_3242

Elizabeth "I think we are getting off-topic again."
Elizabeth "Now that our plan has been successfully hashed out, I suggest we set it into motion."
$ lbody='maid1'
show lizzie at c2
Elizabeth "Would you be so kind as to enter the warehouse, Mr. Ogasawara, and parley with the kidnappers?"
Elizabeth "I can tell that milady is nearby, and I cannot - {i}will not{/i} - rest until she has been retrieved."
$ lface='sad'
show lizzie at c1
Elizabeth "Milady's safety is of the utmost concern to me."
$ lface='angry'
show lizzie at c3
Elizabeth "Everything else can wait."
Hiroki "R-Right."
"I face the abandoned warehouse which looms before me, with its water-damaged walls and its broken windows, and inhale."
"My fingers, which are resting at my sides, curl into fists."
"A few moments pass, during which I gather what little remnants of courage I possess, and then..."
Hiroki "I'll do it."
"I step forth, tightly clutching the briefcase full of money Marina bequeathed to me earlier, in her office."
Hiroki "Just you wait, Steffy. I won't abandon you: not to the mercy of these vile kidnappers."
Hiroki "We're all here, and we all want to rescue you."
Hiroki "I'm going to look after you: I promise."

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
scene factory with wiperight_slow
window show dissolve

Hiroki "Urgh. Ayu was right. This place really {i}is{/i} scuzzy..."

play music "bgm/sak_suc_alice_loop.ogg" fadein 1.0
scene factory:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 30.0 crop (400, 120, 1280, 720)
with wiperight_slow

"I glance about the warehouse's interior, all the while clutching the briefcase Marina gave me, as though it's some kind of lifeline."
"This old warehouse has a high, tall ceiling, which seems to amplify every single noise I make, no matter how quiet."
"The warehouse has stood abandoned for many years - though how many, exactly, I don't know - and the roof which towers above me is full of holes."
"Through these holes, rainwater has fallen, and the ground is scattered with foetid puddles."
"I step into one such puddle, which soaks the sole of my shoe, and my sock."
"I shudder to feel it, and try to suppress a hiss of surprise."
"I don't feel at all welcome here, but this, I guess, is to be expected. {i}Nobody{/i} should be here."
"I could probably get into legal trouble, I muse, while glancing about, for trespassing, if the authorities knew I'd come here, but the police are the last concern on my mind right now."
"I'm more fixated upon Stephania and her safety, and the status of the kidnappers."
"I've only taken a few steps into the warehouse, but I've not seen anybody suspicious {i}just{/i} yet."
"Is Stephania really here?"
"What about the people who held her captive?"
"I'm starting to second-guess myself."
"Did I come to the wrong place?"
"I take a few more steps into the darkness, my heart hammering inside my chest the whole while."
Hiroki "Ah..."
"Out of the corner of my eye, I see something scuttle in the shadows."
"Could it be a rat? Maybe several rats?"
"Ayu {i}did{/i} say she thought she saw one, back when we stood outside, on the wharf - and, unlike Cosmos, I don't think rats are cute."
"I'll have to side with Ayu on this affair."
"I think they're perfectly revolting."

scene factory with wipeleft_slow

Hiroki "Urgh..."
"I shudder again. It's so cold, my teeth are beginning to chatter."
"When I inhale, I can smell dirt and grime and rust."

stop music fadeout 1.0

"I turn a corner, skirting around a heap of old packing crates, my eyes wide in the oppressive darkness, and then..."

window hide dissolve
$ achievement.grant("in_a_bind")
play music "bgm/succubus_pensive_loop.ogg" fadein 1.0
if persistent.adult==True:
    scene cg11_a with wiperight_slow
else:
    scene cg11 with wiperight_slow
$ renpy.pause()
window show dissolve

Hiroki "Ah..."
"Finally, I spot Stephania."
"So, she really {i}is{/i} here."
"Stephania is sitting on a wooden chair, her arms and her legs tied together with lengths of coarse rope."
"Her expression is an anxious one, as well it might be, given her dire circumstances."
"She looks afraid but, fortunately, it doesn't seem like she's come to any physical harm."
"That's a relief, if nothing else."
"The kidnappers mustn't have done anything too vile to her - or, at least, I hope they haven't."
"Speaking of said kidnappers, I still can't see any trace of them, but I'm more concerned with Stephania's welfare right now."
"I dash over to her, then cry..."
Hiroki "Steffy! Are you alright?"
"This seems like a bit of a stupid question to ask, given the situation (it's obvious, just to look at her, that she isn't \"alright\"), but I feel obliged to ask it regardless."
"Stephania looks unscathed, for the most part, but I need to double check."
Stephania "H-Hiroki?! You came for me...?"
Hiroki "Of course I did! I couldn't just leave you; not when you were in trouble!"
Hiroki "I've been so worried about you!"
Stephania "I am glad to hear that, I suppose, though I must apologize for making you fret."
Hiroki "You don't need to apologize: not at all! You didn't do anything wrong!"
Hiroki "The real villains are whoever tied you up!"
Stephania "Oh, yes, indeed..."
"At the mention of these as-of-yet unseen villains, Stephania's pretty face blanches."
Stephania "I need to warn you about that, Hiroki. There aren't any villains, plural: there is only one!"
Hiroki "What? Did {i}one{/i} person orchestrate all of this, then? Did they tie you up?"
Stephania "Yes, they did, but-"
Hiroki "Damn it. They're gutsier than I thought, but that should make things easier."
Hiroki "If we're only up against one person, they should be easy enough to take down!"
Stephania "\"We\"?"
"Stephania blinks."
Stephania "What do you mean?"
Hiroki "I mean, I'm not alone. Elizabeth came here too, to protect you, and so did Marina, and Ayu, and Cosmos. We're all here for you, Steffy!"
Stephania "Oh my..."
"I had hoped Stephania would be relieved at this news, but instead, she look concerned."
Stephania "I am flattered to hear that, of course, but that only makes me worry all the more!"
Stephania "The woman who kidnapped me, you see..."
"So, the culprit behind all of this is a woman? This is getting curiouser and curiouser."
Stephania "Isn't an ordinary woman!"
Stephania "I've no idea {i}what{/i} she is, exactly - I've never seen anybody quite like her before - but she is truly frightening! I think she might be a demon!"
Hiroki "A demon...?"
Stephania "Yes, indeed! I know this might sound crazy, but please, Hiroki, you must believe me! Her powers are not of this world!"
"If this weren't such a tense situation, I'd be almost tempted to laugh at that."
"Stephania doesn't need to worry about seeming \"crazy\" in my company: not when I have a whole harem of sexy succubi lusting after me."
"If demons really do exist, I think I'd be prepared to take it in my stride, at this point."
"I mean, why not?"
"So many wild things have happened to me already, demons don't seem all that farfetched."
"Hell, Stephania could even throw a vampire or two into her tale, and I wouldn't bat an eyelid."
Stephania "You need to retreat, Hiroki! You, and all the others! It isn't me she wants, you see!"
Hiroki "I beg your pardon...?"
Stephania "She told me a bit about her plans, when she tied me to this chair! She told me I was never her target!"
Stephania "I was nothing more than bait meant to lure you out!"
Stephania "You aren't safe here! If you try to rescue me, she will appear, and then she will hurt you!"
Stephania "I don't want you being injured for my sake, Hiroki! I would never forgive myself if that happened!"
Stephania "Please, you have to-"
"Stephania entreaties me - or, at least, she tries to..."

stop music
# sfx?
with vpunch

"But, before Stephania can finish this heartfelt plea, I feel something collide with the back of my head."
"There's a dull, sick {i}crack{/i}, which I realize, a split second later, must have emitted from my cranium..."

scene factory:
    size (1920, 1080) crop (800, 600, 640, 360)
with vpunch

Hiroki "Oof..."
"And then, with a low moan of pain, I slump forwards..."
"My knees hit the cold, hard floor..."
Stephania "No! Hiroki...!!!"

scene black with circleirisout

"And then, everything goes black."

window hide dissolve
$ renpy.pause(1.0)
play music "bgm/spooky_loop.ogg" fadein 1.0
scene factory:
    size (1920, 1080) crop (800, 600, 640, 360)
with circleirisin
window show dissolve

Hiroki "Nn... What...?"
"I blink, scattering white dots from the field of my vision, and lift my head."
"My head aches, and I can feel a weight on my chest."
"My back is pressed against something cold and hard, and my limbs feel numb, as though they don't really belong to me."
"I can taste iron in my mouth and it's hard to breathe."
"What's going on?"
"Why do I feel so weak?"
"I blink a few more times, and then..."
Hiroki "Ah...?"

window hide dissolve
$ achievement.grant("ensnared")
if persistent.adult==True:
    scene cg12_a with wipeup_slow
else:
    scene cg12 with wipeup_slow
$ renpy.pause()
window show dissolve

"Finally, my vision comes into focus - and, when it does, I discern the source of my current discomfort."
"I'm lying on the ground and there's somebody sitting atop me: a very attractive somebody who looks faintly familiar."
W "Oh, good. You're finally awake. It's good to see that you are alright, Mr. Ogasawara..."
W "Or, would it be alright if I called you \"Hiroki\"?"
W "We've become so close, it would be awkward to keep using your family name, and I've liked you for quite a long time..."
W "Ehehe."
"The woman sitting astride me, pinning me to the ground with her thighs, has pale skin and long, fair hair."
"I've seen this woman before - I'm certain of that much - though, during our last encounter, she was in a decidedly more rumpled state."
"I remember, now, that I saw her in the theme park. I ran into her, and knocked her to the ground."
"I felt pretty bad about that, so I offered her my hand, but she declined."
"Now, how did our encounter go? I think it was a little like this..."
W "{i}I-I am, um, v-very sorry for getting in your way, Mr. Ogsawara. Pl-Please, forgive me for my clumsiness.{/i}"
W "{i}Y-You have been too good to me already. I-I could not ask for more.{/i}"
"...Yeah, that's right."
"I can remember being perturbed at the time on account of her knowing my name. I wondered how she'd learnt it, when I'd not had the chance to tell her, but I never had the chance to ask."
"I never thought I'd see her again, but it seems I was mistaken."
"The woman sitting astride me, in this dank, dark warehouse is {i}definitely{/i} her, though she doesn't look quite as I recall."
"She's dispensed with the frilly, Victorian-style attire, and instead, she's wearing something rather more form-fitting."
"I can see horns protruding from her scalp, too, and wings from her back: black, bat-like wings, which flutter behind her."
"...Yeah. I thought there was something odd about this woman, when I first clapped eyes on her, but now I'm certain of it."
"She isn't an ordinary woman."
"She is, instead..."
Hiroki "A-A succubus...?"
Alice "That is correct. My name is Alice, and I come from the succubus realm."
Alice "It is a pleasure to finally meet you, at long last. I have been waiting."
Hiroki "Right. Uh... I-It's nice to meet you too, um, Alice...?"
"That isn't a very Japanese name. It sounds pretty Western. I can't help but think of that popular children's book, with the blonde girl who tumbled into Wonderland, though this Alice has silver hair."
"There's something distinctly gothic about her, even attired in her succubus form."
"...Well, I guess that fits. Edgy interpretations of the Alice character are pretty popular, too."
"The name's not a common one, but I think it suits this woman."
"That doesn't really explain what she's doing here, though, or why she's straddling my chest in this old warehouse."
Hiroki "What's going on? How do you know my name - and what do you mean, you were watching me...?"
"Could it be...?"
Hiroki "Have you been stalking me...?!"
Alice "\"Stalking\" is an unpleasant word. I prefer \"watching from a distance\"."
Hiroki "So, you {i}were{/i} stalking me."
"That answers one question, at least, but..."
Hiroki "What are you doing here?"
Alice "I thought it would be apparent. I wanted to see you, Hiroki."
Hiroki "But why...?"
Alice "Why, you ask...?"
"Alice frowns, while resting her pale fingers against my chest: just above my beating heart."
Alice "It is because I like you, of course."
Hiroki "You... {w}like me...?"
Alice "Yes, I do. I like you so, so much, I don't know what to do with myself."
Alice "I've liked you for a very, very long time, in fact, and though I tried to keep my distance, I can no longer do that."
Alice "It just isn't fair..."
"Alice's expression twists."
Alice "I've been watching you, and I know that you are very popular among my succubus sisters."
Alice "Marina is in love with you, and Cosmos, and Ayu - and even Hifumi and Hazel."
Alice "They all adore you. They dote upon you."
Alice "They are some of the most beautiful succubi from our realm, but they've all taken a shine to you."
Alice "This made me very, very curious about meeting you myself. I wanted to see what was so very wonderful about you, that so many succubi would fall in love with you..."
Alice "And so, I began to follow you."
Alice "I wanted to learn more about you, and as I did, I found myself growing more and more enamoured."
Alice "I started to fall for you, but my feelings for you weren't fully cemented until I saw you in Yumemiru Land."
Alice "I knew, after you knocked me over, then offered me your hand, that you really were a good, kind man."
Alice "I knew what my sisters had seen in you."
Alice "It was very good of you to care for a useless succubus like myself, who has never been in a relationship before; who is nothing more than a waste of space..."
"Alice leans in, so as to bring her face, which is already perilously close to my own, only a few inches away from me."
Alice "And so, I wanted to spend even more time with you."
Alice "I want you all to myself, if only for one night."
Alice "I want you to know just how much I love you."
Alice "I {i}adore{/i} you."
Alice "I only hope, before the night ends, you will grow to love me, too..."
Alice "My dear Hiroki."
"Alice dips her head, meaning, I think, to kiss me, but I pre-empt her."
"I'm used to women trying to kiss me, at this point, and I'm able to jerk my head to one side before her lips can meet my own."
Hiroki "N-Now wait just a second...!"
Hiroki "I-I'm very flattered that you feel this way about me, Alice, but you're a perfect stranger. I don't know the first thing about you!"
Hiroki "I don't go around kissing women I've never met before!"
"{i}Not often, at least,{/i} I append inside my head, while recalling my very first meeting with Cosmos."
"I engaged in actions far more salacious than kissing with Cosmos during our first encounter, but what Alice doesn't know doesn't need to hurt her."
"...Um, I {i}hope{/i} Alice doesn't know about that."
"Just how much does she know about me and my relationships, anyway?"
"How long has she been watching me?!"
"She must know me well enough, at least, to know about my relationship with Stephania, or she wouldn't've kidnapped her to lure me out."
"I'm pretty sure, now, that's what happened, but I'd like some confirmation of that fact."
Hiroki "I especially don't kiss women who force themselves on me, either!"
Hiroki "Were you the one who kidnapped Steffy, Alice, and were you the one who wrote that ransom note?!"
Alice "..."
"There's a brief silence, during which Alice observes me, her eyes narrowed, before she replies."
Alice "...Yes, you are correct. I did kidnap the Astorian princess, and I did write that note."
"Ah-ha. I knew it."
Alice "I did it so you would have no choice but to come and see me. I wanted to talk to you, but I didn't know how else to approach you."
Alice "I have always been shy, you see, and awkward."
Alice "I was afraid you would not give me the time of day otherwise, if I did not do something drastic."
Alice "So many beautiful women are in love with you already, I doubted you would pay me any attention unless I did something crazy."
Alice "I apologize for my underhanded actions, but I really was desperate."
Alice "I want us to be together."
Alice "I want you in a way I have never wanted anybody before."
Alice "You were so kind to me, and so considerate. Surely you will not push me away...?"
Hiroki "You're heaping an awful lot of expectations upon my shoulders here. It doesn't seem very fair..."
"I look away from Alice, my brow furrowed."
"She is pretty, yes - that much is undeniable - but her singular obsession with me, not to mention the lengths she went to to get my attention, are pretty yikes-inducing."
"I don't think I want to commend this sort of behavior."
"Damn it. If I wasn't trapped beneath her, I'd give her shoulders a good, proper shake!"
Hiroki "And, I'm sorry, but I don't think I can forgive you for dragging Steffy into this. She's totally innocent."
Hiroki "Now, let me go...!"
Alice "I am sorry, but I cannot do that: not when I went to such lengths to claim you."
Alice "Now that I have you, Hiroki, I won't let anybody come between us."
Alice "I won't let anybody interrupt our love."
Alice "I just want to know what it feels like to be adored!"
Hiroki "What do you mean, \"you won't let anybody come between us\"?"
Hiroki "Did you do something to the others? What about Marina, Ayu, Cosmos, and Elizabeth...?!"
Alice "Oh, {i}them{/i}."
Alice "Do we really need to talk about that lot?"
Hiroki "Yes, we do! I'm worried about them! You didn't hurt them, did you?!"
Alice "No, I didn't. I am not powerful enough to harm my succubus sisters. They are all much more proficient at magic than I am."
Alice "I only used my abilities to waylay them. They should, at this moment, be in quite a bind."
Alice "I doubt they will be interrupting us: not for half an hour or so, at least."
Hiroki "Huh...?"
"What in the world did Alice do to Marina, Ayu, Cosmos, and Elizabeth?!"
"I can only imagine..."

stop music fadeout 1.0

"Maybe it's a little something like this?"

window hide dissolve
scene black with slow_dissolve
$ renpy.pause(0.3)
window hide dissolve
play music "bgm/succubus_lewd_loop.ogg" fadein 1.0
$ achievement.grant("sticky_succubi")
if persistent.adult==True:
    scene cg13_a with circleirisin
else:
    scene cg13 with circleirisin
$ renpy.pause()
window show dissolve

Marina "Khh... This is humiliating... I-I cannot believe I let this happen to me..."
Marina "What even {i}is{/i} this stuff, anyway? It's so slimy, nn..."
Marina "C-Could this be the work of a succubus?"
Marina "It's impossible that a human could have conceived of something like this!"
Marina "I thought the princess had been kidnapped by a group of ne'er-do-wells, but this really {i}is{/i} beyond the pale!"
Marina "I feel, nn, l-like I'm being touched in places I didn't even know I possessed...!"
Marina "Th-This is, nn, s-so disgusting..."
Marina "Cosmos! Ayu! Elizabeth! Are you three alright?!"

window hide dissolve
if persistent.adult==True:
    scene cg14_a with wiperight_slow
else:
    scene cg14 with wiperight_slow
$ renpy.pause()
window show dissolve

Ayu "N-No, I most certainly am {i}not!{/i} There's some, aah, h-horrible slimy thing clinging to me! I-It's clinging all over my body, nn, ahh..."
Ayu "Eeek!"
Elizabeth "M-Me too. I'm being covered, nn, in some strange liquid - or is it a solid?"
Elizabeth "I cannot tell, but... Nn, aah...!"
Elizabeth "It, mm, d-doesn't feel good!"
Cosmos "It's gross, and it smells foul..."
Cosmos "{i}Sniff, sniff...{/i}"
Ayu "Wh-Why are you smelling it, you weirdo?!"
Cosmos "I wanted to know what it reminded me of, and I think I have it."
Cosmos "It reminds me of when I went on Tanaka's quiz show. I got every question wrong, and then I was covered in slime."
Cosmos "It felt like this, but this slime... Nn..."
Cosmos "I-It feels like it's moving on its own?"

if persistent.adult==True:
    scene cg13_a with wipeleft_slow
else:
    scene cg13 with wipeleft_slow

Marina "It must be enchanted. These restraints are made of magic. I can feel them, nn, nullifying my own powers..."
Marina "I feel so weak..."
Ayu "Hmph. Some help {i}you{/i} are! I thought you were meant to be the mature, reliable one?!"
Marina "I {i}am{/i} mature and reliable - or, at least, I try to be! I am certainly more mature and reliable than you are!"
Marina "My powers do have limits, however!"
Marina "I hadn't a chance to counter attack before this awful, viscous liquid was upon us..."
Marina "Now it has me ensnared, I'm not sure what to do, nn... Khh..."

if persistent.adult==True:
    scene cg14_a with wiperight_slow
else:
    scene cg14 with wiperight_slow

Elizabeth "Nn, aah... N-No..."
Elizabeth "I-I cannot, nn, l-let things end like this; n-not when milady is in trouble!"
Elizabeth "I-I need to help her! I {i}have{/i} to help her, but I cannot move...!"
Ayu "Eeek! D-Don't touch me there! Do you hear me?!"
Ayu "If you lay your horrible, filthy fingers on me, my fans will lynch you!"
Cosmos "Hmm... You say that, but does slime even have fingers? It feels too gloopy."
Ayu "I don't know, and I don't care! I just want it to get off me!"
Cosmos "Would \"tentacles\" be better, or maybe \"tendrils\"? That sounds more accurate..."
Ayu "I really couldn't care less! I'm being, nn, felt up here, out in public! Th-This is horrible...!"
Ayu "You can't just, nn, t-touch an idol like that! Don't you have any shame?!?!"
Cosmos "I {i}don't{/i} have any shame, but this is embarrassing, even for me... Nn, aah..."
Cosmos "I-It d-doesn't feel good..."
Cosmos "Or maybe it feels {i}too{/i} good?"
Cosmos "I don't know {i}how{/i} I feel!"
Ayu "I know how I feel! I feel like I want to peel my skin off! This is the worst!"

if persistent.adult==True:
    scene cg13_a with wipeleft_slow
else:
    scene cg13 with wipeleft_slow

Marina "Nn, khh... I-I can't stand it..."
Marina "Th-This is utterly humiliating...!"
Marina "I don't know who is behind this cowardly attack, but when I get my hands on them, I'll wring their neck!"
Marina "I won't stand for this!"
Cosmos "Is that why, nn, y-you're lying on the ground, then...?"
Marinayu "Oh, shut up, Cosmos! You're not helping!"

if persistent.adult==True:
    scene cg14_a with wiperight_slow
else:
    scene cg14 with wiperight_slow

Cosmos "I'm sorry... I thought it was a funny pun, at least. I wanted to lighten the mood, nn, haah..."
Cosmos "B-But maybe I shouldn't've said anything."
Cosmos "I only ever seem to make things awkward..."
Ayu "As if things could get {i}more{/i} awkward than this!"
Ayu "Where's Hiroki when you need him?!"
Ayu "Won't he come and help us?!?!"
Ayu "What is that idiot doing, anyway?!"

stop music fadeout 1.0
window hide dissolve
scene black with circleirisout
$ renpy.pause(0.3)
play music "bgm/spooky_loop.ogg" fadein 1.0
if persistent.adult==True:
    scene cg12_a with slow_dissolve
else:
    scene cg12 with slow_dissolve
$ renpy.pause()
window show dissolve

Hiroki "Hey...!"
"I stare at Alice's face, into her striking eyes."
"She's still pinning me to the ground, her fingers curled about my wrists. Her irises bore into mine with disturbing intensity: so much so, I shudder."
Hiroki "What did you do to the others? Don't tell me you've hurt them...?!"
Alice "I won't tell you anything. I'm under no obligation to do that: not when you refused to honor my wishes."
Alice "I told you not to come here with other people, didn't I?"
Alice "I believe I was very particular about that in my note."
Hiroki "You were, it's true, but-"
Alice "But {i}nothing.{/i}"
Alice "I told you to come here alone, Hiroki, but you didn't listen to me. You ignored me."
Alice "You {i}betrayed{/i} me."
Alice "You hurt my feelings..."
Alice "But, that's fine. I can forgive you for that."
Alice "I would forgive you for anything, Hiroki."
Alice "You could call me names, or pull my hair, or spit on me, and I would still adore you."
Alice "I love you so, so much, and I want to show you that."
Alice "I want to show you how serious I am."
Alice "The other women you see might say that they love you, but they don't care about you as much as I do. They don't think about you every waking hour."
Alice "They don't understand. They can {i}never{/i} understand..."
Alice "But I would like to think that you might be able to understand me: that you might love me."
Alice "I want to make you all mine."
Alice "Then, nobody can come between us; not Marina, or Cosmos, or Ayu..."
"Alice's eyes flash dangerously."
Alice "Or even that foreign princess."
Alice "I won't let them."
"So saying, Alice dips her head, then pushes her mouth against mine."

stop music fadeout 2.0

Hiroki "Mm, nn..."
"I gasp into the kiss, surprised, which Alice - of course - uses to her advantage."
"She thrusts her tongue inside my mouth, then coils it with my own."
"Her kiss is deep and intense, and I sigh against it."

play music "bgm/sak_suc_alice_loop.ogg" fadein 1.0

"It feels, as she kisses me, like I'm sinking in a deep, dark swamp, all the way to the bottom: to a realm utterly devoid of light, from which I'll never be able to escape."
"Alice has me completely in her thrall."

if persistent.adult==True:
    jump adult5
else:
    jump merge5

label merge5:

    Alice "Mm, nn... Chh, aah..."
"Alice sighs against my mouth, then draws back, a gossamer strand of saliva stretching between our parted lips."
"She caresses my cheek with one hand, and staring at me, she murmurs, in a voice low with lust..."
Alice "Oh, Hiroki, you really {i}are{/i} sweet."
Alice "I was right to fall for you. I can't think of any man would I like to be with more than you - or any woman, for that matter."
Alice "You feel so good - and you taste so good, too!"
Alice "Can't you hear my heart pounding?"
Alice "I feel like I'm going crazy."
Alice "Mmm, chh... Mmm..."
"Soft sighs fall from Alice's mouth as we kiss, which - if I weren't in such a precarious situation - I might find cute."
"As it is, however, I feel pretty gosh-darned uncomfortable to be in this situation, and that's not just in a physical sense."
"Alice's kisses feel like they're draining me."
"My body grows cold as she continues her onslaught of affection. The tips of my fingers are starting to feel distinctly numb: so much so, I can't bend them."
"Alice's ardour is sapping my own strength."
Alice "Mm, nn, haa..."
"I know, as Alice continues to kiss me, that I'm in a pretty dire spot."
"Alice might be slighter than me, and shorter, but I'm in no fit state to throw her off me. I'm too tired."
"Like a hapless princess from a fairytale, I need somebody to come and rescue me - but who?"
"The only people who know I'm here are in similar states of helplessness themselves."
"Marina, Ayu, Cosmos, and Elizabeth all fell into Alice's trap. They won't be able to rescue me."
Alice "Mm, nn... Haa..."
"Is this... {w}really it...?"
"Is this how my life ends?"
"Am I going to expire here and now, in a cold, dreary warehouse in the middle of the night: kissed to death by a possessive, promiscuous succubus?"
"I don't want this to happen, but what can I do...?"
"{i}Is{/i} there anything I can do?"
"I'm only a human. I'm weak and feeble: positively puny"
" Alice, meanwhile, is much stronger than I am, and she gets stronger with every kiss she steals from me."
Alice "Mm, nn, haa..."
"Her power is increasing every time she takes my saliva into her mouth."
"I can't withstand her."

if succ_points >= 12:
    jump good_end
else:
    jump bad_end

label bad_end:

    "I guess this really is it: the end of the proverbial road."
"My energy is failing me."
"My body, still pressed against the cold, hard floor of the warehouse, gives one last, fitful spasm..."
Alice "Oh, Hiroki... I love you so much."
Alice "You're so cute when you're like this, lying helplessly beneath me."
Alice "This way, we really {i}can{/i} be together..."
Alice "{i}Forever.{/i}"
Alice "Ufufufufu..."

window hide dissolve
stop music fadeout 1.0
scene black with circleirisout

window show dissolve

"And then everything goes black."

window hide dissolve

jump credits

label good_end:

    "I'm almost beginning to give up on hope, when..."
W "Excuse you, but that is {i}my{/i} boyfriend you are currently slobbering over."

stop music fadeout 3.0

W "I would advise you to get your hands - and your mouth - off him, if you know what's good for you."
W "This is shameless behavior, even for a succubus, and I will not stand for it!"
Alice "Oh...?"
"Alice starts, perhaps abashed, and glances over her shoulder."
"I glance too, past Alice's head, to the mysterious interloper who's stepped inside the warehouse - and, when my eyes meet theirs, I stare."

play music "bgm/spooky_loop.ogg" fadein 1.0
scene factory
$ yface='angry'
$ ybody='succ1'
$camera_move(0,400,300,0,0,'dissolve')
call s_yue from _call_s_yue_2323
with wipeup_slow

"I know this woman, with her cool, icy gaze and her intense, indomitable aura."
"It's none other than Yue, the queen of the succubus realm."
"She must have been watching me from the succubus realm, as she occasionally does - and she must have seen, too, when I found myself in this dire situation."
"Now, she's come to save me, just like I dreamed."
"Damn. Now, that's a little embarrassing."
"I'm distinctly abashed, being seen in an emasculating position like this: pinned bodily beneath Alice, my mouth swollen from the intensity of her kisses."
"I really {i}do{/i} feel like a princess from a fairytale - but a ravished princess, from some non-child-friendly, R18 retelling."
"Would that make Yue the handsome prince, then?"
"She looks dashing enough, I suppose, standing by the entrance of the warehouse, with her arms folded beneath her ample chest."
"If I had to describe Yue's expression in a word, I'd say that she looks pissed."
"If granted two words to describe the look on Yue's face, then I'd say she looks {i}really{/i} pissed."
"Yue's ire isn't directed towards me, but to Alice, but even so, I feel myself shuddering."
"If looks could kill, Alice would be dead ten times over."
"Alice herself seems to realize this, because she gets to her feet, then stares at Yue, alarmed."

$camera_move(400,300,200,0,4,'ease')
$ alface='surprised'
$ albody='succ1'
call s_yalice from _call_s_yalice_1

Alice "L-Lady Yue...?! Wh-What are you doing here...?!"
$ ybody='succ2'
show yue at c3
Yue "Why do you think?"
"Yue surveys Alice archly, her eyes narrowed."
$ yface='serious'
show yue at c2
Yue "I noticed that you were taking liberties with my boyfriend, and I thought I ought to put you in your place."
$ yface='angry'
show yue at c1
Yue "Though I agreed to share Hiroki with some of my other subjects, I made no such agreement with you."
$ ybody='succ1'
show yue at c4
Yue "You do not have my permission to lay so much as a finger on him, much less {i}kiss him{/i}."
Yue "You have been a very, very naughty girl indeed - and, as such, you deserve to be punished!"
$ alface='sad'
show alice at c4
Alice "H-Huh? Y-Your boyfriend...?"
"A dumbstruck Alice looks at me, then back to Yue. Quickly, she puts two and two together (it's no mystery, based on Yue's speech, what our relationship is), then gawps."
$ alface='surprised'
$ albody='succ3'
show alice at c2
Alice "Th-Then, do you mean to say that you are in a relationship with Hiroki too?!"
$ yface='neutral'
show yue at c3
Yue "Indeed, I am. Did you not know that?"
Yue "I am surprised that this matter escaped your attention, given how intently you have been observing him."
Yue "I suppose you didn't know him as well as you thought you did."
$ yface='serious'
show yue at c2
Yue "How sad."
$ yface='sadist'
show yue at c1
Yue "And you thought you were in love with him. What a joke."
$ ybody='succ2'
show yue at c4
Yue "You can't have loved him all that much if you did not know that he is the property of your queen."
$ yface='angry'

stop music fadeout 1.0

show yue at c3
Yue "Now..."

play music "bgm/sak_suc_alice_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("none_shall_pass")
if persistent.adult==True:
    scene cg15_a with dissolve
else:
    scene cg15 with dissolve
$ renpy.pause()
window show dissolve

"Yue extends her palm, and when she does, dark energy begins to gather about her fingertips."
"Yue's eyes, which were already hard and flinty, grow harder still, as she stares Alice down."
Yue "Would you kindly leave Hiroki alone?"
Yue "I shall overlook this indiscretion, gross though it is, if you promise to leave, and to never interact with him again."
Yue "If you are unable to do that, though, then..."
"The darkness swirling about Yue's fingers grows more and more pronounced."
Yue "You and I will be at quite an impasse."
Alice "I... I don't..."
Yue "Powerful though you may be, after feeding on Hiroki's essence, you cannot hope to compete with me."
Yue "I am your queen, and I have ways at my disposal to make you bow to me, whether you wish it or not."
Yue "When it comes to a competition of raw strength, you {i}cannot{/i} win!"
Yue "Now, be a good girl and stand aside, or I will {i}make you!{/i}"
Alice "I... I didn't... I just..."
"Alice takes a step back, perturbed. She holds her hands to her chest, her expression stricken, then says..."
Alice "I didn't... {w}want things to end like this..."
Yue "Then maybe you should step away from Hiroki {i}before{/i} things get nasty."
Yue "Believe me, I do not want to hurt you either."
Alice "I know that, but I... I..."
"Alice swallows."
Alice "I didn't want to get on your bad side, milady: truly, I did not!"
Alice "If I had known that Hiroki was your beloved, I wouldn't have been so brazen in pursuing him!"
Yue "You oughtn't to have been so brazen in pursuing him regardless of our relationship."
Yue "It is in bad form, you know, to force yourself upon somebody who does not care for your affections. No succubus should resort to such aggressive tactics."
Yue "You have brought shame upon us succubi with your actions."
Yue "It is not me you should be apologizing to, really, but Hiroki. You subjected him to a great deal of abuse all in the name of \"love\"..."
"Here, Yue snorts."
Yue "As if what you felt for him was really \"love\", regardless of what you claim, when you had no compunctions in making him feel so uncomfortable!"
Alice "Th-Then, what I felt for Hiroki..."
Alice "Was it not love?"
Yue "Not, it was not. What you felt was obsession. It is quite different."
Alice "Obsession? But that sounds... {w}so ugly..."

stop music fadeout 1.0

"Alice sniffles. Her eyes begin to bead with tears: tears of abashment, perhaps, at her own actions."
Alice "I thought my feelings for Hiroki were pure and true. That is why I pursued him. I never would have attempted otherwise."
Alice "I was certain that my feelings must have been love..."
Alice "But you are saying I was mistaken?"
Yue "I am certain that you were."

play music "bgm/succubus_pensive_loop.ogg" fadein 1.0
scene factory
$ yface='neutral'
$ ybody='succ1'
$ alface='sad'
$ albody='succ3'
$camera_move(400,300,200,0,0,'dissolve')
call s_yalice from _call_s_yalice_2
with dissolve

"Yue lets her hand drop as she speaks, and the dark magical energy pulsating about her begins to dissipate."
"She must have realized, as I have, while listening to Alice, that she isn't about to launch a counter-attack."
"Alice looks too forlorn to try and strike a blow against Yue - and, even if her heart wasn't breaking (which it seems to be), I don't think she would try to attack her anyway."
"Alice seems to respect Yue too much for that."
$ yface='serious'
show yue at c4
Yue "I can say this with certainty, for I am speaking from past experience."
$ yface='shy'
show yue at c3
Yue "Once, I, too, mistook my petty, envious feelings of obsession for love."
Yue "I pushed my feelings upon Hiroki, one-sided though they were, and I made him suffer for them."
$ yface='serious'
show yue at c2
Yue "I told myself that this was the true nature of romance, but now I know I was mistaken."
$ yface='angry'
$ ybody='succ2'
show yue at c1
Yue "Love is not something you can force on somebody: not without their consent."
Yue "If you {i}truly{/i} love somebody, it should manifest in wanting them to be happy, regardless of whether they wish to seek that happiness with you or not."
$ alface='surprised'
show alice at c2
Alice "What? But that sounds painful..."
$ albody='succ2'
show alice at c4
Alice "I don't want Hiroki to reject me. I want to stay with him!"
$ alface='sad'
show alice at c3
Alice "I want to know what it feels like to be loved, just like you, and the rest of my succubus sisters!"
$ alface='shy'
show alice at c1
Alice "Hiroki loves all of them - he even loves Ayu, despite her bad attitude - so why can he not love me?!"
Alice "What is wrong with me?!"
$ alface='surprised'
show alice at c4
Alice "Why does nobody care about me?!"
$ alface='sad'
show alice at c3
Alice "Why..."
$ albody='succ1'
show alice at c2
Alice "Wh-Why can I never get what I want?!"
$ alface='surprised'
show alice at c1
Alice "I just wanted to know, for once, what it felt like to care for somebody, and to be cared for in return!"
Alice "Was that really so very awful of me?!"
$ alface='sad'
show alice at c4
Alice "Did I really do something that unforgivable...?!"
$ albody='succ3'
show alice at c3
Alice "Please, tell me, milady! Will I always be alone?!"
$ yface='neutral'
show yue at c1
"A few moments of silence pass, during which Yue regards Alice, and Alice regards Yue."
"During these quiet, understated moments, neither of them speak. Perhaps neither of them know what to say."
"Alice is inhaling sharply, her breathing ragged, as her chest rises and falls."
"Yue, meanwhile, regards Alice with a curious expression upon her face. Yue doesn't look angry anymore, at least, but I'm not sure if she's sad, either."
"Is she pitying, instead?"
"Does she... {w}feel sorry for Alice?"
$ ybody='succ1'
show yue at c4
Yue "...Oh, Alice. You poor, misguided thing."
"Yue takes a step forth, the heels of her formidable shoes striking against the ground."
$ alface='shy'
show alice at c2
Alice "Nn..."
"Alice shrinks away from Yue like a startled cat might, but Yue doesn't draw back."
"Instead, she continues to walk towards her subject, until they're only a few feet away from one another - and then Yue reaches out."
$ albody='succ2'
show alice at c4
Alice "Eek...!"

stop music fadeout 1.0

"I can tell, as Alice recoils, that she fears Yue will enact upon her some kind of violent vengeance. She must be expecting some kind of blow: perhaps a slap across the face, or fingers furling in her hair..."
"But, contrary to Alice's expectations, Yue does none of those things."

play music "bgm/succubus_romance_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("common_ground")
if persistent.adult==True:
    scene cg16_a with wiperight_slow
else:
    scene cg16 with wiperight_slow
$ renpy.pause()
window show dissolve

"Instead, she takes hold of Alice's trembling hand, then says, her voice gentle, and almost motherly..."
Yue "No, I do not think it a bad thing to want to be loved. I cannot judge you for that."
Alice "M-Milady..."
"Shyly, Alice cracks her eyes open, and surveys Yue: blinking at her from beneath her sweep of long, dark lashes."
"Alice's expression is incredulous, as though she can't quite believe what Yue is saying or doing, and for good reason."
"Only a few moments prior, Yue threatened to obliterate Alice."
"Now, however, Yue's expression is almost tender."
Alice "Milady, you... I mean, um..."
Alice "I-I thought that you were mad at me...?"
Yue "I {i}was{/i} mad at you, when I saw you had resorted to such underhanded tactics to gaining Hiroki's attention."
Yue "I am {i}still{/i} mad at you, in fact, for forcing yourself upon him so, and leaving him quite powerless to resist..."
Yue "But I cannot judge you too harshly for your actions."
Yue "As I said, I was once like that. I thought much like you did. I told myself I was in love with Hiroki, and I used my feelings to justify committing many awful actions against him."
Yue "I took away his freedom, and I tried to forcibly steal his affections from him."
Yue "I thought this my right, as his first ever partner, and the queen of the succubi to boot..."
Yue "But I know, now, I was only making convenient excuses for myself."
Yue "Deep down, I think part of me realized my actions were unconscionable."
Yue "In trying to bend Hiroki to my will, I ran the risk of ruining whatever remained of our relationship - and that, if I had been allowed to continue, would have been a true pity."
Yue "My relationship with Hiroki is very precious to me, after all."
Yue "It is more precious now than it was before, because, after relenting in my advances, I finally gave Hiroki the opportunity to love me properly."
Yue "I gave him a choice, for that is what all relationships are about."
Yue "Both parties must consent to love one another. It is not something that can come about through force."
Yue "I had to learn this lesson the hard way, through much trial and error."
Yue "I only hope you can come to learn this, too."
Alice "Milady..."
Alice "I-I had no idea you had ever felt like that before. I-I thought I was alone in my feelings; i-in my one-sided... {w}obsession, as you termed it."
Alice "I didn't think anybody would be able to understand me."
Alice "I-I was afraid I was broken...!"
Yue "You aren't broken. You were lonely, that is all, and jealous. I can understand these feelings well."
Yue "I, too, was lonely, whiling away my days in the succubus realm - and I was horribly, horribly jealous when I saw Hiroki cavorting around with my subjects: including my older cousin."
Yue "I was so jealous, I could hardly stand it."
Alice "What? Then, you and I..."
"Alice blinks, and as she does, she disturbs a few tears clinging to her lower eyelashes."
"These tears course down her cheeks, then drip onto the dirty floor of the warehouse."
Alice "Are we... {w}similar...?"
Yue "We are - or, at least, we {i}were{/i}."
Yue "I am not the petty, vindictive, angry woman I once was - or, at least, I am better able to keep my uglier emotions in check."
Yue "I still have a long way to go, but I am still young. I am sure I will change much in the years to come, as will the nature of my relationship with Hiroki."
Yue "That is how we all are, though: human and succubus. None of us can remain the same."
Yue "No matter how wretched you may feel right now, Alice, you can still change. It is not too late."
Yue "With time, patience, and genuine effort, I am certain you can become a better version of yourself, too: a version that you are able to like."
Alice "D-Do you really think so...?"
Yue "I am certain of it."
Yue "I am your queen, so you ought to listen to me. My word is the law, and I am confident when I say, despite your actions, I do not think you are an evil person."
Yue "You were just misguided."
Yue "You wanted to be loved, so you forced your feelings upon Hiroki."
Yue "I can understand this well, and I will not condemn you for it."
Yue "Instead, I would like to become your friend."
Yue "I think you deserve it."
Alice "Y-Your friend...?!"
"Alice gawps at Yue, her eyes almost comically wide."
Alice "B-But m-milady, I am but a lowly succubus with hardly any power to call my own! I-I am unsuccessful, a-and I have no friends, nor any special talents!"
Alice "My fellow succubus sisters all think of me as a failure, and they're right! I've never been able to seduce anybody before: not in all my life!"
Alice "H-How could you ever want to be my friend?! I-I don't deserve it!"
Yue "Now, {i}that{/i}, you see, is your problem. You need to learn to like yourself. Then, perhaps you will feel less inclined to seek affection from men like Hiroki, who are unwilling to give it."
Yue "Please, try to have more confidence."
Yue "You are very pretty in your own way, and I think you are strong."
Yue "You can overcome your affliction, as surely as I could - so long as we stay together."
Alice "Milady...! Oh, milady...!"
"Alice whimpers, then - after a pause - leans forth, and lets Yue embrace her: her head cradled against Yue's chest."
Alice "I-I do not think I am worthy of your affections, b-but if you insist upon being so nice to me, th-then I will accept them!"
Alice "I-It would be rude to reject your offer to cheer me, so..."
Alice "I-I would like to be your friend. I-I would like it very, very much!"
Alice "I-I'm tired of being alone...!"
Yue "Shh. It's alright, Alice. You aren't alone: not anymore. I am here, and I want to comfort you: I promise."
Yue "That is what friends do, after all."

stop music fadeout 1.0

Marina "Friends, hmm?"
"I hear footsteps, and then a derisive laugh."

play music "bgm/succubus_lewd_loop.ogg" fadein 1.0
scene factory
$ mface='serious'
$ mbody='succ1'
call s_marina from _call_s_marina_3432
$camera_move(0,400,300,0,0,'dissolve')
with wipeleft_slow

Marina "I suppose that is easy enough for you to say, Yue, when that woman-"
"Marina points an accusatory finger in Alice's direction."
$ mbody='succ2'
show marina at c3
Marina "-didn't humiliate you."

$camera_move(400,300,200,0,4,'ease')
$ yface='neutral'
$ ybody='succ1'
call s_ym from _call_s_ym_1

Yue "Oh?"
$ yface='smile1'
show yue at c4
Yue "What did Alice do to \"humiliate\" you, might I ask?"
$ mface='shy'
show marina at c1
Marina "W-Well, that is... It was..."

hide marina with dissolve
$ cface='sweatdrop'
$ cbody='succ2'
call s_yco from _call_s_yco_1

Cosmos "It was very sticky."
$ cface='neutral'
show cosmos at c4
Cosmos "Slimy, too."
$ yface='neutral'
$ ybody='succ2'
show yue at c2
Yue "\"Sticky and slimy\", hmm?"
$ cface='sweatdrop'
show cosmos at c3
Cosmos "Yeah. It got all over me, and I think some of it even got {i}inside{/i} me."
$ cbody='succ1'
show cosmos at c1
Cosmos "It's horrible, and it stinks like rotten eggs."
$ cface='sad'
show cosmos at c4
Cosmos "I feel like I need a shower."

hide cosmos with dissolve
$ aface='urgh'
$ abody='succ1'
call s_ya from _Call_s_ya_23

Ayu "Me too. This is, like, one of the worst nights I've had in my whole life."
$ aface='disgusted'
show ayu at c4
Ayu "This is even worse than that one handshake event I staged, where a crazy fan of mine tried to cut off a hank of my hair to keep as a souvenir!"
$ abody='succ2'
show ayu at c2
Ayu "I feel like I've been violated!"
$ yface='surprised'
show yue at c4
Yue "My my! That {i}does{/i} sound like an unpleasant fate, indeed!"
$ yface='sadist'
show yue at c3
Yue "Don't tell me you were humiliated in a similar manner, Marina, by this mysterious \"sticky, slimy\" substance?"

hide ayu with dissolve
$ mface='angry2'
$ mbody='succ1'
call s_ym from _call_s_ym_2

Marina "Khh..."
"Marina grits her teeth together, aggrieved, and glances away."
$ mface='angry'
show marina at c4
Marina "I won't dignify that with an answer: not when you're taking such obvious amusement in my plight."
$ mface='angry2'
show marina at c2
Marina "For our queen, you don't seem to care about the welfare of your subjects as much as you ought!"
$ yface='neutral'
show yue at c3
Yue "I will care about your welfare, Marina, when you show me the respect I am deserved."
$ yface='angry'
$ ybody='succ2'
show yue at c1
Yue "I cannot help but note you still, even after all this time, refuse to address me as \"milady\"."
$ mbody='succ2'
show marina at c4
Marina "Maybe I'll address you as that when you start acting like a ruler ought!"
$ mface='serious'
show marina at c3
Marina "I cannot believe that you would forgive Alice after all she has done! She deserves {i}some{/i} manner of punishment, at the very least!"
Marina "You've gone soft!"
$ yface='neutral'
show yue at c4
Yue "I suppose I might have mellowed out somewhat, it is true, after I commence my relationship with Hiroki..."
$ yface='smile1'
show yue at c3
Yue "...but I do not think that is a bad thing."
$ yface='smile2'
show yue at c1
Yue "I am happy with the way I am now. I am not the angry, indignant woman I once was, forever spoiling for a fight, although..."
"Yue's eyes harden."
$ yface='angry'
show yue at c2
Yue "You do test my patience at times, Marina."
$ mface='angry2'
show marina at c1
Marina "How do {i}I{/i} test your patience? {i}I{/i} did nothing wrong!"
$ mbody='succ1'
show marina at c3
Marina "I was trying to {i}help{/i} Hiroki! This wench over here is the one who caused all these problems!"

$camera_move(0,0,0,0,4,'ease')
$ alface='surprised'
$ albody='succ2'
call s_yalm from _call_s_yalm_1

Alice "Eep..."
"Alice, doubtless afraid of Marina, takes a step back at this, and hides herself away behind Yue's back."
"Yue notes this, because of course she does, and sighs."
$ yface='serious'
show yue at c3
Yue "Marina, please, do not raise your voice. That is no way to endear Alice to us."
$ yface='angry'
show yue at c1
Yue "Can you not see that she is afraid of you?"
show marina at c4
Marina "She {i}should{/i} be afraid of me! She deserves a good spanking after what she did!"
$ alface='shy'
show alice at c3
Alice "A-A spanking...?"
"Alice trembles fitfully, like a baby bird."
$ alface='surprised'
show alice at c2
Alice "M-My apologies, b-but I am not interested in that kind of play: n-not unless Hiroki was the one doing the spanking..."

$camera_move(0,400,300,0,3,'ease')
hide yue
hide alice
hide marina
with dissolve

$ aface='urgh'
$ abody='succ1'
call s_ayu from _call_s_ayu_23432

Ayu "Urgh. This is all so ridiculous."
$ aface='disgusted'
show ayu at c4
Ayu "At this point, I couldn't care less who's to blame for whatever the hell it is that happened tonight."
$ abody='succ2'
show ayu at c2
Ayu "I just wanna get out of this cold, miserable warehouse so I can have a shower."
Ayu "Cosmos is right. This stuff really {i}does{/i} stink."
$ aface='shock'
show ayu at c3
Ayu "It'll ruin my hair!"

$camera_move(0,0,0,0,3,'ease')
$ mface='serious'
$ cface='neutral'
call s_all from _Call_S_all_324432

Marina "Hmmm..."
"Marina frowns."
$ mface='angry'
show marina at c4
Marina "I'm not happy about letting Alice off the hook so easily, but I suppose I concur. I, too, would very much like to have a shower."
$ cface='grin'
show cosmos at c1
Cosmos "Me too. Showers are the best. Banzai."

$camera_move(0,400,300,0,3,'ease')
hide ayu
hide marina
hide cosmos
with dissolve

$ yface='neutral'
$ ybody='succ1'
call s_yue from _call_s_yue_2432423

Yue "Let us do that, then. Hiroki."
"Yue approaches me, then helps to my feet."
$ ybody='succ2'
show yue at c4
Yue "Would you mind escorting us back to your apartment? I think we should be able to relax then."
Hiroki "Sure, I guess. That's no problem, but what about..."
"\"Steffy\", I'm about to say - but my curious query is soon intercepted by an aggrieved cry."

stop music fadeout 1.0

Elizabeth "Stephania! Oh, Stephania! I was so worried about you...!"
Stephania "Lizzie? Lizzie, is that really-"

window hide dissolve
play music "bgm/succubus_romance_loop.ogg" fadein 1.0
$ achievement.grant("a_lady_and_her_maid")
if persistent.adult==True:
    scene cg17_a with wiperight_slow
else:
    scene cg17 with wiperight_slow
$ renpy.pause()
window show dissolve

Stephania "Oof...!"
"Stephania gasps, unable to make any further remarks, as Elizabeth descends upon her."
"Elizabeth frees Stephania from her restraints swiftly, with nothing save a snap of her fingers, then draws Stepania's body close to her own."
"Elizabeth's arms twine protectively about Stephania's shoulders, while she pulls Stephania's head to her bosom."
"As far as reunions go, it makes for quite the touching scene, but there's something a little \"off\" about Elizabeth's appearance."
"Elizabeth isn't wearing the black and white maid's attire she donned before we made our way to the warehouse."
"She's foregone her usual dress, and instead, she's dressed in something decidedly more skintight: something which bears great similarities to the clothes my succubus companions wear."
"From Elizabeth's head, meanwhile, a pair of horns sprout, and from her back, I can see the distinctive bat-like wings that Marina, Yue, and the rest sport."
"I had suspected this, of course, back in Astoria - or, to be more precise, Hifumi, Hazel, and Marina had suspected it - but to have it confirmed comes as quite the shock."
"I guess Elizabeth isn't an ordinary woman after all."
Stephania "Lizzie...?"
"Stephania stares at Elizabeth, her eyes wide."
Stephania "What in the world is going on, and what are you wearing?"
Elizabeth "That is... {w}a long story."
Elizabeth "There is much I have to tell you, milady. but, for the present, I am simply relieved to see that you are alright."
Elizabeth "I was so, so worried about you!"
Stephania "Well, you needn't worry further. I am quite alright, despite being treated somewhat roughly by this Miss... um... Alice...?"
"Stephania's confusion is so palpable, I can practically see the question marks hovering above her blonde head."
Stephania "Though I do have to wonder at all I have heard, and all I have seen."
Stephania "I have never seen a human with wings and a tail before: not until I met Miss Alice!"
Stephania "I thought they might, perhaps, be props, but then Alice started to speak of being a succubus - and then Yue appeared...!"
"Stephania stares at Elizabeth, her green eyes wide."
Stephania "Is this some sort of practical joke?"
Elizabeth "It is no joke, milady. Alice really is a succubus - as is Yue, and Cosmos, and the others."
Elizabeth "We are all succubi: myself included."
Elizabeth "I kept this a secret from you for many years, while working in Astoria's palace, because I feared you would take against me."
Elizabeth "I did not want to frighten you."
Elizabeth "While working as your maid, I tried to suppress my instincts as a succubus, so we might be close companions, but alas...!"
Elizabeth "When I saw that you had been kidnapped, I could no longer help myself."
Elizabeth "In my agitation, I could no longer maintain my human form."
Elizabeth "I tried to resume my old appearance, before reuniting with you, but I could not. This night has been so very stressful, I feel quite unlike myself!"
Elizabeth "I could no longer conceal my true self from you - but know this, milady."
Elizabeth "No matter what I look like, and no matter who I am, I shall always adore you."
Elizabeth "You are my beloved princess, and I would do anything to protect you!"
Stephania "Oh, Lizzie..."
Stephania "I cannot pretend I understand what I have seen and heard tonight, nor that I can make heads nor tails of your strange story, but..."
"Stephania twines her arms about Elizabeth's waist, so as to hold her close, and then says..."
Stephania "I am so, so glad you came for me. I knew I could trust you, and that is why I wasn't afraid."
Stephania "You really are the best maid I ever could have asked for!"
Elizabeth "Do you not resent me, then, for keeping secrets from you?"
Stephania "Of course not! How could I resent you, when you have been by my side for so very long?"
Stephania "Whether you are a human, a succubus, or... Goodness, I don't know, an eldritch abomination from beyond the stars, you will always be Lizzie to me!"
Elizabeth "Oh, milady...! You are so good to me! You are {i}too{/i} good, in fact!"
Elizabeth "I do not know whether I deserve your understanding, but now I have received it, I will do all in my power to prove myself worthy!"
Elizabeth "From this day forth, I vow that I shall be fully transparent with you. I will tell you the truth about myself - the whole truth - so please, do not turn against me!"
Elizabeth "I could not bear that!"
Stephania "I never would. I want to stay with you, too. You are my darling Lizzie, after all - and, my maid though you might be, you are more, even than that!"
Stephania "You are best friend in all the world, and I really do love you!"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
scene skyn with wiperight_slow
window show dissolve

"With the debacle in the warehouse well and truly over, I (finally) return home, my retinue of succubi (plus Stephania) in tow."
"Once we return, Alice looks at me, and somberly, she says..."

play music "bgm/succubus_slife_of_life_1_loop.ogg" fadein 1.0
scene kitchen_n
$ alface='shy'
$ albody='cas1'
call s_alice from _Call_s_alice_8
$camera_move(0,400,300,0,0,'dissolve')
with wipedown_slow

Alice "I really am sorry, Hiroki, for causing you so many problems."
$ albody='cas2'
show alice at c4
Alice "I just... {w}wanted to spend some time with you..."
"Well, I think wryly, if that was Alice's little scheme, it certainly succeeded. She was able to spend quite a lot of time with me before Yue interrupted."
"I shudder to think what would've happened if Yue hadn't come to my rescue. She was pretty cool back then."
"Kya~ I think I'm falling for Yue more and more..."
"Or something."
$ alface='sad'
show alice at c3
Alice "But I know, now, after talking to Lady Yue, that the way I went about it was totally wrong."
$ albody='cas3'
show alice at c2
Alice "I didn't ask you how you felt about any of this, and I didn't think about your boundaries."
show alice at c1
Alice "I was being horribly selfish."
$ alface='shy'
show alice at c4
Alice "If I could go back in time, I never would have forced myself on you like that..."
$ alface='sad'
$ albody='cas2'
show alice at c2
Alice "Not that this really helps, I suppose, given I {i}did{/i} force myself on you."
Alice "It's too late to change the past, but... Um..."
$ albody='cas1'
show alice at c4
Alice "I don't know if I deserve your forgiveness, so I won't ask for it, but I really am sorry."
$ alface='surprised'
show alice at c3
Alice "If you never want to see me again, I would understand!"
$ albody='cas3'
show alice at c1
Alice "Just say the word and I'll disappear from your life for good!"

$camera_move(400,300,200,0,4,'ease')
$ mface='serious'
$ mbody='wcas1'
call s_alina from _call_s_alina_1

Marina "We should be so lucky..."
"Marina murmurs this mutinously under her breath (she doesn't seem at all thrilled by Alice's words), but I feel rather more lenient towards her."
"It's true enough that Alice forced herself on me, but I can't bring myself to hate her for it. She seems pretty repentant about it, to look at her."
"In fact, I think she appears pretty cut up about all of this."
"That talk Yue gave her must have drummed some sense into her."
"I can't bring myself to resent her: not when she looks so very lost."
"I don't want to make her cry - she's so cute, it'd be a waste to spoil her pretty face with snot and tears - so..."
Hiroki "It's alright."
"I reassure Alice, after a pause."
$ alface='shy2'
show alice at c4
Alice "Huh...?"
$ mface='angry2'
show marina at c3
Marina "Is it {i}really{/i} alright? Don't forget what she did to you, darling!"
$ mface='serious'
$ mbody='wcas2'
show marina at c2
Marina "I know you're a soft touch, but there's such a thing as being {i}too{/i} forgiving!"
Marina "If you let Alice get away with her awful behavior, who's to say she won't walk all over you in the future? She'll never take you seriously: not like this!"
Hiroki "I know that, and I know Alice made a lot of mistakes. I'm going to absolve her for everything she did, but..."
"I inhale, then, smiling, I step forwards, and ruffle the top of Alice's head."
Hiroki "I know why you did what you did. You were lonely, weren't you?"
$ alface='sad'
show alice at c3
Alice "Y-Yes, that's right."
$ albody='cas2'
show alice at c1
Alice "I-I was horribly, horribly lonely, and I had nobody I could confide in. I've never really had any friends, you see, s-so I'm not good at talking to people..."
Alice "I guess that's why I did what I did. I didn't know how else to get your attention!"
$ mface='angry'
show marina at c1
Marina "Oh, please. There are better ways to get people's attention than assaulting them."

hide marina
$ aface='angry'
$ abody='wcas1'
call s_ayulice from _call_s_ayulice_1

Ayu "I agree. You're being way too nice to her, Hiroki! I've always known you're a total push-over-"
"I guess I must be, to put up with Ayu's vitriol..."
$ aface='urgh'
show ayu at c4
Ayu "-but Marina's right! Sometimes, you need to stand up for yourself!"
$ aface='disgusted'
show ayu at c2
Ayu "Don't you have {i}any{/i} self-respect?"
Hiroki "I have plenty of it, at the moment, but I don't think I would if I made Alice cry. That would be unforgivable."
$ aface='angry'
$ abody='wcas2'
show ayu at c3
Ayu "Ew. Who are you trying to impress here, idiot? You don't need to try and act like a knight in shining armor; not when Alice is obsessed with you already."
show ayu at c2
Ayu "You'd better be careful, or she'll fall for you even harder than she has, and before you know it..."
"Grimly, Ayu runs a hand across her neck."
$ aface='urgh'
show ayu at c1
Ayu "She'll decapitate you, cover your skull in diamonds, and start talking to it quicker than you can say \"for the love of God\"."
$ alface='surprised'
show alice at c4
Alice "N-No, I wouldn't! I might not be entirely normal-"
"Now, that's putting it lightly."
$ alface='shy'
show alice at c2
Alice "-but I'm not completely insane!"
$ aface='angry'
show ayu at c4
Ayu "So, you're only a {i}little{/i} insane, then?"
$ alface='surprised'
$ albody='cas2'
show alice at c1
Alice "J-Just a bit!"
$ alface='sad'
show alice at c3
Alice "I know I have problems, but I'd never murder Hiroki! I love him, in case you hadn't realized!"
$ alface='shy'
show alice at c2
Alice "D-Don't put horrible ideas like that into Hiroki's head..."
$ alface='neutral'
show alice at c4
Alice "Although..."
"Alice pauses, her expression thoughtful."
$ alface='smile'
show alice at c2
Alice "If I {i}did{/i} pull Hiroki's skull out of his head, he would never be able to leave me. Then, we really {i}could{/i} stay together forever..."
$ alface='yandere'
$ albody='cas2'
show alice at c1
Alice "That... {w}might not be so bad..."
Alice "Uhehe..."

$camera_move(0,0,0,0,5,'ease')
$ yface='serious'
$ ybody='wcas1'
call s_ayuyulice from _call_s_ayuyulice_1

Yue "...I'm sorry, but I will have to veto that interesting plan of yours."
$ yface='angry'
show yue at c2
Yue "While I do sympathize with you, Alice, my sympathy would soon dry up if you hurt Hiroki in any meaningful way. I do love him, after all."
$ aface='disgusted'
show ayu at c4
Ayu "So do I!"
Ayu "If you want to share him with us, you need to learn how to treat him properly!"
$ aface='angry'
$ abody='wcas1'
show ayu at c3
Ayu "You need to ensure you hand him back to the rest of us in one piece, OK - with his skull {i}inside{/i} his head!"
$ alface='shy'
$ albody='cas1'
show alice at c2
Alice "R-Right...! I'll do my best, um..."
$ alface='shy2'
show alice at c1
Alice "P-Provided you wouldn't mind me being a member of your harem, Hiroki?"
Hiroki "Of course not."
"I smile at Alice, and give her head another ruffle."
Hiroki "You're very cute - when you're not saying horrifying things, I mean. I'd be more than happy to spend more time with you."

$camera_move(0,400,300,0,4,'ease')
hide alice
hide yue
hide ayu
with dissolve
$ sface='smile2'
$ sbody='cas2'
call s_steffy from _call_s_steffy_232432

Stephania "Me too...!"
$ sface='smile'
show steffy at c3
Stephania "You might have kidnapped me, Alice, but you didn't really hurt me, and I understand that you meant me no ill-will."
$ sface='sad'
show steffy at c2
Stephania "I, too, know what it feels like to be lonely, having spent so much of my life shut up inside the palace, so I can't fault you."
$ sface='worried'
show steffy at c1
Stephania "Who knows?"
$ sbody='cas1'
show steffy at c4
Stephania "If I didn't have a wonderful friend like Lizzie to keep me company, I might have done something desperate, too!"

$camera_move(400,300,200,0,4,'ease')
$ lface='angry'
$ lbody='maid1'
call s_stefeli from _call_s_stefeli_3242

Elizabeth "You are too kind, milady."
$ lface='serious'
show lizzie flip at c3
Elizabeth "This woman treated you very poorly indeed. You would be well within your rights if you held a grudge."
$ lbody='maid2'
show lizzie flip at c1
Elizabeth "It is a touch unnatural, in fact, that you don't..."
$ lface='smile'
show lizzie flip at c4
Elizabeth "But you always have been a good girl. That is one of the reasons why I love you so much."
$ lface='serious'
$ lbody='maid1'
show lizzie flip at c1
Elizabeth "As for myself, however..."
"Elizabeth looks at Alice archly."
$ lface='worried'
show lizzie flip at c4
Elizabeth "I am rather less forgiving."
$ lface='serious'
show lizzie flip at c3
Elizabeth "I will let matters slide for now, because it is what milady wants, but if you cause any future problems for her, or for Mr. Ogasawara, I will make you regret it."
Elizabeth "Do I make myself plain?"

$camera_move(0,0,0,0,5,'ease')
$ alface='surprised'
$ albody='cas2'
call s_lizalste from _call_s_lizalste_1

Alice "Q-Quite plain...!"
$ alface='shy'
show alice at c3
Alice "I-I'm sorry for being such a bother! I-I'll be on my best behavior from now on!"

$camera_move(0,0,0,0,5,'ease')
hide lizzie
hide steffy
with dissolve

$ cface='laugh'
$ cbody='wcas1'
$ aface='angry'
$ abody='wcas1'
call s_ayalco from _call_s_ayalco_1

Cosmos "Ehehe~ Well, isn't this nice?"
$ cface='smile2'
show cosmos at c4
Cosmos "Things were a bit dicey for a while, but it looks like we've all made up. All's well that ends well!"
$ aface='urgh'
show ayu at c1
Ayu "I think this ended a little {i}too{/i} well. It's so schmaltzy, I feel like throwing up."

hide ayu
$ mface='serious'
$ mbody='wcas1'
call s_maalco from _call_s_maalco_1

Marina "Agreed. It still doesn't sit easily with me that Alice hasn't been punished for this."
$ mface='angry2'
show marina at c4
Marina "My right hand is itching to deliver retribution to her behind: especially after she put me through so much humiliation!"
$ alface='surprised'
$ albody='cas2'
show alice at c4
Alice "Eep...!"
$ cface='sad'
show cosmos at c1
Cosmos "Oh, come on, everynyan, let's not be so mean. Hiroki forgives Alice, and so does Steffy, so we should, too."
$ cface='smile2'
show cosmos at c3
Cosmos "Let's all turn the other cheek."
$ cface='smile'
show cosmos at c1
Cosmos "I advocate for peace, not war. Humanity will never advance if we're all at one another's throats!"
$ cbody='wcas5'
show cosmos at c4
Cosmos "Now, since Steffy and Lizzie will be going back to Astoria soon, why don't we all have fun?!"
$ cface='laugh'
show cosmos at c3
Cosmos "I have a lot of dates planned for us in the next few days - and, of course, you'd be more than welcome to come along, Alice."
Cosmos "The more, the merrier!"
$ alface='shy2'
show alice at c2
Alice "G-Going on dates, hmm..."
$ alface='shy'
show alice at c4
Alice "I've never been on a date before. The thought is a little scary, honestly. I-I don't know much about romance, but..."
$ alface='shy2'
$ albody='cas3'
show alice at c3
Alice "If I can experience it with you, Hiroki, then..."
"Alice takes a step towards me, then takes hold of the front of my shirt."
"She looks up at me, her eyes half-lidded, and says..."
$ alface='happy'
show alice at c2
Alice "It might not be so bad after all."
$ alface='shy'
$ albody='cas2'
show alice at c1
Alice "Pl-Please, look out for me. I'll be in your care."

stop music fadeout 1.0

"So saying, Alice stands on her tiptoes..."

play music "bgm/succubus_romance_loop.ogg" fadein 1.0
window hide dissolve
$ achievement.grant("kiss_kiss_fall_in_love")
if persistent.adult==True:
    scene cg18_a with wiperight_slow
else:
    scene cg18 with wiperight_slow
$ renpy.pause()
window show dissolve

Hiroki "Mm...?"
Cosmos "Oh my..."
Ayu "Urgh. Do you have to do that right in front of my face?"
Elizabeth "Youngsters today really are brazen."
Stephania "How romantic!"
Marina "Is this supposed to be a declaration of war?"
Marina "I suppose I admire her confidence, but kissing my darling, right in front of the rest of us..."
Marina "How shameless!"
Yue "I don't much like to see other women being intimate with my Hiroki, it's true, but I'm trying to be less jealous."
Yue "I need to learn how to share him, and I want Alice to be happy, too."
Yue "I think she deserves it."
Alice "Mm, chh..."
"Alice's lips meet mine in a kiss."
"This isn't a harsh, driving kiss, like the ones she bestowed upon me in the abandoned warehouse. This kiss, instead, is sweet and gentle; almost chaste."
"Alice unnerved me when I first met her, it's true, but..."
Hiroki "Mm, nn..."
"I don't hate her."
"I'm glad, in fact, that I met her."
"I'm cautiously looking forward to spending more time with her, and I hope we can all get along."
"It's just like Cosmos said. Things really do seem to be shaping up well."
"Perhaps this really {i}is{/i} a \"happily ever after\" after all."

stop music fadeout 1.0
window hide dissolve
scene black with slow_dissolve

jump credits
