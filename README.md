# thomomys

Thomomys is a [pelican](http://blog.getpelican.com/) theme based on
[pelican-material](https://github.com/greizgh/pelican-material) which is based
on [Materialize](http://materializecss.com/), a material design framework.

It uses [Material Design Lite](http://www.getmdl.io) to do most of the heavy lifting.

## Required Configuration

This template uses a custom filter to sort tags by article count. You need to add this to your config:

```python
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order
```

## Optional Configuration

You will probably want to use
[pelican-materialbox](https://github.com/greizgh/pelican-materialbox),
a pelican plugin to use
[materialboxed](http://materializecss.com/media.html#materialbox) from
Materialize.


## Dependencies

A straight up checkout of the theme should just work, however npm is setup if
you want to mess with stuff.

Run this command from theme's root directory:

    npm

## License

MIT
