from io import BytesIO


class BufferedImageHandler:

    def create_buffer_image(self, barcode_tag):
        image_buffer = BytesIO()

        barcode_tag.write(image_buffer)
        image_buffer.seek(0)

        image_content = BytesIO(image_buffer.getvalue())
        return image_content
