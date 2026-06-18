import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import current_app


class EmailService:

    @staticmethod
    def send_email(
        recipient,
        subject,
        body
    ):

        try:

            message = MIMEMultipart()

            message["From"] = current_app.config[
                "MAIL_USERNAME"
            ]

            message["To"] = recipient

            message["Subject"] = subject

            message.attach(
                MIMEText(
                    body,
                    "html"
                )
            )

            server = smtplib.SMTP(
                current_app.config["MAIL_SERVER"],
                current_app.config["MAIL_PORT"]
            )

            server.starttls()

            server.login(
                current_app.config["MAIL_USERNAME"],
                current_app.config["MAIL_PASSWORD"]
            )

            server.sendmail(
                current_app.config["MAIL_USERNAME"],
                recipient,
                message.as_string()
            )

            server.quit()

            return True

        except Exception as e:

            print(f"Email Error: {e}")

            return False

    @staticmethod
    def send_ticket_email(
        recipient,
        attendee_name,
        ticket_number,
        event_name
    ):

        subject = f"{event_name} Ticket"

        body = f"""
        <h2>EventHQ Ticket</h2>

        <p>Hello {attendee_name},</p>

        <p>Your ticket has been generated successfully.</p>

        <p>
        <strong>Event:</strong> {event_name}<br>
        <strong>Ticket Number:</strong> {ticket_number}
        </p>

        <p>Present this ticket at the venue.</p>

        <p>Thank you.</p>
        """

        return EmailService.send_email(
            recipient,
            subject,
            body
        )