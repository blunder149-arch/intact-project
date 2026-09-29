with open(r'c:\xampp\htdocs\intact\ceiling.php', 'r', encoding='utf-8') as f:
    ceiling_html = f.read()

with open(r'c:\xampp\htdocs\intact\walls.php', 'r', encoding='utf-8') as f:
    walls_html = f.read()

# Extract Colour & Finish Library Section from ceiling.php
start_tag = '<!-- Colour & Finish Library Start -->'
end_tag = '<!-- Colour & Finish Library End -->'

c_start = ceiling_html.find(start_tag)
c_end = ceiling_html.find(end_tag) + len(end_tag)
finish_section = ceiling_html[c_start:c_end]

# Change title in finish_section for wall panels
finish_section_walls = finish_section.replace('Extruded PVC Ceiling Panel Finishes', 'Extruded PVC Wall Panel Finishes')

w_start = walls_html.find(start_tag)
w_end = walls_html.find(end_tag) + len(end_tag)

new_walls_html = walls_html[:w_start] + finish_section_walls + walls_html[w_end:]

# Update JS in new_walls_html
old_js = """\t<script>
\t\tjQuery(document).ready(function ($) {
\t\t\t$('.pbmit-finish-filter a').on('click', function (e) {
\t\t\t\te.preventDefault();
\t\t\t\t$('.pbmit-finish-filter a').removeClass('pbmit-selected');
\t\t\t\t$(this).addClass('pbmit-selected');
\t\t\t\tvar filter = $(this).data('filter');
\t\t\t\tif (filter === '*' || filter === 'all') {
\t\t\t\t\t$('.finish-item').fadeIn(300);
\t\t\t\t} else {
\t\t\t\t\t$('.finish-item').hide();
\t\t\t\t\t$('.finish-item.' + filter).fadeIn(300);
\t\t\t\t}
\t\t\t});
\t\t});
\t</script>"""

new_js = """\t<script>
\t\tjQuery(document).ready(function ($) {
\t\t\t// Filter tabs
\t\t\t$('.pbmit-finish-filter a').on('click', function (e) {
\t\t\t\te.preventDefault();
\t\t\t\t$('.pbmit-finish-filter a').removeClass('pbmit-selected');
\t\t\t\t$(this).addClass('pbmit-selected');
\t\t\t\tvar filter = $(this).data('filter');
\t\t\t\tif (filter === '*' || filter === 'all') {
\t\t\t\t\t$('.finish-item').stop(true, true).fadeIn(250);
\t\t\t\t} else {
\t\t\t\t\t$('.finish-item').stop(true, true).hide();
\t\t\t\t\t$('.finish-item.' + filter).stop(true, true).fadeIn(250);
\t\t\t\t}
\t\t\t});

\t\t\t// Finish type button switcher (Simple / Golden / Copper)
\t\t\t$(document).on('click', '.finish-type-btn', function (e) {
\t\t\t\te.preventDefault();
\t\t\t\tvar $btn = $(this);
\t\t\t\tvar $card = $btn.closest('.finish-card-box');
\t\t\t\tvar type = $btn.data('type');
\t\t\t\tvar $imgWrap = $card.find('.finish-img-wrap');
\t\t\t\tvar $img = $imgWrap.find('.finish-panel-img');

\t\t\t\tvar simpleSrc = $img.data('simple') || $img.attr('src');
\t\t\t\tvar goldenSrc = $img.data('golden') || simpleSrc;
\t\t\t\tvar copperSrc = $img.data('copper');

\t\t\t\t// Reset groove overlay classes
\t\t\t\t$imgWrap.removeClass('show-copper show-golden-overlay');

\t\t\t\tif (type === 'simple') {
\t\t\t\t\t$img.attr('src', simpleSrc);
\t\t\t\t} else if (type === 'golden') {
\t\t\t\t\t$img.attr('src', goldenSrc);
\t\t\t\t\tif (goldenSrc === simpleSrc) {
\t\t\t\t\t\t$imgWrap.addClass('show-golden-overlay');
\t\t\t\t\t}
\t\t\t\t} else if (type === 'copper') {
\t\t\t\t\tif (copperSrc) {
\t\t\t\t\t\t$img.attr('src', copperSrc);
\t\t\t\t\t} else {
\t\t\t\t\t\t$img.attr('src', simpleSrc);
\t\t\t\t\t\t$imgWrap.addClass('show-copper');
\t\t\t\t\t}
\t\t\t\t}

\t\t\t\t$card.find('.finish-type-btn').removeClass('active');
\t\t\t\t$btn.addClass('active');
\t\t\t});
\t\t});
\t</script>"""

if old_js in new_walls_html:
    new_walls_html = new_walls_html.replace(old_js, new_js)
    print('JS replaced successfully!')
else:
    print('old_js not found exact match')

with open(r'c:\xampp\htdocs\intact\walls.php', 'w', encoding='utf-8') as f:
    f.write(new_walls_html)

print('walls.php updated successfully!')
