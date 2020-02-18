''' simple tool for sending email with sendmail, postfix or ssmtpd

    import pysema
    send(
        ['alice@example.com', 'bob@example.com'],
        'really good subject line',
        'Message body goes here'
        )
'''

import subprocess
from email.message import EmailMessage


# path to the sendmail programm
SENDMAIL_PATH = '/usr/sbin/sendmail'


class SendMailException(Exception):
    ''' Exception while using pysema '''
    pass


def send(to=None, subject='', message='', **headers):
    msg = create_message(to, subject, message, **headers)
    send_message(msg)


def create_message(to=None, subject='', message='', **headers):
    if isinstance(to, str):
        recipients = to
    elif isinstance(to, (list, set, tuple)):
        recipients = ', '.join(to)
    else:
        raise SendMailException('No recipients given')

    # ensure that the 'from' keyword (if given) is uppercase
    sender_mail = headers.pop('from', None)
    if sender_mail is not None:
        headers['From'] = sender_mail

    headers['To'] = recipients
    headers['Subject'] = subject

    msg = EmailMessage()
    msg.set_content(message)
    for key, value in headers.items():
        msg[key] = value

    return msg


def send_message(msg):
    if not isinstance(msg, EmailMessage):
        raise SendMailException('Type Error: not an EmailMessage')

    try:
        subprocess.run(
            [SENDMAIL_PATH, '-t', '-oi'],
            input=msg.as_bytes(),
            check=True
            )
    except subprocess.CalledProcessError as e:
        raise SendMailException from e
