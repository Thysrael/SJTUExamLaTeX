import re

section_pattern = re.compile(
    r'\\section\{(?P<title>.*?)(?:\\score\{(?P<score>[^}]*)\})?\}'
)

score_pattern = re.compile(r'\\score\{([^}]*)\}')

answer_pattern = re.compile(r'\\begin\{answer\}.*?\\end\{answer\}', re.DOTALL)

results = []

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

content_without_answers = answer_pattern.sub('', content)

lines = content_without_answers.splitlines(True)

for line_no, line in enumerate(lines, start=0):
    matches = section_pattern.finditer(line)
    for match in matches:
        title = match.group('title').strip()
        score = match.group('score')
        results.append({'line': line_no, 'title': title, 'score': score})

all = 0
for i, section in enumerate(results):
    start = int(section['line'] + 1)
    end = len(lines) if i == len(results) - 1 else results[i + 1]['line'] - 1
    text = ''.join(lines[start:end])
    scores = score_pattern.findall(text)
    scores = [int(score) for score in scores]
    all += sum(scores)
    if section['score'] == None:
        print(section['title'], "doesn't have score, which should be", sum(scores))
    elif int(section['score']) != sum(scores):
        print(section['title'], "has score", section['score'], ", which should be", sum(scores))

if all != 100:
    print('Total score is', all)