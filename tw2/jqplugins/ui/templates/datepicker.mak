<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}:wrapper">
     
     <input type="text" ${tw.attrs(attrs=w.attrs)} />

<%include file="generic_jq_ui_js.mak" />
</div>
