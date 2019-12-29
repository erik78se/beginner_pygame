
# Testa att göra något när "on_mouse_down" händer.
# Testa att skriva det någon annan stans än på 10,10

def on_mouse_down(pos):
    print("mouse")
    screen.draw.text("Mouse",topleft=(10,10))
