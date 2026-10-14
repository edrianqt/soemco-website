"""Email SOEMCO staff when a contact message or application arrives.

Set NOTIFY_EMAILS (comma-separated) and the EMAIL_* settings in .env to turn this on.
In development, emails are printed in the terminal instead of being sent.
"""
import logging

from django.conf import settings
from django.core.mail import send_mail

log = logging.getLogger(__name__)


def notify_staff(subject, body):
    recipients = getattr(settings, "NOTIFY_EMAILS", [])
    if not recipients:
        return
    try:
        send_mail(f"[SOEMCO website] {subject}", body, None, recipients)
    except Exception:  # never let email problems break the visitor's form submission
        log.exception("Could not send staff notification")
