import os

files_data = {
    '2-groove-pvc-ceiling-panel.php': {
        'title_from': 'font-size: 32px; font-weight: 700; line-height: 1.3;',
        'title_to': 'font-size: 34px; font-weight: 700; line-height: 1.25;',
        'p_from': 'max-width: 820px; line-height: 1.6;',
        'p_to': 'line-height: 1.6;',
        'break_from': 'assistance. We supply',
        'break_to': 'assistance.<br> We supply'
    },
    '2-groove-pvc-wall-panel.php': {
        'title_from': 'font-size: 32px; font-weight: 700; line-height: 1.3;',
        'title_to': 'font-size: 34px; font-weight: 700; line-height: 1.25;',
        'heading_from': 'Elevate Your Ceilings with INTACT 2 Groove Panels',
        'heading_to': 'Elevate Your Walls with INTACT 2 Groove Wall Panels',
        'p_from': 'max-width: 820px; line-height: 1.6;',
        'p_to': 'line-height: 1.6;',
        'panel_from': '2 Groove PVC ceiling',
        'panel_to': '2 Groove PVC wall',
        'break_from': 'assistance. We supply',
        'break_to': 'assistance.<br> We supply'
    },
    'plain-pvc-ceiling-panel.php': {
        'p_from': 'max-width: 820px; line-height: 1.6;',
        'p_to': 'line-height: 1.6;',
        'break_from': 'assistance.',
        'break_to': 'assistance.<br> We supply Plain PVC ceiling panels to dealers, contractors and customers across India.'
    },
    '9-groove-pvc-wall-panel.php': {
        'p_from': 'max-width: 820px; line-height: 1.6;',
        'p_to': 'line-height: 1.6;',
        'break_from': 'assistance. We supply',
        'break_to': 'assistance.<br> We supply'
    },
    '10-groove-pvc-wall-panel.php': {
        'p_from': 'max-width: 820px; line-height: 1.6;',
        'p_to': 'line-height: 1.6;',
        'break_from': 'assistance. We supply',
        'break_to': 'assistance.<br> We supply'
    },
    'ceiling.php': {
        'p_from': 'max-width: 820px; line-height: 1.6;',
        'p_to': 'line-height: 1.6;',
        'break_from': 'assistance. We supply',
        'break_to': 'assistance.<br> We supply'
    },
    'walls.php': {
        'p_from': 'max-width: 820px; line-height: 1.6;',
        'p_to': 'line-height: 1.6;',
        'break_from': 'assistance. We supply',
        'break_to': 'assistance.<br> We supply'
    }
}

for fname, changes in files_data.items():
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    for k, v in changes.items():
        if k.endswith('_from'):
            to_key = k[:-5] + '_to'
            target_to = changes[to_key]
            content = content.replace(v, target_to)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {fname}')

print('All pages synchronized to SUMO CTA design!')
