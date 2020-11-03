# -*- coding: utf-8 -*-
"""Script for Default keyword"""
import sys
import shuangpin
from workflow import Workflow3


def main(workflow):
    """The main workflow entry function"""
    workflow.run(shuangpin.convert)


if __name__ == "__main__":
    WF = Workflow3(
        default_settings={},
        update_settings={"github_slug": "tomy0000000/Coinc", "frequency": 7},
        help_url="https://git.io/JfjXg",
    )
    sys.exit(WF.run(main))
