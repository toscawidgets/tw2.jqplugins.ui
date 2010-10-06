<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}-wrapper">
	% if w.type == 'button':
		<button ${tw.attrs(attrs=w.attrs)}>${w.value}</button>
	% elif w.type == 'input':
		<input  ${tw.attrs(attrs=w.attrs)} type="submit" value="${w.value}"/>
	% elif w.type == 'anchor':
		<a      ${tw.attrs(attrs=w.attrs)} href="#">${w.value}</a>
	% endif
<%include file="generic_jq_ui_js.mak" />
</div>
