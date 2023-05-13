def message_to_user(emotion: str = "😒") -> str:
    """
    The function returns a message to the user based on the given emotion, prompting them to input a
    link to an article for summarization.
    
    @param emotion a string parameter that represents the emotion of the message. It has a default value
    of "😒" if no value is provided.
    
    @return a message based on the input emotion.
    """
    match emotion:
        case "😒":
            return "Put the link to the article on the box below and well, yeah, I'll try to summarize it 😒."
        case "😊":
            return "Hello 😊!!! Just put the link to the article on the box below and I'll try to summarize it!"
        case "🤓":
            return "Hello there! Don't have time to read thousands of words? 🤓 Just put the link below and I'll sum it up for you!"


def express(emotion: str = "😒") -> str:
    """
    The function "express" takes an emotion as input and returns a corresponding tone or vibe in a
    string format.
    
    @param emotion A string parameter that represents an emoji depicting a certain emotion.
    
    @return The function `express` takes an optional string argument `emotion` and returns a string that
    describes the tone or vibe associated with that emotion.
    """
    match emotion:
        case "😒":
            return "very grumpy, sceptic and sarcastic tone."
        case "😊":
            return "bright, cheerful and positive vibe!"
        case "🤓":
            return "nerdy, meticulous, technical, and detailed way."
