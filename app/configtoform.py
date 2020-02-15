import pandas as pd

filter=['PADRÃO', 'Seguros']

templates= pd.read_csv('configs.csv')
form_generator_attrs = ['type', 'inputType','readonly','featured','required', 'disabled', 'default', 'values', 'multi', 'label', 'model']
schema=templates.copy().set_index('Nome_campo')
schema=schema[form_generator_attrs].to_dict(orient='records')
model=templates.copy()[['model', 'valor_base']].set_index('model').fillna('')
model=model.to_dict()
final_schema=[]
for dici in schema:
    new_dici = {key: dici[key] for key in dici if dici[key] not in ['NSA']}
    final_schema.append(new_dici)