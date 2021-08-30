from datetime import date
import random

print('           /^\/^\\')
print('         _|__|  O|')
print('\/     /~     \_/ \\')
print(' \____|__________/ \\')
print('        \_______     \\')
print('                `\     \                 \\')
print('                  |     |                  \\')
print('                 /      /                    \\')
print('                /     /                       \\\\')
print('              /      /                         \ \\')
print('             /     /                            \  \\')
print('           /     /             _----_            \   \\')
print('          /     /           _-~      ~-_         |   |')
print('         (      (        _-~    _--_    ~-_     _/   |')
print('          \      ~-____-~    _-~    ~-_    ~-_-~    /')
print('            ~-_           _-~          ~-_       _-~')
print('               ~--______-~                ~-___-~')
input('Press Enter')

print('Today is', date.today().strftime('%A'))
print('Have a nice day')
input('To continue press enter')

'''
Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
Zakladamy ze:
-liczba mrugniec na minute to 20
-liczba minut w godzinie to 60
-liczba godzin w dobie 24
-liczba lat (czyli nasz X) 50
Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
powinna wynosic 16
'''
# liczba mrugniec okiem na minute
blinksPerMin = 20
# liczba minut na godzine i liczba godzin w dobie
minInHour = 60
hoursInDay = 24
daysInYear = 365
# liczba lat
years = 50
# liczba mrugniec w ciagu X lat
print(blinksPerMin * minInHour * hoursInDay * daysInYear)
# definitionOfVariables
daysOfWorkPerMonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
# result
print((daysOfWorkPerMonth * monthsInYear - vacation) * yearsOfWOrk)

ProgramName = 'BBC'
Item = 'News'
Time = '18:00'

print('I like watching', Item, 'at', Time, 'on', ProgramName, '.')
print('I like watching ', Item, ' at ', Time, ' on ', ProgramName, '.', sep='')

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one', '1'))
print(quote.replace('one', '1').replace('both', '2'))

firstName = 'Kasia'
familyName = 'Sowa'
lastName = 'Mrugała'
newName = firstName + ' ' + familyName + ' ' + lastName
print(newName)

music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
print(music)
music = '"Universal Fanfare" Jerry Goldsmith\n "Happy Together" Garry Bonner\n "I\'m a Man" Steve Winwood'
print(music)

print('(\\(\\')
print('( -.-)')
print('O_(")(")')

article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and influence, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]

Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, including Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.

