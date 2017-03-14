#!/usr/bin/env /bin/bash
# Convert every .ipynb as fake .html files

function tohtml() {
    ipynb="${1}"
    html="${1%.ipynb}.html"
    echo -e "\nJupyter notebook = $ipynb ---> HTML file = $html"
    ls -larth "$ipynb"
    ls -larth "$html" 2>/dev/null
    if [ -f "$ipynb" ]; then
        if [ -f "$html" ]; then
            echo -e "${red}Warning${white}: $html already exist."
            cp -vf "$html" /tmp/
        fi
        echo -e jupyter-nbconvert "$ipynb" --to html --output "$(basename "$html")"
        jupyter-nbconvert "$ipynb" --to html --output "$(basename "$html")"
    else
        echo -e "${red}Error${white}: $ipynb does not exist."
    fi
}

for i in *.ipynb */*.ipynb; do
    tohtml "$i"
done
