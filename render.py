#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os, glob, codecs, re, argparse, time, string, unicodedata, subprocess
from collections import OrderedDict

import markdown
from jinja2 import Environment, FileSystemLoader

skip_paths = ['drafts', 'css', 'old']
must_have = ['title']

conf = {'TITLE': 'klab',
        'AUTHOR': 'Jonas Kubilius',
        'SITENAME': 'klab.lt',
        'SITEURL': 'https://klab.lt',
        'DESCRIPTION': '',
        'KEYWORDS': 'mid-level vision, computer vision, human vision',
        'TAGLINE': u'"What I cannot create, I do not understand." – R. Feynman',
        'FOOTER': '',
        'DATE_FORMATS': ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d'],
        'GOOGLE_SITE_VERIFICATION': 'k1wISsyM_ADFRsWYOmwrowOMYSYu3MV5afsd-8B2AuQ',
        'current_year': time.strftime('%Y')
        }

nav = [('Blog', []),
       ('Publications', [
            'Papers',
            'Posters',
            'Talks',
            'Figures',
            # 'Software',
            ]),
       ('Outreach', [
            # ('Python for Vision Research',
            #  'http://nbviewer.ipython.org/github/gestaltrevision/python_for_visres/blob/master/index.ipynb'),
            'Lectures',
            'Machine Art'
            ]),
       ('About', [
            'Me',
            ('My CV', 'https://dl.dropboxusercontent.com/u/2498793/Kubilius-CV.pdf'),
            'Media'
            ])
        ]

parser = argparse.ArgumentParser()
parser.add_argument('--deploy', action='store_true')
parser.add_argument('--dry', action='store_true')
args = parser.parse_args()

if not args.deploy:
    conf['SITEURL'] = 'file:///' + os.getcwd().replace('\\','/') + '/content'
    index_href = 'index.html'
else:
    index_href = ''

md = markdown.Markdown(extensions=['markdown.extensions.meta'],
                       output_format='html5')
env = Environment(loader=FileSystemLoader('layout'),
                  autoescape=True,
                  trim_blocks=True,
                  # lstrip_blocks=True,
                  extensions=['jinja2.ext.autoescape', 'jinja2.ext.loopcontrols'])


def safestr(text):
    valid_chars = '-_ %s%s' % (string.ascii_letters, string.digits)

    # try:
    #     slug = unicode(text, 'utf-8')
    # except:
    slug = text
    slug = unicodedata.normalize('NFKD', slug)#.encode('ascii','ignore')
    try:
        slug = ''.join(c for c in slug if c in valid_chars)
    except:
        import ipdb; ipdb.set_trace()
    slug = slug.replace(' ','-').lower()
    while '--' in slug:
        idx = slug.find('--')
        slug = slug[:idx] + '-' + slug[idx+2:]
    return slug


def render(fname, pagetype='blog'):
    item = get_meta(fname)
    item['pagetype'] = pagetype
    if item['role'] == 'post' and item['status'] != 'draft':
        all_posts.append(item)
    template = env.get_template('single.html')
    output = template.render(item=item, nav=nav, include_footer=True, **conf)
    write(fname, output)


