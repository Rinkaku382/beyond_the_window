define slowfade = Fade(1.0, 0, 3.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)
define w = Character("Wife")
define h = Character("Husband")
define s = Character("Student")
define g = Character("Laura")
define d = Character("Game Director")
define t = Character("Tech Lead")
define a = Character("Lead Artist")
define i = Character("Interviewer")
define f = Character("Old Friend")

init:
    $ timer_range = 0
    $ timer_jump = 0

label start:
    stop music fadeout(3.0)
    scene black
    with slowerfade
    """
    You're in your room.

    In front of you there's a scratchpad. On the pages you've left some notes, the days before.

    Yet, they're useless, now.
    """

    scene room
    with slowfade
    """
    From the window in front of you, you see a building's facade.

    Different apartments for different people. From where you're you can see glimpses of all these lives.

    On their faces you see the shadows of different problems, difficult situations they don't seem to be able to fix.

    Maybe, they think those situations are impossible to be repaired.

    As you watch them, you wonder what problems are they dealing with and if you could be able to fix them.
    """

label room:
    call screen roomscreen

label apartments:
    scene apartments
    with slowdissolve
    call screen apartmentsscreen
##### ARGUMENT SCENE START ############################################################################################################################
label apartment1:
    scene arguebase
    with slowfade
    $ argument = 3
    """
    In this house live two people: a woman and her husband.

    A normal conversation in the living room, during morning, leads to unexpected truths.
    """
    w "So, have you finished that book we bought last month?"
    h "Which book?"
    w "The one with the red cover, don't you remember it?"
    h "Oh, that one! Yes, I do remember."
    w "...and have you finished it, then?"
    h "Guess I haven't. I think I forgot about it."
    w "You forgot?"
    h "Yes, I did. Why you ask?"
    w "I told you when we bought it that I wanted to read it, decided that I would have after you and now you forgot about it."
    h "But what's wrong with it? It's a book, not the end of the world."
    """
    Relationships between husbands and wives are indeed difficult.

    Every position taken means having the other as opponent.

    But, maybe, sometimes choosing between one or the other could lead to a repairment of the situation...
    """

label choose:
    call screen apartment1screen

### ARGUE HER #######
label herstart:
    scene argueher
    with slowdissolve
    jump arguestarther
    w "It's not the end of the world, you say...of course it isn't! But what does it mean? You're always like that!"
    h "Like that? Like that how?"
    jump arguestarther

label arguestarther:
    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'no_ansher'
    show screen countdown

    menu:
        "You're careless, and don't pay any attention.":
            $ argument += 1
            hide screen countdown
            h "Maybe sometimes I am, yes, but I'm trying my best!"
            jump apt1_2her
        "Just a selfish, old idiot!":
            $ argument -=1
            hide screen countdown
            h "An old idiot? How...well, the genius has spoken, right?"
            jump apt1_2her

label apt1_2her:
    if argument == 4:
        hide screen countdown
        w "I know you're trying, but you've got to try and stay focused. Or at least more focused."
        h "Of course, but..."
        w "But?"
        h "You're talking as if you're better than me..."
        jump apt1_good1her
    if argument == 2:
        hide screen countdown
        w "At least I pay some attention to the world surrounding me!"
        h "Oh and what world is surrounding you? And what is it like?"
        jump apt1_bad1her

label apt1_good1her:
    $ time = 20
    $ timer_range = 20
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "Why do you always say that?":
            hide screen countdown
            $ argument += 1
            h "Because it's true! Don't you realize it?"
            jump apt1_3her
        "Stop acting like a victim!":
            hide screen countdown
            $ argument -= 1
            h "A victim? I'm not acting like a victim, I AM the victim!"
            jump apt1_3her

label apt1_bad1her:
    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "It's the same as yours.":
            hide screen countdown
            $ argument += 1
            h "The same as mine..."
            jump apt1_3her
        "I don't know, real maybe?":
            hide screen countdown
            $ argument -= 1
            h "You're kidding me, right? Come on, say it. You're definately kidding."
            jump apt1_3her

