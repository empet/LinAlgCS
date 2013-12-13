from IPython.core.display import HTML
def  css_styling():
    styles = open("./styles/custom.css", "r").read()
    return HTML(styles)
css_styling()
