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
    'запишись к психологу купи поводок и намордник',
    'вспомнишь крутую песню, которую давно не слушал ',
    'успеешь сделать все дела вовремя',
    'упадёшь с тазика в бане',
    'завтра проснешься в Биробиджане',
    'пойдешь пить пиво',
    'база женской тюрьмы',
    'все в этом чате должны заценить твой мейк',
    'держись пж',
    'Ночь пройдёт, наступит утро ясное \nЗнаю, счастье нас с тобой ждёт \nНочь пройдёт, пройдёт пора ненастная \nСолнце взойдёт\nСолнце взойдёт',
    'победишь сегодня в своей задротской игре',
    'быстро дождешься автобус и там будет свободное место ',
    'в любом начинании сегодня будет преследовать удача',
    'ураааа sesbian lex',
    'тебя сталкерит тейлор свифт',
    'stay strong, live on\nand power to the local dreamer',
    'у ии а ии у ии а и и',
    'все в чате должны рассказать как у них дела',
    'сходи погуляй',
    'сегодня можно не работать, все подождут',
    'у вас порвутся штаны на попе приседайте аккуратнее 🍑',
    'жду тебя сегодня в майнкрафте',
    'остерегайся толпу школьников с кириешками',
    'удача сегодня на твоей стороне',
    'ботай ботай',
    'сегодня очень вкусно поешь',
    'отдай 50 рублей которые занимал в среду',
    'шмакодявка',
    'разуй глаза, ведь сегодня ты СиЯеШь🤩',
    'бросай всё и убегай в тайгу',
    'сегодн стоит размяться, твои колену хрустят...',
    'сегодня ты обязана поесть суп',
    'на учёбу не идешь',
    'на работу не идёшь',
    'believe in yourself and your swag dude',
    'держимся держимся держимся',
    'скачаешь вирусы без игры',
    'будешь сегодня весь день ржать',
    'нереальный вайб от тебя идёт сегодня, делись им с людьми рядом',
    'будь лучше чем вчера, а не лучше чем другие',
    'умей замечать детали',
    'придумай на сегодня праздник и отпразднуй его',
    'будь осторожна,высокая вероятность потерять варежку в автобусе',
    'хватит плевать в потолок',
    'сегодня на спортивном',
    'посмотри уже этот фильм',
    'фигачь.',
    'хлебни Амура',
    'придумай предсказание и напиши чтобы я добавила пж'
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