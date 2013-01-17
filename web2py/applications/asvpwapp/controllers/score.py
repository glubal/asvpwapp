

def index():
    # Show main page to enter a user's score
    html = dict()
    form = SQLFORM(db.shooters)
    html['message'] = 'Title'
    return html


def add():
    # Add a result to the user's score
    pass


def confirm():
    # Confirm the entered round score
    pass