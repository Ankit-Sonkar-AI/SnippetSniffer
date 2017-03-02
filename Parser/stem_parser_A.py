'''

split file into paragraphs
for each paragraph
    for each word
        find stems (if any)
        #record link between paragraph and stem
        create_stem_cloud_for_paragraph

Data:
    stems [
        1 : [cat, kitty.., ], 
        2 :  [dog, doggo]
    ]
    paragraphs [
        1 : "bkakawbkjbkb",
        2 : "jlknan lanck  ewclwehc"
    ]
    link_paragraphs_stems [
        1 : [p1, s1, 3, "cat 2, kitty 1"],
        2 : [p2, s2],
        3 : [p2, s1]
    ]

q = "khk kjkjh k jkkj"
1, 2
{s1: s2} = {cT , DOG, KITYY, DOGGO}
 
 P1 = tHE CAT CHASES THE DOG 
 sT1 = {S(tHE)+S(CAT)+ S(CHASE)} 

    link_para [
        1: [p1, {s1:s3:s2}] - 2
        2: [p2, {s2:s1}]
        .
        .
        N: 
    ]
'''

import time
def is_separator(line):
    text = line.strip()
    premises = [
        is_time_string(text), 
        is_all_dashes(text)
        ]
    return any(premises)

def is_all_dashes(text):
    """
    >>> is_all_dashes("-90")
    False
    >>> is_all_dashes("----")
    True
    >>> is_all_dashes("")
    False
    """
    i = len(text)
    return text.count("-") == i and i > 0

def is_time_string(text):
    """
    >>> is_time_string("hello byee bye")
    False
    >>> is_time_string("5:16")
    True
    """
    try:
        time.strptime(text, '%H:%M')
        return True
    except ValueError:
        return False

def extract_paragraphs(file):
    with open(file) as f:
        lines = f.readlines()
    paragraphs = []
    paragraph = None
    for line in lines:
        if is_separator(line) or paragraph is None:
            paragraph = []
            paragraphs.append(paragraph)
        else:
            paragraph.append(line)
    return ["".join(paragraph) for paragraph in paragraphs]

def run():
    paragraphs = extract_paragraphs(file)
    paragraph_stem_clouds = []
    for paragraph in paragraphs:
        stemcloud = StemCloud()
        paragraph_stem_clouds.append(stemcloud)

def demo_file():
    file = "JuanEnriquez_2016T-480p.txt"
    f = extract_paragraphs(file)
    print(len(f))
    #for i in extract_paragraphs(file)[:4]:
    #    print(i)



if __name__ == "__main__":
    #if "--count-dashes" in sys.argv:
    #    premises.append()
    import doctest
    doctest.testmod()
    demo_file()
    print("Tests finished")



