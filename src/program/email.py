import logging

from django.core.exceptions import ObjectDoesNotExist
from teams.models import Team
from utils.email import add_outgoing_email

logger = logging.getLogger("bornhack.%s" % __name__)


def add_new_speaker_proposal_email(speaker_proposal):
    formatdict = {"proposal": speaker_proposal}

    try:
        content_team = Team.objects.get(camp=speaker_proposal.camp, name="Content")
    except ObjectDoesNotExist as e:
        logger.info("There is no team with name Content: {}".format(e))
        return False

    return add_outgoing_email(
        text_template="emails/new_speaker_proposal.txt",
        html_template="emails/new_speaker_proposal.html",
        to_recipients=content_team.mailing_list,
        formatdict=formatdict,
        subject="New speaker proposal '%s' was just submitted" % speaker_proposal.name,
    )


def add_new_event_proposal_email(event_proposal):
    formatdict = {"proposal": event_proposal}

    try:
        content_team = Team.objects.get(camp=event_proposal.camp, name="Content")
    except ObjectDoesNotExist as e:
        logger.info("There is no team with name Content: {}".format(e))
        return False

    return add_outgoing_email(
        text_template="emails/new_event_proposal.txt",
        html_template="emails/new_event_proposal.html",
        to_recipients=content_team.mailing_list,
        formatdict=formatdict,
        subject="New event proposal '%s' was just submitted" % event_proposal.title,
    )


def add_speaker_proposal_updated_email(speaker_proposal):
    formatdict = {"proposal": speaker_proposal}

    try:
        content_team = Team.objects.get(camp=speaker_proposal.camp, name="Content")
    except ObjectDoesNotExist as e:
        logger.info("There is no team with name Content: {}".format(e))
        return False

    return add_outgoing_email(
        text_template="emails/update_speaker_proposal.txt",
        html_template="emails/update_speaker_proposal.html",
        to_recipients=content_team.mailing_list,
        formatdict=formatdict,
        subject="Speaker proposal '%s' was just updated" % speaker_proposal.name,
    )


def add_event_proposal_updated_email(event_proposal):
    formatdict = {"proposal": event_proposal}

    try:
        content_team = Team.objects.get(camp=event_proposal.camp, name="Content")
    except ObjectDoesNotExist as e:
        logger.info("There is no team with name Content: {}".format(e))
        return False

    return add_outgoing_email(
        text_template="emails/update_event_proposal.txt",
        html_template="emails/update_event_proposal.html",
        to_recipients=content_team.mailing_list,
        formatdict=formatdict,
        subject="Event proposal '%s' was just updated" % event_proposal.title,
    )


def add_speaker_proposal_rejected_email(speaker_proposal):
    formatdict = {"proposal": speaker_proposal}

    return add_outgoing_email(
        text_template="emails/speaker_proposal_rejected.txt",
        html_template="emails/speaker_proposal_rejected.html",
        to_recipients=speaker_proposal.user.email,
        formatdict=formatdict,
        subject=f"Your {speaker_proposal.camp.title} speaker proposal '{speaker_proposal.name}' was rejected",
    )


def add_speaker_proposal_accepted_email(speaker_proposal):
    formatdict = {"proposal": speaker_proposal}

    return add_outgoing_email(
        text_template="emails/speaker_proposal_accepted.txt",
        html_template="emails/speaker_proposal_accepted.html",
        to_recipients=speaker_proposal.user.email,
        formatdict=formatdict,
        subject=f"Your {speaker_proposal.camp.title} speaker proposal '{speaker_proposal.name}' was accepted",
    )


def add_event_proposal_rejected_email(event_proposal):
    formatdict = {"proposal": event_proposal}

    return add_outgoing_email(
        text_template="emails/event_proposal_rejected.txt",
        html_template="emails/event_proposal_rejected.html",
        to_recipients=event_proposal.user.email,
        formatdict=formatdict,
        subject=f"Your {event_proposal.camp.title} event proposal '{event_proposal.title}' was rejected",
    )


def add_event_proposal_accepted_email(event_proposal):
    formatdict = {"proposal": event_proposal}

    return add_outgoing_email(
        text_template="emails/event_proposal_accepted.txt",
        html_template="emails/event_proposal_accepted.html",
        to_recipients=event_proposal.user.email,
        formatdict=formatdict,
        subject=f"Your {event_proposal.camp.title} event proposal '{event_proposal.title}' was accepted!",
    )


def add_event_scheduled_email(eventinstance, action):
    formatdict = {"eventinstance": eventinstance, "action": action}
    recipients = [speaker.email for speaker in eventinstance.event.speakers.all()]
    recipients.append(eventinstance.event.proposal.user.email)
    # loop over unique recipients and send an email to each
    for rcpt in set(recipients):
        return add_outgoing_email(
            text_template="emails/event_scheduled.txt",
            html_template="emails/event_scheduled.html",
            to_recipients=rcpt,
            formatdict=formatdict,
            subject=f"Your {eventinstance.camp.title} event '{eventinstance.event.title}' has been {action}!",
        )
