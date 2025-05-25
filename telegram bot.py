#you should first go to the (BotFather)
#now click on /newbot, give you a token 
#copy token and paste it in TOKEN variable 
#now click on all tages in EditBots section and enter whatever it asks of you
# now you can start coding 

####################################################################################################### 
#pip install python-telegram-bot
#pip install typing

from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

###########################################################################################################

TOKEN = "7720399180:AAGb5Y9akdSbU-_M1DaJTb_q-0YBj3nc9no"
BOT_USERNAME = "@First_rest_bot"

#comands 

async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('HELLO! im first bot for this developer :)')
    
async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('plase type somthing :)')

async def custom_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('THIS IS A CUSTOM COMMAND :)')

#responses
def handel_respons(text: str) -> str :
    processed: str=text.lower()

    if "hello" in processed:
        return 'Hey there'
    
    if 'how are you' in processed:
        return 'im good whatabout you'
    else:
        return "I DONT UNDRESTAND WHAT YOU WROTE"

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text


    print(f'User {update.message.chat.id} in {message_type}: "{text}"')
    
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text : str = text.replace(BOT_USERNAME, '').strip()
            reponse:str = handel_respons(new_text)
        else:
            return 
    else:
        reponse:str = handel_respons(text)
    print('bot', reponse)
    await update.message.reply_text(reponse)

async def error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__' :
    print('Starting bot ...')
    #commands
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    #Message:
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #polls the bot
    print('Polling ...')
    app.run_polling(poll_interval=3)

#after coding you must restart your bot
# if you want add your bot in the group you must first admin it and tag it in the chat 
#example = @your bot name (your chat)