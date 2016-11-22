"""
Client side templates have a way to denote placeholders, to be filled in with dynamic content later. A placeholder in a template has the format {{placeholder}}, and it gets replace with the appropriate value one the page is loaded. For example, a welcome page template may greet a user as "Hello {{name}}" where the user's name is determined later.

Your task is to implement a function that will replace the placeholders in the given template. Note, that the template can contain nested placeholders.

Example

For template = "{{foo}}" and placeholders = [["foo","bar"]], the output should be
fillTemplate(template, placeholders) = "bar".
"""

def fillTemplate(t, p):
    for a,b in p*10:
        t = t.replace("{{"+a+"}}",b)
    return t

if __name__ == "__main__":
    assert fillTemplate("{{foo}}", [["foo", "bar"]]) == "bar"
    assert fillTemplate("Hello, {{foo}}", [["foo", "bar"]]) == "Hello, bar"
    assert fillTemplate("Some {{ text with random {{stuff}} }} in it", [["stuff", "things"]]) == "Some {{ text with random things }} in it"
    assert fillTemplate("{{nested {{placeholders}} oh noes!}}", [
        ["nested placeholders! oh noes!", "nah is k"], ["placeholders", "placeholders!"]]) == "nah is k"
    assert fillTemplate("As you might notice, the given {{template}} cannot be loaded properly", []) ==\
            "As you might notice, the given {{template}} cannot be loaded properly"
