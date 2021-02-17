#! python3
# customSeatingCards.py - Creates a seating card image, with the guest name on top, custom image below and a black outline.
#
# NOTES:  The program will get names of guests from a text file called 'guests.txt'. 
#         To change the card, you'll need to modify quite a few places in the code, depending on what you want to change.

from PIL import Image, ImageDraw

# Read the names from the txt file and save them into a list.
f = open('guests.txt')
names = f.readlines()
names = [name.rstrip() for name in names] # Strip the newline character from each name.
f.close()

for name in names:
    # Generate image file.
    im = Image.new('RGBA', (288, 260), 'yellow')

    # Add guest name to image.
    draw = ImageDraw.Draw(im)
    draw.text((120, 20), name, fill='blue', align='center')

    # Add png to image.
    imToPaste = Image.open('example.png')
    im.paste(imToPaste, (30, 50))

    # Add black rectangle to the edges of the image.
    draw.line([(0, 0), (287, 0), (287, 259), (0, 259), (0, 0)], fill='black')

    im.save('_' + name + '_card.png')

