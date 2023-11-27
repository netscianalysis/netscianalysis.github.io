from pathlib import Path


def make_examples_collapsible(html_path):
    with open(html_path, "r") as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            line = line.replace("</div><!-- fragment -->", "</div><!-- fragment -->\n</details>\n\n")
            line = line.replace("<p><b>Python Example</b><br  />", "\n<details><p><summary><b>Python Example</b></summary>\n\n")
            line = line.replace("<p> <b>Python Example</b><br  />", "\n<details><p><summary><b>Python Example</b></summary>\n\n")
            line = line.replace("<p><b>C++ Example</b><br  />", "\n<details><p><summary><b>C++ Example</b></summary>\n\n")

            new_lines.append(line)
        with open(html_path, "w+") as f:
            for line in new_lines:
                f.write(line)


if __name__ == "__main__":
    network_html = Path.cwd() / "classNetwork.html"
    cuarray_html = Path.cwd() / "classCuArray.html"
    node_html = Path.cwd() / "classNode.html"
    atoms_html = Path.cwd() / "classAtoms.html"
    atom_html = Path.cwd() / "classAtom.html"
    netcalc_html = Path.cwd() / "namespacenetcalc.html"
    html_files = [network_html, cuarray_html, node_html, atoms_html, atom_html, netcalc_html]
    for f in html_files:
        make_examples_collapsible(f)
