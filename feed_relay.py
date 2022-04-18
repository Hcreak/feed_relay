# coding=utf-8

import feedparser
import PyRSS2Gen
from datetime import datetime
import time
from translation import translate

feed_input = feedparser.parse("https://letsencrypt.org/feed.xml")

translate_source = [ item.description for item in feed_input.entries ]
translate_target = translate(translate_source, "auto2zh")

rss = PyRSS2Gen.RSS2(
    title = feed_input.feed.title,
    link = feed_input.feed.link,
    description = feed_input.feed.description,

    lastBuildDate = datetime.fromtimestamp(time.mktime(feed_input.feed.updated_parsed)),

    items = [
        PyRSS2Gen.RSSItem(
            title = item.title,
            link = item.link,
            description = translate_target[ feed_input.entries.index(item) ],
            guid = PyRSS2Gen.Guid(item.id),
            pubDate = datetime.fromtimestamp(time.mktime(item.updated_parsed))
        ) for item in feed_input.entries
    ]
)

rss.write_xml(open("pyrss2gen.xml", "w"))