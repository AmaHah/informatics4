def main(s):
    if ("<" or ">") not in s: return s

    tag_name = get_tag_name(s)
    open_tag = f"<{tag_name}>"
    close_tag = f"</{tag_name}>" 
    
    print(s)

    if s.find(close_tag) + len(close_tag) == len(s):
        return {tag_name: main(s[s.find(open_tag) + len(open_tag):s.find(close_tag)])}
    return {tag_name: main(s[s.find(open_tag) + len(open_tag):s.find(close_tag)]), get_tag_name(s[s.find(close_tag) + len(close_tag):]): main(s[s.find(close_tag) + len(close_tag):])}


def get_tag_name(s):
    return s[s.find('<')+1:s.find(">")]




a = open("file.txt", "r").read()
a = a.replace('\t', '').replace('\n', '')
print(main(a))