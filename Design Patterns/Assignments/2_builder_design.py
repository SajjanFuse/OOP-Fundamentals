"""
Design a document generator using the Builder Design Pattern.
Create a DocumentBuilder that creates documents of various 
types (e.g., PDF, HTML, Plain Text). Implement the builder 
methods to format the document content and structure 
according to the chosen type. Demonstrate how the Builder 
Design Pattern allows for the creation of different 
document formats without tightly coupling the document 
generation logic.
"""
from abc import ABC 
from abc import abstractmethod


# every document will have these contents
class DocumentBuilder(ABC):
    @abstractmethod
    def create_title(self, title):
        pass
    
    @abstractmethod
    def create_heading(self, heading):
        pass
    
    @abstractmethod
    def create_paragraph(self, paragraph):
        pass
    
    @abstractmethod
    def get_document(self):
        pass

    @abstractmethod
    def save_document(self):
        pass


class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = "PDF Document\n\n"

    def create_title(self, title):
        self.document += f"Title: {title}\n"

    def create_heading(self, heading):
        self.document += f"Heading: {heading}\n"

    def create_paragraph(self, paragraph):
        self.document += f"Paragraph: {paragraph}\n"

    def get_document(self):
        return self.document
    
    # this does not really save it in pdf format
    # just an instance of how it can be saved
    def save_document(self):
        with open('pdf_doc' + '.pdf', "w") as f:
            f.write(self.document)


class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = "<html>\n<body>\n"

    def create_title(self, title):
        self.document += f"<h1>{title}</h1>\n"

    def create_heading(self, heading):
        self.document += f"<h2>{heading}</h2>\n"

    def create_paragraph(self, paragraph):
        self.document += f"<p>{paragraph}</p>\n"

    def get_document(self):
        self.document += "</body>\n</html>"
        return self.document
    
    def save_document(self):
        with open('html_doc' + '.html', "w") as f:
            f.write(self.document)


class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

    def create_title(self, title):
        self.document += f"Title: {title}\n"

    def create_heading(self, heading):
        self.document += f"Heading: {heading}\n"

    def create_paragraph(self, paragraph):
        self.document += f"Paragraph: {paragraph}\n"

    def get_document(self):
        return self.document
    
    def save_document(self):
        with open('plaintext_doc'+'.txt', "w") as f:
            f.write(self.document)


class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_document(self, title, heading, paragraphs):
        self.builder.create_title(title)
        self.builder.create_heading(heading)
        for paragraph in paragraphs:
            self.builder.create_paragraph(paragraph)

        self.builder.save_document()


pdf_builder = PDFDocumentBuilder()
pdf_director = DocumentDirector(pdf_builder)
pdf_director.build_document("Sample PDF Document", "Introduction", ["Paragraph 1", "Paragraph 2"])
pdf_document = pdf_builder.get_document()
print("PDF Document:")
print(pdf_document)

htmldoc_builder = HTMLDocumentBuilder()
htmldoc_director = DocumentDirector(htmldoc_builder)
htmldoc_director.build_document("Sample HTML Document", "Introduction", ["Paragraph 1", "Paragraph 2"])
htmldoc_document = htmldoc_builder.get_document()
print("HTML Document:")
print(htmldoc_document)

plaintext_builder = PlainTextDocumentBuilder()
plaintext_director = DocumentDirector(plaintext_builder)
plaintext_director.build_document("Sample PlainText Document", "Introduction", ["Paragraph 1", "Paragraph 2"])
plaintext_document = plaintext_builder.get_document()
print("PlainText Document:")
print(plaintext_document)