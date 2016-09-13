from json import loads


def form_id_dic(form, table_id):
    return {'form': form, 'id': table_id}


def parse_json_serialized_list(json):
    json_parse = loads(json)
    li = []
    for item in json_parse:
        dic = {}
        for dic_rec in item:
            dic[dic_rec.get('name')] = dic_rec.get('value')
        li.append(dic)
    return li


def create_full_table_context(table, data=None):
    cols = table['columns']
    if data:
        col_list = [item['col'] for item in cols]
        table['rows'] = [[str(rec.get(col, '')) for col in col_list] for rec in data]
    return table



def parse_dic(data):
    cols = table['columns']
    col_list = [item['col'] for item in cols]
    table['rows'] = [[str(rec.get(col, '')) for col in col_list] for rec in data]
    return table


