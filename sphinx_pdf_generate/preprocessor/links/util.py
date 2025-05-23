import os
import re
from pathlib import Path

from bs4 import BeautifulSoup
from weasyprint import urls


# check if href is relative --
# if it is relative it *should* be an HTML that generates a PDF doc
def is_doc(href: str):
    tail = Path(href).name
    ext = Path(tail).suffix

    absurl = urls.url_is_absolute(href)
    abspath = os.path.isabs(href)
    htmlfile = ext.startswith(".html")
    relative_link = re.search(r"^\.{,2}?[\w\-.~$&+,/:;=?@%#*]*?$", href)
    if relative_link is not None:
        return True
    if absurl or abspath or not htmlfile:
        return False

    return True


def rel_html_href(base_url: str, href: str, site_url: str, outdir: str):
    new_base_url = os.path.dirname(base_url)
    rel_url = new_base_url.replace("file://", "")
    pattern = r"^(/tmp|tmp)/pages[\w\-]+|^[\w\-:\\]+\\+(temp|Temp)\\+pages[\w\-]+|^{}".format(outdir.replace("\\", "/").rstrip("/"))
    replace_build_dir = re.compile(pattern)

    internal = href.startswith("#")
    web_url = re.search(r"^(https://|http://|mailto:|tel:)", href)
    if web_url or internal or not is_doc(href):
        return href

    # Include absolute paths to other page files relative to the build directory
    if href.startswith('/'):
        abs_html_href = site_url.rstrip("/") + href
    else:
        abs_html_href = Path(rel_url).joinpath(href).resolve()
        abs_html_href = replace_build_dir.sub(site_url.rstrip("/"), str(abs_html_href))
        abs_html_href = abs_html_href.replace("\\", "/")
    if abs_html_href:
        return urls.iri_to_uri(abs_html_href)
    return href


def abs_asset_href(href: str, base_url: str):
    if urls.url_is_absolute(href) or Path(href).is_absolute():
        return href
    return urls.iri_to_uri(urls.urljoin(base_url, href))


#
def replace_asset_hrefs(soup: BeautifulSoup, base_url: str):
    """Replace hrefs and srcs in link and img tags respectively by making all relative asset links absolute"""
    for link in soup.find_all("link", href=True):
        link["href"] = abs_asset_href(link["href"], base_url)

    for asset in soup.find_all(src=True):
        asset["src"] = abs_asset_href(asset["src"], base_url)
    return soup
