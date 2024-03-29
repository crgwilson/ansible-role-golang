def test_default_go(host):
    f = host.file('/usr/local/bin/go')
    assert f.is_symlink


def test_default_go_version(host):
    go_version = 'go version go1.18.3 linux/amd64'
    assert host.check_output('/usr/local/bin/go version') == go_version
