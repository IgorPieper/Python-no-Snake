import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

text = " The text whose emotional sentiment we will assess. Polish Edition "

id2label = {0: "negative", 1: "neutral", 2: "positive"}

tokenizer = AutoTokenizer.from_pretrained("Voicelab/herbert-base-cased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("Voicelab/herbert-base-cased-sentiment")

encoding = tokenizer(
          text,
          add_special_tokens=True,
          return_token_type_ids=True,
          truncation=True,
          padding='max_length',
          return_attention_mask=True,
          return_tensors='pt',
        )
output = model(**encoding).logits.to("cpu").detach().numpy()
prediction = id2label[np.argmax(output)]
print("Opinion = ", prediction)
