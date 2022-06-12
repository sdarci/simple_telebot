
from distutils.cmd import Command
from operator import inv
from random import randint
import time
import string
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
bot = telebot.TeleBot('TOKEN HERE') #put ur telegramm token here
surname = ''
name = ''
age = ''
CNT = 3
inventory = ['money:' ,25,'pocket:']
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

@bot.callback_query_handler(func=lambda call: call.data == 'Л')
def call_back3(call):
    a = string_init(0)
    if call.data == 'M':
        bot.answer_callback_query(call.id,show_alert=True, text='Вы подняли достаточно тяжелую лопату' )
        inventory.append('Пустая банка')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='"Пригодиться в огороде"-подумали вы', reply_markup=a)
        print(inventory) 
        bot.send_message(call.message.chat.id, 'Вдруг вы слышите стук в дверь. Интересно кто там?', reply_markup=klava_init(1,'Открыть дверь'))

@bot.callback_query_handler(func=lambda call: call.data == 'O')
def call_back3(call):
    global CNT
    a = string_init(0)
    if call.data == 'O':
        bot.answer_callback_query(call.id,show_alert=True, text='Вы достали оладьи из холодильника' )
        inventory.append('Оладьи')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выглядит аппетитно!", reply_markup=a)
        print(inventory)
        bot.send_message(call.message.chat.id, 'Вдруг вы слышите стук в дверь. Интересно кто там?', reply_markup=klava_init(1,'Открыть дверь'))

@bot.callback_query_handler(func=lambda call: call.data == 'M')
def call_back3(call):
    a = string_init(0)
    if call.data == 'M':
        bot.answer_callback_query(call.id,show_alert=True, text='Банка оказалась пуста' )
        inventory.append('Пустая банка')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="И зачем я ее достал?! видно же было что она пустая", reply_markup=a)
        print(inventory) 
        bot.send_message(call.message.chat.id, 'Вдруг вы слышите стук в дверь. Интересно кто там?', reply_markup=klava_init(1,'Открыть дверь'))

