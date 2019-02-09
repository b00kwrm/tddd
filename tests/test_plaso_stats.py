import pytest
import shutil
import json
from plaso_stats import plaso_stats


@pytest.fixture(scope="session")
def tag_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("tag_linux.txt")
    shutil.copyfile("test_data/tag_linux.txt", fn)
    return fn


@pytest.fixture(scope="session")
def custom_json(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("custom.json")
    shutil.copyfile("test_data/custom.json", fn)
    return fn


def test_get_tags_from_file(tag_file):
    tags = plaso_stats.get_tags_from_file(tag_file)
    expected_tags = [
        "T1168_local_job_scheduling",
        "T1078_valid_accounts",
        "T1215_Kernel_Modules_and_Extensions",
        "T1057_Process_Discovery",
        "T1156_bash_profile_and_bashrc",
        "T1136_create_account",
        "ssh_logs",
        "T1098_account_manipulation",
    ]
    assert list == type(tags)
    assert tags == expected_tags


def test_open_psort_json(custom_json):
    jf = plaso_stats.open_psort_json(custom_json)
    assert dict == type(jf)


def test_get_tagged_events(tag_file, custom_json):
    tags = plaso_stats.get_tags_from_file(tag_file)
    jf = plaso_stats.open_psort_json(custom_json)
    tagged_events = plaso_stats.get_tagged_events(jf)
    assert list == type(tagged_events)


def test_check_for_tag(tag_file, custom_json):
    tags = plaso_stats.get_tags_from_file(tag_file)
    jf = plaso_stats.open_psort_json(custom_json)
    tagged_events = plaso_stats.get_tagged_events(jf)
    tag_status = plaso_stats.check_for_tag(tags, tagged_events)
    assert dict == type(tag_status)
    for tag in tag_status:
        assert tag_status[tag] == True


def test_get_data_types(custom_json):
    jf = plaso_stats.open_psort_json(custom_json)
    data_types = plaso_stats.get_data_types(jf)
    assert set == type(data_types)
