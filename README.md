# Base Href rewriter GitHub Action

This GitHub Action is designed to rewrite the `<base href>` tag within HTML files. It can be useful when you need to update the base URL for your web application.

## Inputs

### `base_href`

**Required** The new base href value that you want to set.

### `html_path`

Path to the HTML file you want to rewrite. Either `html_path` or `html_glob` must be set.

### `html_glob`

Glob pattern to match multiple HTML files. Either `html_path` or `html_glob` must be set.

## Example Usage

```yaml
name: Rewrite Base Href

on:
  push:
    branches:
      - main

jobs:
  rewrite-base-href:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Rewrite Base Href
      uses: kannansuresh/rewrite-base-href-action@latest
      with:
        base_href: 'https://your-updated-url.com'
        html_glob: '**/*.html'
