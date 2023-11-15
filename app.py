import openai
import configparser
import requests
import os
from openai import OpenAI
import streamlit as st
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY
client = OpenAI(api_key = OPENAI_API_KEY)
config = configparser.ConfigParser()
config.read("config.ini")
SIZES = ('1024x1024', '512x512', '256x256')




def generate_text(prompt):
    TEXT = f"As a seasoned expert in the realm of artificial intelligence, you delve deep into the transformative power of AI and its impact on modern society. Pen down an illuminating blog post discussing the latest advancements and ethical considerations in AI. Your insights are crucial in shaping the discourse around this cutting-edge technology. Provide a title and content based on this prompt: {prompt}."
    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content":TEXT},

  ]
  )
    return response.choices[0].message.content



def generate_image(prompt):
    response = client.images.generate(
    model="dall-e-3",
        prompt=f"You are a digital artist, creating evocative imagery for a thought-provoking blog post. Given the post's text: --- {prompt} ---, generate an image that encapsulates warmth and emotion without excessive detail.",
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = response.data[0].url
    return image_url 

    


def main():
    st.title("Let's talk about AI")

    # User input for the tweet
    prompt = st.text_area('What do you wish to talk about :')

    if st.button('Generate Blog Post'):
        # Generate image and text
        image_url = generate_image(prompt)
        text = generate_text(prompt)

        # Display image and text as a blog post
        st.image(image_url, caption='Generated Image')
        st.write(text)


if __name__ == "__main__":
    main()





