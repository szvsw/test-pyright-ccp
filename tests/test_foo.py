from test_pyright_ccp.foo import foo


def test_foo():
    assert foo("foo") == "foo"
