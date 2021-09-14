#!/Applications/anaconda3/bin/python
def intro():
    print('''
                                        ,æ#▀▒▒▒▒#╗▄                                                     
                    ,▄▄▄▄,,          ▄▀░░▒▄▄▀▀▀╬╬▓▓▓██▄                                                 
           _▄▄▓▓█╫╫▓▄▄▄▄░░░╬▀#▄    ▄╬░▒▄▓╬▒▒▓▀▀╬░░░▒░░░╚╬▀#▄                                            
           ╙▀╬▒▒╠╠╠╠▒╠╠▒╠╬▀▄▒░░╠▀▄█░░▄▀░╬▀╚░░φ▒░▄▄##╪╪╪╗▄▄▄░░╬#▄                                        
                ╙▀╫▀█╠╠╠╠╠╠╠╬▓▒░░░▀▄█░▓▀░╠░▄▓▀╬╬╠╠╠╠╠╠╠╠╬╠▒╬╬▀▀▄╬▀▄                                     
                 ,▄▄█▓╫╫╫▄▄▒▒╠╬█░░░╚██░▒░▓▀░╠╠╠╠╠╠╠╠╠╠╣▓▒╠╬╠╠╠╠╠▒╬▀╣▓                                   
            ▄#▒░░▒░░░░░░░░▒░░░╙▀▀╪▄▄▌░▄▄█╝▀▀▀▀▀╣▄▒╠╠▒╣╨  ▀╙╙``╙╙╙▀▀▀╨╝█,                                
         ,@▒▒░░▄#▀▀▀▒▒╬▒▀▀▓█▀▀▀▒╬██▀██▀▀▀▀▀▀╗▄▄▒░░╚▀╗                                                   
        Æ▒░░▄▀╬╠╠╠╠╠╠╠▒▓▀░░░▒▓▀╬▒╬╠╠╠█╠╠╠╠╠╠╠╠▒╬▀▓▄░░░▀▄                                                
       █░░▓▒╠╠╠╠╠╠╠╠╠▓▒░░▒▄▀╬╠╠╠╠╠╠╠╠▓╬╠╠╠╠╠╠╠╬╠╠╠▒╬▓▄░▒╠▄                                              
      █░▄▀╠╠╠╡╠╠╠╠╠╣▀░░░▄▓░╠╠╠╠╠╠╠╠╠╠█╠╠╠╠╠╠╠▒╠╠╠╠╠╠╠░▀▓░▒╣▄                                            
     ▐▒▓▒╠╬╠╣█╠▒▄╝╣▌░░▒▓▒╠╠╠╠╠╠╠╠▓▓▒╫▓▒▒╠╬╠▓█╠╠╠▒╠╠╠╠╠╠╠╬▓░╚▌                                           
     █▓▒╠╬╠╠▌└    █▒░░█▒╠╠╠╠╠╠╠╠╠╠█╠▓╣█  ╙▀ ╫▒╣▀▒╠╠╠╠╠╠╠╠╠╬▓░▓                                          
     ▓▒╠╬▄▀╙     ▐░░Γ█╬╠╠╠╠╠╠░╬╠╠╠█╬╬╬█        ▐▓▒╠╠╠╠╠╠╠╠╠▒▓▒▓                                         
    ▐█╠╝`        █░╩█╠╠╠╠╠╠╠╠▓▓▒▓█╬╬╠╠▌           ╙▀╬▒╠╠╠╠╠╠╠╬▓▓                                        
    ╟█           ▌φ╫▒╠╠╠╠╠╠╠╠╠▌╙█╬▒╠╠╠▌               ╙▀╬▒╠╠╠╠░▓▓                                       
    ╙            ▌▒█╠╠╠╠╠╠╠╠╣▀  █╬▒╠╬╢▌                   `▀╬▒╠╠█▌                                      
                 ▒╫▒╠░╠╠╠╠▄▀    █╬╬╠╠╬▌                       ╙▀╬█▄                                     
                 ▌█╠╠█▓╬▓▀      █╬╬╠╠╠█                           ╙                                     
                 █▌╠╠╬⌐╙        █╬╬╠╠╠╫                                                                 
                 █▒▓▀           █▓╬▒╬╬╬▌                                                                
                 ╙▀             ╟▓╬╬╠╠╠╟                           ▄K▄                                  
                                └█╬╬╠╠╠╠█                Æ▓@╗╗▄,  ╟╔▒█                                  
                                 █▓╬╬╬╬╬╬█              █╠█▀█▓▓▓▓╬╬╬▀▓▌╗▄▄,                             
                                 ╙█╬╬╬╬╠╬╬▓            █╬█░▒╬█╬╬╬╬╣╫╬█▓▓▓▓▓╬╬█▓▄                        
                                  ╟╬╬╬╬╠╠╬╬▓         ,▓╬█╬╠╠╠╬█╬╬╬╬╣╫╬╬╬╬╬█╬▓▒▓▒╬▄                      
                                   █▓╬╬╠╠╠╠╠█       ╓▓╣█╬╠╬▒Å╢▓╬╬╬╣╫╬╬╬╬╣█╬█▒▓▒╟█╬▌                     
                                    █▓╬╬╠╠╠╠▒▓     ▄▒▓▒╬▒╣╬▒╠╣█╬╬╣╢╬╬╬╬▓▒╬█▒█░╬╢╣▒╫                     
                                    ╙╬╬╬╬╠╠╬╬╬▌   ▄▒╬█▓╣▓▓╬▓█╬╬╬╬╣╬╬╬╬█▒╣█╬█▒▒╣╬╣▒▓                     
                                     █▓╬╬╬▓█╠╢╬█╨╙╚╩╜╩╩▓▓▓█╬╬▓▓████╣╫█▒▓▌╣█╠╬╣╬▓▌╣▀                     
                                  ,▄╗╬██╨,╠╝█╫╩▀╥▄▄╣╥▄╧δ╟╟▒╬╨╫╨╩▓╫▓▓╬╬▓▒╫█▓╫▓╬╬▓▀                       
                                 █╬▀▓▓█▄▄╥╫▄▄▄èÆ▒µ╓à╜▀▀╣-╩╝▓▀╠▒▓S╬▓▓▓╣▌╙╙▀▀▀▀╙                          
                                 ▐╬╣█▓▓█████╣▓▓▀▄╫▓▌▐╬╠▒▄╗╬╬╬▓▓▀╬▒▓▒╬╣                                  
                                  █╬█╬█╠╫╬▓████"██*█▒╬╬▓▓▓╬╠╬▓▓▀╟╠╣▒╣█                                  
                                █╬█╬╫█╬▒▄██░▌╟╠▌▀▓╬╟▒╬▓▀╠╡╠╠▒╠╪╬╫╬╫▌                                  
                                ,▄█╬█╬╪╠╞╬╠░╣╠▌╫╣▌╟█╬╣▒╬█╠╠╡╠╠▒╬╡╬▓╠╬█╗▄,                               
                           ,▄Θ▒│∩░╚╫╬╬╬▓▓▄╪╠╣╠█╙▓▄╫█╬╣▒╬█╠╠╡╠╠▒╬▓╬█╠╣▒░╚░░╚▀╗▄                          
                        ▄Θ╙.¡░░;░│░░│╙▀▀▓╬╬▓╫▓╬▓▓╬╠█╠╣▒╬█╬╬▓╬╬▓▓╬╬▓▓▀░░░░░░╚░φ╚▀▄                       
                     ,Θ╙.¡░░░░││││││░│░░░│╙▀╫▓╬╬▓▓▓█╬╣▒╬█▓▓▓╬╬▓╝▀│┘░│░░░░│░░░░╚▒▒╚▀,                    
                   ▄▀ ;░░░░░││││││││││││░░\░░░│╙▀╣▓╬╬╣▌╬╬▓▓▀╙│░░││││││░░;░│░░░░░░╚░░▓,                  
      ,,-»⌐      ,▀.;░│░░░│░░░│││││││││░\│░░░░░│░░░│╙▀▀╙│░░░│││││││││░░░│░░░││░Γ░░░╠▒╚▓▒░└░Å            
    φ «▐ %▒░└╙φ░▄▀ ░░░░░░░░░░░░░││││░░░││││││░░░│││░Γ░░░░│││░░││││░░░░│││││░░░░░░░░░φ░▒╝▒φ└░▒▒▒▒░≥≥≈«,  
     `ⁿφ░░=-,`"╜╩╬▀▀▀▀▀╪╪#▄▄▄▄▄▄▄▄▄▄░░░░│││││││░░░░░░│││││││░░░░░░░;▄▄▄▄▄▄▄▄▄▄▄▄▄▄##▀▀▀░░╩░ ,µσσ≈≈╜╙"`  
            "ⁿφ░>-┌░'         ░╙╙╠░▄▓▀░░░░░░░░░░░░░░░░░░░░░░░░░╙▀╝▄│╙""""""░░ ░│\└          ▒ε «'≥      
              ░.²-,  ``"""ⁿⁿ²≈≈═≤φ▒╙╙╚╚▀▀▀▀▀▀▀###╪╪#╪╪╪╪╪╪#▀▀▀▀▀▀░Γ░')╜""""^`^```````````,,,-»=" ⌠      
              `"ⁿⁿ≈≈≈ⁿ""      ,-ⁿ  ⁿ═çµ,.  └│└░`""╙╙╙░╙╙╙╙╙╙""░      ,,Å               ```              
                            ,░ ░≥-,        ``^""""ⁿⁿⁿⁿⁿⁿⁿⁿ"""""``                                       
                             `"ⁿ=≈»≥σ≥≥≥≤≥≥≥δδδδ╚╚φ░≥      ,,--»=="                                     
                                                  'σ≥≡≥≥-≈ⁿ"`                                                                                                                                               

    ''')

    print("Welcome to Treasure Island!!")
    print("Your mission is to find the treasure.\n")

