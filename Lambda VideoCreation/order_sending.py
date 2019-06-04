import os, smtplib

MY_SMTP_HOST = os.getenv('MY_SMTP_HOST')
MY_SMTP_USER = os.getenv('MY_SMTP_USER')
MY_SMTP_PASS = os.getenv('MY_SMTP_PASS')

def send_order_result(email, animation_url):
    
    subject = 'Zamówienie animacji zostało zrealizowane'
    text = 'Udało się utworzyć animację 😅. Animacja dostępna pod adresem {}\n\nPozdrawiam serdecznie\nD'.format(animation_url)
    message = 'Subject: {}\n\n{}'.format(subject, text)

    server = smtplib.SMTP_SSL(MY_SMTP_HOST, 465)
    server.login(MY_SMTP_USER, MY_SMTP_PASS)
    server.sendmail(
        "no-reply@danb.pl", 
        email, 
        message.encode('utf-8')
    )
    server.quit()