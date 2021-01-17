from pathlib import Path
import pandas as pd
import re
from slot_faker import SlotFaker
from utterer import Utterer

domain_xl = Path.home() / 'Downloads' / 'MediaCable Testing.xlsx'
df = pd.read_excel(domain_xl, sheet_name='Scripts')

df = df.where(pd.notnull(df), '')


fake = SlotFaker()

bs = Utterer()
rows = []


def amazon_attr(name: str):
    return '_'.join(
        part.lower()
        for part in re.findall(r'[A-Z][^A-Z.]*', name.replace('AMAZON.', ''))
    )


for row in df.itertuples(name='row'):
    if row.TurnID == 0:
        rows.append(['', '', '', []])
        continue
    if not row.SlotName and row.TurnID != 0:
        rows.append(['', '', '', []])
        continue
    utterance_templates = []
    if row.SlotTypeName and 'amazon' not in row.SlotTypeName.lower():
        utterance_templates = [
            row.Customer1, row.Customer2, row.Customer3, row.Customer4,
            row.Customer5, row.Customer6, row.Customer7, row.Customer8
        ]
    turn = [
        row.SlotName,
        row.SlotTypeName,
        row.Method,
        utterance_templates
    ]
    rows.append(turn)

for i, (slot_name, slot_type_name, slot_method, utterance_templates) in enumerate(rows):
    if not slot_name:
        continue
    if not utterance_templates and (bs_method := getattr(bs, amazon_attr(slot_type_name), None)):
        for j in range(8):
            utterance_templates.append(bs_method())
    new_utterances = []
    if (bs_value := getattr(fake, slot_method, None)):
        for template in utterance_templates:
            slot_value = f"{bs_value()}"
            new_utterances.append(slot_value)
            new_utterances.append(template.format(slot_value))
    rows[i][3] = new_utterances if new_utterances else [
        '', '', '', '', '', '', '', ''
        '', '', '', '', '', '', '', ''
    ]


values = [[*row[:3], *row[3]] for row in rows]
out_file = Path.home() / 'Downloads' / 'mc_out.xlsx'
new_df = pd.DataFrame(
    values, columns=[
        'SlotName', 'SlotValueType', 'SlotMethod',
        'Customer1', 'SlotValue1',
        'Customer2', 'SlotValue2',
        'Customer3', 'SlotValue3',
        'Customer4', 'SlotValue4',
        'Customer5', 'SlotValue5',
        'Customer6', 'SlotValue6',
        'Customer7', 'SlotValue7',
        'Customer8', 'SlotValue8'
    ]
)
new_df.to_excel(out_file, index=False)