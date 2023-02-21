# Python To HTML

Un module python simple à utiliser qui permet d'écrire du HTML et du CSS dans python. C'est une alternative très nul à écrire nativement, mais c'etait un projet sur le quel j'ai bien aimé travailler

## Syntaxe

D'abord cloné le repo ou téléchargé le fichier .zip, puis créé un fichier python et écrivé le snippet suivant:
```python
from element import Element, FullHTML
from styles import Property, Style, Stylesheet
```

## HTML

Pour créé des élement HTML, utilisez la classes **Element**. ie:
```python
h1 = Element("h1", {"class": "title"}, "Hello World!")
```
résultat:
```HTML
<h1 class="title">Hello World!</h1>
```

La classe accepte 3 arguments: l'element de base, les options, et les enfants

L'enfant peut être une instance de la classe Element ou un string. ie:
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

Ici, l'élement **<p>** n'as pas d'options donc le second paramètre est un dictionnaire vide.
Ceci, marche avec tout les élement HTML pas seulement **<p>** et **<h1>**

Finalement, pour render le HTML, vous pouvez utiliser ceci:
```python
FullHTML().__init__("My very cool website", "./style.css')
```
Le premier argument est le titre de la page et le second le fichier css a être utilisé, vous pouvez ne pas le spécifier si vous souhaitez pas utilisé CSS, laissez le vide

## CSS

La parti CSS a 3 partis: Property, Style, Stylesheet. La classe Property definie une règle CSS, la classe Style, définie le sélecteur et Stylesheet est utilisé pour le fichier

Pour écrire des reègle vous pouvez écrire:
```python
title = [
    Property("font-size", "large")
    Property("text-decoration", "underline")
]
```
Ce qui ressemble à:
```CSS
    font-size: large;
    text-decoration: underline;
```

Pour définier un selecteur:
```python
styles = Style(".title", title) # styles can also be a list
```
Ce qui donne:
```CSS
.title{
    font-size: large;
    text-decoration: underline;
}
```

Finalement, pour render le CSS, utilisez:
```python
css = Stylesheet(styles, "style.css")
```
