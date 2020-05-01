"""
Clean solution to the following problem using regex:

What might not be so trivial is instead to get a decent breadcrumb from your current url. For this kata, your purpose
is to create a function that takes a url, strips the first part (labelling it always HOME) and then builds it making
each element but the last a <a> element linking to the relevant path; last has to be a <span> element getting the
active class.

All elements need to be turned to uppercase and separated by a separator, given as the second parameter of the
function; the last element can terminate in some common extension like .html, .htm, .php or .asp; if the name of the
last element is index.something, you treat it as if it wasn't there, sending users automatically to the upper level
folder.

Well, probably not so much, but we have one last extra rule: if one element (other than the root/home) is longer than
30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be
always given in the format this-is-an-element-of-the-url and you should ignore words in this array while
acronymizing: ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; a url composed of more words
separated by - and equal or less than 30 characters long needs to be just uppercased with hyphens replaced by spaces.

Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.
"""
# imports
import re


def generate_bc(url, separator):
    """

    Args:
        url: string url in the format of f.ex.
        "mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm"
        separator: separator symbol for breadcrumbs such as "/", "+" etc.

    Returns:
        string of breadcrumbs such as f.ex. '<a href="/">HOME</a> > <a
        href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span
        class="active">EXAMPLE</span>'
    """

    def formater(name):
        """
        Finds acronyms and removes stop words.
        Args:
            name: value name to be shortened

        Returns:
            Acronyms of words
        """
        if len(name) > 30:
            stoplist = ['the', 'of', 'in', 'from', 'by', 'with', 'and', 'or', 'for', 'to', 'at', 'a']
            return ''.join([ch[0].upper() for ch in name.split('-') if ch not in stoplist])
        else:
            return name.replace('-', ' ').upper()

    result = []

    url = re.sub(r'^https?:\/\/', '', url)  # remove protocol
    url = re.sub(r'\.[^\/]*$', '', url)  # remove extensions
    url = re.sub(r'(?:\#|\?).*$', '', url)  # remove anchors and queries
    url = re.sub(r'index$', '', url)  # remove indexes
    url = url.rstrip('/')  # remove trailing slash

    crumbs = url.split('/')

    for i, crumb in enumerate(crumbs):
        if i == 0:
            result.append('<a href="/">HOME</a>' if len(crumbs) > 1 else '<span class="active">HOME</span>')
        elif i == len(crumbs) - 1:
            result.append('<span class="active">{}</span>'.format(formater(crumb)))
        else:
            result.append('<a href="/{}/">{}</a>'.format('/'.join(crumbs[1: 1 + i]), formater(crumb)))

    return separator.join(result)