@bot.callback_query_handler(func=lambda call: call.data == 'K')
def call_back2(call):
    global CNT
    if call.data == 'K':
        if CNT == 3:
            bot.answer_callback_query(call.id, show_alert=True,text ='Нет, Даю вторую попытку!')
            a = string_init_n(2,'Aбигейл', 'Xэйли')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='"Интересное имя! А ты попробуй угадать мое!" Она назвала вам 3 имени на выбор и вы задумались', reply_markup=a)
            CNT = 2
        elif CNT==2:
            bot.answer_callback_query(call.id,show_alert=True,text='Нуууу и снова мимо, Меня зовут Хэйли')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вам не удалось угадать имя((', reply_markup=string_init_n(0))
            CNT = 2
            bot.send_message(call.message.chat.id, '"Да, я плох в угадывании чего-либо"- подумали вы', reply_markup=klava_init(1,'"Прекрасное имя! А что ты тут делаешь?"'))
@bot.callback_query_handler(func=lambda call: call.data == 'A')
def call_back2(call):
    global CNT
    if call.data =='A':
        if CNT == 3:
            bot.answer_callback_query(call.id, show_alert=True,text ='Нет, Даю вторую попытку!')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='"Интересное имя! А ты попробуй угадать мое!" Она назвала вам 3 имени на выбор и вы задумались', reply_markup=string_init_n(2, 'Kаролина', 'Xэйли'))
            CNT = 2
        elif CNT==2:
            bot.answer_callback_query(call.id,show_alert=True,text='Нуууу и снова мимо, Меня зовут Хэйли')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вам не удалось угадать имя((', reply_markup=string_init(0))
            CNT = 2
            bot.send_message(call.message.chat.id, '"Да, я плох в угадывании чего-либо"- подумали вы', reply_markup=klava_init(1,'"Прекрасное имя! А что ты тут делаешь?"'))
@bot.callback_query_handler(func=lambda call: call.data == 'H')
def call_back2(call):
    if call.data == 'H':
            bot.answer_callback_query(call.id, show_alert=True,text ='Да! Ты что экстрасенс?')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы угадли имя Поздравляю!!', reply_markup=string_init(0))
            bot.send_message(call.message.chat.id, '"Да, он самый"- подумали вы', reply_markup=klava_init(1,'"Прекрасное имя! А что ты тут делаешь?"'))

# @bot.message_handler(commands=["stats"])
# def stats(message):
#     i = 0
#     # bot.send_message(message.chat.id, str(inventory[0] + str(inventory[1])))
#     for i in range(len(inventory)):
#         bot.send_message(message.chat.id,str(inventory[i]))
#     i = 0
def string_init_n(cnt,*args):
    key = telebot.types.InlineKeyboardMarkup(row_width=cnt)
    if cnt == 2:
        b1 = telebot.types.InlineKeyboardButton(args[0], callback_data=args[0][0])
        b2 = telebot.types.InlineKeyboardButton(args[1], callback_data=args[0][0])
        key.add(b1, b2)
    if cnt== 0:
        key =[]
    if cnt == 3:
        b1 = telebot.types.InlineKeyboardButton(args[0], callback_data='K')
        b2 = telebot.types.InlineKeyboardButton(args[1], callback_data='A')
        b3 = telebot.types.InlineKeyboardButton(args[2], callback_data='H')
        key.add(b1, b2,b3)
    return key

def string_init(cnt,*args):
    key = telebot.types.InlineKeyboardMarkup(row_width=cnt)
    if cnt == 2:
        b1 = telebot.types.InlineKeyboardButton(args[0], callback_data=args[0][0])
        b2 = telebot.types.InlineKeyboardButton(args[1], callback_data=args[1][0])
        key.add(b1, b2)
    if cnt== 0:
        key =[]
    if cnt == 3:
        b1 = telebot.types.InlineKeyboardButton(args[0], callback_data='K')
        b2 = telebot.types.InlineKeyboardButton(args[1], callback_data='A')
        b3 = telebot.types.InlineKeyboardButton(args[2], callback_data='H')
        key.add(b1, b2,b3)
    return key

@bot.callback_query_handler(func=lambda call: call.data == 'C')
def call_back(call):
    global CNT
    a = string_init(0)
    if call.data == 'C':
        bot.answer_callback_query(call.id, 'Вы приобрели морковь ('+str(inventory[1] - 5) +' мон. ваш баланс)' )
        inventory.append('Морковь')
        show_alert=True
        inventory[1] = inventory[1] - 5
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы приоьрели Морковь", reply_markup=a)
        print(inventory) 
        bot.send_message(call.message.chat.id,'"Извини ассортимент небольшой, все раскупили, надо приходить пораньше! Ну а мне пора уходить! Приятно было познакомиться"')
        bot.send_message(call.message.chat.id,'Пьер ушел по своим делам и теперь нужно думать что делать дальше?', reply_markup=klava_init(2,'Вернуться домой','Присесть отдохнуть'))
@bot.callback_query_handler(func=lambda call: call.data == 'P')
def call_back1(call):  
    a = string_init(0)
    if call.data == 'P':
        bot.answer_callback_query(call.id, 'Вы приобрели картошку (' + str(inventory[1] - 3) +' мон. ваш баланс)')
        show_alert=True
        inventory.append('Картошка')
        inventory[1] = inventory[1] - 3
        print(inventory)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы приобрели картошку", reply_markup=a)
        bot.send_message(call.message.chat.id,'"Извини ассортимент небольшой, все раскупили, надо приходить пораньше! Ну а мне пора уходить! Приятно было познакомиться"')
        bot.send_message(call.message.chat.id,'Пьер ушел по своим делам и теперь нужно думать что делать дальше?', reply_markup=klava_init(2,'Вернуться домой','Присесть отдохнуть'))
def klava_init(z, *args):
    klava=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = args[0]
    if len(args) == 3:
        btn3 = args[2]
        klava.add(btn1, btn2, btn3)
    if len(args) == 2:
        btn2 = args[1]
        klava.add(btn1, btn2)
    if len(args) == 1:
        klava.add(btn1)
    return klava

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'старт' or message.text == 'start' or message.text == 'Старт' or message.text == 'Start':
        photo = open('/Users/ksu/Downloads/src/railway.jpeg', 'rb') # change path here 
        bot.send_photo(message.from_user.id, photo, 'Прибытие на поезде в долину!')
        bot.register_next_step_handler(message, yes_o_no)
        photo = 'https://static.wikia.nocookie.net/stardewvalley/images/0/02/%D0%9B%D1%8C%D1%8E%D0%B8%D1%81.png/revision/latest/scale-to-width-down/332?cb=20180410054555&path-prefix=ru'
        bot.send_photo(message.from_user.id, photo, 'Так выглядит ваш дедушка')
        bot.send_message(message.chat.id, "Вы - работник Корпорации Джоджа, усталый и измученный рутиной. В один прекрасный день вы получаете письмо с завещанием от своего дедушки, который оставил вам свою ферму в долине Стардью. Решив бросить все, вы намереваетесь начать новую жизнь и направляетесь туда. Там вас ждет наследство от дедушки. \nПримите ли вы его?",reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, 'Попробуйте "старт", "Старт", "Start" или "start"',reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=['text'])
def yes_o_no(message):
    if message.text in ['Да', 'да','Принимаю', 'принимаю']:
        bot.send_message(message.chat.id,'Супер!!! тогда просто впиши свое имя в документе и все это твое')
        bot.register_next_step_handler(message, take_name)
    else:
        photo = 'https://clck.ru/etU99'
        bot.send_photo(message.from_user.id, photo, 'Хитрый дед!')
        bot.send_message(message.chat.id, 'Что? я тебя плохо слышу повтори еще раз громко, пожалуйста\n Старик явно хочет услышать положительный ответ')
        bot.register_next_step_handler(message, yes_o_no)


def take_name(message):
    global name
    name = message.text
    photo = open('/Users/ksu/Downloads/src/Дом.png', 'rb') # change path here 
    bot.send_photo(message.from_user.id, photo, 'Ваш дом ')
    bot.send_message(message.chat.id, name + ', поздравляю. этот дом твой, а я отправляюсь на заслуженный отдых\n дед обнял тебя и пошел в сторону остановки \n')
    btn1 = types.KeyboardButton("Да, мой старик немногословен...")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'ты оглядел свои новые владения', reply_markup=markup)
    bot.register_next_step_handler(message, start)

def start(message):
    if message.text != 'Да, мой старик немногословен...':
        bot.send_message(message.chat.id, '"'+message.text + '...ОЙ! ЭТО БЫЛО СКАЗАНО ВСЛУХ?" - спросили вы сами себя смотря вдаль провожая деда', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Да, мой старик немногословен...':
        bot.send_message(message.chat.id, 'вы посмеялись тихонько', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Чтож нужно осмотреться вокруг и найти магазин или сначала все же пойти в дом и отдохнуть')
    a = klava_init(2, 'Пойти в магазин', 'Исследовать дом')
    bot.send_message(message.chat.id, 'Что же сделать?', reply_markup=a)
    bot.register_next_step_handler(message, trees)

def trees(message):
    if message.text == 'Пойти в магазин':
        bot.send_message(message.chat.id, 'Отпрвлюсь в магазин\nВидел его когда проезжал на поезде', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Вы направляетесь в магазин. Неплохо для небольшого исследования деревни "Stardew" и покупки чего нибудь перекусить')
        photo = 'https://clck.ru/etUQk'
        bot.send_photo(message.from_user.id, photo)  
        #отправить логотип стардью
        i = 0
        while i !=4:
           bot.send_message(message.chat.id, 'Шагаем к магазину... Подождите')
           time.sleep(1)
           i+=1
           bot.send_message(message.chat.id, 'Проходим мимо Аллеи')
           time.sleep(0.5)
           i+=1
           bot.send_message(message.chat.id, '"О какая красивая бабочка"-Подмуал ты')
           time.sleep(1)
           i+=1
           bot.send_message(message.chat.id, ' Уже виднеется магазин')
           time.sleep(1)
           i+=1
           #dobavit random death)) 
        photo=open('/Users/ksu/Downloads/src/Pierres_shop_02', 'rb') # change path here 
        bot.send_photo(message.from_user.id, photo,'Вы подошли к магазину') 
        bot.send_message(message.chat.id, '"Вот и дошел. Так что тут написано?" - но вы не успели дочитать, вас встретил мужчина в очках\n')
        time.sleep(1)
        photo = 'https://clck.ru/etVKr'
        bot.send_photo(message.from_user.id, photo,'Пьер Дунн')
        #photo piera
        bot.send_message(message.chat.id, '"Привет, Я Пьер, А твое имя как?"-произнес мужчина')
        a = klava_init(2, 'Представиться', 'Испугаться')
        bot.send_message(message.chat.id, 'Вы не ожидали кого-то встретить',reply_markup=a)
        bot.register_next_step_handler(message, shop)
    elif message.text == 'Исследовать дом':
        bot.send_message(message.chat.id, 'Для начала исследую дом. Что там оставил дедушка', reply_markup=types.ReplyKeyboardRemove())
        a = klava_init(1,'Подняться')
        bot.send_message(message.chat.id, '"Чтож, Поднимаемся"',reply_markup=a)
        bot.register_next_step_handler(message, Home)
    else:
        bot.send_message(message.chat.id, 'Может быть все таки выберешь что то из кнопок?)')
        bot.register_next_step_handler(message, start)

def Home(message):
    if message.text == 'Подняться':
        photo='https://clck.ru/etUWf'
        bot.send_photo(message.from_user.id, photo, 'Планировка дома') 
        bot.send_message(message.chat.id, 'Вы поднимаетесь по ступенькам и проходите в дверь',reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Вы входите в дом\nВидите перед собой старую кровать, небольшой обеденный стол и спуск в погреб')
        a = klava_init(2,'На кухню за едой!!!', 'В подвал')
        bot.send_message(message.chat.id, 'Пойти пошариться в погребе или поискать еду?',reply_markup=a)
        bot.register_next_step_handler(message, Podval_or_kitchen)
    elif message.text != 'Подняться':
        bot.send_message(message.chat.id, '"Чтож, Поднимаемся" (Подсказка: Попробуй кнопку)',reply_markup=types.KeyboardButton('Мб все таки поднимемся?'))
        bot.register_next_step_handler(message, Home)

def Podval_or_kitchen(message):
    t = message.text
    photo1='https://clck.ru/etUoa'
    if t == 'На кухню за едой!!!':
        bot.send_message(message.chat.id, 'Вы направляетесь прямо к холодильнику?',reply_markup=types.ReplyKeyboardRemove())
        time.sleep(1)
        bot.send_message(message.chat.id, 'Вы открываете холодильник и видите перед собой:',reply_markup=string_init(2,'Oладьи', 'Mайонез')) # 
        photo2 = 'https://clck.ru/etUw3'
        bot.send_media_group(message.chat.id, [InputMediaPhoto(photo1), InputMediaPhoto(photo2)])
        bot.register_next_step_handler(message, OpenTheDoor)
    elif t == 'В подвал':
        photo3='https://clck.ru/etVC7'
        bot.send_message(message.chat.id,'Поищу что нибудь полезное в подвале.',reply_markup=types.ReplyKeyboardRemove())
        time.sleep(1)
        bot.send_message(message.chat.id, 'Вы спускаетесь в подвал и видите там:',reply_markup=string_init(2,'Лопата', 'Mайонез'))
        bot.send_media_group(message.chat.id, [InputMediaPhoto(photo1), InputMediaPhoto(photo3)])
        bot.register_next_step_handler(message, OpenTheDoor)

    else:
        bot.send_message(message.chat.id,'Хм... что же все таки сделать сначала?')
        bot.register_next_step_handler(message, Home)

def OpenTheDoor(message):
    photo='https://clck.ru/etVES'
    bot.send_photo(message.from_user.id, photo, 'Незнакомка') 
    bot.send_message(message.chat.id,'Вы видите перед собой девушку',reply_markup=klava_init(2,'Представиться', '"Привет, Как тебя зовут?"'))
    bot.register_next_step_handler(message, after_shop,1)

def shop(message):
    if message.text == 'Представиться':
        bot.send_message(message.chat.id,'"' + name + '" - Вы представились, "могу я у вас что то приобрести ?"',reply_markup=types.ReplyKeyboardRemove())
        key = string_init(2, 'Морковь (5 мон.)', 'Картошка (3 мон.)')
        bot.send_message(message.chat.id, '"Да, Есть семена" - Пьер показал вам на лавку ', reply_markup=key)
        time.sleep(5)
    elif message.text == 'Испугаться':
        key = string_init(2, 'Морковь (5 мон.)', 'Картошка (3 мон.)')
        bot.send_message(message.chat.id,'"'+ name[0] + name[1]+ '...' + name + '" - Испуганно проинозити вы и добавляете "Нельзя же так пугать"\nПьер явно сам не ожидал такой рекции и извинился',reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id,'"Извини" - произнес он - " Не хочешь приобрести что то ? в ассортименте есть ↓', reply_markup=key)
        time.sleep(4)
    bot.register_next_step_handler(message, after_shop, 0)


def after_shop(message, flag):
    i = 0
    if message.text == 'Вернуться домой' and flag == 0:
        bot.send_message(message.chat.id,'Вы решили направиться домой', reply_markup=types.ReplyKeyboardRemove())
        while i !=3:
            bot.send_message(message.chat.id,'Вы проходите мимо той же самой аллеи')
            i+=1
            time.sleep(1)
            bot.send_message(message.chat.id,'"Эта бабочка совсем отличается от той что я видел по пути сюда" - подметили вы')
            i+=1
            time.sleep(1)
            bot.send_message(message.chat.id,'Вы подходите к дому')
            i+=1
        a = klava_init(1, 'Подняться')
        bot.send_message(message.chat.id,'Поднимаемся?',reply_markup=a)
        bot.register_next_step_handler(message, Home)
    elif message.text == 'Присесть отдохнуть' and flag == 0:
        bot.send_message(message.chat.id, 'Вы присели на лавочку около магазина, но побыть в одиночесвте вам не удалось, к вам сразу подошла рыжеволосая девшука\n "О, я тебя раньше не видела здесь, Как тебя зовут?" - спросила она', reply_markup=klava_init(0,'Представиться', '"Сначала представься ты!"'))
        bot.register_next_step_handler(message, after_shop, 1)
    elif message.text == 'Представиться' and flag == 1:
        bot.send_message(message.chat.id, '"' + name + ', а тебя как зовут?"', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, '"Интересное имя! А ты попробуй угадать мое!" Она назвала вам 3 имени на выбор и вы задумались',reply_markup=string_init(3,'Каролина', 'Абигейл', 'Хэйли'))
        bot.register_next_step_handler(message,  diolog_next)
    elif message.text in ['"Сначала представься ты!"', '"Привет, Как тебя зовут?"'] and flag == 1:
        bot.send_message(message.chat.id, '"Нет, ну вы городские и наглые!!! Я не назову свое имя, но дам подсказку. Каролина или Хэйли?" - возмущенно сказала она',reply_markup=string_init(3,'Каролина', 'Абигейл', 'Хэйли'))
        bot.register_next_step_handler(message,  diolog_next)

def diolog_next(message):
    bot.send_message(message.chat.id, '"Я шла к реке, не хочешь отправиться со мной? Расскажешь как там в городе дела по тебе видно что ты ГОРОДСКОЙ" - слово "городской" она выделила специально  чтобы вас задеть ')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Похоже у меня нет выбора и я просто следую за девушкoй', reply_markup=types.ReplyKeyboardRemove())
    reka(message,0)
def reka(message, flag):
    if flag == 1:
        bot.send_message(message.chat.id, 'Вы уходите от магазина Пьера и идете в сторону реки')
        time.sleep(1)
    elif flag == 0:
        bot.send_message(message.chat.id, 'Вы уходите от Дома и идете в сторону реки')
        time.sleep(1)
    bot.send_message(message.chat.id, 'Рассказываете Хейли что в городе совсем все не так и машины уже давно летают по воздуху')
    time.sleep(1)
    bot.send_message(message.chat.id, 'И про дедушку рассказали и что теперь вы будете жить по крайней мере какое то время здесь в далине стардью')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Сама же Хэйли рассказала вам что идет рыбачить и обещала вас научить')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Вы провели с ней весь день и это было чудесно\n КОНЕЦ 1 части :)')

    





 



        







    
























bot.polling(none_stop=True, interval=0)

