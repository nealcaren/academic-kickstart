import re
import os

def parse_bib(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []
    # Split by newline + @ to separate entries robustly
    raw_chunks = re.split(r'\n@', '\n' + content)
    
    for chunk in raw_chunks:
        if not chunk.strip(): continue
        
        type_match = re.match(r'^(\w+)\s*\{', chunk)
        if not type_match: continue
        
        entry = {'type': type_match.group(1)}
        
        lines = chunk.split('\n')
        current_field = None
        current_value = []
        
        for line in lines:
            line = line.strip()
            if not line: continue
            
            field_match = re.match(r'^(\w+)\s*=\s*(.*)', line)
            
            if field_match:
                if current_field:
                    full_val = " ".join(current_value)
                    full_val = clean_bib_value(full_val)
                    entry[current_field.lower()] = full_val
                
                current_field = field_match.group(1)
                val_start = field_match.group(2)
                current_value = [val_start]
            else:
                if current_field:
                    current_value.append(line)
                    
        if current_field:
            full_val = " ".join(current_value)
            full_val = clean_bib_value(full_val)
            entry[current_field.lower()] = full_val
            
        entries.append(entry)
        
    return entries

def clean_bib_value(val):
    val = val.strip()
    if val.endswith(','):
        val = val[:-1]
    
    # Remove quotes/braces
    while (val.startswith('{') and val.endswith('}')) or \
          (val.startswith('"') and val.endswith('"')):
        val = val[1:-1].strip()
    
    val = val.replace('{', '').replace('}', '')
    val = val.replace('--', '-')
    return val

def format_authors(author_str):
    if not author_str: return ""
    author_str = re.sub(r'\s+', ' ', author_str)
    authors = author_str.split(' and ')
    formatted = []
    for i, auth in enumerate(authors):
        parts = auth.split(',')
        if len(parts) >= 2:
            last = parts[0].strip()
            first = parts[1].strip()
            if i == 0:
                formatted.append(f"{last}, {first}")
            else:
                formatted.append(f"{first} {last}")
        else:
            formatted.append(auth)
    if len(formatted) == 0: return ""
    if len(formatted) == 1: return formatted[0]
    if len(formatted) == 2: return f"{formatted[0]} and {formatted[1]}"
    return ", ".join(formatted[:-1]) + f", and {formatted[-1]}"

def find_bib_files(root_dir):
    bib_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.bib'):
                bib_files.append(os.path.join(root, file))
    return bib_files

def main():
    bib_files = []
    if os.path.exists('data/publications.bib'):
        bib_files.append('data/publications.bib')
    
    bib_files.extend(find_bib_files('publications'))
    
    entries = []
    seen_titles = set()
    
    for bib_path in bib_files:
        try:
            parsed = parse_bib(bib_path)
            for p in parsed:
                # Deduplicate by title (normalized)
                title_norm = re.sub(r'\W+', '', p.get('title', '').lower())
                if title_norm and title_norm not in seen_titles:
                    seen_titles.add(title_norm)
                    entries.append(p)
        except Exception as e:
            print(f"Skipping {bib_path}: {e}")
    
    entries = [e for e in entries if 'year' in e]
    entries.sort(key=lambda x: x.get('year', '0000'), reverse=True)
    
    md_lines = [
        "---",
        "title: \"Publications\"",
        "page-layout: article",
        "---",
        "",
        "::: {.publications-list}",
        ""
    ]
    
    for e in entries:
        authors = format_authors(e.get('author', ''))
        year = e.get('year', '')
        title = e.get('title', 'Untitled')
        journal = e.get('journal', e.get('booktitle', ''))
        doi = e.get('doi', '')
        volume = e.get('volume', '')
        issue = e.get('number', '')
        pages = e.get('pages', '')
        
        if doi:
            if not doi.startswith('http'):
                url = f"https://doi.org/{doi}"
            else:
                url = doi
            title_html = f'<a href="{url}" target="_blank">{title}</a>'
        else:
            title_html = title
            
        citation_details = ""
        if volume:
            citation_details += f" {volume}"
        if issue:
            citation_details += f"({issue})"
        if pages:
            if volume or issue:
                citation_details += f":{pages}"
            else:
                citation_details += f" {pages}"

        line = f"{authors}. {year}. \"{title_html}.\""
        if journal:
             line += f" *{journal}*"
        line += f"{citation_details}."
        
        md_lines.append(line + "\n")
        
    md_lines.append(":::")
    
    with open('publications/index.qmd', 'w') as f:
        f.write('\n'.join(md_lines))
        
    print(f"Generated {len(entries)} publications from {len(bib_files)} bib files.")

if __name__ == "__main__":
    main()
