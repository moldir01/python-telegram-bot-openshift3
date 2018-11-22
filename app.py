import logging
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, ParseMode
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '726719622:AAE0uHCSnxl2d283ZJrFWnDwz_XXnXhaQtU'


def start(bot, update):
    """Send a message when the command /start is issued."""
    """update.message.reply_text('Welcome to the Test Bot! I will reply you what you will write me.')"""
    bot.send_message(chat_id=update.message.chat_id,
                     text='<b> Привет от Акжан,Жансая,Жанбота,Молдир. Че вы хотите?</b>', parse_mode=ParseMode.HTML)


def help(bot, update):
    """Send a message when the command /help is issued."""
    # update.message.reply_text('You can get any help here.')

    keyboardButtons = [[InlineKeyboardButton("скорая помощь", callback_data="1")],
                       [InlineKeyboardButton("служба пожаратушения", callback_data="2")],
                       [InlineKeyboardButton("служба газа", callback_data="3")],
                       [InlineKeyboardButton("полиция",callback_data="4")]]
    keyboard = InlineKeyboardMarkup(keyboardButtons)
    update.message.reply_text('Сделайте выбор:', reply_markup=keyboard)


def button(bot, update):
    query = update.callback_query
    if query.data == "1":
        text = "телефон 103"
    elif query.data == "2":
        text = "телефон 101"
    elif query.date == "3":
        text = "телефон службы газа 104"
    elif query.date == "4":
        text = "телефон 102"
    bot.editMessageText(text=text, chat_id=query.message.chat_id,
                        message_id=query.message.message_id)




def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"' % (update, error))


# Write your handlers here


def setup():
    updater = Updater(TOKEN)  # Create the EventHandler and pass it your bot's token.
    bot = updater.bot
    dp = updater.dispatcher  # Get the dispatcher to register handlers
    dp.add_handler(CommandHandler("start", start))  # on /start command answer in Telegram
    dp.add_handler(CommandHandler("help", help))  # on /help command answer in Telegram
    dp.add_handler(CallbackQueryHandler(button))

        # log all errors
    dp.add_error_handler(error)

    updater.start_polling()  # Start the Bot
    updater.idle()


if __name__ == '__main__':
    setup()
