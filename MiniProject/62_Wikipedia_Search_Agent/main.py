import wikipedia

class WikipediaAgent:
    def __init__(self):
        wikipedia.set_lang("en")

    def invoke(self, context):
        input_text = context.get("input", "")
        try:
            search_results = wikipedia.search(input_text)
            if not search_results:
                return "Nie znaleziono informacji na temat: " + input_text

            page_summary = wikipedia.summary(search_results[0], sentences=3)
            return page_summary
        except Exception as e:
            return "Wystąpił błąd: " + str(e)


agent_executor = WikipediaAgent()

# Testing
response = agent_executor.invoke({"input": "When do young pigeons leave the nest?"})
print(response)
