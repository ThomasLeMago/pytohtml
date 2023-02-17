# Python To HTML

A very simple and easy to use, library to be able to write HTML and CSS code using python.
This is a terrible alternative to writing the code by hand but it was a fun little project to work on.

## How to use

first of clone the repo or download the .zip, then create a new python file and write the following
```python
from element import Element, FullHTML
from styles import Property, Style, Stylesheet
```

## HTML

To create HTML elements you can use the **Element** class. ie:
```python
h1 = Element("h1", {"class": "title"}, "Hello World!")
```
result:
```HTML
<h1 class="title">Hello World!</h1>
```

The class takes 3 arguments: the base element, the options, and the child

The child can be instance of the Element class or a string. ie:
```python
p = Element("p", {}, "How are you ?")
div = Element("div", {"class": "content"}, p)
```
result:
```HTML
<div class="content">
    <p>How are you ?</p>
</div>
```

Here the **p** tag doesn't have any options which is why the second argument is an empty dictionnary.
This works with any html elements not just **p** and **h1**

Finally to render the html, you can run the following
```python
FullHTML().__init__("My very cool website", "./style.css')
```
The first argument specifies the title of the page and the second the stylesheet which you can leave blank if you don't want to use CSS.

## CSS

The CSS has 3 parts to it: Property, Style and Stylesheet. The Property class is used to define the rules, Style is used to define the target for a set of rules and Stylesheet combines all of that together

To write rules in python you would use the following:
```python
title = [
    Property("font-size", "large")
    Property("text-decoration", "underline")
]
```
Which would result in the following CSS:
```CSS
    font-size: large;
    text-decoration: underline;
```

Except we also need a selector for the CSS which can be defined using Style:
```python
styles = Style(".title", title) # styles can also be a list
```
and the output would be:
```CSS
.title{
    font-size: large;
    text-decoration: underline;
}
```

Finally, to render the css you can run:
```python
css = Stylesheet(styles, "style.css")
```
