from PIL import Image
import os, numpy

# Parameters
input_directory = 'input'
output_directory = 'output'
resolution = (512, 512)
icon_width = 330
white = (255, 255, 255)
black = (0,0,0,255)

for filename in os.listdir(input_directory):
    input_file = os.path.join(input_directory, filename)
    output_file = os.path.join(output_directory, filename)

    # Load base icon image
    img = Image.open(input_file, 'r')
    img = img.convert('RGBA')

    # Convert Black to White
    data = numpy.array(img)
    red, green, blue, alpha = data.T
    white_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][white_areas.T] = white
    img = Image.fromarray(data)

    # Combine icon into a black backgreound
    wpercent = (icon_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((icon_width, hsize), Image.Resampling.LANCZOS)
    img_w, img_h = img.size
    bg = Image.new('RGBA', resolution, black)
    bg_w, bg_h = bg.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 5)
    bg.paste(img, offset, mask=img)

    #Save the file
    bg.save(output_file)