"""
Client side templates have a way to denote placeholders, to be filled in with dynamic content later. A placeholder in a template has the format {{placeholder}}, and it gets replace with the appropriate value one the page is loaded. For example, a welcome page template may greet a user as "Hello {{name}}" where the user's name is determined later.

Your task is to implement a function that will replace the placeholders in the given template. Note, that the template can contain nested placeholders.

Example

For template = "{{foo}}" and placeholders = [["foo","bar"]], the output should be
fillTemplate(template, placeholders) = "bar".
"""

def fillTemplate(template, placeholders):
    for _ in placeholders:
        for p in placeholders:
            template = template.replace("{{"+p[0]+"}}",p[1])
    return template