label apt1_3her:
    if argument == 5:
        w "No, I don't realize it, I'm sorry. I'm just trying to talk with you, don't you get it?"
        h "Of course I get it, of course..."
        jump apt1_good2her
    if argument == 3:
        w "What?"
        h "Well, you said we live in the same world, but you treat me like we're in parallel worlds."
        jump apt1_neutralher
    if argument == 1:
        w "Kidding? I'm not kidding."
        h "Oh God, you really are terrible then."
        jump apt1_bad2her

label apt1_good2her:
    $ time = 25
    $ timer_range = 25
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "Then why don't you listen to me?":
            hide screen countdown
            $ argument += 1
            h "I...I try to listen...I try my best."
            jump apt1_4her
        "Stop pretending being superior, then!":
            hide screen countdown
            $ argument -= 1
            h "I'm not pretending of being superior, you are!"
            jump apt1_4her

label apt1_neutralher:
    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "And we are, if you continue being so distracted.":
            hide screen countdown
            $ argument += 1
            h "Yes, I understand what you mean..."
            jump apt1_4her
        "Can't you just stop complaining?":
            hide screen countdown
            $ argument -= 1
            h "Oh, sorry Madame, I didn't want to upset you."
            jump apt1_4her

label apt1_bad2her:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "Oh, so now I'm terrible...":
            hide screen countdown
            $ argument += 1
            h "No, I'm sorry, I didn't mean that..."
            jump apt1_4her
        "Terrible? How can you say I'm terrible?":
            hide screen countdown
            $ argument -= 1
            h "You're being absolutely terrible!"
            jump apt1_4her

label apt1_4her:
    if argument == 0:
        w "Oh, fantastic! I'm sorry to disturb your highness!"
        h "Oh fuck off!"
        w "You know what? I hate you! Really, I'm tired of this. All this!"
        h "So now you're tired! Well, I'm tired too. I'm tired of you, tired of your complainings, tired of hearing your voice."
        w "Then why are we even here? What are we still arguing about? Justo go away, the door is right there!"
        scene arguenegend
        with slowdissolve
        "As she says that, he looks at her face for a moment, then turn around and reaches the door, leaving without saying anything."
        scene black
        with slowfade
        jump room
    if argument == 2:
        h "Listen, I'm tired of this, I'm tired of arguing over a stupid fucking book."
        w "It's not about the book, it'a about the attitude. It's about you being so careless to forget even the most basic things."
        h "So you are saying I'm stupid?"
        w "I'm not! This is what I'm telling you! I'm only saying you have to fix this thing and I'm here to help you."
        h "I understand...ok, that's fine."
        w "Really...?"
        h "Yes, don't worry. It's good."
        scene arguenegend
        with slowdissolve
        "Yet, he doesn't say anything more than that. And her, too, finds it difficult to say anything at all."
        scene black
        with slowfade
        jump room
    if argument == 4:
        h "Listen, why don't we just stop? It's useless. I'm sorry for the book and for being so careless, really."
        w "I don't know, it's just that sometimes you get on my nerves and I really...can't do anything but feel rage."
        h "I didn't know that...for all these years you've felt that?"
        w "Well, yes..."
        h "Oh, I'm so sorry about that...I really never noticed it."
        scene argueposend
        with slowdissolve
        "He hugs her, feeling a deep sadness that seems to flow after years of containment."
        scene black
        with slowfade
        jump room
    if argument == 6:
        w "I know you try your best. And it's wonderful, I'm just telling you that there is this problem."
        h "Yeah, I understand."
        w "And we can fix it together, right?"
        h "Really?"
        scene argueposend
        with slowdissolve
        w "Yes, of course. I won't leave you alone."
        scene black
        with slowfade
        jump room
label no_ansher:
    h "If you won't even answer me than why are we here talking? Sorry, but I have better things to do."
    w "No, wait..."
    h "I'm tired of waiting. I'll see you later."
    scene arguenegend
    with slowdissolve
    "He exits the room, leaving her alone."
    scene black
    with slowfade
    jump room

#### ARGUE HIM ########
label himstart:
    scene arguehim
    with slowdissolve
    w "It's not the end of the world, you say...of course it isn't! But what does it mean? You're always like that!"
    h "Like that? Like that how?"
    """
    He starts to think how stupid this situation is. How absurd it is.

    But till, he can't do anything about it, as frustrating as it may seem.
    """
    w "You're careless, and don't pay any attention."
    jump arguestarthim

