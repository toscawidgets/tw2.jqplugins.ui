<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}:wrapper">
	<div id="${w.attrs['id']}">
		% for btn in w.items:
		% if btn['isSelected']:
			<input type="checkbox" id="${btn['id']}" checked="checked" />
		% else:
			<input type="checkbox" id="${btn['id']}"/>
		% endif
		<label for="${btn['id']}">${btn['label']}</label>
		% endfor
	</div>
	<%include file="generic_jq_ui_js.mak" />
</div>
