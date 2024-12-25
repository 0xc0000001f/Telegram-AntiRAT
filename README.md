<h1>Telegram-AntiRAT with API</h1>

When you find api in php code who using this api for hacking anyone you can hack this attacker with only telegram api &amp; python.

Typically, logs are embedded in scripts used for phishing purposes. When you steal an account from the victim, this account is sent both to your text file and to the log collector via a message. The only way to detect this is by thoroughly inspecting all script files. Alternatively, you might find log files by chance, for example with names like telegram.php or log.php, and directly access them to detect the log. So, how do we perform offensive defense?

First of all, the only goal of the person who created the bot is: "To pull the logs." In other words, the attacker sends a message command to the bot, and along with it, sends a message to the bot. Now, let's dive deeper into the process.

When you create a normal bot, you can never send a message to a person. If that person hasn’t sent a message to the bot, you can never send a message. So, the attacker will send a message to their own bot. We will use this vulnerability to attempt RAT infection or to disrupt the process.

We will handle this in two ways: using the API through the web or via code. The best method is to send a message using code. This way, we can easily imitate a message created by the victim. First, I want to tell you about Telegram bots. Let’s quickly create a bot.

We send a message to the bot called "BotFather" and use the /newbot command to create a bot. We specify the bot's name, and that's it.

![rdkayuc](https://github.com/user-attachments/assets/2ca37417-3de0-40bd-857f-08ef264b32be)

We’ve created the bot and received a token. We can now use this token along with the API. t.me/OffSecDarkBot is now my bot. Let’s test the bot now. I will send a message to myself using the API. However, I need to start the bot first by sending the /start command so I can send myself a message. Let's test the bot. I will use Python’s "telebot" package.

Look telebot.py if you want to review my python code.

Now, let's test the /start command.

![qmacgdo](https://github.com/user-attachments/assets/51879164-946e-49ee-8eee-10f449b6e1b7)

As you can see, the bot is working. There are no issues with the code. By simply writing the /start command, we were able to send a message. Now, we can send messages to ourselves as the bot. The API is where it comes into play.

<h3>Telegram API</h2>

In short, we can use the API via a URL. Now, imagine you're looking at this from the perspective of a victim, and you are the offensive defender. Let's leave a note. But first, we need to understand the API.

You can view the available methods from the following URL: https://telegram-bot-sdk.readme.io/reference/. If we investigate, we’ll see that many methods are available, which will be very useful for us. For now, let’s try sending a message via URL.

To use the API, we will go to api.telegram.org. We will specify /bot{token}. Here’s an example URL usage:

https://api.telegram.org/bot3812894394392493024932423/method?chat_id=432784783&text=naber

In the section that says bot3812894394392493024932423, we will write our token, and in the chat_id section, we will write our chat ID.

To find the chat ID:

You can use the <a href="https://t.me/get_my_telegram_chat_id_bot" target="_blank">Get Chat ID BOT</a> Telegram bot. Let’s test it. : )

![qcesh0g](https://github.com/user-attachments/assets/7f0be1a9-b032-4528-b121-615edf9c9b0f)

As you can see, the API was successful, and the message was returned.

![cw2i4f5](https://github.com/user-attachments/assets/c24d76e1-3874-4815-9514-f2c805058991)

Now I think we’ve solved the API usage quite easily. However, I want to emphasize again: if you haven’t sent a message to the bot, the API will return a failure. So, if you provide the USER ID of someone who hasn’t sent a message to the bot, the operation will fail. Now, let’s move on to the interesting part.

Here are the bot and ID information of the log collector that my friend found:

![f9kyi9t](https://github.com/user-attachments/assets/c41343ec-2596-4811-b733-6d0a35e726d9)

1st Section: The token of the bot used by the log collector
2nd Section: The chat ID of the log collector
3rd Section: The log message sent by the log collector to themselves

Now, we have the necessary information. Let’s move on to offensive defense. Now, we have two ways to proceed:

<b>1 - Infecting with RAT</b><br>
<b>2 - Getting the IP address and the city they live in</b>

<h3>1 - Infecting with RAT</h3>

As you might have guessed, we will perform this operation by sending fake logs to the person. The success rate is low, and if you don’t get caught, at worst, you can just send a message and finish the job. Let's prepare a simple code for this. We will send the message via the API.

Now, there’s no need to fuss with Python or anything like that. On the right side of the address I sent, there is a ready-to-run command that works by itself.

Let's set the language to Python by clicking the three dots in the upper part of the shell under the "Language" section at the <a href="https://telegram-bot-sdk.readme.io/reference/sendmessage" target="_blank">sendMessage</a> address. I will copy the code and run it in my own code reader. I will set the text to match the log collector’s format.

After a few attempts (since I didn’t have the request details), I was able to prepare the code and successfully send the output of the message.

![hq7pz0h](https://github.com/user-attachments/assets/528f1a11-7aa7-4b23-aaa2-15a35c66d3a9)

Now, let’s make the final few adjustments.

Let’s assume we’ve prepared a virus. We’ll name it log.bat, and we’ll integrate it into the message. I discovered that we can create GIFs, PDFs, and ZIP files. In this case, I’m converting the virus into a PDF.

Now, we’ll send the document via Discord. First, I send the virus to a secondary account and copy the "cdn" URL.

![5ytqcrx](https://github.com/user-attachments/assets/0f6f3752-8f60-4293-b195-f1b3b5d21758)

There’s not much left to do now. I need to combine the PDF with the message and send it to the victim.

And yes, the code structure worked, and the message was sent. There’s no certainty, it’s purely phishing. If it works, it’s up to your luck.

Full Python Code

(Please review phishing.py)

<h3>2 - Getting the IP address and the city they live in</h3>

In short, you will add iplogger inside the message. If you add website: iploglink as an extra, this is another phishing method. Sample code:

iplogger.py 

Anyone with code knowledge can improve this part even more with their imagination. You can already guess how you will get the necessary information once you have the API. Maybe you can get the ip address by using an instagram account with fake followers. There are 1000 kinds of methods like this.

Thank you for listening to me. I posted this project on the TurkHackTeam forum on Sep 25, 2022. <a href="https://www.turkhackteam.org/konular/telegram-logcularina-rat-yedirin-ofansif-savunma.2024595/" target="_blank">Click here if you want to review it.</a>

In this project, I got code support from Nemesis and CaptainKanka was my friend who found the logs. This project is for educational purposes and has never been tested on anyone. Created bots have been destroyed.

![icegif-287](https://github.com/user-attachments/assets/8a5955c4-eb1d-45f5-a377-ad67c2ba17c4)
