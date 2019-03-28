
Source: W3 schools

What is a HTML?
- HTML is the standard markup language for creating Web pages.
- It stands for Hyper Text Markup Language.
- It describes the structure of Web pages using markup.
- The HTML elements are the building blocks of HTML pages, which are represented by tags.
- HTML tags label pieces of content such as "heading", "paragraph", "table", and so on.

How is it displayed on a web browser?
- While browsers do not display the HTML tags, but use them to render the content of the page.
- Only the content inside the <body> section is displayed in a browser.

Why HTML?

HTML Attributes:
- All HTML elements can have attributes.
- Attributes provide additional information about an element.
- Attributes usually come in name/value pairs like: name="value".
- <a href => </a> for links
- <img src = ></img> for images
- The alt attribute specifies an alternative text to be used, when an image cannot be displayed.
- The value of the attribute can be read by screen readers. This way, someone "listening" to the webpage, e.g. a blind person, can "hear" the element.
- W3C recommends lowercase in HTML, and demands lowercase for stricter document types like XHTML.

HTML headings:
- Search engines use the headings to index the structure and content of your web pages.
- Users skim your pages by its headings. It is important to use headings to show the document structure.
- Don't use headings to make text BIG or bold.
- Each HTML heading has a default size. However, you can specify the size for any heading with the style attribute, using the CSS font-size property.

HTML Style Attribute:
- <tagname style="property:value;"> syntax

HTML Formatting:
Formatting elements were designed to display special types of text:
<b> - Bold text
<strong> - Important text
<i> - Italic text
<em> - Emphasized text
<mark> - Marked text
<small> - Small text
<del> - Deleted text
<ins> - Inserted text
<sub> - Subscript text
<sup> - Superscript text
<b> and <i> defines bold and italic text, but <strong> and <em> means that the text is "important".

CSS:
- CSS stands for Cascading Style Sheets.
- CSS describes how HTML elements are to be displayed on screen, paper, or in other media.
- It can control the layout of multiple web pages all at once.
- CSS can be added to HTML elements in 3 ways:
    - Inline - by using the style attribute in HTML elements
    - Internal - by using a <style> element in the <head> section
    - External - by using an external CSS file
- The most common way to add CSS, is to keep the styles in separate CSS files.

Important points while coding:
- HTML elements can be nested (elements can contain elements).
- Some HTML elements will display correctly, even if you forget the end tag.
  But tags like comment tag (<!-->) need to be ended as it will take the code further this tag as comments if not properly ended.
- HTML elements with no content are called empty elements.
- <br> is an empty element without a closing tag (the <br> tag defines a line break).
- Empty elements can be "closed" in the opening tag like this: <br />.
- HTML5 does not require empty elements to be closed. But if you want stricter validation,
  or if you need to make your document readable by XML parsers, you must close all HTML elements properly.
- HTML tags are not case sensitive. But lowercase is recommended for clean code.
- W3C recommends quotes in HTML, and demands quotes for stricter document types like XHTML.
- Double quotes around attribute values are the most common in HTML, but single quotes can also be used.
- Metadata typically define the document title, character set, styles, links, scripts, and other meta information.
- Browsers automatically add some white space (a margin) before and after a paragraph.
- With HTML, you cannot change the output by adding extra spaces or extra lines in your HTML code.
- The browser will remove any extra spaces and extra lines when the page is displayed.
- HTML also defines special elements for defining text with a special meaning.
- HTML colors are specified using predefined color names, or RGB, HEX, HSL, RGBA, HSLA values.
-

How to View HTML Source?
View HTML Source Code:
Right-click in an HTML page and select "View Page Source" (in Chrome) or "View Source" (in IE), or similar in other browsers.
This will open a window containing the HTML source code of the page.
Inspect an HTML Element:
Right-click on an element (or a blank area), and choose "Inspect" or "Inspect Element" to see what elements are made up of.
You can also edit the HTML or CSS on-the-fly in the Elements or Styles panel that opens.