def separator():
    print("==========================================================================================")
    print("")

def victory(message):
    print(message)
    print('''
                                             ,,              e▒╬╫╬╣╬╬▒▒╗╗╖,         
                                   ,╓╖≥╦▒╬╬╣╫▓╬╬¼           ╘╬╬╫▄░╞╚╝╝╣▌╬╬╬▌        
                        ,╓╖╗@▒▒╬╠╠╫▓▓▓▓▓▓██████▌╚▒╗          ▌"╝., `"""╙` ╩         
             ,╓«≤#▒╠╬╬╬╫╫▓▓▓▓▓▓▓▓╬▓▓█████████▓▓██▌Å╬╗                    #          
      ╒å▒▒╠╬▄╫╣▓▓▓▓▓▓▓▓█████████▓▓██████▀╠╣▓▓▓▓▓▒█▀╨╣╠╗     .-w    <⌂   á           
      ▄░▓▌╠▓██████████████▓▓██▓▓▓▓▓▓▓▓╠▓▓╬╬╬╬╬╬╬╣▓▓▓▌░▓╬▌ / ▐▒φ╫"w,«⌐  ƒ            
      Æ╨░∞╫▌╬▓███████▓▓▓▓╬╬▓▓▓▓▓▓▓▓██#▓▒ ╢╬╬╝╬╫╬╟▓███▓╚▒└╙▀Å╚çz^ φ╗▀ -4@ ╜╗╢▓       
     ╝▄▓╫▓▀╩▀▄╠█▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓╝╬╬╬╣╣╬╫╬╝▒░╙▀▌ ╬╫▒  ,║x╜╨▀` ╙╕╙ │╨7╣▓▓▀▄  ..  
    #:)╬▓▓▓▌µ╫▓▒╬█▓▓╬╬╣▓▓███▓▓▓▓▓▓▓▌]▓▓▓╣▒╚░╙╬▓▌∩░φ▓▓▒  └"░Å,µ╗▓▒╗≡▀▄ Γ,)╣░│╠▌░▒ ░╓▄
    ▌Σ▌▓╬╫╬╢▓▒ ╠▓▒╫▓██▓▓▓╣▓▓▓▓▓▓▓▓▓▓╚▓╙ ╙▓░;┌¡[\░φ╠▌└ ▄▌ èεεεφ╩'╚µµ╦▌░ ╙╙└╘╦»α╠▒╟▓▌█
    ▓╬▌▓╩▄▒Å╟▓▓▄╫▀╬╠▓▓▓▓▓▓▓▓▓▓▓▓▓██▀▀╬#w≤╠▓▓Å╜▒╩. ▄▌╨╨▒▒▄ ,⌐└W » └░ó  ╓φ∩ '≥^▐╦▄▓▓▒╫
    ╘┌╚▓╬▒╠╬▒½╬╣▄]"▀▌╠▓▓▓▓▓▓▓█▓▓▓▀▀¬¬µ└╙└'╠╖«Å╙╠╠Σ ▐╚║╣║▓.  ╒▒▄┘"╙▓╠╙"└╠▒▄ ,╫▄╝▓╣╫╩▌
     ╟▄▓╫╩╙░φ▒▒╣▀╣▓╬╨▀▒╬█████▀ ├ Θ▒▒╩╙.---   ╖.»φ▒⌐ ,╠╢╣▒,Å╩╩▐╦αφ▒╙║▄╦▒╩▓▓▄▄▓▓`╠╣╫╬▌
      ╙░╙▒▄δφ╟╬▒╣╬╬▓▄"╠▓╬╬▓▓▓╙T/    ╘φφφ▒╜╒^  ╙▄ ]▒  ,╣j--εφ╩K╙╙╬▄φ▓▓╬▓▌~▓╬╬▓╬▌╓▓╫╠▌
       ^▄║╣▒╬░Å╠╬╬╬╣ ╙╬▒╬▓▓▄╠▒╙φ╛ Å .╟▀╨  ╠▓▓╫╩╙  ╙╚╚╙ Γ ╩═ç▐,',╩╣╬╣▒╬▓╬▒╙╬╣╫╬▌¬▓▌╬▌
         ╙Q ╙▓▄▄▓╣╝╥╓▓▓╣▓▓▄▄▌ └╠╬▄▓#╩  ╬b╟    µ -¬¬ⁿw ½,▌  ]▌░j▓▒▌▒▒▓▒▓╬▓,▓╣╬╬╝▐▌▓╫⌐
           "╪▄▌,,▐╗▓█╝╙   b ▓▓▓╣▓▓▄,@Θ▌▌,╙╨╢╝╢ ╟▒≥╖≥Q╙.╡╠╙▀╬╣╗╬▓▓▓▄╬▓▓╬╬╣▌▌, ▄▓▓▌▌╟ 
               └╙╙        ╟-▓▓╫╙▌╠▌╩╬╣╬▓▓╣ ╟^╟▌╙╙╬╬╠╦╣⌐┤╣▓▓▓█▓▓╬╬╬╬▓╬╬╬╬╬╬▓╣╬╣▓▓╬╫▓ 
                          "▀╣╣╟░▌░╡φ╡║░╠╠║.╫`╟╬╣▓▀╩▓╬▓"¼╣╬▓╣▓╬▓╬▓╣╣▓╬╣╬▓╬╬▓▓▓╬╣▄╩`  
                           ▌ ▌▒░▓░░▐▓╬╬▓▓╚»╩▒▐▒╢▒▒'▌╠▓`]┴╬╬╣█╬╣╬╣╬╬▓▓╣╬▓▓╬╬╬╠╣╙     
                           ║▄▓▌░╫φ▐▓▌╬╬╣█▒▒⌐╩,▒╠▒▌╠█▄▓▄j"╣╬╬█╬╬╬╣╬╣▓▓╬╬╫╬╬╣╨        
                            ╛╟╫░╣╫▓█╣▓╬╬▓█▒▒`}┴╬▒▌╙▓╠▓,╫ ╟╣╬█╬╬╬╣▓▓▓▓▓╬▄▀`          
                            ▌╠╣░╣╬▌╙╠╠▌▀▓▓▓▒╫╦ƒ╙▒▌┴▓"y╣▓▒▐╣╬█╬▓╬╣▓╬╬╬▓╙             
                            ╟╙╬▒╠╣╬╩▄▄▌▄╬▓▓╬▓▒╬▓╓▄▄▄▓▓╣▓-╫╣╬█▓▓▌▀▒▓▀                
                             ▒╝╬╬▒╬▓▓▓▓▓▓╬▒▌▓▒╠▒╬▄╨╙╜╫`%╣╬╣╬╫╬▒▓▀                   
                             ▀▀╬µΓ╠▓╙╝╬╬╩╬▒▒▓▒║▒▒▌╙▓▒▓▓▓╬▓▀╫╬╝╙                     
                                  └╙Φ╣▄▓╚╙╙╝╫╬╫╬▒▓▀▓╬▓▓▀╠╠▓╨                        
                                        `╙Φ╣▄╣▒│▒╫φ╟▒╟▒▄▀                           
                                              `╙╝▓▓▓╬▓└                                                                                                             
    ''')

