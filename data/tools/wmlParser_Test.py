# encoding: utf-8

import wesnoth.wmlparser3 as wmlparser

p = wmlparser.Parser()
cfg = p.parse_file('wmlParser_SplitDesc_WMLFile.cfg')
for unit in cfg.get_all(tag = "unit"):
    print(unit.get_text_val("id"))
    print(unit.get_text_val("name"))
    for abilities in unit.get_all(tag = "abilitities"):
        for ability in abilities.get_all(tag = ""):
            print(ability.get_name())
            print(ability.get_text_val("id"))