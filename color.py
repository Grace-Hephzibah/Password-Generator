import random

def color_light():
    color = [
        "#ebc934",
        "#dfeb34",
        "#8feb34",
        "#34eb86",
        "#34ebe2",
        "#34a8eb",
        "#bd71f0",
        "#ed8282",
        "#e028a0",
        "#bafffd"]
    return random.choice(color)

def color_dark():
    color = [
        "#c21515",
        "#053b87",
        "#870585",
        "#87054f",
        "#070587",
        "#036b80",
        "#03801e",
        "#807803",
        "#803903",
        "#800303"]
    return random.choice(color)