label arguestarthim:
    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "Maybe sometimes I am but I'm trying my best!":
            $ argument += 1
            hide screen countdown
            w "I know you're trying, but you've got to try and stay focused. Or at least more focused."
            jump apt1_2him
        "So, now I don't pay any attention...":
            $ argument -= 1
            hide screen countdown
            w "No, you don't. You never do."
            jump apt1_2him

label apt1_2him:
    if argument == 4:
        hide screen countdown
        h "Of course, but..."
        w "But?"
        h "You're talking as if you're better than me..."
        w "Why do you always have to say that?"
        jump apt1_good1him
    if argument == 2:
        hide screen countdown
        h "And who are you to judge? Huh? You are so perfect that you can judge anyone you want?"
        w "I'm nobody, ok? Doeas that make you feel better?"
        jump apt1_bad1him

label apt1_good1him:
    $ time = 20
    $ timer_range = 20
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "Because it's true! Don't you realize it?":
            hide screen countdown
            $ argument += 1
            w "No, I don't realize it, I'm sorry. I'm just trying to talk with you, don't you get it?"
            jump apt1_3him
        "Because you make me feel like that!":
            hide screen countdown
            $ argument -= 1
            w "I hope you don't think it's intentional, at least!"
            jump apt1_3him

label apt1_bad1him:
    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "No, that's not the point.":
            hide screen countdown
            $ argument += 1
            w "And what is it, then?"
            jump apt1_3him
        "Yes, of course it does!":
            hide screen countdown
            $ argument -= 1
            w "You asshole!"
            jump apt1_3him

label apt1_3him:
    if argument == 5:
        h "Of course I get it, of course..."
        w "Then why don't you listen to me?"
        jump apt1_good2him
    if argument == 3:
        h "The point is that you can't decide who to judge when you want. Life isn't like that."
        w "And you can decide what others can or can't do?"
        h "Well, no, of course, but what I was telling is that I don't find it correct that you do that with me."
        w "So, I should not tell you about something that I don't like about you?"
        jump apt1_neutralhim
    if argument == 1:
        h "I'm an asshole? How could you?"
        w "And what should I tell you, then? Do you expect some compliments?"
        jump apt1_bad2him

label apt1_good2him:
    $ time = 25
    $ timer_range = 25
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "I...I try to listen...I try my best.":
            hide screen countdown
            $ argument += 1
            w "I know you try your best. And it's wonderful, I'm just telling you that there is this problem."
            jump apt1_4him
        "Why don't I listen? I listen too much!":
            hide screen countdown
            $ argument -= 1
            w "Too much? This thing you're doing here is listening too much?"
            jump apt1_4him

label apt1_neutralhim:
    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "And have you listened to your tone?":
            hide screen countdown
            $ argument += 1
            w "What if I didn't?"
            jump apt1_4him
        "You know what? Do the fuck you want!":
            hide screen countdown
            $ argument -= 1
            w "Fine, I will!"
            jump apt1_4him

label apt1_bad2:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "Maybe not, but it doesn't mean you have to insult me.":
            hide screen countdown
            $ argument += 1
            w "Yeah you're right...I'm sorry."
            jump apt1_4him
        "You just insulted me!":
            hide screen countdown
            $ argument -= 1
            w "And what about it? Is it a crime."
            jump apt1_4him

