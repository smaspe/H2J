def map_element_to_json(element, mapping):
    if isinstance(mapping, str):
        return element.xpath(mapping)

    elements = element.xpath(mapping['$']['root'])
    is_array = mapping['$']['type'] == 'array'
    ml = [(k, v) for k, v in mapping.items() if k != '$']
    result = ({k: map_element_to_json(element, v) for k, v in ml} for element in elements)
    if not is_array:
        return next(iter(result), None)
    else:
        return list(result)
