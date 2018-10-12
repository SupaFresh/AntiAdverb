import easygui

alist = [
    'accidentally',
    'always',
    'angrily',
    'awkwardly',
    'badly',
    'blindly',
    'boldly',
    'bravely',
    'brightly',
    'coyly',
    'crazily',
    'defiantly',
    'deliberately',
    'devotedly',
    'doubtfully',
    'dutifully',
    'eagerly',
    'elegantly',
    'evenly',
    'eventually',
    'exactly',
    'finally',
    'foolishly',
    'fortunately',
    'gleefully',
    'gracefully',
    'happily',
    'honestly',
    'hopelessly',
    'hourly',
    'innocently',
    'inquisitively',
    'irritably',
    'justly',
    'kindly',
    'lazily',
    'madly',
    'merrily',
    'mortally',
    'nervously',
    'never',
    'obediently',
    'occasionally',
    'often',
    'only',
    'politely',
    'poorly',
    'powerfully',
    'quickly',
    'rapidly',
    'rarely',
    'rudely',
    'safely',
    'seldom',
    'seriously',
    'shakily',
    'sharply',
    'slowly',
    'solemnly',
    'sometimes',
    'sternly',
    'technically',
    'tediously',
    'usually',
    'victoriously',
    'vivaciously',
    'wearily',
    'weekly',
    'wildly',
    'anxiously,' 
    'boastfully',
    'cheerfully',
    'deftly',
    'dramatically',
    'enormously',
    'faithfully',
    'frequently',
    'hastily',
    'hungrily',
    'jealously',
    'loosely',
    'mysteriously',
    'obnoxiously',
    'perfectly',
    'promptly',
    'regularly',
    'selfishly',
    'silently',
    'speedily',
    'unexpectedly',
    'warmly',
    'yearly',
    'suddenly',
    'bashfully',
    'stealthily',
    'quietly',
    'friendly',
    ]
    
    
while 1 == 1:
    reply = easygui.enterbox(msg = 'Enter a word \n Lowercase only!', title = 'Anti Adverb', strip = True)
    if reply in alist:
        easygui.msgbox(reply + " is an adverb!")
        
    elif reply == "":
        print("Retry that")
        
    elif reply == "AntiAdverb":
        easygui.msgbox(msg = "Anti Adverb is a creation of the great SupaFresh! \n Find me at https://github.com/SupaFresh \n Happy Writing! \n \n Version 0.5 Alpha \n 10/12/2018", title = "About Anti Adverb", ok_button = "That's Nice")
    
    else:
        easygui.msgbox(reply + " is NOT an adverb!")
        
print("Uh Oh!")
    