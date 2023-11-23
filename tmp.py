from pathlib import Path

network_html = Path.cwd() / "classNetwork.html"

with open(network_html, "r") as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        line = line.replace("</div><!-- fragment -->", "</div><!-- fragment -->\n</details>\n\n")
        line = line.replace("<p><b>Python Example</b><br  />", "\n<details><p><summary><b>Python Example</b></summary>\n\n")
        line = line.replace("<p> <b>Python Example</b><br  />", "\n<details><p><summary><b>Python Example</b></summary>\n\n")
        line = line.replace("<p><b>C++ Example</b><br  />", "\n<details><p><summary><b>C++ Example</b></summary>\n\n")

        new_lines.append(line)
    with open(network_html, "w+") as f:
        for line in new_lines:
            f.write(line)

