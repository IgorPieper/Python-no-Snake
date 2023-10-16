from transformers import pipeline

text = """ Text to which we will pose questions. Polish Edition """

model = "henryk/bert-base-multilingual-cased-finetuned-polish-squad2"
tokenizer = "henryk/bert-base-multilingual-cased-finetuned-polish-squad2"

question_answering = pipeline("question-answering", model=model, tokenizer=tokenizer)

questions = ["First Question", "Second Question", "Third Question"]

answers = []

for question in questions:
    answer = question_answering(question=question, context=text)
    answers.append(answer)

for i, question in enumerate(questions):
    print(f"Pytanie: {question}")
    print(f"Odpowiedź: {answers[i]['answer']}")
