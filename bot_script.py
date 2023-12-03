from telegram import InlineQueryResultVoice, InlineQuery, Update
from telegram.ext import Application, InlineQueryHandler, ContextTypes

BOT_TOKEN = 'BOT_TOKEN'

async def handle_inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query
    results = [
        InlineQueryResultVoice(
            id='1',
            voice_url='https://raw.githubusercontent.com/okuzan/tg-voice-bot/main/voices/IDGAF.ogg',
            title='Похуй максимально'
        ),
        InlineQueryResultVoice(
            id='2',
            voice_url='https://raw.githubusercontent.com/okuzan/tg-voice-bot/main/voices/pillow_scream.ogg',
            title='Pillow scream'
        ),
        InlineQueryResultVoice(
            id='3',
            voice_url='https://raw.githubusercontent.com/okuzan/tg-voice-bot/main/voices/yebaat.ogg',
            title='Єбаать'
        ),
        InlineQueryResultVoice(
            id='4',
            voice_url='https://raw.githubusercontent.com/okuzan/tg-voice-bot/main/voices/i_dont_sleep.ogg',
            title='Блять я не сплю'
        ),
        InlineQueryResultVoice(
            id='5',
            voice_url='https://raw.githubusercontent.com/okuzan/tg-voice-bot/main/voices/dead_inside.ogg',
            title='Dead inside'
        ),
        InlineQueryResultVoice(
            id='6',
            voice_url='https://raw.githubusercontent.com/okuzan/tg-voice-bot/main/voices/wtf.ogg',
            title='Что за хуйня'
        ),
        InlineQueryResultVoice(
            id='7',
            voice_url='https://raw.githubusercontent.com/okuzan/tg-voice-bot/main/voices/fuck_it.ogg',
            title='Забити хуй'
        )
    ]
    await update.inline_query.answer(results)
def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    inline_query_handler = InlineQueryHandler(inline_query_handler)
    application.add_handler(inline_query_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