def death(message):
    print(message)
    print('''
                        ,▄██████▄▄                    
                     ▄██████████████▄                 
                    ██████████████████▄               
                   ████████████████████µ              
                  j████████████████████▌              
                   ████    ▐███    ╙███▌              
                   ╙██▌    ████▄    ██▀               
                   █████████  █████████               
                    ╙▀██████████████▀▀                
                      ██╙████████▀▄█                  
          ╓▄█▄        ╟█▌▀▐▌█╟██▀ ██        ,██▄      
         ██████µ      └██▄ Æ@█@ ▄██▀      ,██████     
      ▄██████████       ▀█████████      ,██████████▄ 
      ██████████████▄      `         ╓▄█████████████▌ 
        ╙▀▀▀▀███████████▄,      ,▄███████████▀▀▀▀▀    
                  `▀▀████████████████▀▀╙              
                      ,▄███████████▄                  
                ,▄▄████████▀▀▀▀████████▄▄,            
       ▄▄██████████████▀`         ▀▀█████████████▄▄   
      █████████████▀                  ╙▀████████████▌ 
      ╙▀████████▀                        ╙█████████▀  
         ▀█████                            ▀█████     
           ╙▀                                ╙▀                                                                                                         
    ''')    

def check_answer(intro,q1,condition,q2):
    print(intro)
    while True:
        try:
            ans=input(q1)
            if not condition(ans): raise ""
            break
        except:
            print(q2,end=" ")
            continue
    return ans

