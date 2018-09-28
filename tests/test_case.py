"""Def a module to be used in test."""

ok = 'OK'
not_ok = u'''
NO
'''


def invalid_sequences():
    assert u'a'
    assert 'a'
    assert U'a'
    assert u"b"
    assert u"b"
    assert "b"
    assert u"""c"""
    assert """c"""
