import requests
import datetime

USERNAME = "CodeNinja22-AS"

def get_contributions(username):
    url = f"https://github-contributions-api.jogruber.de/v4/{username}"
    data = requests.get(url).json()
    return data["contributions"]

def get_color(count):
    if count == 0:
        return "#161b22"   # dark background
    elif count < 2:
        return "#3b0a0a"
    elif count < 5:
        return "#7a0f0f"
    elif count < 10:
        return "#b91c1c"
    else:
        return "#ff4d4d"

def generate_svg(contributions):
    size = 12
    gap = 3

    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="150">']
    svg.append('<rect width="100%" height="100%" fill="#0d1117"/>')

    x_offset = 10
    y_offset = 20

    for i, day in enumerate(contributions):
        x = x_offset + (i % 52) * (size + gap)
        y = y_offset + (i // 52) * (size + gap)

        color = get_color(day["count"])

        svg.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}" rx="2"/>')

    svg.append('</svg>')
    return "\n".join(svg)

def main():
    contributions = get_contributions(USERNAME)
    svg = generate_svg(contributions)

    with open("dist/heatmap.svg", "w") as f:
        f.write(svg)

if __name__ == "__main__":
    main()
