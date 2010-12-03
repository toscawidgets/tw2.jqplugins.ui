<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}:wrapper">
<div ${tw.attrs(attrs=w.attrs)}>
	% for header, item in w.items:
        <h3><a href="#">${header}</a></h3>
        <div>${item}</div>
	% endfor
</div>
<%include file="generic_jq_ui_js.mak" />
</div>
