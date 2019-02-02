import json
import sys

tagged_lines = []
tag_events = []
tag_counts = {}

with open(sys.argv[1]) as f:
    reader = f.read()
    jf = json.loads(reader)

for event in jf.keys():
    if jf[event].get("tag"):
        tag_events.append((event, jf[event]))

for tag_event in tag_events:
    if tag_event[1].get("tag"):
        if tag_event[1]["tag"]["labels"][0] == "T1168_local_job_scheduling":
            tagged_lines.append(tag_event[1]["tag"]["labels"][0])
        if tag_event[1]["tag"]["labels"][0] == "T1078_valid_accounts":
            tagged_lines.append(tag_event[1]["tag"]["labels"][0])
        if tag_event[1]["tag"]["labels"][0] == "T1215_Kernel_Modules_and_Extensions":
            tagged_lines.append(tag_event[1]["tag"]["labels"][0])
        if tag_event[1]["tag"]["labels"][0] == "T1057_Process_Discovery":
            tagged_lines.append(tag_event[1]["tag"]["labels"][0])
        if tag_event[1]["tag"]["labels"][0] == "T1156_bash_profile_and_bashrc":
            tagged_lines.append(tag_event[1]["tag"]["labels"][0])

# test that the tags got created
assert "T1168_local_job_scheduling" in tagged_lines
assert "T1078_valid_accounts" in tagged_lines
assert "T1215_Kernel_Modules_and_Extensions" in tagged_lines
assert "T1057_Process_Discovery" in tagged_lines
assert "T1156_bash_profile_and_bashrc" in tagged_lines

tag_set = set(tagged_lines)

for tag in tag_set:
    c = tagged_lines.count(tag)
    tag_counts[tag] = c


# test that the tags counts match what we expect.
assert tag_counts["T1057_Process_Discovery"] == 1
assert tag_counts["T1215_Kernel_Modules_and_Extensions"] == 3
assert tag_counts["T1156_bash_profile_and_bashrc"] == 3
assert tag_counts["T1078_valid_accounts"] == 1
assert tag_counts["T1168_local_job_scheduling"] == 1
