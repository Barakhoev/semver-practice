import datetime

def hello_world(name="World", language="en"):
    if not name:
        name = "World"
    
    greetings = {
        "en": f"Hello, {name}!",
        "es": f"¡Hola, {name}!",
        "fr": f"Bonjour, {name}!",
        "de": f"Hallo, {name}!"
    }
    
    return greetings.get(language, greetings["en"])

# ... остальные функции