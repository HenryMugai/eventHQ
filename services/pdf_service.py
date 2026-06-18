import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PDFService:

    REPORT_FOLDER = "uploads/reports"

    @staticmethod
    def create_event_report(
        event,
        summary
    ):

        os.makedirs(
            PDFService.REPORT_FOLDER,
            exist_ok=True
        )

        filepath = os.path.join(
            PDFService.REPORT_FOLDER,
            f"event_report_{event.id}.pdf"
        )

        document = SimpleDocTemplate(
            filepath
        )

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                f"Event Report - {event.event_name}",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

        elements.append(
            Paragraph(
                f"Venue: {event.venue}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Revenue: KES {summary['revenue']:,.2f}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Tickets Sold: {summary['tickets']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Attendance: {summary['checked_in']}",
                styles["Normal"]
            )
        )

        document.build(
            elements
        )

        return filepath