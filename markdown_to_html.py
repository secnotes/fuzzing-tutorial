#!/usr/bin/env python3
"""
Convert Markdown files to HTML with a responsive template and TOC sidebar.
This script converts the fuzzing tutorial markdown files to HTML format
and saves them in the docs/ directory with a table of contents sidebar.
"""

import os
import markdown
import glob
from pathlib import Path
import re


def extract_toc_from_markdown(markdown_content):
    """
    Extract table of contents from markdown content by finding headers
    """
    toc = []
    # Regex to find headers in markdown
    header_pattern = r'^(#{1,6})\s+(.*)'

    lines = markdown_content.split('\n')
    for line in lines:
        match = re.match(header_pattern, line.strip())
        if match:
            level = len(match.group(1))  # Number of # indicates header level
            title = match.group(2).strip()

            # Create slug for anchor link (convert spaces to hyphens, remove special chars)
            slug = re.sub(r'[^\w\s-]', '', title.lower()).strip().replace(' ', '-')

            toc.append({
                'level': level,
                'title': title,
                'slug': slug
            })

    return toc


def generate_sidebar_toc(toc):
    """
    Generate HTML sidebar TOC based on extracted TOC
    """
    if not toc:
        return "<p>No table of contents available</p>"

    html = '<div class="toc-title">Contents</div>\n<ul class="toc-list">\n'

    current_level = 1
    for item in toc:
        level = item['level']

        # Adjust nesting based on level
        if level > current_level:
            # Open nested lists
            for _ in range(level - current_level):
                html += '    <ul class="nested-toc">\n'
        elif level < current_level:
            # Close nested lists
            for _ in range(current_level - level):
                html += '    </ul>\n</li>\n'

        # Add list item
        html += f'    <li><a href="#{item["slug"]}">{item["title"]}</a>'

        current_level = level

    # Close any remaining nested lists
    for _ in range(current_level - 1):
        html += '    </ul>\n</li>\n'
    html += '</li>\n</ul>\n'

    return html


def convert_markdown_to_html(input_file, output_dir):
    """
    Convert a single markdown file to HTML with a responsive template and TOC sidebar
    """

    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Extract TOC before converting to HTML
    toc = extract_toc_from_markdown(markdown_content)

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'toc',
        'codehilite'
    ])
    html_body = md.convert(markdown_content)

    # Extract title from the first heading
    title_match = re.match(r'^#\s+(.+)', markdown_content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
    else:
        title = Path(input_file).stem.replace('_', ' ').title()

    # Generate the sidebar TOC
    sidebar_content = generate_sidebar_toc(toc)

    # Create the complete HTML document with responsive template and sidebar
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Fuzzing Tutorial</title>
    <style>
        /* CSS Reset */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        /* Main styles */
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
            padding: 0;
            margin: 0;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            gap: 20px;
        }}

        .main-content {{
            flex: 1;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .sidebar {{
            width: 300px;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            align-self: flex-start;
            position: sticky;
            top: 20px;
            max-height: calc(100vh - 40px);
            overflow-y: auto;
        }}

        .toc-title {{
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 1rem;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
        }}

        .toc-list {{
            list-style-type: none;
            padding-left: 0;
        }}

        .toc-list li {{
            margin-bottom: 0.5rem;
        }}

        .toc-list a {{
            color: #2980b9;
            text-decoration: none;
            display: block;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            transition: all 0.2s;
        }}

        .toc-list a:hover {{
            background-color: #e3f2fd;
            color: #1a5ca3;
            padding-left: 0.75rem;
        }}

        .nested-toc {{
            padding-left: 1rem;
            margin-top: 0.25rem;
        }}

        header {{
            background-color: #2c3e50;
            color: white;
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 20px;
        }}

        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        h1 {{
            font-size: 1.8rem;
            margin-bottom: 0;
        }}

        nav ul {{
            list-style: none;
            display: flex;
            gap: 1rem;
        }}

        nav a {{
            color: white;
            text-decoration: none;
            padding: 0.5rem;
            border-radius: 4px;
            transition: background-color 0.2s;
        }}

        nav a:hover {{
            background-color: #34495e;
        }}

        .main-content_area {{
            padding: 1rem 0;
        }}

        /* Markdown content styling */
        .markdown-body {{
            max-width: 100%;
        }}

        .markdown-body h1, .markdown-body h2, .markdown-body h3, .markdown-body h4, .markdown-body h5, .markdown-body h6 {{
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            color: #2c3e50;
        }}

        .markdown-body h1 {{
            font-size: 2.2rem;
            border-bottom: 2px solid #eee;
            padding-bottom: 0.5rem;
        }}

        .markdown-body h2 {{
            font-size: 1.8rem;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.3rem;
        }}

        .markdown-body h3 {{
            font-size: 1.5rem;
        }}

        .markdown-body p {{
            margin-bottom: 1rem;
        }}

        .markdown-body ul, .markdown-body ol {{
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }}

        .markdown-body li {{
            margin-bottom: 0.5rem;
        }}

        .markdown-body a {{
            color: #3498db;
            text-decoration: none;
        }}

        .markdown-body a:hover {{
            text-decoration: underline;
        }}

        .markdown-body img {{
            max-width: 100%;
            height: auto;
        }}

        .markdown-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }}

        .markdown-body th, .markdown-body td {{
            border: 1px solid #ddd;
            padding: 0.75rem;
            text-align: left;
        }}

        .markdown-body th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}

        .markdown-body tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        .markdown-body code {{
            background-color: #f4f4f4;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        }}

        .markdown-body pre {{
            background-color: #2d3748;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: 5px;
            overflow-x: auto;
            margin: 1rem 0;
        }}

        .markdown-body pre code {{
            background: none;
            padding: 0;
            color: inherit;
        }}

        .markdown-body blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 1rem;
            margin: 1rem 0;
            color: #666;
            font-style: italic;
            background-color: #f8f9fa;
            border-radius: 0 4px 4px 0;
        }}

        .markdown-body hr {{
            border: 0;
            border-top: 1px solid #eee;
            margin: 2rem 0;
        }}

        footer {{
            text-align: center;
            padding: 2rem 0 1rem;
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-top: 2rem;
            border-top: 1px solid #eee;
        }}

        /* GitHub corner styling */
        .github-corner {{
            position: fixed;
            top: 0;
            right: 0;
            z-index: 1000;
        }}

        .github-corner:hover .octo-arm {{
            animation: octocat-wave 560ms ease-in-out;
        }}

        @keyframes octocat-wave {{
            0%,100% {{ transform: rotate(0); }}
            20%,60% {{ transform: rotate(-25deg); }}
            40%,80% {{ transform: rotate(10deg); }}
        }}

        @media (max-width: 500px) {{
            .github-corner:hover .octo-arm {{
                animation: none;
            }}

            .github-corner .octo-arm {{
                animation: octocat-wave 560ms ease-in-out;
            }}
        }}

        /* Responsive design */
        @media (max-width: 1024px) {{
            .container {{
                flex-direction: column;
            }}

            .sidebar {{
                width: 100%;
                max-height: none;
                margin-top: 20px;
                position: static;
            }}

            .main-content {{
                padding: 20px;
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 10px;
            }}

            .header-content {{
                flex-direction: column;
                gap: 1rem;
            }}

            nav ul {{
                flex-wrap: wrap;
                justify-content: center;
            }}

            .main-content {{
                padding: 15px;
            }}
        }}
    </style>
