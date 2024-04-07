from langchain_community.llms import Ollama
import base64
from io import BytesIO

from IPython.display import HTML, display
from PIL import Image


class imageAnalysis:
    def __init__(self, file_path):
        self.llm = Ollama(model="llava")
        self.file_path = file_path

    def convert_to_base64(self):
        """
        Convert PIL images to Base64 encoded strings

        :return: Re-sized Base64 string
        """
        pil_image = Image.open(self.file_path).convert("RGB")  # Convert RGBA image to RGB
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")  # You can change the format if needed
        img_str = base64.b64encode(buffered.getvalue())
        return img_str

    def invoke(self, prompt):
        image_b64 = self.convert_to_base64()
        llm_with_image_context = self.llm.bind(images=[image_b64.decode("utf-8")])
        return llm_with_image_context.invoke(prompt)


# result = imageAnalysis(r"c:\Users\origi\Pictures\Screenshots\Review.png").invoke("Analyse reviewing of customer comments.")
# print(result)