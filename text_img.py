from PIL import Image, ImageFont, ImageDraw


def text_image(image_path,title_text):
    '''
    image_path : path to the original image that we want to modify
    title_text : the text we want to add to the image

    It returns the None if image path is not Valid else returns the modified image path save in the same directory where original image is located.
    '''
    try:
        my_image = Image.open(image_path)
    except:
        return None
    width, height = my_image.size
    # arial.ttf - I have downloaded this font from other source
    # source url - https://github.com/JotJunior/PHP-Boleto-ZF2/blob/master/public/assets/fonts/arial.ttf
    title_font = ImageFont.truetype('arial.ttf', int(float(width) / 8))
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)

    # create path to save the text image
    img_path_split = image_path.split('/')
    if len(img_path_split)>1:
        img_path_split[-1] = 'text_' + img_path_split[-1]
        text_img_file = '/'.join(img_path_split)
    elif len(img_path_split)==1:
        text_img_file = 'text_' + image_path

    my_image.save(text_img_file)

    return text_img_file


print(text_image('/home/gadget/Desktop/text_image/jubliee.jpeg','Jubilee Park'))