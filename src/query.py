from llama_index import Document, VectorStoreIndex, ServiceContext, LLMPredictor
from llama_index.llms.openai import OpenAI
from llama_index.node_parser import SimpleNodeParser


# The `DocumentQuery` class allows you to generate summaries and replies based on a given text.
class DocumentQuery:
    def __init__(self, text: str) -> None:
        """
        The above function initializes a class instance with a given text, creates a document, sets up a
        node parser and a service context, creates a vector store index from the document using the service
        context, and sets up a query engine using the index.
        
        :param text: The `text` parameter is a string that represents the content of a document. It is used
        to initialize a `Document` object, which is then added to the `documents` list
        :type text: str
        """
        self.documents = [Document(text=text)]
        node_parser = SimpleNodeParser.from_defaults(chunk_size=512, chunk_overlap=10)
        service_context = ServiceContext.from_defaults(
            llm_predictor=LLMPredictor(llm=OpenAI(model="gpt-4")),
            node_parser=node_parser,
        )
        self.index = VectorStoreIndex.from_documents(
            self.documents, service_context=service_context
        )
        self.query_engine = self.index.as_query_engine()

    def generate_summary(self, numwords: int = 20) -> str:
        """
        The `generate_summary` function takes an optional argument `numwords` and returns a summary of the
        text using the specified number of words.
        
        :param numwords: The `numwords` parameter is an integer that specifies the maximum number of words
        that the summary should contain, defaults to 20
        :type numwords: int (optional)
        :return: a string.
        """
        return self.query_engine.query(
            "In {} words or less, summarize the text.".format(numwords)
        )

    def generate_reply(self, prompt: str = "") -> str:
        """
        The `generate_reply` function takes a prompt as input and returns a response generated by a query
        engine, or a default message if no prompt is provided.
        
        :param prompt: The `prompt` parameter is a string that represents the input prompt or question that
        you want to generate a reply for
        :type prompt: str
        :return: The `generate_reply` method returns a string. If a non-empty `prompt` is provided, it
        returns the result of querying the query engine with the prompt. If no prompt is provided, it
        returns the string "No prompt detected."
        """
        if len(prompt) > 0:
            return self.query_engine.query(prompt)
        else:
            return "No prompt detected."