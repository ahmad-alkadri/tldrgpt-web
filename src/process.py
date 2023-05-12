import openai
from src.preprocess import splittochunk, summarize_chunks
from src.textgetter import get_text_from_url
from src.profiling import express
from dotenv import load_dotenv
import os

load_dotenv()


async def summarize_article(
    url: str = "",
    st_status=None,
    num_words: int = 20,
    emotion: str = "😒",
) -> str:
    openai.api_key = os.environ.get("OPENAIAPI")

    txt = get_text_from_url(url)

    num_iter = 0
    while len(txt) > 3500:
        if st_status:
            st_status.warning(
                "Text is too long ({} characters). Split-processing them...".format(
                    len(txt)
                )
            )

        txt = await summarize_chunks(
            splittochunk(txt),
            openaiapi=os.environ.get("OPENAIAPI"),
        )
        num_iter += 1
        if num_iter > 3:
            raise RuntimeError(
                "Text too long even after splitting——can't be summarized."
            )

    if st_status:
        st_status.info("Summarizing...")

    personality = express(emotion)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {
                "role": "assistant",
                "content": txt,
            },
            {
                "role": "user",
                "content": f"Summarize article into exactly {num_words} words or less in \
                    {personality}. Still, don't lose the core of the article. \
                        Oh, and you're allowed to use emoticons (if you want it).",
            },
        ],
    )

    st_status.empty()

    return completion.choices[0].message["content"]
