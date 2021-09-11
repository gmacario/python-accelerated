# slides-revealjs

File `slides-python.md` in this directory contains the slides in Markdown.

## How to display slides

There are several ways which can be used to render the slides.

### Using reveal.js

The slides may be rendered using the [reveal.js](https://revealjs.com/) HTML presentation framework.

Please refer to the [reveal.js installation guide](https://revealjs.com/installation/) for details.

### Using reveal-md

Alternatively, you may use the [reveal-md](https://github.com/webpro/reveal-md) package:

#### Installation

```bash
npm install -g reveal-md
```

#### Usage

```bash
reveal-md contrib/slides-revealjs/slides-python.md
```

Result:

```text
gmaca@alpha MINGW64 /e/data/gmaca/github/gmacario/python_accelerated (master)
$ reveal-md contrib/slides-revealjs/slides-python.md 
Reveal-server started at http://localhost:1948
```

You browser will also automatically open a page with the slides rendered in HTML.


### Using VScode

Alternatively, if you are using Visual Studio Code you may install
the "[reveal-markdown](https://github.com/tokiedokie/reveal-markdown)"
extension

> VSCode: View > Extensions

then install extension "reveal-markdown"
(do not install "vscode-reveal" which is no longer maintained)

Once the extension is installed, press `Ctrl-Shift-P` to activate the Command Palette,
then run the following command

> "VSCode Reveal: Focus on Slides View"

which will make it easier to navigate across the slides of the presentation.

At the top right of this view you should also find a few icons which allow you to

- Export the slides in HTML
- Export the slides in PDF
- Open presentation in browser
- Show presentation by side

## How to customize the slides

Please refer to the documentation at <https://revealjs.com/>

<!-- EOF -->