# Intro
intro()

# 1-0
a1 = check_answer(
    intro = '''You wake up on a desert island, nobody is around and you don't remember how you got there.
You start walking through the forest trying to find a way out, when you get to a fork.''',
    q1= "Where do you wanna go? Type 'left' or 'right'\n",
    condition = lambda x: x.lower() in ["left","right","l","r"],
    q2 = "There is no other way, and you can't go back.",
)
separator()

# 2.1-1
if a1.lower() in ["left","l"]:
    a2 = check_answer(
    intro = '''After walking for a little while you come to a lake, with a little isle in the middle of it.''',
    q1 = "Type 'wait' to wait for a boat. Type 'swim' to try and reach the isle swimming.\n",
    condition = lambda x: x.lower() in ["swim","wait","s","w"],
    q2 = "There are no other options.",
    )
    separator()

# 3.1-2.1
    if a2.lower() in ["swim", "s"]:
        a3 = check_answer(
        intro = '''You start swimming, and with much effort you reach the little isle in the middle of the lake.
You feel completely drained and you are hungry.
Close to the shore you spot a book covered in the sand.''',
        q1 = "Type 'take' to take the book. Type 'leave' to leave it where it is.\n",
        condition = lambda x: x.lower() in ["take","leave","t","l"],
        q2 = "hmm..I'm starving! Should I take that book or not?!",
        )
        separator()

