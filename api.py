import paralleldots
paralleldots.set_api_key('eComg6tMaW8q7GwLg1UIMLFW6MzwpH5ct3bvu9OseWY')

def ner(text):
    return paralleldots.ner(text)

