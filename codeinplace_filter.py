"""
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file name from user input
    filename = get_file()
    
    # Load image and show image before the transform
    image = SimpleImage(filename)
    image.show()

    # Apply the filter
    for pixel in image:
        new_red = pixel.red * 1.5
        new_green = pixel.green * 0.7
        new_blue = pixel.blue * 1.5
    #assign the new filter
        pixel.red = new_red
        pixel.green = new_green
        pixel.blue = new_blue
    # Show the image after the transform
    image.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()
