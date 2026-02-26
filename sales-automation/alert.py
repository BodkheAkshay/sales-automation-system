import smtplib
from email.mime.text import MIMEText

def send_email_alert(insight, suggestion):

    sender_email = "sender_mail.com"    # Enter sender email ID (used to send alerts)
    receiver_email = "recivermail.com"    # Enter receiver email ID (who will receive alerts)
    app_password = "app_password"  # Generate Gmail App Password (Google Account → Security → App passwords)
    
    subject = "Sales Alert: Performance Change Detected"

    body = f"""
    SALES ALERT

    {insight}

    Suggested Actions:
    {suggestion}
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()

        print("Email alert sent successfully!")

    except Exception as e:
        print("Error sending email:", e)
