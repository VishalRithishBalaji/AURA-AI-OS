department_messages = []


def publish_department_message(
    sender: str,
    message: str
):

    department_messages.append({

        "sender": sender,

        "message": message
    })


def get_department_messages():

    return department_messages[-50:]