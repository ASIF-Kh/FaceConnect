from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import threading

def send_emails_concurrently(receiver_emails, subject, message_html, url=None):
    sender_email = settings.DEFAULT_FROM_EMAIL

    def send_email(receiver_email, subject, message_html, sender_email):
        message = render_to_string('email_template.html', {
            'subject': subject,
            'message_body': message_html,
            'url': url
        })
        email = EmailMessage(
            subject, message, sender_email, [receiver_email]
        )
        email.content_subtype = "html"  # Main content is now text/html
        email.send()

    threads = []
    for receiver_email in receiver_emails:
        thread = threading.Thread(target=send_email, args=(receiver_email, subject, message_html, sender_email))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()




# Example usage
# receiver_emails = ['email@example.com', 'anotheremail@example.com']
# subject = "Your Daily Digest"
# message_html = "Here's an interesting update just for you!"
# send_emails_concurrently(receiver_emails, subject, message_html, "https://www.example.com")
