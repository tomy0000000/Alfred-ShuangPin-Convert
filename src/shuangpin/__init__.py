# -*- coding: utf-8 -*-
"""Functions to be called by workflow"""
from .utils import convert_bopomofo, convert_xiaohe, matching_sequence


def convert(workflow):
    """convert input pattern"""
    # print(workflow.args[0])
    results = matching_sequence(workflow.args[0])
    bopomofo = convert_bopomofo(results)
    xiaohe = convert_xiaohe(results)
    for bp, xh in zip(bopomofo, xiaohe):
        workflow.add_item(title=xh, subtitle=bp)
    workflow.send_feedback()
