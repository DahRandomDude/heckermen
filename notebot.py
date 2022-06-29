import numpy
import spacy
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$note'):
        nlp = spacy.load("en_core_web_sm")
        p_sentences = [] # processed sentences
        n_sentences = [] # note-form sentences
        text = message.content.split(' ', 1)[1]
        sentences = text.split(".")
        for x in sentences: # loop through sentences
            parts = nlp(x)
            texts = [token.lemma_ for token in parts if token.pos_ == "VERB" or token.pos_ == "NOUN" or token.pos_ == "PREP"] # get all words from text that are verbs, nouns or prepositions
            print(texts)
            p_sentences.append(texts)
        for x in p_sentences:
            n_sentences.append(" ".join(x))
        message_to_send = ""
        n_sentences.pop()
        for x in n_sentences:
            message_to_send+="```"+x+"```"
        await message.reply(message_to_send, mention_author=True)
        
client.run('OTkxNDM2NDk5NjY3MTI4Mzky.GvoKAf.vOu2RlvpXOHu9oz12PYIJRdLTqySAku-saJgBY')
