def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="content">
    <div class="content_title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="main_idea">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept

MY_TEXT="""
TITLE: HTML Basics
DESCRIPTION: HTML stands for Hyper Text Markup Language, which is what defines most web pages.  HTML is made up of the following...  Text content shows what you see.  Markup shows what your page will look like.  References to other documents, such as images are possible.  Links to other web pages are possible too.
TITLE: Tags
DESCRIPTION: HTML uses tags in a certain structure to create a webpage, such as !doctype, head, title, body, etc.  Tags are what HTML uses to mark text in a certain way.  A tag normally has an opening tag, text, then a closing tag.  Tags that do not contain content are called "void" tags.  I learned how to use bold and to provide emphasis via the italics tags.
TITLE: Inline vs. Blocks
DESCRIPTION: Tags can be either inline or block.  Inline tags examples are break, bold, emphasis, void tags, new lines, etc.  Block tags create an invisible block around the content.  Examples of this is paragraph and div."""

def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html

print generate_all_html(MY_TEXT)

