from main import set_arguments
from torbot.modules.linktree import parse_links


def test_version_flag_does_not_require_url() -> None:
    parser = set_arguments()
    args = parser.parse_args(["--version"])

    assert args.version is True
    assert args.url is None


def test_parse_links_resolves_relative_urls_against_base_url() -> None:
    html = """
    <html>
        <body>
            <a href="/about">About</a>
            <a href="https://example.com/docs">Docs</a>
            <a href="javascript:void(0)">JS</a>
        </body>
    </html>
    """

    links = parse_links(html, base_url="https://example.com/index")

    assert links == ["https://example.com/about", "https://example.com/docs"]