label apt1_4him:
    if argument == 0:
        h "You know what? I'm tired of this. I'm tired of arguing, of getting mad and I'm tired of you."
        w "You're tired of me?"
        h "Of course I'm tired of you! You insult me, you despise me, you hate me!"
        w "And what about you, then?"
        h "I'm tired of feeling guilty for everything! I'm tired of being guilty even because I haven't read a fucking book!"
        w "That's because you value less than that book! That's the truth!"
        h "Oh, what a surprise! I would've never guessed something like that!"
        w "I hate you! I really hate you!"
        h "Fine, then you know what? I'm fucking leaving. I'm done with all this, done with you."
        scene arguenegend
        with slowfade
        "Moved by anger, he punches the nearest wall, leaving his fist's trace behind."
        scene black
        with slowfade
        jump room
    if argument == 2:
        h "Ok, fine, I get it. You don't want me here, right? Absolutely fine, really."
        w "What?"
        scene arguenegend
        with slowfade
        h "It's just clear. Very clear. I'll leave you your space, no problem. I'll go take a walk."
        w "Yeah...maybe that will calm us both."
        h "Yeah, maybe."
        scene black
        with slowfade
        jump room
    if argument == 4:
        h "...I'm sorry about all this. I'm sorry about the book, about the argument, about everything."
        w "It's ok, it came from both of us..."
        h "Yeah, right, but nothing in this was nice from my part."
        w "Not from mine either, I'd say."
        h "So...what now?"
        scene argueposend
        with slowfade
        "She gently hugs him, softly crying of happiness."
        scene black
        with slowfade
        jump room
    if argument == 6:
        h "Yeah, I understand."
        w "And we can fix it together, right?"
        h "Really?"
        scene argueposend
        with slowfade
        w "Yes, of course. I won't leave you alone."
        scene black
        with slowfade
        jump room
label no_anshim:
    w "So, you're pretending to be mute, now?"
    h "No, I'm not, I-"
    w "Yeah, right, whatever. I'm leaving, by the way."
    scene arguenegend
    with slowfade
    h "You're leaving?"
    w "You don't want to talk and I don't want to talk with a wall, so I'm leaving."
    scene black
    with slowfade
    jump room

##### PHONECALL SCENE START ############################################################################################################################
label apartment2:
    scene phonecallprep
    $ emb = 3

    """
    The ugliest apartment in the building is occupied by a young student.

    He's now immersed in the shadow of his room, looking at the darknes surrounding him.

    In his head there's his girlfriend's face. He misses her. Deadly.

    He'd like to call her and tell her he's sorry about everything, that he'll try to do his best to be a better person.

    But he doesn't know how to say it.
    """
    s """
    So, uhm...what could I say to her...?

    Well, let's start with the intention...the intention would be to bring her back with me.

    ...I think, at least.

    So, maybe I could start with...
    """

label apt2_lessemb1:
    menu:
        "Laura, I really love you.":
            $ emb += 1
            s "Yes, that's good. I'm sure it's good."
            jump apt2_1
        "I think we should talk, Laura.":
            $ emb -= 1
            s "Hmm..."
            jump apt2_1

label apt2_1:
    if emb == 2:
        s "I don't know, it's very exaggerated...but it could work."
        jump apt2_lessemb2
    if emb == 4:
        s "Maybe more enphasis on the love..."
        jump apt2_moreemb2

label apt2_lessemb2:
    menu:
        "I thought that, maybe, you'd want to come back with me...":
            $ emb += 1
            s "Yes, sorry is good."
            jump apt2_2
        "I'm sorry for what I've done, very sorry.":
            $ emb -= 1
            s "Now that I think about it, the house seems empty."
            jump apt2_2

label apt2_moreemb2:
    menu:
        "I want to be sincere with you. About everything.":
            $ emb += 1
            s """
            Well, but everything what, exactly?

            Guess I'll figure it out, somehow.
            """
            jump apt2_2
        "I miss you, enormously.":
            $ emb -= 1
            s """
            For all this time, these days, I thought about you...

            Yes, that seems good.
            """
            jump apt2_2

label apt2_2:
    show phonecalldef
    if emb == 5:
        s """
        Hi, uhm....I just wanted to know if you'd like to love me.

        No, wait, I wanted to say that I love you. Yes.

        And I'm sorry for what I've done, you can't even imagine how much.

        I thought that, maybe, you'd want to go back together. You know...
        """
        jump apt2_negative
    if emb == 3:
        s """
        Hi, Laura. I want to talk with you.

        I think...uhm I think I want to say sorry, you know.

        I miss you a lot, really. It's lonely without you.
        """
        jump apt2_neutral
    if emb == 1:
        s """
        Hi, Laura. I really need to talk with you.

        You know, I'm sorry for what I've done.

        Truly sorry. I wanted to know what I could do to repair all this...situation?
        """
        jump apt2_good