# 4.1-3.1
        if a3.lower() in ["leave", "l"]:
            a4 = check_answer(
            intro = '''Naah there's something strange surrounding that book, better leave it where it is.
    You keep walking when you reach an oasis with 3 caves.''',
            q1 = "Type '1' to enter the first cave. Type '2' to enter the second cave. Type '3' to enter the third cave.\n",
            condition = lambda x: x in ["1","2","3"],
            q2 = "There's a heavy storm about rage on here! Better get insde one of the caves!\n",
            )
            separator()

# 5.1-4.1
            if a4.lower() == '1':
                victory(message = '''WOOOOOOOW You find a worthless trasure inside the cave!!!
                CONGRATULATONS!!''')
            
# 5.2-4.1
            elif a4.lower() == '2':
                death(message = '''
You find shelter inside the cave. You feel cold and you start looking for some rocks and pieces of wood to start a fire.
You see a nice rock and decide to take it, when a venomous snake gets out from under the rock and bites you!
You DIE poisoned.''')

# 5.3-4.1
            else:
                death(message = '''As you enter the cave you hear a strange noise. You feel like you are not alone...
All of a sudden a gian spider crawls towards you! You try to escape but there's no way out.
You become its DINNER!''')

# 4.2-3.1
        else:
            death(message = "As you approach to get the book, a huge hole form around you and you get swallowed into it, never to be seen again!")
# 3.2-2.1
    else:
        death(message = "You wait until you DIE starving.")
# 2.2-1        
else:
    death(message = "You were attacked by a giant tiger!!\nYou DIED.")