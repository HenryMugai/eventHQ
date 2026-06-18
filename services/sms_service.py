import requests


class SMSService:

    API_URL = ""
    API_KEY = ""

    @staticmethod
    def send_sms(
        phone,
        message
    ):

        try:

            payload = {
                "phone": phone,
                "message": message,
                "api_key": SMSService.API_KEY
            }

            response = requests.post(
                SMSService.API_URL,
                json=payload,
                timeout=30
            )

            return response.status_code == 200

        except Exception as e:

            print(f"SMS Error: {e}")

            return False

    @staticmethod
    def send_ticket_sms(
        phone,
        event_name,
        ticket_number
    ):

        message = (
            f"{event_name} Ticket "
            f"#{ticket_number} "
            f"generated successfully."
        )

        return SMSService.send_sms(
            phone,
            message
        )

    @staticmethod
    def send_checkin_confirmation(
        phone,
        event_name
    ):

        message = (
            f"You have successfully "
            f"checked in to {event_name}."
        )

        return SMSService.send_sms(
            phone,
            message
        )