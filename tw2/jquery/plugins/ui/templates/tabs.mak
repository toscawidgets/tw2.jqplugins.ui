<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}-wrapper">
<div ${tw.attrs(attrs=w.attrs)}>
	<ul>
	% for i in range(len(w.items)):
		<li><a href="#${w.attrs['id']}-${str(i)}">${w.items[i][0]}</a></li>
	% endfor
	</ul>
	% for i in range(len(w.items)):
		<div id="${w.attrs['id']}-${str(i)}">${w.items[i][1]}</div>
	% endfor
</div>
<%include file="generic_jq_ui_js.mak" />
</div>
