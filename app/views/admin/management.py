from . import admin


@admin.route('/', methods=['GET', 'POST'])
def management():
    return 'I am admin'
