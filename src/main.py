# -*- coding: utf-8 -*-
"""Script for Default keyword"""
import os
import sys

from shuangpin import convert_layout, matching_sequence
from workflow import Workflow3


def convert(workflow):
    """Convert input pattern"""
    sequence = "".join(workflow.args)
    results = matching_sequence(sequence)
    layout_main = os.getenv("MAIN_LAYOUT", "xiaohe")
    layout_secondary = os.getenv("SECONDARY_LAYOUT", "zhuyin")
    xiaohes = convert_layout(results, layout_main)
    zhuyins = convert_layout(results, layout_secondary)
    for zhuyin, xiaohe in zip(zhuyins, xiaohes):
        workflow.add_item(title=xiaohe, subtitle=zhuyin)
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
