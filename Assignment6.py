from textwrap import dedent
from random import randint

class song1():
    def love_boat1(self):
        print(dedent("""Love, exciting and new
        Come aboard, were expecting you
        Love, lifes sweetest reward
        Let it flow, it floats back to you
        Love Boat soon will be making another run
        The Love Boat promises something for everyone
        Set a course for adventure
        Your mind on a new romance
        Love wont hurt anymore
        Its an open smile on a friendly shore
        Yes love...
        Its love...
        Love Boat soon will be making another run
        The Love Boat promises something for everyone
        Set a course for adventure
        Your mind on a new romance
        Love wont hurt anymore
        Its an open smile on a friendly shore
        Its love...
        Its love...
        Its love...
        Its the Love Boat
        Its the Love Boat"""))


class song2():
        def love_boat2(self):
            print(dedent("""
            You're just too good to be true I can't take my eyes off you
            You'd be like heaven to touch I wanna hold you so much 
            At long last love has arrived And I thank God I'm alive
            You're just too good to be true Can't take my eyes off you
            Pardon the way that I stare There's nothing else to compare
            The sight of you leaves me weak There are no words left to speak
            But if you feel like I feel Please let me know that is real
            You're just too good to be true I can't take my eyes off you
            """))



class song3():
        def love_boat3(self):
            print(dedent("""
            Many days I've longed for you
            Wanting you
            Hoping for the chance to get to know you
            Longing for your kiss
            For your kiss, for your touch, for your essence (your beautiful essence)
            Many nights I've cried from the things you do 
            Felt like I could die from the thought of losing you
            I know that you're real
            With no doubt or no fears
            Or no questions
            Love
            So many people use your name in vain
            Love
            Those who faith in you sometimes go astray
            Love
            Through all the ups and downs the joy and hurt
            Love
            For better or worse I still will choose you first
            """))



song1().love_boat1()


board = input("Do you wish to board the Love Boat?")
if board == 'yes' or board == 'Yes':

    print("""You enter into a tunnel of love with 6 streams.
    Each stream holds your fate down them.
    Either you can row merrily down the stream, or you 
    can become ship wrecked on Giligans Island. Choose wisely!""")
elif board == 'no' or board == 'No':
  print ("Sorry for asking...")

else:
    print()
stream = input("> ")


if stream == "1":
    print("You row down the first stream, you hear a woman giggle.")
    print("To your surprise you see a 300 lb Hillbilly.")
    print("She grabs you and starts kissing you......")
    print(".............")
    print("SHIP WRECKED!!!!!!!")
    print("Should've chose more wisely")

elif stream == "2":
    print("You row down the second stream, you see a beautiful woman.")
    print("You immediately jump off the boat to pursue her.")
    print("""In the blink of an eye her 12 kids run out screaming,
    Daddy Daddy ......""")
    print(".............")
    print("SHIP WRECKED!!!!!!!")
    print("Should've chose more wisely")

elif stream == "3":
    print("You row down the third stream,you see the woman of your dreams .")
    print("Beautiful face, slim waist...Your mind is blown.")
    print("You both gaze into each other eyes, and immediately fall in love......")
    print(".............")
    print("Wedding Bells!!!!!!!")
    
    song2().love_boat2()
    print("HOORAAAAAYYYYYYYY")


elif stream == "4":
    print("You row down the fourth stream, you see something, but not sure of what it is.")
    print("When you finally get a good glance you notice that it's a man!!!")
    print("He is cock-eyed, has yellow teeth and holds an unbearable stinch")
    print("Before he can grab you you jump into the stream and drowns yourself......")
    print(".............")
    print("SUICIDE!!!!!!!")
    print("Should've chose more wisely")

elif stream == "5":
    print("You row down the fifth stream, you see a shadow moving swiftly down the bank.")
    print("You start screaming, REVEAL YOURSELF!!!!")
    print("A rabid wolverine jumps onto the boat and eats your face")
    print(".............")
    print("SUDDEN DEATH!!!!!!!")
    print("Should've chose more wisely")

elif stream == "6":
    print("You row down the sixth stream, you see a handsome man")
    print("He stands at 6ft tall, muscular, with a nice smile")
    print("You melt in his arms.....")
    print("He carries you away to his man-made hut!")
    
    song3().love_boat3()
    print("HOORAAAAAYYYYYYYY")

song1().love_boat1()















