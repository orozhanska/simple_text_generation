import io
import re

pattern = r"\b\w+(?:'\w+)?\b|[^\w\s]"

with io.open('to_kill_a_mockingbird.txt', encoding='utf-8') as file:
    file_content = file.read().lower().replace('\n', ' ').replace('“', '').replace('”', '')
    tokens = re.findall(pattern, file_content)
    keys = set(tokens)
    tokens_dict = {}
    for key in keys:
        if key not in tokens_dict:
            tokens_dict[key] = []
        for ind, token in enumerate(tokens):
            if token == key:
                if ind != len(tokens) - 1:
                    tokens_dict[key].append(tokens[ind + 1])
