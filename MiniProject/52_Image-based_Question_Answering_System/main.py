from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image

# wget -O image.jpg "link"
img = Image.open('image.jpg')

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")


questions = ["First Question", "Second Question", "Third Question"]
answers = []

for question in questions:
    encoding = processor(img, question, return_tensors="pt")

    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    answers.append(model.config.id2label[idx])

for i, question in enumerate(questions):
    print(f"Pytanie: {question}")
    print(f"Odpowiedź: {answers[i]}")
