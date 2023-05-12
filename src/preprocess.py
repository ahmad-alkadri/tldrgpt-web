import asyncio
import aiohttp
import cachetools
import threading


def splittochunk(text: str, max_length: int = 3500) -> list[str]:
    """
    The function "splittochunk" takes a string and splits it into chunks of a specified maximum length,
    returning a list of the resulting chunks.

    @param text A string that needs to be split into chunks of a maximum length specified by the
    max_length parameter.
    @param max_length The maximum length of each chunk of text that the function will split the input
    text into. By default, it is set to 3500 characters.

    @return The function `splittochunk` takes in a string `text` and an integer `max_length` (default
    value of 3500). It then splits the string `text` into chunks of length `max_length` and returns a
    list of these chunks.
    """
    return [text[i : i + max_length] for i in range(0, len(text), max_length)]


async def summarize_chunk_async(
    chunk: str, max_sentences: int = 2, openaiapi: str = ""
) -> str:
    """
    This is an asynchronous Python function that uses the OpenAI API to summarize a given text chunk
    into a specified number of sentences or less.

    @param chunk The text chunk that needs to be summarized.
    @param max_sentences The maximum number of sentences that the text should be summarized into.
    @param openaiapi The `openaiapi` parameter is a string that represents the OpenAI API key that is
    required to access the OpenAI API. This key is used to authenticate the user and authorize access to
    the API's resources.

    @return The function `summarize_chunk_async` returns a string that represents the summarized text of
    the input `chunk` with a maximum of `max_sentences` sentences. The summary is generated using the
    OpenAI GPT-3 model and the `openaiapi` parameter is used for authentication. If an error occurs
    during the API call, an empty string is returned.
    """
    async with aiohttp.ClientSession() as session:
        headers = {
            "Authorization": f"Bearer {openaiapi}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "messages": [
                {
                    "role": "assistant",
                    "content": chunk,
                },
                {
                    "role": "user",
                    "content": f"Summarize the text into exactly {max_sentences} sentences or less.",
                },
            ],
        }

        try:
            async with session.post(
                "https://api.openai.com/v1/chat/completions", headers=headers, json=data
            ) as resp:
                completion = await resp.json()
                return completion["choices"][0]["message"]["content"]
        except Exception:
            return ""


cache_lock = threading.Lock()
cache = cachetools.TTLCache(
    maxsize=100, ttl=3600
)  # maxsize is set to 100, and ttl is set to 1 hour (3600 seconds)


async def summarize_chunks(
    chunks: list[str], max_sentences: int = 2, openaiapi: str = ""
) -> str:
    """
    This is an asynchronous Python function that takes a list of text chunks, a maximum number of
    sentences, and an OpenAI API key as input, and returns a summarized version of the text chunks. The
    function uses caching to improve performance.

    @param chunks A list of strings representing the text chunks that need to be summarized.
    @param max_sentences The maximum number of sentences to include in the summary for each chunk of
    text.
    @param openaiapi The `openaiapi` parameter is a string that represents the API key for the OpenAI
    API. It is an optional parameter and its default value is an empty string. If a valid API key is
    provided, it will be used to access the OpenAI API to generate the summaries. If no

    @return The function `summarize_chunks` returns a string that is the concatenation of the summaries
    of all the chunks passed as input to the function. The summaries are generated using the
    `summarize_chunk_async` function, which is called asynchronously for each chunk. The function also
    uses a cache to store the results of previous calls with the same input parameters, in order to
    avoid redundant computations.
    """
    cache_key = (tuple(chunks), max_sentences, openaiapi)

    with cache_lock:
        if cache_key in cache:
            return cache[cache_key]

    tasks = []

    for chunk in chunks:
        tasks.append(summarize_chunk_async(chunk, max_sentences, openaiapi))

    summaries = await asyncio.gather(*tasks)
    result = " ".join(summaries)

    with cache_lock:
        cache[cache_key] = result

    return result
