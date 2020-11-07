"""Tests for Zhuyin"""
from shuangpin import convert_layout, matching_sequence


def test_zhuyin_a():
    assert "".join(convert_layout(matching_sequence("a"), "zhuyin")) == "ㄚ"


def test_zhuyin_an():
    assert "".join(convert_layout(matching_sequence("an"), "zhuyin")) == "ㄢ"


def test_zhuyin_ang():
    assert "".join(convert_layout(matching_sequence("ang"), "zhuyin")) == "ㄤ"


def test_zhuyin_zi():
    assert "".join(convert_layout(matching_sequence("zi"), "zhuyin")) == "ㄗ"


def test_zhuyin_zhi():
    assert "".join(convert_layout(matching_sequence("zhi"), "zhuyin")) == "ㄓ"


def test_zhuyin_ya():
    assert "".join(convert_layout(matching_sequence("ya"), "zhuyin")) == "ㄧㄚ"


def test_zhuyin_yan():
    assert "".join(convert_layout(matching_sequence("yan"), "zhuyin")) == "ㄧㄢ"


def test_zhuyin_yang():
    assert "".join(convert_layout(matching_sequence("yang"), "zhuyin")) == "ㄧㄤ"


def test_zhuyin_nv():
    assert "".join(convert_layout(matching_sequence("nv"), "zhuyin")) == "ㄋㄩ"


def test_zhuyin_lv():
    assert "".join(convert_layout(matching_sequence("lv"), "zhuyin")) == "ㄌㄩ"


def test_zhuyin_xi():
    assert "".join(convert_layout(matching_sequence("xi"), "zhuyin")) == "ㄒㄧ"


def test_zhuyin_xia():
    assert "".join(convert_layout(matching_sequence("xia"), "zhuyin")) == "ㄒㄧㄚ"


def test_zhuyin_xian():
    assert "".join(convert_layout(matching_sequence("xian"), "zhuyin")) == "ㄒㄧㄢ"


def test_zhuyin_xiang():
    assert "".join(convert_layout(matching_sequence("xiang"), "zhuyin")) == "ㄒㄧㄤ"


def test_zhuyin_ba():
    assert "".join(convert_layout(matching_sequence("ba"), "zhuyin")) == "ㄅㄚ"


def test_zhuyin_ban():
    assert "".join(convert_layout(matching_sequence("ban"), "zhuyin")) == "ㄅㄢ"


def test_zhuyin_bang():
    assert "".join(convert_layout(matching_sequence("bang"), "zhuyin")) == "ㄅㄤ"


def test_zhuyin_zhu():
    assert "".join(convert_layout(matching_sequence("zhu"), "zhuyin")) == "ㄓㄨ"


def test_zhuyin_zhua():
    assert "".join(convert_layout(matching_sequence("zhua"), "zhuyin")) == "ㄓㄨㄚ"


def test_zhuyin_zhuan():
    assert "".join(convert_layout(matching_sequence("zhuan"), "zhuyin")) == "ㄓㄨㄢ"


def test_zhuyin_zhuang():
    assert "".join(convert_layout(matching_sequence("zhuang"), "zhuyin")) == "ㄓㄨㄤ"


def test_zhuyin_zhe():
    assert "".join(convert_layout(matching_sequence("zhe"), "zhuyin")) == "ㄓㄜ"


def test_zhuyin_zhen():
    assert "".join(convert_layout(matching_sequence("zhen"), "zhuyin")) == "ㄓㄣ"


def test_zhuyin_zheng():
    assert "".join(convert_layout(matching_sequence("zheng"), "zhuyin")) == "ㄓㄥ"
