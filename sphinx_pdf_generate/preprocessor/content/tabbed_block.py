import re

from bs4 import BeautifulSoup


def restructure_tabbed_content(soup: BeautifulSoup) -> BeautifulSoup:
    """
    Function to restructure tabbed content in HTML, so it can be compatible for PDF conversion.

    :param soup: HTML content
    :return: Restructured HTML content
    """
    labels = soup.find_all("label", attrs={"for": re.compile(r"^__tabbed_[\d_]+$|^sd-tab-item-\d+$")})
    print(f'Labels: {labels}\n\n')
    blocks = soup.find_all("div", attrs={"class": re.compile(r"tabbed-block|sd-tab-content")})
    print(f'Blocks: {blocks}\n\n')
    tab_content = soup.find_all("div", attrs={"class": "tabbed-content"})
    print(f'Content: {tab_content}\n\n')

    new_blocks = []

    for div in blocks:
        div["class"] = "new_tabbed_block"
        new_blocks.append(div)

    for label, div in zip(labels, new_blocks):
        label.insert_after(div)

    for tab_ in tab_content:
        tab_.decompose()

    return soup
