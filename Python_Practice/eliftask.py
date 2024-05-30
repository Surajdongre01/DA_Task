##join text

def join_text(*args,seprator=" "):
    return seprator.join(args)

text1 = 'arc'
text2 = 'technologies'

joined_text = join_text(text1, text2)

print(joined_text)


## Trim Text


def trim(text, side= 'both'):
    if (side == 'both'):
        return text.strip()
    elif(side == 'left'):
        return text.lstrip()
    elif (side == 'right'):
        return text.rstrip()
    else:
        return "choose correct trim"

text = " arc"    
trimmed_text = trim(text, 'right')

print(trimmed_text)
    

### Substitute text

def substitute(text, old_string, new_string):
    return text.replace(old_string,new_string)

orignal_text = "i am going to newyork"
old_text = "newyork"
new_text = "USA"

substituted_text = substitute(orignal_text,old_text,new_text)

print(orignal_text)
print()
print(substituted_text)


### Cut Text

def cut_text(text, max_length):
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length]

original_text = "i love india"
cut_text_result = cut_text(original_text, 7)
print()
print(cut_text_result)
