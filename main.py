import telebot
import random
from telebot.types import InlineQueryResultArticle, InputTextMessageContent



bot = telebot.TeleBot('7617651774:AAEI16upFN6b7D4vXMTKmOJe6rWpsCCipno')

predictions = [
    'МЯУ',
    'антон может тебе руку сломать чтоб меньше выебывался',
    'А этом и суть людей, увы. Вкусно похавать - выше морали, справедливости и жизни живых существ. Хотя в 2025 году альтернативное мясо ничем не хуже по вкусу.',
    'Узнаешь хорошую новость ',
    'появится возможность кайфово отдохнуть ',
    'вспомнишь крутую песню, которую давно не слушал ',
    'успеешь сделать все дела вовремя',
    'упадёшь с тазика в бане',
    'база женской тюрьмы'
    'быстро дождешься автобус и там будет свободное место ',
    'в любом начинании сегодня будет преследовать удача',
    'ураааа sesbian lex',
    'тебя сталкерит тейлор свифт'
]

@bot.inline_handler(lambda query:True)
def query_text(inline_query):
    try:
        prediction = random.choice(predictions)


        result = InlineQueryResultArticle(
            id =str(random.randint(1, 1000000)),
            title = 'Узнать предсказание',
            description ='Нажмите, чтобы узнать предсказание',
            input_message_content = InputTextMessageContent(f'Твоё предсказание на сегодня:\n\n{prediction}')
        )

        bot.answer_inline_query(inline_query.id, [result], cache_time=0)
    except Exception as e:
        print('Ошибка',e)



bot.polling(non_stop=True)