At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution To Cinema. In 1998, they were awarded the AFI Star Award by the American Film Institute. Many sketches from their TV show and films are well-known and widely quoted. Both Holy Grail and Life of Brian are frequently ranked in lists of greatest comedy films. In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]'''

print(article.upper())
print(article.lower().replace('monty', 'flying'))
print(article.split(' '))
print('Word python appears', article.lower().count('python'))

print('to print the \\ you need to put \\ twice in your text like this: \\\\')

print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")

amountPLN = 234
print('cur      exchange    amount')
print('USD      3.65    ', amountPLN / 3.65)
print('EUR      4.23    ', amountPLN / 4.23)

ValueAsText = 123.45
factor = 1.23

print('Value is', ValueAsText, 'factor is', factor, ValueAsText.__float__() * factor)

helloMessage = "Hello %s!"

print(helloMessage % ("Kate"))
print(helloMessage % ("Chris"))

helloMessage = "Hello {0:s}!"

print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))

helloMessage = "%s has %d %s"

print(helloMessage % ("Kate", 1, "animal"))
print(helloMessage % ("Chris", 100000, "$"))

helloMessage = "{0:s} has {1:d} {2:s}"

print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, "$"))

line = "{0:20s} costs {1:6d} €"

print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAWAII", 6))

name = "Filip"
age = 32
daysInYear = 365
message = "%s is %d years old, so is about %d days old"

print(message % ("Jan", 26, 9490))
print(message % (name, age, age * daysInYear))

message = '{0:s} is {1:d} years old, so is about {2:d} days old'

print(message.format("Chris", 17, 6205))
print('1234567890 divided by 12345 is', 1234567890 // 12345, 'and the rest is', 1234567890 % 12345)

# is the light switch in AUTOMATIC mode
isAutomaticMode = True

# is the level of day-lighr above 80%
is80PercentLight = True

# is the Sun ligthing directly into the driver's face
isDirectLight = False

# is it rainy, foggy or other weather conditions are present
isRainy = False

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'

print(v1, type(v1))
print(v2, type(v2))
print(v3, type(v3))
print(v4, type(v4))
print(v1 + v3, type(v1 + v3))
print(v2 + v4, type(v2 + v4))
print(7 - 1 * 0 + 3 + 3)
print(4 ** 5 / 2 ** 3)
print(99 + 9 / 9)

q = 'THE EYES'
print(q)
print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

q = "a gentleman"
print(q)
print(q[3], q[6], q[7], q[2], q[0], q[4], q[5], q[1], q[8:])
print(q[3] + q[6] + q[7] + q[2] + q[0] + q[4] + q[5] + q[1] + q[8:])

q = "THE MORSE CODE"
print(q[1:3] + q[6] + q[8:12] + q[4] + q[2:4] + q[12] + q[11] + q[0] + q[7])
print(q[1:3], q[6], q[8], q[3], q[10:12], q[4], q[13], q[9], q[12], q[5], q[0], q[7])
'''
line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(':')+2:]
print(time)
tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[: tmp.find('"')]
print(title)
print(title, time)
'''
line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(':') + 2:]
print(time)
tmp = line[line.find('"') + 1:]
title = tmp[: tmp.find('"')]
print(title, time)

print((38 * 5 + 50) * 20 + 1017 - 1988)
shoeSize = 38
number = (shoeSize * 5 + 50) * 20 + 1017 - 1988
print('Shoe size is:', number // 100)
print('birth date is:', number % 100)

hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM',
              'WISH YOU WERE HERE']
print(hitsTitles)
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
print(hitsTitles)
hitsTitles.insert(2, "HOTEL CALIFORNIA")
print(hitsTitles)
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles)
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
print(hitsTitles)
hitsTitles[0] = 'ENJOY THE SILENCE'
print(hitsTitles)
hitsToRead = hitsTitles.copy()
print(hitsToRead)
print(hitsToRead.reverse())
print(hitsToRead.sort())
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
print(hitsToRead)
additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
print(additionalSongs)
print(hitsToRead.extend(additionalSongs))
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))
hitsToRead.clear()
print(hitsToRead)

marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2, 'investor relations')
print(marketing)
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
print(internalEmails)
emailMarketing.extend(internalEmails)
print(emailMarketing)
emailTuple = tuple(emailMarketing)
print(emailTuple)

channels = {'Google': 1480, 'Email': 300, 'Natural Traffic': 440, 'TV Spot': 700}
print(channels)
print(channels['Email'])
channelsUpdate = {'Natural Traffic': 520, 'News': 600}
print(channelsUpdate)
channels.update(channelsUpdate)
print(channels)
print(channels.keys())
channels.pop('Email')
print(channels)

MIN_LIKES = 500
MIN_SHARES = 100
num_likes = 2000
num_shares = 999

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('We have today drop prizes about 10%!!')
else:
    print('We still need more likes and shares to promotion!')

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('You have coupon for burger!')
else:
    print('To get the promotion order pizza or big drink on week day')

diskSize = 100
diskSizeUsed = 80
fileSize = 1

if fileSize <= diskSize - diskSizeUsed:
    print('File can be downloaded')
else:
    print('You don\'t have enough free space on disk')

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('We have today drop prizes about 10%!!')
else:
    if num_likes < MIN_LIKES:
        print("We still need more likes")
    else:
        print("We still need more shares")

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('We have today drop prizes about 10%!!')
elif num_likes < MIN_LIKES:
    print('We still need more likes')
else:
    print('We still need more shares')

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('You have a coupon for burger')
else:
    if isWeekend:
        print('For free burger come back on non-Weekend day')
    else:
        print('For free burger order pizza or big drink')

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('You have a coupon for burger')
elif isWeekend:
    print('For free burger come back on non-Weekend day')
else:
    print('For free burger order pizza or big drink')

musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print('Suspicion of influenza')
else:
    print('The flu is unlikely')

if musclePain and fever and weakness:
    print('Suspicion of influenza')
elif weakness and not (musclePain or fever):
    print('Just take a rest!')
else:
    print('You may be cold')

isMan = True

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print('Suspicion of influenza')
elif weakness and not (musclePain and fever):
    print('Just take a rest!')
else:
    print('This only be cold')

isCheckCompleted = False

print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET!')

firstRow = 1
lastRow = 31
currentRow = firstRow
while currentRow <= lastRow:
    print('Row number: ', currentRow)
    currentRow += 1

start = 1
end = 13
number = start
while number <= end:
    print(number, number * number, number * number * number)
    number += 1

start = 0
end = 16
x = start
while x <= end:
    print(x, 2 ** x)
    x += 1

start = 1
end = 10
num = start
while num <= end:
    print(num * 'x')
    num += 1

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) - 2
while i < max:
    print(i, numbers[i], numbers[i + 1])
    if numbers[i] ** 2 == numbers[i + 1]:
        print('\tFOUND!')
    i += 1

while i < max:
    print(i, numbers[i], numbers[i + 1], numbers[i + 2])
    if numbers[i] ** 2 == numbers[i + 1] and numbers[i + 1] ** 2 == numbers[i + 2]:
        print('\tFOUND!')
    i += 1

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
i = 0
max = len(texts) - 1
while i < max:
    print(i, texts[i], texts[i + 1])
    if len(texts[i]) == len(texts[i + 1]):
        print("\tFOUND!")
    i += 1

number = 1
previousNumber = 0
while number <= 50:
    print(number + previousNumber)
    previousNumber = number
    number += 1
'''
my_number = random.randint(0, 20)
guess = -1
print("I draw number from 1 to 20, guess my number!")
while guess != my_number:
    guess = int(input())
    if guess == my_number:
        print('Congratulation, it was:', my_number)
    elif guess > my_number:
        print('Sorry - my number is smaller than your guess, Try again!')
    else:
        print('Sorry - my number is greater than your guess, Try again!')

