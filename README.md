# MirrorChat

The MirrorChat project aims to harness Artificial Intelligence to chat with yourself. Basically, an LLM model learns the way you chat and captures the essential traits of your personality to replicate it in a conversation or wherever you want.

<figure>
    <img src="test.gif" height="360" />
    <figcaption> The example is in italian cause we speak italian :) </figcaption>
</figure>

## Description

MirrorChat is designed to provide an engaging and interactive chat experience by employing AI technology. By training the model on your own chat data, MirrorChat allows you to engage in conversations that mirror your own style and mannerisms. This project aims to explore the boundaries of personalized AI communication.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Internet Connection
- Python 3.6+
- A machine suitable for LLM training (GPU) or access to Colab (and other various cloud services)

## Quickstart

To get started with MirrorChat, follow these steps:

1. **Export WhatsApp chats (with permission!) and save them all inside a folder**
2. **Clone the repo**

After placing yourself with a terminal in the repo folder:

4. **Run `> python3 make_dataset.py` to preprocess the chat data**
5. **Train the model using the `train.ipynb` notebook**
6. **Run `> python3 chat.py` to start chatting!**

Please note that the quality of the conversations may depend on the size and diversity of your chat dataset.

## 🚧 To-Do
- [x] Currently support only italian and english system languages
- [ ] Data integration from multiple sources (Twitter, Instagram, Linkedin...)
- [ ] Model selection with a flag
- [ ] Create a web app

Feel free to contribute to this project! We welcome any contributions, suggestions, or improvements. Open a pull request or submit an issue.
