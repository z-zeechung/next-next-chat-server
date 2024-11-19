from paint.Paint import Paint


class DummyPaint(Paint):

    def paint(self, prompt: str, image: str) -> str:
        from PIL import Image, ImageDraw, ImageFont
        import base64
        import io

        # 创建一个新的图像
        width, height = 1280, 768
        image = Image.new('RGB', (width, height), '#C4F1F9')

        # 获取绘图对象
        draw = ImageDraw.Draw(image)

        # 定义文字内容和字体
        text = "This is a dummy image.\nPrompt: "+prompt
        font_size = 72
        font = ImageFont.load_default(font_size)

        # 计算文字大小并获取位置
        text_x = 20
        text_y = 20

        # 在图像上绘制文字
        draw.text((text_x, text_y), text, font=font, fill="#2B6CB0")


        # 将图像保存到字节流中
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # 创建Base64 URL
        img_url = f"data:image/png;base64,{img_str}"

        # 打印或使用Base64 URL
        return img_url