my_number = random.randint(0, 20)
trials = 0
guess = -1
print("I draw number from 1 to 20, guess my number!")
while guess != my_number:
    guess = int(input())
    if guess == my_number:
        print('Congratulation, it was:', my_number, 'and you guessed after', trials, 'trials.')
    elif guess > my_number:
        print('Sorry - my number is smaller than your guess, Try again!')
    else:
        print('Sorry - my number is greater than your guess, Try again!')
    trials += 1
'''

data = ['Error:File cannot be open', 'Error:No free space on disk', 'Error:File missing', 'Warning:Internet connection'
        ' lost', 'Error:Access denied']

for s in data:
    print(s.upper())

for s in data:
    elements = s.split(':')
    print(elements[0].upper())
    print(elements[1])

for s in data:
    elements = s.split(':')
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)

for i in range(9):
    print(string_A, '\n', string_B)

for i in range(1, 10):
    print("x"*i)

for i in range(1, 10):
    if i % 2 == 0:
        print("x"*i)
    else:
        print("o"*i)

i = 10
result = 1

for j in range(1, i + 1):
    result *= j

print(result)

x = 10

for i in range(1, x + 1):
    result = 1
    for j in range(1, i + 1):
        result *= j

    print(result)

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(noun, adj)

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or ' \
       'machine system. The device preserves the input power and simply trades off forces against movement to obtain' \
       ' a desired amplification in the output force. The model for this is the law of the lever. Machine components' \
       ' designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits ' \
       'power without adding to or subtracting from it. This means the ideal mechanism does not include a power' \
       ' source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance' \
       ' of a real system relative to this ideal.'

short_text = ''
words = text.split(' ')
counter = 0

for word in words:

    short_text += word+' '
    counter += 1

    if counter >= 20:
        print(short_text)
        break

definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or'
    ' machine system. The device preserves the input power and simply trades off forces against movement to obtain'
    ' a desired amplification in the output force. The model for this is the law of the lever. Machine components'
    ' designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power'
    ' without adding to or subtracting from it. This means the ideal mechanism does not include a power source,'
    ' is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real'
    ' system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt,'
    ' ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und'
    ' Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando'
    ' un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para'
    ' contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale'
    ' dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une'
    ' force importante transmise au système de freinage pour une course de faible distance.'
    ]

for definition in definitions:

    words = definition.split(' ')
    short_text = ''
    counter = 0

    for word in words:

        short_text += word+' '
        counter += 1

        if counter>=20:
            print(short_text)
            break

menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''

smile = '''

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''

while True:
    print(menu)
    letter = input('Enter from menu: ')
    if letter == '1':
        print('Function COFFEE not implemented')
        input('Please press enter')
        continue
    if letter == '2':
        print('Function TEA not implemented')
        input('Please press enter')
        continue
    if letter == '3':
        print(smile)
        input('Please press enter')
        continue
    if letter == '0':
        break
    print('You need to make a valid choice. Press ENTER and try again!')
    input('PRESS ENTER, to back to menu')

def print_cat():
    # this function prints a cat ascii-art
    txt = r'''
|\---/|
| o_o |
 \_^_/'''
    print(txt)
    return

def print_bear():
    # this function prints a bear ascii-art
    txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    print(txt)
    return


def print_bat():
    # this function prints a bat ascii-art
    txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
    print(txt)
    return


print_cat()
print_bear()
print_bat()
