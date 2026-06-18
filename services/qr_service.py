import os
import qrcode


class QRService:

    QR_FOLDER = "static/qr_codes"

    @staticmethod
    def generate(ticket_number):

        os.makedirs(
            QRService.QR_FOLDER,
            exist_ok=True
        )

        filename = f"{ticket_number}.png"

        filepath = os.path.join(
            QRService.QR_FOLDER,
            filename
        )

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(ticket_number)

        qr.make(fit=True)

        image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        image.save(filepath)

        return filepath

    @staticmethod
    def generate_ticket_qr(ticket):

        path = QRService.generate(
            ticket.ticket_number
        )

        return path