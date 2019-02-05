import json
import sys
from pprint import pprint
from collections import Counter


def get_tags_from_file(tag_file):
    """Open tag file and pull out tags.
       return a list of tags"""
    tags = []
    with open(tag_file) as f:
        lines = f.readlines()
        for line in lines:
            if not line.startswith(" ") and not line.startswith("\n"):
                tag = line.strip()
                tags.append(tag)
    return tags


def open_psort_json(json_file_name):
    """Open psort json file"""
    with open(json_file_name) as f:
        jf = json.load(f)
        return jf


def get_tagged_events(psort_dict):
    """Iterate over psort dict and
       pull out tagged events. return
       a list of tuples containing the event_id
       and the event dict"""
    tagged_events = []
    for event in psort_dict.keys():
        if psort_dict[event].get("tag"):
            tagged_events.append((event, jf[event]))
    return tagged_events


def check_for_tag(tags, tagged_events):
    """Check for the existence of a specific tag in a tag_event."""
    found_tags = set()
    tags_set = set(tags)
    for tag in tags:
        for tag_event in tagged_events:
            if tag in tag_event[1]["tag"]["labels"]:
                found_tags.add(tag)
    not_found = tags_set - found_tags
    tag_status = {}
    for tag in found_tags:
        tag_status[tag] = True
    for tag in not_found:
        tag_status[tag] = False
    return tag_status


def count_tags(tag_events):
    """Count the number of each tag in tag_events.
       Return a dict of tags and counts."""
    tagged_lines = []
    for tag_event in tag_events:
        for tag in tag_event[1]["tag"]["labels"]:
            tagged_lines.append(tag)
    tag_counts = Counter(tagged_lines)
    return tag_counts


if __name__ == "__main__":
    tags = get_tags_from_file(sys.argv[1])
    jf = open_psort_json(sys.argv[2])
    tagged_events = get_tagged_events(jf)
    tag_status = check_for_tag(tags, tagged_events)
    tag_counts = count_tags(tagged_events)
    pprint(tags)
    pprint(tagged_events)
    pprint(tag_status)
    pprint(tag_counts)
