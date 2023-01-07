import PyPDF2
import markdown

# Open the PDF file in read-binary mode
with open('The Elements of Computing Systems.pdf', 'rb') as file:
  # Create a PDF object
  pdf = PyPDF2.PdfReader(file)

  # Create a list to store the text from each page
  text_list = []

  # Iterate over every page in the PDF
  for page in range(len(pdf.pages)):
    # Extract the text from the page
    text = pdf.pages[page].extract_text()

    # Add the text to the list
    text_list.append(text)

  # Join the text from the list into a single string
  all_text = '\n'.join(text_list)

  # Convert the text to Markdown
  markdown_text = markdown.markdown(all_text)

  # Write the Markdown text to a file
  with open('The Elements of Computing Systems.md', 'w') as outfile:
    outfile.write(markdown_text)
