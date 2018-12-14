from django.db import models

'''
Design
- id (auto-generated)
- name
- description

Design_Version
- id (auto-generated)
- design_id (fk Design.id)
- description
- date_created
- material_costs
- cost_breakdown

Design_Version_Designer
- id (auto-generated)
- designer_id (fk directory.Designer)
- design_version_id (fk Design_Version)

Product
- id (auto-generated)
- design_id (unique, fk Design.id)
- name
- description

Item
- id (auto-generated)
- product_id (fk Product)
- design_version_id (fk Design_Version.id)
- date_begun
- date_completed
- selling_price

Item_Maker
- item_id (fk Item)
- maker_id (fk directory.Maker)
- production_time
- commision_requested
'''
