import requests


def sendToDb(integration_token, database_id, title, description, issue_type, file_links):
    """
    Send feedback to the different providers [notion, GitHub, jira, trello, etc.
    :param integration_token: The integration token from notion
    :param database_id: The database id for your notion database
    :param title: The title of the issue
    :param description: The description of the issue
    :param issue_type: The type of issue (bug, feature, feedback)
    :param file_links: The link to the added files
    """
    # Construct the request headers with the integration token
    headers = {
        'Authorization': f'Bearer {integration_token}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28',  # Notion API version
    }

    if len(file_links) == 0:
        file_links = "https://www.notion.so/"

    data = {
        "Title": {"title": [{"text": {"content": title}}]},
        "Type": {"select": {"name": issue_type}},
        "Description": {"rich_text": [{"text": {"content": description}}]},
        "Statues": {"select": {"name": "To-Do"}},
        "File link": {"url": file_links},
    }
    page_properties = {'parent': {'database_id': database_id}, 'properties': data}

    res = requests.post("https://api.notion.com/v1/pages", headers=headers, json=page_properties)
    print(res.status_code)
