import re

with open('file_with_comments.txt', 'r') as f:
    text = f.read()

# видалення коментарів, що починаються з /* та закінчуються на */
text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

with open('file_without_comments.txt', 'w') as f:
    f.write(text)