def get_meta(fname):
    with codecs.open(fname, mode='r', encoding='utf-8') as f:
        text = f.read()
    html = md.reset().convert(text)
    item = md.Meta
    item['html'] = html
    if 'status' not in item:
        item['status'] = 'published'

    if all([tag in item for tag in must_have]):
        for key, value in item.items():
            if isinstance(value, list):
                if len(value) == 1:  # and key != 'video':
                    item[key] = value[0]

        if 'authors' not in item:
            if 'author' in item:
                item['authors'] = item['author']
            else:
                item['authors'] = conf['AUTHOR']

        if 'links' in item:
            item['links'] = OrderedDict([li.split(': ') for li in item['links'] if len(li) > 0])
        else:
            item['links'] = OrderedDict()

        if not args.deploy:
            item['href'] = os.path.splitext(fname)[0] + '.html'
        else:
            item['href'] = os.path.dirname(fname) + '/'

        item['href'] = item['href'].replace('content', '')

        if 'role' not in item:
            item['role'] = 'post'

        if 'date' in item:
            struct_date = None
            for date_format in conf['DATE_FORMATS']:
                try:
                    struct_date = time.strptime(item['date'], date_format)
                except:
                    pass
                else:
                    break
            if struct_date is None:
                print(fname)
                raise Exception('ERROR: Date format not recognized for %s' % item['date'])

        if 'year' in item:
            try:
                struct_date = time.strptime(item['year'], '%Y')
            except:
                print(fname)
                raise Exception('ERROR: Date format not recognized for %s' % item['year'])

        if 'datestamp' not in item:
            item['datestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(fname)))
            with codecs.open(fname, mode='wb', encoding='utf-8') as f:
                # normalize text endings
                normtext = text.replace('\r\n','\n').replace('\r','\n')
                lines = normtext.split('\n')
                for lineno, line in enumerate(lines):
                    if lineno == 0:
                        if line == '---': isyaml = True
                        else: isyaml = False
                    if line == '' or (line == '---' and isyaml and lineno != 0):
                        break
                    else:
                        f.write(line + '\n')

                f.write('datestamp: %s\n' % item['datestamp'])
                f.write('\n'.join(lines[lineno:]))

        if 'date' not in item:
            struct_date = time.strptime(item['datestamp'], '%Y-%m-%d %H:%M:%S')

        item['dateonly'] = time.strftime('%Y-%m-%d', struct_date)

        if 'year' not in item:
            item['year'] = time.strftime('%Y', struct_date)

        item['categories'] = item['categories'].split(', ')
        item['cathref'] = cathrefs[item['categories'][0]]

        return item

    elif item['status'] != 'draft':
        print('WARNING: author or categories not found in %s' % fname)


def write(fname, output):
    if not args.dry:
        path = os.path.join(os.path.dirname(fname), 'index.html')
        with codecs.open(path, 'wb', 'utf-8') as f:
            f.write(output)
    else:
        print(fname)


# Format navigation
slug2cat = {}
cathrefs = {}
for tno, (topic, cats) in enumerate(nav):
    if len(cats) == 0:
        cathref = '/'.join(['', safestr(topic), index_href])
        cathrefs[topic] = cathref
        cathrefs[safestr(topic)] = cathref
        nav[tno] = (topic, cathref)
    else:
        for cno, cat in enumerate(cats):
            if not isinstance(cat, tuple):
                cat = (cat, safestr(cat))

            if not cat[1].startswith('http://') and not cat[1].startswith('https://'):
                slug2cat[cat[1]] = cat[0]
                cathref = '/'.join(['', safestr(topic), cat[1], index_href])
                cathrefs[cat[0]] = cathref
                cathrefs[cat[1]] = cathref
                nav[tno][1][cno] = (cat[0], cathref)


def render_posts(path, pagetype):
    for post in glob.glob(os.path.join(path, '*')):
        if os.path.isdir(post):
            postname = os.path.join(post, 'index.md')
            if not os.path.isfile(postname):
                print('WARNING: %s not found' % postname)
            else:
                render(postname, pagetype=pagetype)


# Collect all posts
all_posts = []
for topic, cats in nav:
    topic_path = os.path.join('content', safestr(topic))
    if not isinstance(cats, list):
        render_posts(topic_path, pagetype='blog')
    else:
        for cat in os.listdir(topic_path):
            cat_path = os.path.join(topic_path, safestr(cat))
            if topic == 'Publications' or cat in ['Lectures', 'Media']:
                pagetype = 'publications'
            else:
                pagetype = 'blog'
            render_posts(cat_path, pagetype=pagetype)


def render_index(selector, path):
    selposts = [item for item in all_posts if selector in item['categories']]
    for item in selposts:
        pdiff = os.path.relpath(item['href'], os.path.dirname(item['cathref']))
        if not args.deploy:  # pdiff has index.html part
            pdiff = os.path.dirname(pdiff)
        for name, href in item['links'].items():
            if not href.startswith('http://') and not href.startswith('https://') and name != 'doi':
                item['links'][name] = pdiff + '/' + href
    template = env.get_template('cat_index.html')
    output = template.render(items=selposts,
                             nav=nav,
                             include_footer=True,
                             category=selector,
                             pagetype=selposts[0]['pagetype'],
                             **conf)
    # except:
    #     import pdb; pdb.set_trace()

    write(os.path.join(path, 'index.md'), output)


# Render category indices and all entries
for topic, cats in nav:
    topic_path = os.path.join('content', safestr(topic))
    if not isinstance(cats, list):
        render_index(topic, topic_path)
    else:
        for cat, cathref in cats:
            if not cathref.startswith('http://') and not cathref.startswith('https://'):
                cat_path = os.path.join(topic_path, safestr(cat))
                page = glob.glob(os.path.join(cat_path, 'index.md'))
                # catname = slug2cat[cat]

                if len(page) > 0:  # separate entries
                    page = page[0]
                    meta = get_meta(page)
                    render(page)
                else:  # category index
                    render_index(cat, cat_path)


# Render index.html
with codecs.open('content/index.md', mode='rb', encoding='utf-8') as f:
    text = f.read()
intro_text = {}
intro_text['html'] = md.reset().convert(text)
intro_text['title'] = md.Meta['title'][0]

template = env.get_template('index.html')
output = template.render(items=all_posts, nav=nav, include_footer=False,
                         intro_text=intro_text, rel='', **conf)
if not args.dry:
    write('content/index.html', output)

# if args.deploy:
#     # transfer to the server
#     subprocess.call('rsync -av --del --exclude=drafts/ content/ klab_nfsn:klab.lt/'.split())
# else:
#     # show locally
#     subprocess.call(['open', os.path.join(conf['SITEURL'], index_href)])