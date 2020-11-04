# -*- coding: utf-8 -*-
"""Script for Default keyword"""
import sys

from shuangpin import convert_layout, matching_sequence
from workflow import Workflow3


def convert(workflow):
    """Convert input pattern"""
    results = matching_sequence(workflow.args[0])
    bopomofos = convert_layout(results, "bopomofo")
    xiaohes = convert_layout(results, "xiaohe")
    for bopomofo, xiaohe in zip(bopomofos, xiaohes):
        workflow.add_item(title=xiaohe, subtitle=bopomofo)
    workflow.send_feedback()


if __name__ == "__main__":
    WF = Workflow3(
        default_settings={},
        update_settings={
            "github_slug": "tomy0000000/Alfred-ShuangPin-Convert",
            "frequency": 7,
        },
        help_url="https://git.io/JfjXg",
    )
    sys.exit(WF.run(convert))
