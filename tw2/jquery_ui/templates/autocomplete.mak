<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}-wrapper">
     
	 <input ${tw.attrs(attrs=w.attrs)} />

<%include file="generic_jq_ui_js.mak" />
% if w.attrs['value'] != '':
	<%include file="ghost_text.mak" />
% endif
</div>
