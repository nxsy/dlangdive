import itertools

config.register_asset(
    'main_css',
    'reset.css',
    'main.css',
    'pygment.css',
    output="cache_main.%(version)s.css")

config.context_update(
    name="dlangdive",
    url="http://dlangdive.org",
    fb_app_id="641472525895652",
)

class Chapter(object):
    chapter_title = None
    sections = None

    def __init__(self, chapter_title, sections = None):
        self.chapter_title = chapter_title
        self.sections = sections if sections is not None else []

@app.template_filter('chapters')
def chapters(pages):
    pages = [p for p in pages if 'published' in p.meta and 'chapter' in p.meta]
    pages.sort(reverse=True, key=lambda p: p.meta['chapter'])
    for chapter, chapter_pages in itertools.groupby(pages, lambda p: (p.meta['chapter'], p.meta['section'])):
        c = None
        sections = []
        for page in chapter_pages:
            print page.meta
            if not c:
                c = Chapter(page.meta['chapter_header'], sections)
            sections.append(page)
        yield c

@app.route('/book/')
def toc():
    articles = [
        p for p in pages if 'published' in p.meta
        and p.meta.get('type', None) == 'page'
    ]
    # Show the 10 most recent articles, most recent first.
    articles.sort(reverse=True, key=lambda p: p.meta['published'])
    return render_template('book-index.html', pages=articles)


def page(path):
    print path
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


def index():
    articles = [
        p for p in pages if 'published' in p.meta
        and p.meta.get('type', None) != 'page'
    ]
    return render_template('index.html', pages=articles)


app.view_functions['page'] = page
app.view_functions['index'] = index
