#!/usr/bin/env python
"""
Nmap XML Output to Json Output in Python
example : data = xml2json('nmap_output.xml')
"""
import json
import click
import xmltodict

def xml_to_json(xml, formatted):
    """convert xml to json"""
    with click.open_file(xml, encoding="utf-8") as xml_file:
        xml_content = xml_file.read()
        xml_file.close()
        xml_json = json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True)
        json_parsed = json.loads(xml_json)
        if formatted:
            json_data = json.dumps(json_parsed, indent=3)
        else:
            json_data = str(json_parsed) + "\n"
    return json_data


@click.command()
@click.option('-f', '--format', 'formatted', is_flag=True, default=False,
              help='format json output ')
@click.option('-o', '--output', default='-', help='output file name')
@click.argument('filename', type=click.Path(dir_okay=False,allow_dash=True))
def cli(formatted, output, filename):
    """Convert the xml file FILENAME to json,
    use - for stdin"""

    json_data = xml_to_json(filename, formatted)
    with click.open_file(output, "w") as output_file:
        output_file.write(json_data)

if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter

# vim:sw=4:ts=4:et:
