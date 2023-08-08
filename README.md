# Twitter-Message-Automata
sending twitter message to mass number of twitter handles Using the tweepy API
# Twitter Message Sender

![Twitter](https://img.shields.io/badge/Social-Twitter-blue.svg)

A Python script to send messages or direct messages on Twitter to different handles using the Tweepy library.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

This Python script utilizes the Tweepy library to send messages or direct messages (DMs) to different Twitter handles. It reads a list of tweet IDs from a CSV file, retrieves user IDs from the list, and sends the specified message to each user as a direct message.

## Features

- Authenticate using OAuth1UserHandler for secure Twitter API access.
- Send direct messages to a list of Twitter handles.
- Handles rate limits and errors gracefully to ensure successful message delivery.
- Customizable message content and list of handles.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/twitter-message-sender.git
   cd twitter-message-sender
   ## Usage
   
   add your custom message and name of the csv file containing the twitter handles in tweepy.py and run the file
