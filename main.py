from pylatex import *

doc = Document(documentclass = 'article')
def generate_header(title):
    geometry_options = {"margin": "0.7in"}
    doc = Document(geometry_options=geometry_options)
    # Add document header
    header = PageStyle("header")
    # Create left header
    with header.create(Head("L")):
        header.append("Name: ")
    # Create center header
    with header.create(Head("C")):
        header.append("Date: ")
    # Create right header
    with header.create(Head("R")):
        header.append("Period: ")

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(title))
        doc.append(LineBreak())

print("Enter the title of the test: ")
title = input()
generate_header(title)
doc.generate_tex("header")