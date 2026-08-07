from datetime import datetime

today = datetime.now()

def date(event=False):
    if event:
        match event:
            case 'anniv':
                print(r"""
🎉 Joyeux anniversaire !

       i i i
      | | |
    =========
   |  HAPPY  |
   | BIRTHDAY|
   |_________|

   Elric : 16y
""")

if today.month == 7 and today.day == 18:
    date('anniv')
