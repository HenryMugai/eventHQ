import os
import pandas as pd


class ExcelService:

    EXPORT_FOLDER = "uploads/exports"

    @staticmethod
    def export_attendees(event, attendees):

        os.makedirs(
            ExcelService.EXPORT_FOLDER,
            exist_ok=True
        )

        filename = (
            f"attendees_event_{event.id}.xlsx"
        )

        filepath = os.path.join(
            ExcelService.EXPORT_FOLDER,
            filename
        )

        rows = []

        for attendee in attendees:

            rows.append({
                "Ticket Number": attendee.ticket_number,
                "Name": attendee.attendee_name,
                "Email": attendee.attendee_email,
                "Phone": attendee.attendee_phone,
                "Status": attendee.status
            })

        df = pd.DataFrame(rows)

        df.to_excel(
            filepath,
            index=False
        )

        return filepath

    @staticmethod
    def export_sales(event, orders):

        os.makedirs(
            ExcelService.EXPORT_FOLDER,
            exist_ok=True
        )

        filename = (
            f"sales_event_{event.id}.xlsx"
        )

        filepath = os.path.join(
            ExcelService.EXPORT_FOLDER,
            filename
        )

        rows = []

        for order in orders:

            rows.append({
                "Reference": order.order_reference,
                "Customer": order.customer_name,
                "Email": order.customer_email,
                "Phone": order.customer_phone,
                "Amount": order.total_amount,
                "Status": order.order_status
            })

        df = pd.DataFrame(rows)

        df.to_excel(
            filepath,
            index=False
        )

        return filepath