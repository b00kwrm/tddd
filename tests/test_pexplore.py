from pexplore import pexplore
from click.testing import CliRunner
import json
import shutil


with open("test_data/pinfo.json") as f:
    pinfo_json = f.read()
    pinfo_file = pinfo_json.encode("utf-8")


def test_pexplore_cli():
    def get_tags_from_file(tag_file):
        tags = []
        with open(tag_file) as f:
            lines = f.readlines()
            for line in lines:
                if not line.startswith(" ") and not line.startswith("\n"):
                    tag = line.strip()
                    tags.append(tag)
        return tags

    ltags = get_tags_from_file("test_data/tag_linux.txt")

    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("pinfo_file.json", "wb") as f:
            f.write(pinfo_file)
        result = runner.invoke(pexplore.cli, ["pinfo_file.json"])
        assert result.exit_code == 0
        results_dict = json.loads(result.output)
        # Get rid of type
        results_dict.pop("__type__")
        # get rid of total
        results_dict.pop("total")
        for ltag in ltags:
            print(ltag)
            assert ltag in results_dict.keys()
