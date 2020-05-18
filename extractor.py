import pytesseract
import cv2
import click


def convert_to_RGB(img):
    """By default cv2 (openCV) stores images in BGR format, 
    we need to convert to RGB format for (py)tesseract.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


@click.command()
@click.option('--img', help='The path to the image to use.')
@click.argument('keyword')
def execute(keyword, img):
    img = convert_to_RGB(cv2.imread(img))
    content = pytesseract.image_to_string(img) # extract content from image
    data = [text.lower() for text in content.split('\n') if text != '' and text != ' ']
    result = by_keyword(keyword, data)
    # echo result on the terminal
    if result:
        click.echo(f'{result}')
    else:
        click.echo('No match found')

def by_keyword(keyword, lines):
    data = {}
    for line in lines:
        if line.startswith(keyword.lower()):
            temp = line.split(' ')
            data.update({temp[0]: temp[1]})
    return data


if __name__ == '__main__':
    execute()
