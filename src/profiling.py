def message_to_user(emotion: str = "😒") -> str:
    match emotion:
        case "😒":
            return "Put the link to the article on the box below and well, yeah, I'll try to summarize it."
        case "😊":
            return "Hello! Just put the link to the article on the box below and I'll try to summarize it!"


def express(emotion: str = "😒") -> str:
    """
    The function "express" takes an emotion as input and returns a corresponding tone in one sentence.
    
    @param emotion The parameter "emotion" is a string that represents a particular emotion. It has a
    default value of "😒" (a grumpy face emoji) if no value is provided when the function is called.
    
    @return If the input parameter `emotion` is "😒", the function will return the string "grumpy and
    sarcastic tone." If the input parameter is "😊", the function will return the string "positive and
    easy-going tone!".
    """
    match emotion:
        case "😒":
            return "grumpy and sarcastic tone."
        case "😊":
            return "bright, cheerful and positive vibe!"
