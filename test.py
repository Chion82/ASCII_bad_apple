from PIL import Image

ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

def scale_image(image, new_width=100, new_height=0):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    if new_height == 0:
        new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=3.69):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image, 100, 30)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            xrange(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception, e:
        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
        print e
        return

    image_ascii = convert_image_to_ascii(image)
    return image_ascii

if __name__=='__main__':
    import os
    import time 
    import cv2
    vidcap = cv2.VideoCapture('test.mp4')
    time_count = 0
    frames = []
    video_length = 218
    while time_count <= video_length*1000:
        print('Generating ASCII frame at ' + str(time_count))
        vidcap.set(0, time_count)
        success, image = vidcap.read()
        if success:
            cv2.imwrite('output.jpg', image)
        frames.append(handle_image_conversion('output.jpg'))
        time_count = time_count + 100

    f = open('play.txt', 'w')
    f.write('SPLIT'.join(frames))
    f.close()

#    os.system('mplayer -vo null -vc null test.mp4 &')
#    for frame in frames:
#        os.system('clear')
#        print(frame)
#        time.sleep(0.1)
#    vidcap.set(0, 20000)
#    success, image = vidcap.read()
#    if success:
#        os.system('clear')
#        cv2.imwrite('output.jpg', image)
#        handle_image_conversion('output.jpg')



