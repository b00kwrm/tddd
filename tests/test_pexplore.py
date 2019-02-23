from pexplore import pexplore
from click.testing import CliRunner
import json

tags = '{"__type__": "collections.Counter", "T1215_Kernel_Modules_and_Extensions": 3, "S0002_mimikatz": 24, "total": 46, "T1057_Process_Discovery": 1, "T1098_account_manipulation": 8, "T1156_bash_profile_and_bashrc": 3, "ssh_logs": 4, "T1003_credential_dumping": 24, "T1078_valid_accounts": 1, "T1136_create_account": 1, "T1168_local_job_scheduling": 1}'


with open("test_data/pinfo.json") as f:
    pinfo_json = f.read()
    pinfo_file = pinfo_json.encode("utf-8")


def test_pexplore_cli():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("pinfo_file.json", "wb") as f:
            f.write(pinfo_file)
        result = runner.invoke(pexplore.cli, ["pinfo_file.json"])
        assert result.exit_code == 0
        assert result.output == tags
        results_dict = json.loads(result.output)
        assert "S0002_mimikatz" in results_dict.keys()