label apt2_negative:
    g "Do you really want me to answer you?"
    $ time = 2
    $ timer_range = 2
    $ timer_jump = 'no_ans'
    show screen countdown
    menu:
        "Well, it would be nice...":
            """
            She ends the call, without saying a word.
            The young student finds himself alone once again, surrounded by the darkness in the room.
            """
        "No, I think you won't...":
            g "I'll have to think about it. Just give me some time, please."
            s "Yes of course...I'll wait."
            g "Ok, bye then...for now."
    scene black
    with slowfade
    jump room
label apt2_neutral:
    g "You think?"
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'no_ans'
    show screen countdown
    menu:
        "I'm sorry, I don't really know what to say.":
            hide screen countdown
            g "I think it's normal. It's not an everyday situation, after all..."
            s "It definately isn't, yes. And I really am sorry about all this."
            g "You know, maybe...maybe we can put all this behind us."
            scene phonecallposend
            with slowfade
            s "Really?"
            g "Yeah, why not?"
            "A smile on the student's face, and the phonecall calmly goes on."
        "You know I'm not good with words.":
            hide screen countdown
            g "And it would be nice if you were..."
            s "I know, but what do I have to do?"
            scene phonecallnegend
            with slowfade
            g "Just...I don't know, I really don't know."
            "The call ends. Without any goodbye, without any smile."
    scene black
    with slowfade
    jump room
label apt2_good:
    g "To repair this situation...?"
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'no_ans'
    show screen countdown
    menu:
        "Yes, I liked being with you.":
            hide screen countdown
            g "You really did?"
            s "Of course I did! It was great, there wasn't any other thing I wanted to do more than being with you."
            g "I'm so happy to hear that...I mean, I was angry, but..."
            s "Why have we done all this?"
            scene phonecallposend
            with slowfade
            g "I don't even remember...and I think it's not important what it was."
            s "You think that?"
            g "Of course. Let's just go back to how we were. We can, right?"
            s "Of course we can."
        "Well you know, all the mess that happened.":
            hide screen countdown
            g "You mean the mess you've made?"
            s "Yeah, and I said I'm sorry about it."
            scene phonecallnegend
            with slowfade
            g "Of course you are, but you'd better remember it. And very well."
            s "But I-"
            g "Don't worry, I understood. And I'll think about it, maybe."
            "She hangs up, leaving the young student by himself. Silent and lonely."
    scene black
    with slowfade
    jump room

label no_ans:
    scene phonecallnegend
    with slowfade
    g "I guess you don't really wanna talk, then..."
    s "No wait-"
    "She instantly hangs up. The student only had the time of hearing the soft beginning of her crying."
    scene black
    with slowfade
    jump room

##### OVERWORK SCENE START ############################################################################################################################
label apartment3:
    $ ease = 50
    scene overworking
    with slowfade
    """
    A small development studio occupies the left side of the third floor.

    As silent as it may seem, it's a very busy place in which work never seems to end.

    In this moment, the whole team is focused on implementing new features.

    The concentration is intense and the schedule tight. One month until the deadline.
    """

label apt3_q1:
    scene overworkingq1
    with slowdissolve
    t "I'm sorry to disturb you, but we have a problem..."
    d "A problem? What kind of problem?"
    t "One of the programmers has made some mistakes in the code, but he realized it just now."
    d "And what kind of mistakes?"
    t "Well, we've found some, but not all of them, yet. They don't seem to be dungerous, but they sure are a lot of pain."
    d "And he pushed them without checking? What is he, an idiot?"
    t "I already told him that."
    d "That's just wonderful. One month until the deadline and some imbecille makes mistakes in the code."
    t "Well, the fact is that we have two options, now..."
    menu:
        "We can fix them, but it'll take time.":
            $ ease -= 25
            d "We can't deliver a bugged game, you know that as well."
            t "Of course, I'll tell the producer we'll have to schedule a new date for the release."
            d "It won't happen."
            t "What do you mean?"
            d "We'll never gain more days. We'll have to manage the time we have and fix everything."
            t "That sure is troublesome..."
            d "Ain't it?"
        "We can leave them be and continue to push until the realease.":
            $ ease += 25
            d "We already are in a bad situation. Adding the fix of a similar problem would only make everything worst."
            t "Yes, I understand...but wouldn't we gain more time to finish the project?"
            d "Of course not. The world won't stop only because we have to fix coding mistakes."
            t "Hm, that makes sense."
    jump apartment3_2
