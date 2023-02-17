from element import Element, FullHTML
from styles import Style, Stylesheet, Property

p = Element("h1", {"class": "title"}, "Sushi Restaurant")
div = Element("div", {"class": "bgred"}, p)
div.render()

f = FullHTML().__init__("TEST WEBSITE", "./style.css")

bgred = [
    Property("background", "red"),
    Property("width", "fit-content")
]

title = [
    Property("font-size", "xx-large"),
    Property("text-decoration", "underline")
]

body = [
    Property("background", "#2D2D2D")
]

styles = [
    Style("body", body),
    Style(".bgred", bgred),
    Style(".title", title)
]


css = Stylesheet(styles, "style.css")