import base64, requests

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

class PostCover:
    
    @classmethod
    def default_cover_colors(cls):
        return (124, 89, 81), (253, 209, 130)
    
    @classmethod
    def font_style(cls, style) -> str:
        return f'https://github.com/JulietaUla/Montserrat/raw/master/fonts/ttf/Montserrat-{style}.ttf'
    
    @classmethod
    def download_font(cls):
        url = cls.font_style('Bold')
        
        response = requests.get(url)
        response.raise_for_status()
        return BytesIO(response.content)
    
    @classmethod
    def download_image(cls, url):
        response = requests.get(url)
        response.raise_for_status()
        return BytesIO(response.content)

    @classmethod
    def add_title(cls, title, font_size, image_url):
        title = str(title)
        font_size = int(font_size)
        
        if len(title) >= 56:
            title = title[:53] + '...'
        
        try:
            font_file = cls.download_font()
            font = ImageFont.truetype(font_file, font_size, encoding='utf-8')
        except Exception as e:
            raise ValueError(f'Error loading font: {e}')
        
        try:
            image_file = cls.download_image(image_url)
            image = Image.open(image_file).convert('RGB').resize((800, 300))
        except OSError as e:
            raise ValueError(f'Error opening image: {e}')
        
        draw = ImageDraw.Draw(image)
        text_bbox = draw.textbbox((0, 0), title, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        
        width, height = image.size
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        
        shadow_offset = 3
        shadow_color = cls.default_cover_colors()[0]
        draw.text((x + shadow_offset, y + shadow_offset), title, font=font, fill=shadow_color)
        
        text_color = cls.default_cover_colors()[1]
        draw.text((x, y), title, font=font, fill=text_color)
        
        return image

    @classmethod
    def save_image(cls, image, output):
        buffered = BytesIO()
        image.save(buffered, format='PNG')
        
        img_str = base64.b64encode(
            buffered.getvalue()
        ).decode('utf-8')
        
        image_png = Image.open(
            BytesIO(
                base64.b64decode(img_str)
            )
        )
        
        image_png.save(output, format='PNG')

    @classmethod
    def generate(cls, params:dict):
        image = cls.add_title(params.title, params.size, params.image)
        return cls.save_image(image, params.output)
