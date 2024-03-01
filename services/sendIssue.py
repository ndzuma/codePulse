from services.NotionSend import sendToDb as notionSend
from dotenv import load_dotenv
import os

load_dotenv()

# Get the environment variables
notionIntegrationToken = os.getenv("NOTION_INTEGRATION_TOKEN")
notionDatabaseId = os.getenv("NOTION_DATABASE_ID")


def sendIssue(service, title, description, issue_type, file_links):
    """
    Send feedback to the different providers [notion, GitHub, jira, trello, etc.]
    :param service: The service to send the issue to
    :param title: The title of the issue
    :param description: The description of the issue
    :param issue_type: The type of issue (bug, feature, feedback)
    :param file_links: The link to the added files
    :return: 1 if successful, 0 if not
    """
    if service == "notion":
        notionSend(
            integration_token=notionIntegrationToken,
            database_id=notionDatabaseId,
            title=title,
            description=description,
            issue_type=issue_type,
            file_links=file_links
        )
    else:
        print("Service not supported")
        return 0
    return 1