</head>
<body>
    <a href="https://github.com/secnotes/fuzzing-tutorial" class="github-corner" aria-label="View source on GitHub">
        <svg width="80" height="80" viewBox="0 0 250 250" style="fill:#2c3e50; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true">
            <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"/>
            <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"/>
            <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"/>
        </svg>
    </a>
    <div class="container">
        <div class="main-content">
            <header>
                <div class="header-content">
                    <h1>Fuzzing Tutorial</h1>
                    <nav>
                        <ul>
                            <li><a href="index.html">Home</a></li>
                            <li><a href="index_en.html">English</a></li>
                            <li><a href="contributing.html">Contributing</a></li>
                        </ul>
                    </nav>
                </div>
            </header>

            <main class="main-content_area">
                <div class="markdown-body">
                    {html_body}
                </div>
            </main>

            <footer>
                <p>Fuzzing Tutorial - Collection of Papers, Blogs, and Tools Related to Fuzzing</p>
                <p>Last updated: {get_current_date()}</p>
            </footer>
        </div>

        <aside class="sidebar">
            {sidebar_content}
        </aside>
    </div>
</body>
</html>"""

    # Generate output filename

    # Generate output filename
    filename = Path(input_file).stem
    if filename.lower() == 'readme':
        filename = 'index'
    elif filename.lower() == 'readme_en':
        filename = 'index_en'
    elif filename.lower() == 'contributing':
        filename = 'contributing'

    output_file = os.path.join(output_dir, f"{filename}.html")

    # Write the HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"Converted {input_file} -> {output_file}")
    return output_file


def get_current_date():
    """Get current date in YYYY-MM-DD format"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


def copy_logo_if_exists():
    """Copy logo from root logo directory to docs/logo directory if it exists"""
    import shutil
    import os

    source_logo = "logo/logo.png"
    dest_dir = "docs/logo"
    dest_logo = "docs/logo/logo.png"

    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Copy logo file if it exists
    if os.path.exists(source_logo):
        try:
            shutil.copy2(source_logo, dest_logo)
            print(f"Copied logo from {source_logo} to {dest_logo}")
        except Exception as e:
            print(f"Error copying logo: {str(e)}")
    else:
        print(f"Logo file {source_logo} does not exist, skipping copy")


def main():
    """Main function to convert all markdown files in the root directory to HTML"""

    # Create docs directory if it doesn't exist
    os.makedirs('docs', exist_ok=True)

    # Copy logo if it exists
    copy_logo_if_exists()

    # Find all markdown files in the root directory
    markdown_files = glob.glob("*.md")

    if not markdown_files:
        print("No markdown files found in the current directory.")
        return

    print(f"Found {len(markdown_files)} markdown files to convert...")

    # Convert each markdown file to HTML
    for md_file in markdown_files:
        try:
            convert_markdown_to_html(md_file, 'docs')
        except Exception as e:
            print(f"Error converting {md_file}: {str(e)}")

    print("\\nConversion complete! HTML files saved in the 'docs/' directory.")


if __name__ == "__main__":
    main()