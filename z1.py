import xml.etree.ElementTree as ET

def authors_pairs(authors):
    pairs = []
    for i in range(len(authors) - 1):
        for j in range(i + 1, len(authors)):
            pairs.append((authors[i], authors[j]))

    return pairs

def format_name(author):
    return "%s, %s" % (author[0].text, author[1].text)

def parse_authors(article):
    return map(format_name, article[1])

def get_all_ordered_names(index):
    return sorted(index, key=index.get)

def get_author_index(author, author_index, A):
    '''
    Gets ID of the author from the global index of authors.
    This index means row/column of current author.
    If author is missing there - add them first.
    '''
    if author not in author_index:
        author_index[author] = len(author_index)
        # adding new row and column for this author
        [c.append(0) for c in A]
        A.append([0]*len(author_index))

    return author_index[author]

def print_matrix(A, author_index):
    header = get_all_ordered_names(author_index)
    print(''.join(["| {:15.15}".format(x) for x in [''] + header]))
    print('|' + '-'*16*(len(header) + 1))

    for i in range(len(A)):
        print(''.join(["| {:15.15}".format(x) for x in [header[i]] + map(str, A[i])]))

def main():
    root = ET.parse('test.xml').getroot()
    author_index = {}
    A = [] # matrix that we are interested in

    for article in root:
        authors = parse_authors(article)
        pairs = authors_pairs(authors)
        for pair in pairs:
            index_1 = get_author_index(pair[0], author_index, A)
            index_2 = get_author_index(pair[1], author_index, A)
            A[index_1][index_2] += 1
            A[index_2][index_1] += 1

    print_matrix(A, author_index)
    return A


if __name__ == "__main__":
    main()
