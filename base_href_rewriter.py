import os
import re
import glob
import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description='Rewrite base href in HTML files')
    parser.add_argument('--base_href', required=True,
                        help='The new base href value')
    parser.add_argument('--html_path', help='Path to the HTML file to rewrite')
    parser.add_argument(
        '--html_glob', help='Glob pattern to match multiple HTML files')

    args = parser.parse_args()

    base_href = os.getenv('INPUT_BASE_HREF', args.base_href)
    html_path = os.getenv('INPUT_HTML_PATH', args.html_path)
    html_glob = os.getenv('INPUT_HTML_GLOB', args.html_glob)

    return base_href, html_path, html_glob


async def run_rewriter(base_href, html_path, html_glob):
    try:
        if not (html_path or html_glob):
            raise ValueError(
                'At least one of --html_path or --html_glob must be set')

        if html_path:
            rewrite_file(html_path, base_href)

        if html_glob:
            files = glob.glob(html_glob)
            print(f'Glob matched {len(files)} files')
            for file_path in files:
                rewrite_file(file_path, base_href)

    except Exception as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)


def rewrite_file(file_path, base_href):
    print(f'Attempting to rewrite base href in {
          file_path} to value {base_href}...')

    with open(file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()

    updated_text = re.sub(r'<base ([^>]*href=["\'])([^"\']*)(["\'][^>]*)>',
                          rf'<base \1{base_href}\3>',
                          original_text)

    if original_text != updated_text:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_text)
        print('Done')
    else:
        print(f'WARNING: no <base> tag with href attribute was found in {
              file_path}', file=sys.stderr)


def main():
    base_href, html_path, html_glob = get_args()
    import asyncio
    asyncio.run(run_rewriter(base_href, html_path, html_glob))


if __name__ == '__main__':
    main()
