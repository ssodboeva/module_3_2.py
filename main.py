def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    if not '@' in sender or '@' not in recipient or not ('.com' in recipient or '.ru' in recipient or '.net' in recipient) or not ('.com' in sender or '.ru' in sender or '.net' in sender):
        print (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    elif sender == recipient:
        print ('Нельзя отправить письмо самому себе!')
        return
    elif sender == "university.help@gmail.com":
        print (f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return
    else:
        print (f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender}')

send_email ('Добрый день', 'ananas@gmail')
send_email ('Добрый день', 'university.help@gmail.com')
send_email ('Добрый день', 'ananas@gmail.com')
send_email ('Добрый день', 'ananas@gmail.com', sender = 'urban.teacher@mail.ru')