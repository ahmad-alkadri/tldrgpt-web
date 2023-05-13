# TL;DR, GPT?

## About <a name = "about"></a>

This Streamlit app allows you to generate a summary of an article or webpage using OpenAI's GPT API. It provides the option to choose between three different profiles, each with its own quirks and personality.

## Getting Started

### Installation
To run this app locally, please follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/ahmad-alkadri/tldrgpt-web.git your-local-path
```

2. Navigate to the project directory:

```bash
cd your-local-path
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m virtualenv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```
### Usage

To start the app, run the following command in your terminal:

```bash
python3 -m streamlit run app.py
```

The app will open in your browser.

## Instructions
Enter the URL of the article or webpage you want to summarize in the provided input field.

Choose one of the following profiles:

"🤓" - The Nerd: This profile provides detailed and technical summaries.

"😊" - The Friendly: This profile generates summaries with a positive and cheerful tone.

"😒" - The Side Eye: This profile adds a touch of sarcasm and attitude to the summaries.

Click the "Generate Summary" button to generate the summary based on the selected profile.

The generated summary will be displayed on the screen.

## Example
Here's an example of how to use the app:

1. Enter the URL of the article: https://www.example.com/article
2. Choose the profile "😊".
3. Click the "Generate Summary" button.

The app will generate a cheerful summary of the article.

## Notes
This app uses OpenAI's GPT API for generating summaries. You will need to have an OpenAI API key to use this app. Please refer to the OpenAI documentation for more information on obtaining an API key.

Once you've obtained the API key, go to `your-local-path` folder
where you've cloned this repo, create a `.env` file and put the following line in it:

```
OPENAIAPI=<your-openai-api-key-here>
```

Once launched, the app will read your `.env` file and load your
OpenAI's API key into it.

The quality and accuracy of the generated summaries may vary depending on the input article and the chosen profile. The app is designed to provide a general summary and may not capture all the nuances or details of the original content.

This app is for demonstration purposes only and should not be used for critical or sensitive applications.

## Acknowledgements
This app was developed using the Streamlit framework (https://www.streamlit.io/).

The text summarization functionality is powered by OpenAI's GPT API (https://openai.com/).
