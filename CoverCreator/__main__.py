from flags import Flags
from post_cover import PostCover

flags = Flags.parser("Usage: python covercreator -t <COVER_TITLE> -i <IMAGE_URL> -fs <FONT_SIZE> -o <IMAGE_OUTPUT>", [
    {'short': 's', 'long': 'size', 'help': 'Font size', 'required': True},
    {'short': 't', 'long': 'title', 'help': 'Cover title', 'required': True},
    {'short': 'i', 'long': 'image', 'help': 'Background image url', 'required': True},
    {'short': 'o', 'long': 'output', 'help': 'Image output address', 'required': True},
])

if __name__ == '__main__':
    PostCover.generate(flags)