label apartment3_2:
    scene overworkingq2
    with slowdissolve
    """
    As the Lead Artist moves closer to the desk, the Director instantly sense the incoming problem.

    Surprisingly, the Lead's face is at ease. Or at least more than usual.
    """
    a "The producer has asked for a reunion, planned for next week."
    d "And?"
    a "He asked for all the departments to be present, but everyone's loaded with work. None of us can go."
    d "Of course, that's a problem."
    a "So...what should we do?"
    menu:
        "There'll be only the leads, it's the most logic thing to do.":
            $ ease += 25
            a "Are you sure? Won't it be a problem?"
            d """
            We'll save some time for the development and it's not that necessary to have everyone there.

            That would only be confusing.
            """
            a "Understood. Fine, I'll tell the others, then."
            d "Good."
        "If he asked for everyone then everyone will go.":
            $ ease -= 25
            a "Is it really a good idea?"
            d """
            Well, as I said, if he has asked for everyone, then everyone has to go.

            I'd like it to be a matter of choice, but it isn't.
            """
            a "Yeah, that's true...I'll go tell all the departments, then."
            d "Fine, good work."
    jump apartment3_3
label apartment3_3:
    if ease ==  100:
        scene overworkingnegend
        with slowfade
        i "The story of this project seems to be interesting, could you tell me more about it?"
        d """
        Well, all I can say is that we decided to fully concentrate on finishing it. At least the base.

        We never thought it would end up like that.

        I only now realize that my choices weren't the best I could make, even though in that moment they seemed to be.

        I think it's my fault if the team disbanded, in the end...it's a very heavy weight on my shoulders.
        """
        scene black
        with slowfade
        jump room
    if ease == 50:
        scene overworkingposend
        with slowfade
        """
        Sitted at his chair, the director continues working, silently and focused.

        Around him, a small number of other people, like a small troop of soldiers, follow his directions obediently.

        And even though sometimes his methods are harsh and the schedule is thight, the project calmly procedes towards the deadline.

        Not all the problems have been repaired but, at least, everything seem to be fine.
        """
        scene black
        with slowfade
        jump room
    if ease == 0:
        scene overworkingneutend
        with slowfade
        """
        Choices and consequences can be cruel.

        Although all the problems have been fixed, it doesn't mean that everything, now, will be alright.

        Even though the director and the whole team are proceeding towards the deadline, the stress rises, tiredness caughts everyone.

        Fixing problems, in the end, could create new and unexpected ones, in an endless circle of choices and consequences.
        """
        scene black
        with slowfade
        jump room

##### SOLITUDE SCENE START ############################################################################################################################
label apartment4:
    $ phonering = False
    $ sleep = False
    $ read = False
    $ mirror = False
    $ smoke= False
    $ tv = False
    $ windowlook = False
    $ boredom = 50
    scene solitude
    with slowfade
    """
    In the fourth and last apartment lives a young girl.

    In a morning of boredom, she's waiting for a phonecall.

    All over the walls and furniture there are signs that she's alone.

    Her loneliness though, is only proof of her complete freedom.

    Freedom to act, freedom to choose.

    She can do whatever she wants, use whatever she wants to spend some time while she waits.
    """
label apt4screen:
    if boredom >= 75:
        play music "ringtone.ogg"
    if boredom <= 25:
        play music "ringtone.ogg"
    call screen apartment4screen
label tv:
    if tv == True:
        scene solitude
        "She already watched television."
    if tv == False:
        scene solitude
        """
        A normal and very old television that her parents gave to her some time ago.

        The colours are pale and it doesn't receive the signal so well.

        But apart from that, she doesn't mind watching it, even though she sometimes get bored.
        """
        menu:
            "Turn it on.":
                scene soltv
                with dissolve
                $ tv = True
                $ boredom += 25
                """
                On every channel there are only boring programs.

                Even though she searches for quite some time, she finds nothing truly exciting.
                """
            "Leave it.":
                """
                She decides to not turn it on.

                There certainly are more interesting things to do in the room.
                """
    jump apt4screen
