# -*- coding: utf-8 -*-

def index():
    html = dict()
    form = SQLFORM(db.shooters)
    html['message'] = 'lala'
    if form.process().accepted:
        html['message'] = 'form accepted'
    elif form.errors:
        html['message'] = 'form has errors'
    html['shooterinputform'] = form
    return html