label bed:
    if sleep == True:
        scene solitude
        "She doesn't want to sleep anymore."
    if sleep == False:
        scene solitude
        """
        A noisy old bed, covered with her favourite duvet and blankets.

        It always keep her warm during cold days and nights.

        Now that she's thinking about it, she feels a little sleepy...
        """
        menu:
            "Sleep.":
                scene solbed
                with dissolve
                $ sleep = True
                $ boredom += 15
                """
                As she lies down on the bed, covering herself up with the duvet and blanket, she fall asleep.

                She doesn't know how long, but she sleeps for quite some time.

                Her dreams are sweet and beautiful.

                But as she wakes up, she still has nothing to do.
                """
            "Don't sleep.":
                """
                It's better if she doesn't, indeed.

                The phonecall she's waiting for is very important and not answering could have terrible consequences.
                """
    jump apt4screen
label windowsol:
    if windowlook == True:
        scene solitude
        "She has already watched outside the window."
    if windowlook == False:
        scene solitude
        """
        A dusty window.

        Sometimes it stuck itself and it's hard to open it.
        """
        menu:
            "Watch outside.":
                scene solwindow
                with dissolve
                $ windowlook = True
                $ boredom -= 15
                """
                Outside the window she sees the facades of other buildings.

                Her eyes wander through all the windows and she can't help but to ask herself who lives in all those houses? How are their lives?
                """
            "Don't watch outside.":
                """
                She stares at the window but doesn't reach it.

                She prefers doing something else.
                """
    jump apt4screen
label cig:
    if smoke == True:
        scene solitude
        "She has already smoked."
    if smoke == False:
        scene solitude
        "In the ashtray there is a cigarette she was smoking a while ago."
        menu:
            "Smoke it.":
                scene solsmoke
                with dissolve
                $ smoke = True
                $ boredom -= 15
                """
                She lights it, then takes a puff.

                The smoke flows in the air, filling the room calmly.

                She feels relaxed, as she watches the small cloud disappearing in the space around her.
                """
            "Don't smoke it.":
                "She leaves it where it is, searching for something else to do."
    jump apt4screen
label mirror:
    if mirror == True:
        scene solitude
        "She doesn't want to stare at herself again."
    if mirror == False:
        scene solitude
        """
        A shiny mirror occupies a large portion of the wall.

        As everything else, it was given to her by her parents.

        Even though it's useful, she doesn't like to stare at herself. In fact, it annoys her a lot.
        """
        menu:
            "Stare just a little.":
                scene solmirror
                with dissolve
                $ mirror = True
                $ boredom += 15
                "She really doesn't like to watch her body. Especially if there's no usefulness in doing so."
            "Don't stare.":
                "In fact, she doesn't want to do it, so it's better not to."
    jump apt4screen
label books:
    if read == True:
        scene solitude
        "She has read enough."
    if read == False:
        scene solitude
        """
        A small group of books.

        Even though they are few, she likes books, but doesn't want to fill the room with them.

        So she has bought only the ones she likes the most and borrows others from a nearby library.
        """
        menu:
            "Read one.":
                scene solbook
                with dissolve
                $ read = True
                $ boredom -= 25
                """
                She takes one of the books from the shelf, after a careful choice.

                It's a book of poetries, written by Arseny Tarkovsky.

                She opens it, searching for a specific poem.
                """
            "Don't read.":
                "Reading is not something she wants to do, for now at least."
    jump apt4screen
label phone:
    if boredom >= 26 and boredom <= 74:
        scene solitude
        scene solphonewait
        with dissolve
        """
        Like everything in the room, even the telephone is old.

        It's still not ringing. She wanders how much time she'll have to wait.
        """
        jump apt4screen
    if boredom >= 75:
        ## Bored answer to phone
        stop music
        scene solphone
        with fade
        "aaa"

        scene black
        with slowfade
        jump room
    if boredom <= 25:
        ## Not bored answer to phone
        stop music
        scene solphone
        with fade
        "bbb"
        scene black
        with slowfade
        jump room
